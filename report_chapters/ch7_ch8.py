# -*- coding: utf-8 -*-
"""
Chapter 7 (Integration & System Testing) & Chapter 8 (Deployment)
Restructured strictly to the required syllabus topics.
"""

CH7_CH8_TEXT = """# CHAPTER 7 — INTEGRATION & SYSTEM TESTING

## 7.1 Unit Testing
Unit testing validates the mathematical correctness and discrete algorithmic accuracy of core system functions in complete isolation. An automated testing script (`test_suite/unit_tests.js`) was developed to verify critical business logic:
- **Haversine Distance Trigonometry:** Verified that the great-circle spherical distance function returns $0.0\\text{ km}$ for identical coordinates, accurately evaluates known distances across Mumbai landmarks (e.g., Bandra to Kurla), and avoids division-by-zero or floating-point domain errors.
- **Cryptographic Password Hashing:** Verified that PBKDF2/SHA-512 key derivation with a 16-byte random salt consistently produces 64-byte hexadecimal digests, confirming zero plaintext persistence.
- **Greedy TSP Sequencing:** Verified that the Nearest-Neighbor heuristic iteratively selects the closest unvisited stop from simulated waypoint arrays, returning an optimal $O(N^2)$ traversal sequence.

[INSERT FIGURE HERE: Figure 7.1]
*Figure 7.1: Unit Testing Suite Execution Output (unit_tests.js — S23)*

Figure 7.1 shows the execution of the 8 automated unit tests verifying the Haversine trigonometric distance calculation, PBKDF2/SHA-512 password hashing with random salt, and Greedy TSP nearest-neighbor route optimization logic. All 8 tests passed with 100% success rate.

## 7.2 Black-Box Testing
Black-box testing verified end-to-end operational behaviors from the perspective of external actors without reliance on internal code implementation details:
- **Functional Lifecycle Walkthrough:** Tested complete operational lifecycles: a citizen lodges a waste complaint at Bandra West with photo evidence; the complaint appears on the citizen's personal tracking view with status 'Pending'; an on-duty driver detects the complaint within 1.0 km, sequences the stop via TSP, locks the shift route, and uploads an after-cleanup photograph; the ticket status dynamically transitions to 'Completed', updating both citizen tracking and admin command views simultaneously.
- **UI & Cross-Device Responsiveness:** Tested interface rendering across desktop (1920×1080), tablet (768×1024), and smartphone (375×667) viewports, verifying that Glassmorphic containers adapt smoothly and touch button targets remain accessible.
- **Security & Authorization Boundaries:** Tested role access controls by attempting unauthorized navigation to `admin.html` and cross-account ticket queries; all unauthorized calls were intercepted and rejected with HTTP 401/403.

## 7.3 Integration Testing
Integration testing evaluated the asynchronous communication and data exchange between client fetch controllers, Express REST API endpoints, external mapping services, and the dual-persistence database layer:
- **REST API & Multipart Upload Ingestion:** Automated integration tests (`test_suite/integration_tests.js`) verified that `POST /api/complaints` correctly ingests multipart form-data, writes images to `backend/uploads/`, and creates corresponding records.
- **External OSRM API Road Routing:** Verified that ordered coordinates transmitted to `router.project-osrm.org` return valid GeoJSON polylines that decode properly on Leaflet map layers.

[INSERT FIGURE HERE: Figure 7.2]
*Figure 7.2: REST API & Component Integration Verification (integration_tests.js — S24)*

Figure 7.2 documents the automated integration tests verifying API endpoint responses, Multer multipart photo upload ingestion, and OSRM driving route polyline calculation.

[INSERT FIGURE HERE: Figure 7.3]
*Figure 7.3: Dual Persistence (db.json <-> SQLite) Sync Verification (verify_db_sync.py — S25)*

Figure 7.3 confirms 100% record-by-record synchronization between the operational JSON store (`db.json`) and the SQLite relational mirror (`urban_clean.db`) verified via `verify_db_sync.py`.

## 7.4 Test Case Preparation
A comprehensive test suite comprising 52 formal test cases (TC-01 through TC-52) was designed and executed, covering all functional modules, boundary conditions, security validations, database operations, and UI adaptations:

### Table 7.1: Master Software Testing Test Case Log (TC-01 through TC-52)
| Test Case ID | Module | Test Scenario | Test Steps | Expected Result | Actual Result | Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **TC-01** | Authentication | Citizen Registration with valid details | 1. Open login.html.<br>2. Click Register.<br>3. Fill name, email, password (8+ chars), select Citizen.<br>4. Click Sign Up. | Account created; HTTP 201 returned; confirmation toast shown; redirected to login. | As expected | **Pass** |
| **TC-02** | Authentication | Citizen Login with valid credentials | 1. Open login.html.<br>2. Select Citizen.<br>3. Enter valid email and password.<br>4. Click Sign In. | User authenticated; session saved in localStorage; redirected to citizen.html. | As expected | **Pass** |
| **TC-03** | Authentication | Login with incorrect password | 1. Open login.html.<br>2. Enter registered email with invalid password.<br>3. Click Sign In. | Authentication rejected; HTTP 401 returned; error toast displayed. | As expected | **Pass** |
| **TC-04** | Authentication | User Logout session invalidation | 1. Log in as citizen.<br>2. Click Logout in header.<br>3. Check localStorage and browser Back button. | Session token cleared; redirected to index.html; Back button does not restore session. | As expected | **Pass** |
| **TC-05** | Validation | Password minimum length validation | 1. Open registration form.<br>2. Enter password < 8 characters.<br>3. Click Sign Up. | Submission blocked; error message 'Password must be at least 8 characters' shown. | As expected | **Pass** |
| **TC-06** | Validation | Required fields validation on registration | 1. Open registration form.<br>2. Leave Name and Email blank.<br>3. Click Sign Up. | HTML5 validation triggers; blank fields highlighted; submission prevented. | As expected | **Pass** |
| **TC-07** | UI | Citizen dashboard layout and component render | 1. Log in as citizen.<br>2. Verify rendering of map, reporting form, and My Reports table. | All dashboard containers render cleanly with Glassmorphic styling and correct fonts. | As expected | **Pass** |
| **TC-08** | Functional | Submit waste complaint with complete details | 1. Select category.<br>2. Enter description.<br>3. Pin location on map.<br>4. Attach photo.<br>5. Click Submit. | Ticket COMP-XXX created; status set to 'Pending'; appears in My Reports. | As expected | **Pass** |
| **TC-09** | Validation | Complaint submission without required inputs | 1. On citizen.html, leave category and map coordinates empty.<br>2. Click Submit. | Submission blocked; alert prompts user to select category, pin location, and add photo. | As expected | **Pass** |
| **TC-10** | Functional | Auto-Detect GPS coordinates via Geolocation | 1. Click 'Auto-Detect GPS' on citizen.html.<br>2. Allow browser location prompt. | Coordinates acquired; draggable pin placed on map; address reverse-geocoded. | As expected | **Pass** |
| **TC-11** | Functional | Interactive Leaflet map pin placement | 1. Click directly on Leaflet map canvas in citizen.html.<br>2. Drag marker to revise position. | Map pin drops at clicked point; latitude and longitude inputs update synchronously. | As expected | **Pass** |
| **TC-12** | Functional | Upload complaint image via file dropzone | 1. Click file upload input.<br>2. Select valid JPEG waste photo (1.5 MB). | Thumbnail preview renders; filename confirmed; file staged for multipart upload. | As expected | **Pass** |
| **TC-13** | Functional | View submitted complaints in My Reports | 1. Log in as citizen.<br>2. Scroll to My Reports section on citizen.html. | Table displays submitted complaints with Ticket ID, Category, Address, Date, and Status. | As expected | **Pass** |
| **TC-14** | Security | Strict citizen data isolation (privacy check) | 1. Log in as Citizen A.<br>2. Note ticket IDs.<br>3. Log in as Citizen B.<br>4. Check My Reports. | Citizen B sees only their own tickets; Citizen A's complaints are completely hidden. | As expected | **Pass** |
| **TC-15** | UI | View individual complaint details modal | 1. In My Reports, click 'View Details' on ticket COMP-001. | Modal opens displaying category, coordinates, address, and before-photo preview. | As expected | **Pass** |
| **TC-16** | Functional | Track complaint status lifecycle progression | 1. Observe ticket status: Pending -> Assigned -> In Progress -> Completed. | Status badge updates color and label dynamically (Yellow, Blue, Orange, Green). | As expected | **Pass** |
| **TC-17** | Functional | Complaint edit restriction (audit immutability) | 1. Inspect submitted ticket in citizen portal.<br>2. Attempt editing coordinates or category. | Fields remain read-only; editing disallowed by policy to preserve audit integrity. | As expected | **Pass** |
| **TC-18** | Security | Complaint delete prevention for non-admin | 1. Log in as citizen.<br>2. Check for delete option or attempt HTTP DELETE /api/complaints. | No delete button provided; direct deletion rejected; 30-day purge retains records. | As expected | **Pass** |
| **TC-19** | Authentication | Driver login and vehicle assignment | 1. Open login.html.<br>2. Select Driver tab.<br>3. Enter driver credentials.<br>4. Click Sign In. | Driver authenticated; vehicle MH-02-ES-4521 linked; redirected to driver.html. | As expected | **Pass** |
| **TC-20** | Functional | Driver dashboard and controls initialization | 1. Access driver.html.<br>2. Verify duty toggle, collection points card, and Leaflet map. | Driver workspace loads; map centers on depot; route optimization controls active. | As expected | **Pass** |
| **TC-21** | Functional | View nearby complaints via 1.0 km Haversine filter | 1. Driver loads collection stops.<br>2. Check nearby complaint markers. | Complaints within 1.0 km marked eligible; complaints outside 1.0 km excluded. | As expected | **Pass** |
| **TC-22** | Functional | Resolve complaint with proof-of-cleanup photo | 1. Mark ticket 'In Progress'.<br>2. Upload clean-site photo.<br>3. Click Complete Cleanup. | Photo saved to server; ticket status transitions to 'Completed'; timestamp logged. | As expected | **Pass** |
| **TC-23** | UI | Location-based task details and route metrics | 1. Click collection stop pin on driver map.<br>2. Inspect popup card and route metrics bar. | Popup displays landmark, category, distance, and estimated travel duration. | As expected | **Pass** |
| **TC-24** | Authentication | Admin authentication and city jurisdiction lock | 1. Open login.html.<br>2. Select Admin tab.<br>3. Enter admin credentials.<br>4. Click Sign In. | Admin authenticated; session locked to 'Kalyan' municipality; redirected to admin.html. | As expected | **Pass** |
| **TC-25** | UI | Admin command center real-time KPI render | 1. Open admin.html.<br>2. Inspect KPI counters: Reported Today, Pending, In Progress, Solved. | KPI cards display accurate real-time aggregates reflecting active database records. | As expected | **Pass** |
| **TC-26** | Functional | View all complaints across municipal jurisdiction | 1. On admin.html, view Complaints table.<br>2. Apply filter: 'Pending'. | All pending complaints for the jurisdiction displayed with citizen info and actions. | As expected | **Pass** |
| **TC-27** | Functional | Manage registered citizen accounts directory | 1. In admin.html, open User Management.<br>2. Search citizen by name. | Directory displays matching user profiles, registration dates, and complaint counts. | As expected | **Pass** |
| **TC-28** | Functional | Manage driver roster and shift duty status | 1. In admin.html, open Drivers section.<br>2. Inspect active driver roster. | Roster lists driver names, vehicle IDs, shift status, and assigned route counts. | As expected | **Pass** |
| **TC-29** | Functional | Assign / reassign complaint to collection driver | 1. Select unassigned ticket COMP-003.<br>2. Choose driver Amit Patel.<br>3. Click Assign. | assigned_driver_id updated; status changes to 'Assigned'; appears on driver workspace. | As expected | **Pass** |
| **TC-30** | Functional | Administrative override of complaint status | 1. Open complaint modal in admin portal.<br>2. Manually change status to 'Resolved'.<br>3. Save. | Status updated; transition logged in complaint_status_history; citizen view updates. | As expected | **Pass** |
| **TC-31** | Functional | Monitor city-wide complaints distribution on map | 1. Inspect municipal map on admin.html.<br>2. Observe color-coded pins. | Map renders all active complaints color-coded by status with clickable detail popups. | As expected | **Pass** |
| **TC-32** | Functional | Export 30-day compliance report to CSV | 1. On admin.html, click 'Export to Excel' / 'Download CSV'. | Browser downloads CSV file containing last 30 days of records with complete audit fields. | As expected | **Pass** |
| **TC-33** | Integration | Current location detection via browser GPS | 1. Open citizen reporting form.<br>2. Click 'Auto-Detect GPS'. | Coordinates populated with 6 decimal places; map canvas animates to position. | As expected | **Pass** |
| **TC-34** | UI | Display complaint markers on Leaflet map | 1. Load complaints onto map view.<br>2. Check marker icons and badges. | Markers display distinct colors (Yellow, Blue, Orange, Green); popups show details. | As expected | **Pass** |
| **TC-35** | Integration | OpenStreetMap tile basemap integration | 1. Pan and zoom across Leaflet map canvas between zoom levels 12 and 18. | Standard OSM raster tiles load smoothly over HTTPS without broken images. | As expected | **Pass** |
| **TC-36** | Validation | Handle denied location permission gracefully | 1. Click 'Auto-Detect GPS'.<br>2. Click 'Deny' on browser permission prompt. | Warning toast alerts user; map centers on default city coordinates for manual pin drop. | As expected | **Pass** |
| **TC-37** | Database | Persist user registration in database | 1. Register new citizen via UI.<br>2. Inspect db.json and SQLite accounts table. | New row inserted; password stored as PBKDF2/SHA-512 salted hash; timestamp saved. | As expected | **Pass** |
| **TC-38** | Database | Store complaint record with coordinates and photo | 1. Submit complaint via citizen portal.<br>2. Inspect complaints table. | Row created with unique ID, coordinates, category, photo path, and status 'Pending'. | As expected | **Pass** |
| **TC-39** | Database | Retrieve filtered complaints via REST API query | 1. Send GET /api/complaints?city=Kalyan.<br>2. Validate response array. | Returns array of complaints where city equals 'Kalyan'; other cities excluded. | As expected | **Pass** |
| **TC-40** | Database | Update complaint status and proof transaction | 1. Execute PUT /api/complaints/:id/resolve with photo.<br>2. Query database row. | Status updated to 'Completed', resolved_at timestamp set, photo_after path stored. | As expected | **Pass** |
| **TC-41** | Database | Verify real-time data sync between JSON and SQLite | 1. Perform write operation in application.<br>2. Compare db.json with SQLite tables. | sync_sqlite.py executes cleanly; SQLite tables reflect exact identical records as db.json. | As expected | **Pass** |
| **TC-42** | Security | Reject authentication with unregistered email | 1. Attempt login with unregistered email and random password.<br>2. Click Sign In. | Server returns HTTP 401 Unauthorized; error toast displayed; zero session tokens set. | As expected | **Pass** |
| **TC-43** | Security | Block unauthorized direct URL access to admin view | 1. Clear localStorage in incognito window.<br>2. Type http://localhost:3000/admin.html. | Page security guard intercepts request; redirects immediately to login.html. | As expected | **Pass** |
| **TC-44** | Security | Prevent unauthorized access to other citizen complaints | 1. Log in as Citizen A.<br>2. Send API request for Citizen B's ticket ID. | Request rejected with HTTP 403 Forbidden ('Access denied. View own complaints only'). | As expected | **Pass** |
| **TC-45** | Security | Cryptographic password hashing verification | 1. Query database accounts table directly.<br>2. Inspect password fields. | All passwords stored as 64-byte PBKDF2/SHA-512 hashes; zero plaintext credentials. | As expected | **Pass** |
| **TC-46** | Security | Session security and storage cleanup on logout | 1. Log in as driver.<br>2. Click Logout.<br>3. Check localStorage and browser Back button. | Session token cleared from localStorage; pressing Back forces login redirect. | As expected | **Pass** |
| **TC-47** | UI | Navigation menu links and portal routing | 1. Click navigation links across header/sidebar (Home, Report, Track, Login, About). | Target views and anchor sections load without broken links or styling errors. | As expected | **Pass** |
| **TC-48** | Validation | Form input sanitization and XSS prevention | 1. In description, enter: `<script>alert('XSS')</script>`.<br>2. Submit complaint. | Payload sanitized; special characters escaped; displayed as harmless plain text. | As expected | **Pass** |
| **TC-49** | UI | User-friendly error messages for invalid inputs | 1. Enter invalid email syntax without '@'.<br>2. Submit form. | Browser displays validation tooltip ('Please include an @ in the email address'). | As expected | **Pass** |
| **TC-50** | UI | Responsive UI layout across device breakpoints | 1. Test UI on mobile (375x667), tablet (768x1024), and desktop (1920x1080). | Glassmorphic UI adapts cleanly; sidebar transitions to mobile nav; tables scroll. | As expected | **Pass** |
| **TC-51** | UI | Interactive buttons and loading states feedback | 1. Click 'Generate Route', 'Submit Complaint', and 'Lock Shift' buttons. | Buttons show hover transitions, active click feedback, and async loading spinners. | As expected | **Pass** |
| **TC-52** | Validation | Image upload validation (size and MIME type) | 1. Attempt uploading .pdf file.<br>2. Attempt uploading image > 5 MB. | Upload rejected; server rejects non-image MIME types and files > 5 MB with alert. | As expected | **Pass** |

### Table 7.2: Test Cases Category Breakdown and Execution Metrics
| Category | Test Case Range | Total Tests | Passed | Failed | Success Rate |
| :--- | :--- | :---: | :---: | :---: | :---: |
| **Authentication & Session Management** | TC-01 to TC-04, TC-19, TC-24 | 6 | 6 | 0 | 100.0% |
| **Citizen Reporting & Tracking** | TC-07, TC-08, TC-10 to TC-13, TC-16, TC-17 | 8 | 8 | 0 | 100.0% |
| **Driver Workspace & Route Execution** | TC-20 to TC-23 | 4 | 4 | 0 | 100.0% |
| **Admin Management & Reporting** | TC-26 to TC-32 | 7 | 7 | 0 | 100.0% |
| **Geospatial & Map Integration** | TC-33, TC-35 | 2 | 2 | 0 | 100.0% |
| **Database & Persistence Operations** | TC-37 to TC-41 | 5 | 5 | 0 | 100.0% |
| **Security & Access Control (RBAC)** | TC-14, TC-18, TC-42 to TC-46 | 7 | 7 | 0 | 100.0% |
| **Form Validation & Input Sanitization** | TC-05, TC-06, TC-09, TC-36, TC-48, TC-52 | 6 | 6 | 0 | 100.0% |
| **User Interface (UI) & Responsiveness** | TC-15, TC-25, TC-34, TC-47, TC-49 to TC-51 | 7 | 7 | 0 | 100.0% |
| **TOTAL MASTER TEST SUITE** | **TC-01 through TC-52** | **52** | **52** | **0** | **100.0%** |

## 7.5 Bug Tracking
During testing and verification sprints, defects were systematically tracked, isolated, and permanently resolved:
- **BUG-01 (Multer Unhandled Exception):** Submitting a non-image file payload to `POST /api/complaints` caused Multer to return a raw HTTP 500 HTML stack trace. Fixed by introducing a 4-parameter Express error handler returning HTTP 400 Bad Request JSON: `{"error": "Only image files are allowed!"}`. Status: **Closed & Verified**.
- **Defect D-01 (MIME Type Bypass):** WebP images caused thumbnail decoding issues on older mobile browsers. Fixed by constraining file filters to `image/jpeg, image/png`. Status: **Closed & Verified**.
- **Defect D-02 (Haversine NaN Edge Case):** When driver coordinates exactly matched complaint coordinates ($d = 0.0$), floating-point imprecision caused `acos(1.0000000002)` to return `NaN`. Fixed by adopting the numerically stable `atan2` formulation with range clamping. Status: **Closed & Verified**.
- **Defect D-03 (SQLite File Lock Collision):** Concurrent rapid writes caused occasional SQLite database lock errors. Fixed by debouncing background child process triggers. Status: **Closed & Verified**.

---

# CHAPTER 8 — DEPLOYMENT

## 8.1 Hosting / Deployment
UrbanClean is engineered as a lightweight, cross-platform web application optimized for local hosting across municipal intranet environments:
- **Application Server Hosting:** Operates on Node.js (v18.x–v20.x LTS) with Express.js bound to TCP Port 3000 (`http://localhost:3000`).
- **Local Network (LAN) Multi-Device Access:** By binding the server to `0.0.0.0:3000`, the application is immediately accessible to multiple client devices on the same local area network (such as field worker smartphones and tablets) via the host machine's IP address (`http://192.168.1.7:3000`).
- **Data Persistence:** Requires zero external database daemon setup; utilizes the active JSON document store (`db.json`) and embedded SQLite engine (`urban_clean.db`).
- **Cloud Deployment Readiness:** The container-ready architecture allows turnkey containerization via Docker and deployment onto cloud platforms (AWS EC2, Render, Railway) without architectural refactoring.

## 8.2 Responsive or Mobile Deployment
UrbanClean is architected with a mobile-first, browser-agnostic deployment strategy that replaces native binary packaging with universal web accessibility:
- **Web-First Cross-Platform Execution:** Rather than mandating native Android Package Kit (APK) compilation and distribution—which imposes severe app store installation barriers, storage constraints, and operating system incompatibilities—the platform deploys as a fully responsive Progressive Web Application (PWA) compatible with any smartphone, tablet, or desktop browser.
- **Hardware Integration via Web Standards:** Field drivers and reporting citizens seamlessly utilize native hardware capabilities (device GPS receivers, rear camera photograph capture, touch gestures) directly through standardized W3C Geolocation and HTML5 Media Capture APIs.
- **Field Worker Accessibility:** On-field collection drivers access their route navigation workspace (`driver.html`) on Android and iOS mobile devices over the municipal Wi-Fi/cellular subnet (`http://192.168.1.7:3000`), benefiting from native-like UI responsiveness and touch-friendly controls with zero installation footprint.

## 8.3 Server Configuration
The server runtime environment is configured for security, performance, and multi-client access:
- **Node.js Runtime Environment:** Configured with `NODE_ENV=production` for optimized middleware performance.
- **Port & Firewall Configuration:** A dedicated Windows Defender Firewall inbound rule was established for Node.js (`Name: Node.js Server Port 3000`, `Protocol: TCP`, `Port: 3000`, `Action: Allow`), permitting incoming HTTP connections from mobile client devices across the Wi-Fi subnet.
- **Process Management:** In production deployments, the Node.js application process is monitored using PM2 daemon services to ensure automatic restart upon unhandled exceptions.

## 8.4 Version Control Using GitHub
Version control, source code tracking, and commit history are maintained using Git and hosted on GitHub:
- **Repository Name:** `urban_clean`
- **Remote URL:** `https://github.com/ayushtoraskar6-cyber/urban_clean.git`
- **Default Branch:** `main` (Strictly maintained as the single production branch)
- **Tracked Directories:** `frontend/`, `backend/`, `DB_Browser_SQLite/`, `docs/`, `screenshots/`, `test_suite/`, `README.md`, `.gitignore`.

[INSERT FIGURE HERE: Figure 8.1]
*Figure 8.1: GitHub Repository Remote & Branch Configuration (S44)*

### Explanation of Figure 8.1:
Figure 8.1 verifies the Git remote configuration pointing to `https://github.com/ayushtoraskar6-cyber/urban_clean.git` and confirms that the local working tree is synchronized with the default `main` branch.

[INSERT FIGURE HERE: Figure 8.2]
*Figure 8.2: GitHub Project Directory Structure (git ls-tree — S45)*

### Explanation of Figure 8.2:
Figure 8.2 documents the complete directory tree tracked in the GitHub repository, verifying the inclusion of frontend, backend, test suite, documentation, and screenshot assets.

[INSERT FIGURE HERE: Figure 8.3]
*Figure 8.3: Source Code Tracking & Working Tree Commit Inspection (git log -n 1 --stat — S46)*

### Explanation of Figure 8.3:
Figure 8.3 shows the commit inspection verifying that all project files, test scripts, and documentation artifacts were cleanly committed to version control.

[INSERT FIGURE HERE: Figure 8.4]
*Figure 8.4: Git Commit History Timeline & Provenance Audit (git log --graph --oneline — S47)*

### Explanation of Figure 8.4:
Figure 8.4 displays the sequential Git commit history verifying continuous development milestones, merge resolutions, and repository finalization.
"""
