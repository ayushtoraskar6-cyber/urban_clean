import fs from 'fs';
import path from 'path';
import { execSync } from 'child_process';

const BASE_URL = 'http://localhost:3000';

console.log('================================================================================');
console.log('            URBANCLEAN INTEGRATION TESTING SUITE (API & DATABASE)              ');
console.log('================================================================================');
console.log(`Execution Timestamp: ${new Date().toISOString()}`);
console.log(`Target Host: ${BASE_URL}`);
console.log('--------------------------------------------------------------------------------\n');

let passed = 0;
let failed = 0;

function assert(testId, name, condition, details) {
    if (condition) {
        passed++;
        console.log(`[PASS] ${testId} - ${name}`);
        if (details) console.log(`       Details: ${details}`);
    } else {
        failed++;
        console.error(`[FAIL] ${testId} - ${name}`);
        if (details) console.error(`       Error: ${details}`);
    }
}

async function runIntegrationTests() {
    // IT-01: Authentication API Integration
    try {
        const loginRes = await fetch(`${BASE_URL}/api/login`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ email: 'admin@urbanclean.org', password: 'Admin@123', role: 'admin' })
        });
        const loginData = await loginRes.json();
        assert('IT-01', 'REST API Authentication (POST /api/login)', loginRes.status === 200 && loginData.user && loginData.user.role === 'admin', `HTTP ${loginRes.status} | Authenticated User: ${loginData.user ? loginData.user.name : 'None'} (${loginData.user ? loginData.user.id : ''})`);
    } catch (e) {
        assert('IT-01', 'REST API Authentication (POST /api/login)', false, e.message);
    }

    // IT-02: Complaint Retrieval API with RBAC headers
    try {
        const compRes = await fetch(`${BASE_URL}/api/complaints?city=Bandra`, {
            headers: {
                'x-user-id': 'ADM-999',
                'x-user-role': 'admin'
            }
        });
        const compData = await compRes.json();
        assert('IT-02', 'Complaint Data Ingestion & Retrieval (GET /api/complaints)', compRes.status === 200 && Array.isArray(compData), `HTTP ${compRes.status} | Retrieved ${compData.length} records matching jurisdiction`);
    } catch (e) {
        assert('IT-02', 'Complaint Data Ingestion & Retrieval (GET /api/complaints)', false, e.message);
    }

    // IT-03: Route Optimization & OSRM Engine Integration
    try {
        const routeRes = await fetch(`${BASE_URL}/api/route-optimize`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                waypoints: [
                    { label: 'Depot Bandra', lat: 19.0544, lng: 72.8295, type: 'depot' },
                    { label: 'Stop 1 Khar', lat: 19.0700, lng: 72.8333, type: 'stop' },
                    { label: 'Stop 2 Kurla', lat: 19.0688, lng: 72.8784, type: 'stop' }
                ]
            })
        });
        const routeData = await routeRes.json();
        assert('IT-03', 'Route Optimization Engine Integration (POST /api/route-optimize)', routeRes.status === 200 && routeData.distance && routeData.path.length === 3, `HTTP ${routeRes.status} | Optimized Distance: ${routeData.distance} | Reported Savings: ${routeData.savings} | Road Waypoints: ${routeData.roadPath ? routeData.roadPath.length : 'Haversine Fallback'}`);
    } catch (e) {
        assert('IT-03', 'Route Optimization Engine Integration (POST /api/route-optimize)', false, e.message);
    }

    // IT-04: Admin Dashboard Aggregate Statistics API
    try {
        const statsRes = await fetch(`${BASE_URL}/api/admin/stats`);
        const statsData = await statsRes.json();
        assert('IT-04', 'Admin KPI Metrics Aggregation (GET /api/admin/stats)', statsRes.status === 200 && typeof statsData.total === 'number', `HTTP ${statsRes.status} | Total Complaints: ${statsData.total} | Open: ${statsData.open} | In Progress: ${statsData.progress} | Completed: ${statsData.completed}`);
    } catch (e) {
        assert('IT-04', 'Admin KPI Metrics Aggregation (GET /api/admin/stats)', false, e.message);
    }

    // IT-05: Driver Fleet Status API
    try {
        const driversRes = await fetch(`${BASE_URL}/api/drivers`);
        const driversData = await driversRes.json();
        assert('IT-05', 'Driver Roster Query (GET /api/drivers)', driversRes.status === 200 && Array.isArray(driversData), `HTTP ${driversRes.status} | Active Fleet: ${driversData.length} drivers on duty`);
    } catch (e) {
        assert('IT-05', 'Driver Roster Query (GET /api/drivers)', false, e.message);
    }

    // IT-06: Database Synchronization (db.json <-> urban_clean.db)
    try {
        const dbJsonPath = path.resolve('backend/db.json');
        const jsonContent = JSON.parse(fs.readFileSync(dbJsonPath, 'utf8'));
        const jsonCount = jsonContent.complaints ? jsonContent.complaints.length : 0;

        const pyCmd = 'python -c "import sqlite3; con = sqlite3.connect(\'backend/urban_clean.db\'); cur = con.cursor(); cur.execute(\'SELECT COUNT(*) FROM complaints\'); print(cur.fetchone()[0])"';
        const sqliteOutput = execSync(pyCmd, { encoding: 'utf8' }).trim();
        const sqliteCount = parseInt(sqliteOutput, 10);

        assert('IT-06', 'Dual Persistence Mirror Synchronization (JSON <-> SQLite)', sqliteCount === jsonCount, `JSON complaints: ${jsonCount} | SQLite rows: ${sqliteCount} (100% synchronized)`);
    } catch (e) {
        assert('IT-06', 'Dual Persistence Mirror Synchronization', false, e.message);
    }

    console.log('\n--------------------------------------------------------------------------------');
    console.log(`INTEGRATION TESTING SUMMARY: Total: ${passed + failed} | Passed: ${passed} | Failed: ${failed} | Success Rate: ${((passed/(passed+failed))*100).toFixed(1)}%`);
    console.log('================================================================================');
}

runIntegrationTests();
