# UrbanClean: Complete Software Testing Process, Evidence & Audit Report

**Candidate:** Mr. Ayush Santosh Toraskar (CS-9147) | **Guide:** Prof. Aarti Gawai  
**Institutional Affiliation:** Modern Education Society's The D. G. Ruparel College of Arts, Science & Commerce  
**Academic Degree:** B.Sc. Computer Science (Semester-V, Academic Year 2026–2027)  
**Testing Execution Timestamp:** 2026-09-28 | **Testing Environment:** Localhost Node.js v24.18.1 / Windows 11  

---

## 1. PROJECT ARCHITECTURAL AUDIT & FEATURE DISCOVERY

### 1.1 Verified Architectural Foundations
- **Frontend Architecture:** Single-Page Application (SPA) architecture utilizing vanilla HTML5, CSS3 Glassmorphism (`styles.css`), and object-oriented DOM controller logic (`script.js`). Geospatial visualization is powered by the Leaflet.js v1.9.4 vector mapping library.
- **Backend Architecture:** RESTful micro-service API built on Node.js and Express.js (`server.js`) listening on `http://localhost:3000` (and `0.0.0.0:3000` for LAN access). Features native Multer multipart/form-data middleware for image ingestion.
- **Database Architecture:** Dual persistence architecture:
  1. *Primary Document Store:* `backend/db.json` providing immediate JSON read/write state persistence.
  2. *Relational Storage Mirror:* `backend/urban_clean.db` (SQLite 3), synchronized automatically via `backend/sync_sqlite.py` across five relational tables (`accounts`, `complaints`, `drivers`, `driver_routes`, `notifications`).
- **User Roles:** Strict Role-Based Access Control (RBAC) supporting three segregated roles: `citizen`, `driver`, and `admin`.

### 1.2 Feature Verification Checklist
#### Features Actually Available & Verified:
1. Multi-role user registration and cryptographic login (`POST /api/register`, `POST /api/login`)
2. Citizen complaint lodging with auto GPS detection and Leaflet click-to-pin coordinate binding (`citizen.html`)
3. Multi-category civic issue reporting (Garbage Overflow, Road Dumps, Blocked Drainage, Hazardous Waste)
4. Proof photo upload with Multer (5 MB limit and image MIME filtering)
5. Citizen "My Complaints" tracking table with real-time status badges (`Pending`, `In Progress`, `Completed`)
6. Driver workspace with vehicle assignment and on-duty status indicators (`driver.html`)
7. Driver collection point adding / pinning (up to 40 waypoints)
8. Haversine 1.0 km proximity boundary filtering for eligible nearby civic complaints
9. Greedy Nearest Neighbor TSP route optimization algorithm with public OSRM real-road geometry projection
10. Daily route locking / shift start with post-lock candidate deferral (`POST /api/driver/route/lock`)
11. Driver proof-of-cleanup upload (`PUT /api/complaints/:id/resolve`)
12. Admin command center with live KPI stat counters (`Reported Today`, `Pending`, `In Progress`, `Solved Today`)
13. On-duty driver fleet roster and jurisdiction monitoring map (`admin.html`)
14. 30-day compliance report export to CSV format (`btn-export-excel`)
15. Dual-database persistence and SQLite mirror synchronization (`sync_sqlite.py`)

#### Features Not Found / Out of Current Scope:
1. Automated email password reset / recovery workflow (manual admin credential issuance implemented)
2. WebSocket bi-directional push streams (client uses periodic HTTP fetch polling)
3. Native mobile compiled binaries (.apk / .ipa) — system operates as a responsive web application
4. Automated cloud CI/CD pipeline (deployment is locally hosted on Node.js/Express)

---

## 2. COMPREHENSIVE TEST CASE EXECUTION LOG (TC-01 TO TC-52)

| Test ID | Module | Test Scenario | Test Data | Expected Result | Actual Result | Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **TC-01** | Authentication | Citizen registration with valid credentials | Name: 'Aarav Sharma', Email: 'aarav.sharma@urbanclean.org', Password: 'Password@123', Role: 'citizen' | Account registered; HTTP 201 Created; record appended to `accounts` | As expected; account saved in `db.json` and SQLite `accounts` | **PASS** |
| **TC-02** | Authentication | Citizen login with valid credentials | Email: 'ayush@urbanclean.org', Password: 'Citizen@123' | Authenticated; session profile stored in localStorage; redirect to `citizen.html` | As expected; session stored, redirected | **PASS** |
| **TC-03** | Authentication | Citizen login with invalid password | Email: 'ayush@urbanclean.org', Password: 'WrongPassword999' | Authentication rejected; HTTP 401; error toast displayed | As expected; HTTP 401 returned | **PASS** |
| **TC-04** | Authentication | User logout and session termination | Active citizen session in localStorage | Session cleared from localStorage; redirected to `index.html` | As expected; localStorage item removed | **PASS** |
| **TC-05** | Validation | Registration password minimum length (<8 chars) | Password: 'short' (5 characters) | Client & server validation flags short password; submission blocked | As expected; validation message displayed | **PASS** |
| **TC-06** | Validation | Registration required fields missing | Name: '', Email: '', Password: 'Password@123' | HTML5 required constraint triggers; field highlighted | As expected; submission blocked | **PASS** |
| **TC-07** | UI | Citizen dashboard layout and component rendering | Authenticated Citizen session | Topbar, sidebar, complaint form, Leaflet map canvas render cleanly | As expected; responsive layout rendered | **PASS** |
| **TC-08** | Functional | Submit civic complaint with full details | Category: 'Garbage Overflow', Lat: 19.0544, Lng: 72.8295, Photo: valid JPG | Ticket generated (COMP-XXX); saved with status 'Pending' | As expected; ticket COMP-819 created | **PASS** |
| **TC-09** | Validation | Missing mandatory inputs on complaint submission | Category: null, Lat: null, Lng: null | Submission blocked; warnings alert user to select category & location | As expected; toast warning displayed | **PASS** |
| **TC-10** | Functional | Auto-detect GPS coordinates via W3C Geolocation | Browser Geolocation API | Exact latitude/longitude extracted to 6 decimals; pin placed on map | As expected; coordinates bound | **PASS** |
| **TC-11** | Functional | Interactive Leaflet map click-to-pin coordinate binding | Click on map canvas at (19.0544, 72.8295) | Draggable marker appears; latitude & longitude input boxes sync | As expected; inputs populated synchronously | **PASS** |
| **TC-12** | Functional | Attach proof photo via dropzone | File: 'waste.jpg' (1.5 MB, image/jpeg) | File accepted; thumbnail preview rendered; filename displayed | As expected; preview displayed | **PASS** |
| **TC-13** | Functional | View submitted complaints in tracking table | Citizen user with active complaints | Table renders ticket ID, category, date, location, status badge | As expected; tracking rows populated | **PASS** |
| **TC-14** | Security | Horizontal data isolation between citizens | Citizen A vs Citizen B | Citizen sees only their own complaints; backend filters by user ID | As expected; strict user isolation verified | **PASS** |
| **TC-15** | UI | Modal details view for individual complaint | Complaint ID: COMP-001 | Modal displays category, coordinates, address, and photo | As expected; details modal opens | **PASS** |
| **TC-16** | Functional | Complaint status transition tracking | COMP-001 lifecycle: Pending -> In Progress -> Completed | Status badges update dynamically with appropriate colors | As expected; color-coded badges rendered | **PASS** |
| **TC-17** | Functional | Complaint immutability policy enforcement | Submitted complaint record | Edit action disallowed after submission to preserve legal audit trail | As expected; fields remain read-only | **PASS** |
| **TC-18** | Security | Complaint delete prevention for non-admin users | Citizen session | No delete controls available on citizen UI; deletion forbidden | As expected; deletion disallowed | **PASS** |
| **TC-19** | Authentication | Driver login and vehicle assignment | Email: 'ramesh@urbanclean.org', Password: 'Driver@123' | Authenticated; vehicle MH-02-ES-4521 linked; redirect to `driver.html` | As expected; driver session initialized | **PASS** |
| **TC-20** | Functional | Driver workspace initialization | Authenticated Driver session | Driver avatar, duty toggle, collection points card, map load | As expected; workspace initialized | **PASS** |
| **TC-21** | Functional | Haversine 1.0 km proximity filter on complaints | Collection stops in Bandra; Complaints at 0.4 km vs 2.5 km | Complaint at 0.4 km displayed on map; complaint at 2.5 km excluded | As expected; proximity filter verified | **PASS** |
| **TC-22** | Functional | Resolve complaint with clean-site proof photo | COMP-001, clean photo upload | Photo stored in `uploads/`; status transitions to 'Completed' | As expected; resolved status saved | **PASS** |
| **TC-23** | UI | Route stop waypoint popup details | Waypoint #2 clicked on map | Popup displays landmark, category, distance, and sequence number | As expected; popup card rendered | **PASS** |
| **TC-24** | Authentication | Admin authentication and jurisdiction lock | Email: 'admin@urbanclean.org', Password: 'Admin@123' | Authenticated; locked to jurisdiction; redirect to `admin.html` | As expected; admin portal opened | **PASS** |
| **TC-25** | UI | Admin command center live KPI metrics | Database state: 5 complaints | KPI cards render accurate counts: Reported, Pending, Progress, Solved | As expected; KPI aggregates displayed | **PASS** |
| **TC-26** | Functional | View complaints across municipal jurisdiction | Filter: 'All' / 'Pending' | Table lists jurisdictional tickets with status tags | As expected; complaints listed | **PASS** |
| **TC-27** | Functional | Registered user directory management | Query registered accounts | Lists citizen & driver accounts with registration dates | As expected; accounts directory verified | **PASS** |
| **TC-28** | Functional | Driver roster shift status management | 3 drivers on duty | Roster shows Ramesh Kumar, Amit Patel, Sunil Shinde | As expected; roster cards rendered | **PASS** |
| **TC-29** | Functional | Assign complaint to specific collection driver | COMP-002 -> Driver Ramesh Kumar | Assigned driver ID updated; complaint visible in driver queue | As expected; assignment linked | **PASS** |
| **TC-30** | Functional | Administrative status override | Ticket COMP-003 status update | Admin updates status; change logged in complaint record | As expected; database status updated | **PASS** |
| **TC-31** | Functional | City-wide waste distribution map monitoring | Multi-ward active tickets | Markers plotted across Mumbai wards with status legend | As expected; markers rendered | **PASS** |
| **TC-32** | Functional | Export monthly compliance report to CSV | Click 'Export to Excel' | Browser downloads `UrbanClean_Monthly_Report_2026-09-28.csv` | As expected; CSV downloaded & toast shown | **PASS** |
| **TC-33** | Integration | Browser GPS coordinate accuracy | W3C Geolocation position | Latitude and longitude bound with 6-digit precision | As expected; 6-decimal precision bound | **PASS** |
| **TC-34** | UI | Status color coding on Leaflet map markers | Open, Pending, In Progress, Completed | Red (Open), Yellow (Pending), Blue (In Progress), Green (Completed) | As expected; colors distinct | **PASS** |
| **TC-35** | Integration | OpenStreetMap raster tile server integration | HTTPS OSM raster tiles | Tiles load smoothly across zoom levels 12 to 18 without network errors | As expected; 100% tile delivery | **PASS** |
| **TC-36** | Validation | Location permission denied fallback | Geolocation denied | Toast alerts user; map falls back to default city coordinates | As expected; graceful fallback | **PASS** |
| **TC-37** | Database | Persist user registration record | New account registration | Appended to `db.json` and mirrored to SQLite `accounts` table | As expected; PBKDF2 hash stored | **PASS** |
| **TC-38** | Database | Persist complaint with coordinates & image path | New complaint submission | Record written to `db.json` and SQLite `complaints` table | As expected; coordinates & photo path saved | **PASS** |
| **TC-39** | Database | Filter complaints via REST API query | `GET /api/complaints?city=Bandra` | Returns complaints belonging strictly to requested city | As expected; query filtered | **PASS** |
| **TC-40** | Database | Complaint resolution transaction | `PUT /api/complaints/:id/resolve` | Ticket updated with `status='Completed'` and `photo_after` | As expected; resolved record updated | **PASS** |
| **TC-41** | Database | Real-time dual persistence synchronization | Compare `db.json` vs `urban_clean.db` | Zero discrepancy: 5 complaints in JSON == 5 rows in SQLite | As expected; 100% sync confirmed | **PASS** |
| **TC-42** | Security | Reject authentication with non-existent user | Email: 'ghost@example.com', Password: 'RandomPass@123' | HTTP 401 Unauthorized; error message displayed; 0 session tokens | As expected; HTTP 401 returned | **PASS** |
| **TC-43** | Security | Block unauthorized direct URL access to admin | Direct request to `/admin.html` without session | Intercepted by page guard; redirected to `login.html?redirect=admin.html` | As expected; redirected immediately | **PASS** |
| **TC-44** | Security | Prevent access to another citizen's complaints | Citizen A headers requesting Citizen B records | Server filters results strictly by caller's user ID | As expected; horizontal access blocked | **PASS** |
| **TC-45** | Security | Cryptographic password hashing and salt verification | Direct inspection of stored accounts | 128-char PBKDF2/SHA-512 hashes with 16-byte random salts; 0 plaintext | As expected; all passwords cryptographically hashed | **PASS** |
| **TC-46** | Security | Session termination and localStorage cleanup | Driver clicks Logout | Session object purged; browser back button redirects to login | As expected; session destroyed | **PASS** |
| **TC-47** | UI | Navigation menu routing and anchor links | Navbar link clicks across portals | Target views load without broken routes or 404 errors | As expected; all navigation links valid | **PASS** |
| **TC-48** | Validation | XSS payload sanitization in text areas | Description: `<script>alert('XSS')</script>` | Script tags escaped to text entities; zero execution occurs | As expected; rendered safely as text | **PASS** |
| **TC-49** | UI | Form input validation error tooltips | Invalid email syntax in form | HTML5 validation tooltip prompts user to include '@' and domain | As expected; tooltip displayed | **PASS** |
| **TC-50** | UI | Multi-viewport responsive layout adaptation | Viewports: 375px (mobile), 768px (tablet), 1280px (desktop) | Glassmorphic cards adapt; sidebar collapses; zero horizontal overflow | As expected; responsive across breakpoints | **PASS** |
| **TC-51** | UI | Button hover states and loading transitions | Clicks on optimization and locking buttons | Visual feedback displayed; loading state shown during async API call | As expected; transitions smooth | **PASS** |
| **TC-52** | Validation | File upload type and size boundary constraints | Non-image file (`package-lock.json`), Image > 5MB | Upload rejected; Multer intercepts and returns HTTP 400 Bad Request | As expected; rejection enforced | **PASS** |

---

## 3. BUG & DEFECT TRACKING AUDIT REPORT

| Bug ID | Test ID | Description | Severity | Status | Actual Defect Root Cause | Fix & Retest Evidence |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **BUG-01** | TC-52 | Unhandled Multer file filter error returning raw HTTP 500 HTML stack trace on non-image upload | Medium | **Resolved & Retested** | Express lacked a 4-parameter error-handling middleware to intercept Multer's fileFilter `new Error('Only image files are allowed!')`. | Express global error middleware added to `server.js` catching `MulterError` and returning clean HTTP 400 JSON `{ "error": "Only image files are allowed!" }`. Retested successfully (S40 -> S41). |

---

## 4. PERFORMANCE & LOAD TESTING BENCHMARKS

### 4.1 Latency & Response Time Benchmark (20 Iterations per Endpoint)
- **Tool:** Node.js native `performance.now()` high-resolution timer.
- **Admin Stats API (`GET /api/admin/stats`):**
  - Average Latency: **21.10 ms**
  - Median Latency (p50): **10.53 ms**
  - Min Latency: **3.26 ms**
  - 95th Percentile (p95): **237.07 ms**
  - HTTP Success Rate: **100% (20/20 succeeded)**
- **Driver Roster API (`GET /api/drivers`):**
  - Average Latency: **12.31 ms**
  - Median Latency (p50): **15.46 ms**
  - Min Latency: **3.11 ms**
  - 95th Percentile (p95): **18.96 ms**
  - HTTP Success Rate: **100% (20/20 succeeded)**
- **Public Landing Page (`GET /index.html`):**
  - Average Latency: **11.76 ms**
  - Median Latency (p50): **14.58 ms**
  - Min Latency: **3.82 ms**
  - 95th Percentile (p95): **18.80 ms**
  - HTTP Success Rate: **100% (20/20 succeeded)**

### 4.2 High-Concurrency Load Testing Audit (Autocannon v8.0.0)
- **Target Endpoint:** `http://localhost:3000/api/admin/stats`
- **Concurrency:** 10 simultaneous HTTP client connections
- **Duration:** 10.05 seconds
- **Total Requests Handled:** **~7,000 requests**
- **Average Throughput:** **688.0 requests / second** (Peak: 741 req/sec)
- **Data Transfer Throughput:** **263.0 kB / second** (Total read: 2.63 MB)
- **Latency Distribution:**
  - 2.5%: 11 ms
  - 50.0% (Median): 14 ms
  - 97.5%: 19 ms
  - 99.0%: 22 ms
  - Max Latency: 48 ms
- **Error Count:** **0 errors, 0 timeouts, 0 non-2xx responses (100% Success Rate)**

---

## 5. COMPLETE SCREENSHOT EVIDENCE CATALOGUE (S01 TO S47)

All 47 screenshot files have been captured and verified in `d:\Urban clean\screenshots\evidence\`.

| ID | Screenshot Filename | Description | Test Category | Target Report Chapter |
| :--- | :--- | :--- | :--- | :--- |
| **S01** | `S01.png` | UrbanClean Application Running (Public Landing Page) | Deployment Verification | Chapter 7 & 10 |
| **S02** | `S02.png` | Registration Page & Form Controls | Citizen Functional Testing | Chapter 7 |
| **S03** | `S03.png` | Multi-Role Authentication Interface (Citizen Mode) | Authentication Testing | Chapter 7 |
| **S04** | `S04.png` | Citizen Dashboard & Personalized Workspace | Citizen Functional Testing | Chapter 7 |
| **S05** | `S05.png` | Complaint Submission Form with Category & Description | Citizen Functional Testing | Chapter 7 |
| **S06** | `S06.png` | Interactive Map GPS Pin Placement & Coordinate Binding | Geospatial Integration | Chapter 7 |
| **S07** | `S07.png` | Successful Complaint Submission Confirmation Toast | Citizen Functional Testing | Chapter 7 |
| **S08** | `S08.png` | My Complaints Real-Time Status Tracking Table | Citizen Functional Testing | Chapter 7 |
| **S09** | `S09.png` | Driver Dashboard & On-Duty Vehicle Status Card | Driver Functional Testing | Chapter 7 |
| **S10** | `S10.png` | Driver Collection Points & Nearby Complaints Map View | Geospatial Integration | Chapter 7 |
| **S11** | `S11.png` | Route Optimization Calculation (28% Efficiency Savings) | Route Optimization | Chapter 7 & 10 |
| **S12** | `S12.png` | Optimized Road Polyline Displayed on Leaflet Map | Route Optimization | Chapter 7 & 10 |
| **S13** | `S13.png` | Daily Route Lock & Shift Active Status Notice | Driver Functional Testing | Chapter 7 |
| **S14** | `S14.png` | Admin Command Center Real-Time KPI Stat Counters | Admin Functional Testing | Chapter 7 & 10 |
| **S15** | `S15.png` | Admin Monthly Waste Tracking Data Table | Admin Functional Testing | Chapter 7 |
| **S16** | `S16.png` | On-Duty Driver Fleet Roster & Shift Allocation | Admin Functional Testing | Chapter 7 |
| **S17** | `S17.png` | City-Wide Waste Monitoring Map & Ward Analytics | Admin Functional Testing | Chapter 7 & 10 |
| **S18** | `S18.png` | Export Monthly Report to Excel / CSV Confirmation | Admin Functional Testing | Chapter 7 |
| **S19** | `S19.png` | Valid Credentials Input Successfully Accepted | Black-Box Testing | Chapter 7 |
| **S20** | `S20.png` | Invalid Email Format Rejected with Validation Warning | Black-Box Testing | Chapter 7 |
| **S21** | `S21.png` | Empty Required Fields Validation Interception | Black-Box Testing | Chapter 7 |
| **S22** | `S22.png` | Invalid File Upload MIME Type Rejected | Black-Box Testing | Chapter 7 & 9 |
| **S23** | `S23.png` | Unit Testing Suite Execution Output (8/8 Passed) | Unit Testing | Chapter 7 |
| **S24** | `S24.png` | Frontend-to-Backend REST API Integration Output | Integration Testing | Chapter 7 |
| **S25** | `S25.png` | Dual Persistence (db.json <-> SQLite) Sync Audit | Database Integration | Chapter 7 |
| **S26** | `S26.png` | OSRM Road Polyline & TSP API Integration Workflow | Integration Testing | Chapter 7 |
| **S27** | `S27.png` | End-to-End Citizen Complaint Workflow Lifecycle Result | System Testing | Chapter 7 |
| **S28** | `S28.png` | End-to-End Driver Route Optimization & Lock Result | System Testing | Chapter 7 |
| **S29** | `S29.png` | End-to-End Admin Command Center Monitoring Result | System Testing | Chapter 7 |
| **S30** | `S30.png` | Duplicate Account Registration Rejection (HTTP 409) | Input Validation Testing | Chapter 9 |
| **S31** | `S31.png` | Complete Input Validation Success Verification | Input Validation Testing | Chapter 9 |
| **S32** | `S32.png` | PBKDF2 Cryptographic Session Authentication Payload | Security Testing | Chapter 9 |
| **S33** | `S33.png` | Unauthorized Direct URL Access Blocked & Redirected | Security Testing | Chapter 9 |
| **S34** | `S34.png` | Role-Based Access Control (RBAC) Cross-Role Guard | Security Testing | Chapter 9 |
| **S35** | `S35.png` | XSS Script Payload Sanitized into Safe Plain Text | Security Testing | Chapter 9 |
| **S36** | `S36.png` | REST API Latency Benchmark (Sub-25 ms Average) | Performance Testing | Chapter 9 & 10 |
| **S37** | `S37.png` | Autocannon High-Concurrency Load Test Configuration | Load Testing | Chapter 9 |
| **S38** | `S38.png` | Autocannon Live Concurrency Load Execution Progress | Load Testing | Chapter 9 |
| **S39** | `S39.png` | Autocannon Load Benchmark Summary (688 Req/Sec, 0 Errors)| Load Testing | Chapter 9 & 10 |
| **S40** | `S40.png` | Defect BUG-01: Raw 500 HTML Stack Trace on Bad Upload | Defect Tracking | Chapter 7 & 9 |
| **S41** | `S41.png` | Defect BUG-01 Retest: Clean HTTP 400 Bad Request JSON | Defect Tracking | Chapter 7 & 9 |
| **S42** | `S42.png` | Express.js REST Server Background Process Terminal | Deployment Verification | Chapter 7 |
| **S43** | `S43.png` | UrbanClean Running on Documented Local URL | Deployment Verification | Chapter 7 |
| **S44** | `S44.png` | GitHub Repository Remote & Main Branch Configuration | Version Control Audit | Chapter 7 |
| **S45** | `S45.png` | GitHub Project File Structure (`git ls-tree`) | Version Control Audit | Chapter 7 |
| **S46** | `S46.png` | Source Code Version Control Inspection (HEAD Commit) | Version Control Audit | Chapter 7 |
| **S47** | `S47.png` | Git Commit History Timeline & Provenance Audit Log | Version Control Audit | Chapter 7 |

---

## 6. FINAL TESTING SUMMARY METRICS
- **Total Test Cases Executed:** 52 Functional (TC-01 to TC-52) + 8 Unit (UT-01 to UT-08) + 6 Integration (IT-01 to IT-06) = **66 Total Tests**
- **Passed:** **66**
- **Failed:** **0** (after resolving defect BUG-01)
- **Blocked:** **0**
- **Not Executed:** **0**
- **Overall Testing Success Rate:** **100.0%**
- **Total Screenshots Captured:** **47** (S01 to S47, 8.70 MB total size)
