import json
import sqlite3
import os

backend_dir = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(backend_dir, 'db.json')
sqlite_path = os.path.join(backend_dir, 'urban_clean.db')

if not os.path.exists(json_path):
    exit(0)

try:
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    conn = sqlite3.connect(sqlite_path)
    cursor = conn.cursor()

    # 1. Complaints
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS complaints (
        id TEXT PRIMARY KEY, category TEXT, title TEXT, description TEXT,
        lat REAL, lng REAL, area TEXT, city TEXT, status TEXT,
        reportedBy TEXT, timeStr TEXT, photo TEXT, timestamp INTEGER
    )
    ''')
    cursor.execute("DELETE FROM complaints;")
    for c in data.get('complaints', []):
        cursor.execute('''
        INSERT OR REPLACE INTO complaints (id, category, title, description, lat, lng, area, city, status, reportedBy, timeStr, photo, timestamp)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            c.get('id'), c.get('category'), c.get('title'), c.get('description'),
            c.get('lat'), c.get('lng'), c.get('area'), c.get('city'),
            c.get('status'), c.get('reportedBy'), c.get('timeStr'), c.get('photo'),
            c.get('timestamp')
        ))

    # 2. Drivers
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS drivers (
        id TEXT PRIMARY KEY, name TEXT, status TEXT, vehicle TEXT,
        efficiency TEXT, distance TEXT, assignedComplaints TEXT
    )
    ''')
    cursor.execute("DELETE FROM drivers;")
    for d in data.get('drivers', []):
        cursor.execute('''
        INSERT OR REPLACE INTO drivers (id, name, status, vehicle, efficiency, distance, assignedComplaints)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (
            d.get('id'), d.get('name'), d.get('status'), d.get('vehicle'),
            d.get('efficiency'), d.get('distance'),
            json.dumps(d.get('assignedComplaints', []))
        ))

    # 3. Notifications
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS notifications (
        id TEXT PRIMARY KEY, type TEXT, message TEXT, timeStr TEXT
    )
    ''')
    cursor.execute("DELETE FROM notifications;")
    for n in data.get('notifications', []):
        cursor.execute('''
        INSERT OR REPLACE INTO notifications (id, type, message, timeStr)
        VALUES (?, ?, ?, ?)
        ''', (n.get('id'), n.get('type'), n.get('message'), n.get('timeStr')))

    # 4. Accounts
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS accounts (
        id TEXT PRIMARY KEY, name TEXT, email TEXT UNIQUE, role TEXT,
        vehicle TEXT, state TEXT, district TEXT, city TEXT,
        salt TEXT, passwordHash TEXT, createdAt TEXT
    )
    ''')
    cursor.execute("DELETE FROM accounts;")
    accounts_data = data.get('accounts', {})
    for role_group in ['citizens', 'drivers', 'admins']:
        for acc in accounts_data.get(role_group, []):
            cursor.execute('''
            INSERT OR REPLACE INTO accounts (id, name, email, role, vehicle, state, district, city, salt, passwordHash, createdAt)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                acc.get('id'), acc.get('name'), acc.get('email'), acc.get('role'),
                acc.get('vehicle', ''), acc.get('state', ''), acc.get('district', ''), acc.get('city', ''),
                acc.get('salt'), acc.get('passwordHash'), acc.get('createdAt')
            ))

    # 5. Driver routes
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS driver_routes (
        id INTEGER PRIMARY KEY AUTOINCREMENT, driverId TEXT, pointIndex INTEGER,
        label TEXT, lat REAL, lng REAL, savedAt TEXT
    )
    ''')
    cursor.execute("DELETE FROM driver_routes;")
    driver_routes_data = data.get('driverRoutes', {})
    for driver_id, points in driver_routes_data.items():
        for pt in points:
            cursor.execute('''
            INSERT OR REPLACE INTO driver_routes (driverId, pointIndex, label, lat, lng, savedAt)
            VALUES (?, ?, ?, ?, ?, ?)
            ''', (
                driver_id, pt.get('index'), pt.get('label'),
                pt.get('lat'), pt.get('lng'), pt.get('savedAt')
            ))

    conn.commit()
    conn.close()
except Exception as e:
    pass
