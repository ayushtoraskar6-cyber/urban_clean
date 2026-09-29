# -*- coding: utf-8 -*-
"""
Chapter 5 (System Architecture Design) & Chapter 6 (Application Development)
Structured strictly according to the required academic format.
"""

CH5_CH6_TEXT = r"""# CHAPTER 5 — SYSTEM ARCHITECTURE DESIGN

## 5.1 Overall System Architecture
The system architecture of **UrbanClean** is engineered around a modern, decoupled, multi-tier client-server paradigm designed for high availability, low latency, and zero infrastructure capital expense. The platform coordinates civic grievance reporting, driver fleet route optimization, and municipal administrative governance through an integrated, asynchronous pipeline.

### Architectural Flow:
The end-to-end operational processing flow proceeds sequentially across five architectural tiers:

$$\text{User / Client Device} \longrightarrow \text{Frontend UI} \longrightarrow \text{Backend / Express Server} \longrightarrow \text{API / Business Logic} \longrightarrow \text{Database Storage}$$

1. **User / Client Device Tier:** Stakeholders (Citizens, Drivers, Municipal Administrators, and Public Guests) interact with the application using standard desktop web browsers (Google Chrome, Microsoft Edge, Mozilla Firefox) or mobile smartphone viewports without requiring dedicated native app installation.
2. **Frontend Presentation Tier:** Built as a responsive Single-Page Application (SPA) using semantic HTML5, CSS3 Custom Properties styled with a modern translucent Glassmorphism design system, and modular JavaScript (ES6+) client controllers (`script.js`). Geospatial mapping is rendered via the lightweight Leaflet.js (v1.9.4) engine.
3. **Backend / Express Server Tier:** An asynchronous, event-driven Node.js runtime environment running an Express.js HTTP server (`backend/server.js`) listening on TCP Port 3000. It manages incoming HTTP requests, enforces Cross-Origin Resource Sharing (`cors`), parses JSON/URL-encoded bodies, and intercepts multipart form-data via `multer`.
4. **API / Business Logic Tier:** Encapsulates the core algorithmic computation and validation services:
   - *Authentication Service:* Cryptographic PBKDF2/SHA-512 password hashing with 16-byte random salts.
   - *Geospatial Filtering Engine:* Spherical Haversine distance calculator evaluating a 1.0 km proximity boundary.
   - *Fleet Route Optimizer:* Internal Greedy Nearest-Neighbor Traveling Salesperson Problem (TSP) algorithm that orders collection waypoints in $O(N^2)$ time.
   - *Daily Route-Lock Engine:* Shift stabilization controller that snapshots active driver routes and defers late submissions to tomorrow's queue.
   - *Municipal Analytics Engine:* Ward-locked KPI aggregation and 30-day compliance report generation.
5. **External Microservices Tier (Actively Utilized in Project):**
   - *OpenStreetMap (OSM) Tile Servers:* Provides global, royalty-free raster map tiles streamed over HTTPS for basemap visualization.
   - *Project-OSRM Driving Engine (`router.project-osrm.org`):* Dedicated road routing service that converts ordered TSP waypoints into street-level turn-by-turn navigation polylines and road travel distances.
   - *OSM Nominatim API:* Provides reverse geocoding to resolve GPS latitude and longitude coordinates into human-readable street addresses.
6. **Persistence Tier:** A dual-persistence storage architecture comprising an active in-memory and disk-backed JSON document store (`backend/db.json`) mirrored in real time into an embedded relational SQLite database (`backend/urban_clean.db`) via an automated Python synchronization daemon (`backend/sync_sqlite.py`).

---

## 5.2 Frontend Architecture and Prototype
The frontend architecture is organized around modular Single-Page Application (SPA) views governed by client-side state managers in `script.js`. Prior to full full-stack deployment, comprehensive high-fidelity interface prototypes were constructed to define the visual layout, user experience (UX) workflows, and role-based interaction boundaries across all twelve system interfaces.

Below, each of the twelve authoritative interface prototypes is documented in the standardized screen-by-screen specification format:

### 5.2.1 Prototype 1 — Public Landing Page
- **Figure Number:** Figure 5.1
- **Prototype Title:** UrbanClean Public Landing Page Prototype
- **Purpose of the Screen:** Serves as the public-facing gateway for civic visitors, presenting high-level municipal cleanliness statistics, system objectives, and quick navigation anchors to civic reporting and authentication.
- **Intended User / Role:** General Public, Civic Observers, and Unauthenticated Guests.
- **Main UI Components:** Glassmorphic header navigation bar, Hero banner with call-to-action buttons ("Report Waste", "Sign In"), real-time municipal KPI counter cards (Total Issues Resolved, Active Reports, Cleanliness Rating), and educational feature summary cards.
- **Main User Action / Workflow:** Visitor arrives at `index.html`, reviews live municipal sanitation metrics, and clicks either "Report Waste" to navigate to civic incident logging or "Login" to access role-segregated portals.

[INSERT FIGURE HERE: Figure 5.1]
*Figure 5.1: UrbanClean Public Landing Page Prototype*

### 5.2.2 Prototype 2 — Multi-Role Login Portal
- **Figure Number:** Figure 5.2
- **Prototype Title:** UrbanClean Multi-Role Unified Authentication Portal Prototype
- **Purpose of the Screen:** Provides a secure, centralized authentication gateway enforcing role-based access control (RBAC) across Citizens, Drivers, and Municipal Administrators.
- **Intended User / Role:** Citizens, Collection Drivers, and Municipal Administrators.
- **Main UI Components:** Segmented tab selector (Citizen / Driver / Admin), email address and password inputs, role-specific badge indicators, "Remember Me" toggle, and "Sign In" action button.
- **Main User Action / Workflow:** User selects their registered stakeholder role tab, inputs credentials, and submits the form; the client controller dispatches `POST /api/login`, validates the returned PBKDF2 credential token, stores session metadata in `localStorage`, and redirects to the appropriate portal.

[INSERT FIGURE HERE: Figure 5.2]
*Figure 5.2: UrbanClean Multi-Role Unified Authentication Portal Prototype*

### 5.2.3 Prototype 3 — Citizen Registration
- **Figure Number:** Figure 5.3
- **Prototype Title:** UrbanClean Citizen Registration Prototype
- **Purpose of the Screen:** Enables new residents to create a verified civic account bound to their residential municipal ward.
- **Intended User / Role:** Unregistered Community Residents / Citizens.
- **Main UI Components:** Input fields for Full Name, Email Address, Contact Number, Password (with 8+ character validation indicators), Confirm Password, and Municipal Jurisdiction dropdown (e.g., Kalyan, Bandra, Thane).
- **Main User Action / Workflow:** Citizen completes all required demographic and security fields, client-side validation verifies password criteria, and the form posts to `POST /api/register`, returning an auto-assigned account identifier (e.g., `CIT-702`) and redirecting to login.

[INSERT FIGURE HERE: Figure 5.3]
*Figure 5.3: UrbanClean Citizen Registration Prototype*

### 5.2.4 Prototype 4 — Citizen Waste Reporting
- **Figure Number:** Figure 5.4
- **Prototype Title:** UrbanClean Citizen Waste Reporting Prototype
- **Purpose of the Screen:** Provides an intuitive, three-step incident reporting interface allowing residents to lodge geotagged waste grievances with mandatory photographic evidence.
- **Intended User / Role:** Authenticated Citizens.
- **Main UI Components:** Standardized waste category selector (Overflowing Bin, Garbage Heap, Hazardous Waste, Dead Animal), descriptive title input, landmark notes textarea, interactive drag-and-drop photo upload dropzone with thumbnail preview, and "Submit Complaint" button.
- **Main User Action / Workflow:** Citizen classifies the waste incident, attaches a photo, inputs descriptive landmark context, coordinates with the map canvas (Prototype 5), and clicks submit to dispatch a multipart payload to `POST /api/complaints`.

[INSERT FIGURE HERE: Figure 5.4]
*Figure 5.4: UrbanClean Citizen Waste Reporting Prototype*

### 5.2.5 Prototype 5 — Location Selection and GPS Map
- **Figure Number:** Figure 5.5
- **Prototype Title:** UrbanClean Interactive Location Selection and GPS Map Prototype
- **Purpose of the Screen:** Facilitates high-precision geospatial coordinate capture via browser GPS telemetry or direct map canvas interaction.
- **Intended User / Role:** Citizens reporting waste incidents.
- **Main UI Components:** Embedded Leaflet.js interactive vector map, "Auto-Detect GPS" telemetry button, draggable location pin with dynamic coordinate readout (Latitude, Longitude), and reverse-geocoded address display banner.
- **Main User Action / Workflow:** Citizen clicks "Auto-Detect GPS" to query the W3C Geolocation API or clicks directly on the Leaflet map; a draggable pin is placed, and the resolved coordinates and street name automatically populate the complaint form fields.

[INSERT FIGURE HERE: Figure 5.5]
*Figure 5.5: UrbanClean Interactive Location Selection and GPS Map Prototype*

### 5.2.6 Prototype 6 — Citizen Complaint Tracking
- **Figure Number:** Figure 5.6
- **Prototype Title:** UrbanClean Citizen Complaint Tracking Prototype
- **Purpose of the Screen:** Delivers transparent, real-time lifecycle tracking of all grievances lodged by the authenticated citizen under strict horizontal privacy isolation.
- **Intended User / Role:** Authenticated Citizens.
- **Main UI Components:** "My Reports" data table displaying Ticket ID, Category, Suburb/Area, Submission Timestamp, and standardized color-coded status badges: Yellow (Pending), Blue (Assigned), Orange (In Progress), Green (Completed), with clickable "View Details" action modals.
- **Main User Action / Workflow:** Citizen opens the dashboard to inspect ticket statuses; clicking "View Details" opens a modal displaying the before-cleanup photo, driver assignment details, and verified after-cleanup resolution photograph once resolved.

[INSERT FIGURE HERE: Figure 5.6]
*Figure 5.6: UrbanClean Citizen Complaint Tracking Prototype*

### 5.2.7 Prototype 7 — Driver Duty Dashboard
- **Figure Number:** Figure 5.7
- **Prototype Title:** UrbanClean Waste Collection Driver Dashboard Prototype
- **Purpose of the Screen:** Acts as the mobile command workspace for sanitation compactor truck operators, managing shift statuses, assigned stops, and vehicle telemetry.
- **Intended User / Role:** Municipal Waste Collection Drivers.
- **Main UI Components:** Operational shift toggle switch (On-Duty / Off-Duty), assigned vehicle registration badge (e.g., Eicher Pro Dump Truck MH-02-ES-4521), scheduled stop count counters, planned travel distance metric cards, and pending stop lists.
- **Main User Action / Workflow:** Driver toggles status to "On-Duty" upon commencing their shift; the interface loads the driver's assigned collection stops and automatically queries complaints filtered within a 1.0 km geodesic radius.

[INSERT FIGURE HERE: Figure 5.7]
*Figure 5.7: UrbanClean Waste Collection Driver Dashboard Prototype*

### 5.2.8 Prototype 8 — Driver Route Optimization
- **Figure Number:** Figure 5.8
- **Prototype Title:** UrbanClean Driver TSP Route Optimization Prototype
- **Purpose of the Screen:** Displays mathematically sequenced collection routes and turn-by-turn real-road navigation geometry to minimize fleet fuel consumption.
- **Intended User / Role:** Collection Drivers.
- **Main UI Components:** Full-screen Leaflet navigation canvas, numbered sequential waypoint pins (Depot → Stop 1 → Stop 2 ... → Disposal Facility), blue road polyline layer generated by OSRM, "Generate Optimized Route" trigger, and "Start Shift / Lock Route" button.
- **Main User Action / Workflow:** Driver clicks "Generate Optimized Route" to execute the Greedy TSP heuristic; the system reorders stops and queries OSRM for street geometry; the driver clicks "Start Shift / Lock Route" to freeze today's operational route snapshot.

[INSERT FIGURE HERE: Figure 5.8]
*Figure 5.8: UrbanClean Driver TSP Route Optimization Prototype*

### 5.2.9 Prototype 9 — Proof-of-Cleanup Upload
- **Figure Number:** Figure 5.9
- **Prototype Title:** UrbanClean Proof-of-Cleanup Upload Verification Prototype
- **Purpose of the Screen:** Enforces closed-loop verification by requiring drivers to submit cryptographic photographic evidence of site remediation before ticket closure.
- **Intended User / Role:** Collection Drivers.
- **Main UI Components:** Cleanup modal dialog displaying Ticket ID, before-cleanup reference photo, camera/file capture dropzone for the after-cleanup image, resolution notes input, and "Complete Cleanup" submission button.
- **Main User Action / Workflow:** Upon physically clearing the waste dump, driver captures an after-cleanup photograph, attaches it to the modal, and submits; the server validates the upload, marks the ticket 'Completed', logs an immutable timestamp, and broadcasts resolution alerts.

[INSERT FIGURE HERE: Figure 5.9]
*Figure 5.9: UrbanClean Proof-of-Cleanup Upload Verification Prototype*

### 5.2.10 Prototype 10 — Municipal Administrator Dashboard
- **Figure Number:** Figure 5.10
- **Prototype Title:** UrbanClean Municipal Administrator Dashboard Prototype
- **Purpose of the Screen:** Provides municipal supervisors with executive-level operational oversight, real-time civic KPI monitoring, and fleet dispatch controls.
- **Intended User / Role:** Municipal Administrators / Ward Supervisors.
- **Main UI Components:** Territorial jurisdiction header (auto-locked to administrator's municipality, e.g., Kalyan, Bandra), real-time KPI counter cards (Total Reported Today, Pending Collection, In Progress, Solved Today), active driver fleet status roster, and recent complaints management table.
- **Main User Action / Workflow:** Administrator monitors real-time complaint volumes across wards, reviews driver operational efficiency, overrides automated driver assignments when necessary, and tracks SLA compliance metrics.

[INSERT FIGURE HERE: Figure 5.10]
*Figure 5.10: UrbanClean Municipal Administrator Dashboard Prototype*

### 5.2.11 Prototype 11 — City-Wide Waste Monitoring / GIS Map
- **Figure Number:** Figure 5.11
- **Prototype Title:** UrbanClean City-Wide Waste Monitoring and GIS Map Prototype
- **Purpose of the Screen:** Delivers spatial intelligence and GIS visualization of waste distribution across the entire municipal jurisdiction.
- **Intended User / Role:** Municipal Administrators and Waste Management Supervisors.
- **Main UI Components:** Interactive Leaflet GIS map with clustered marker points, status-based color filtering toggles (All, Pending, In Progress, Resolved), driver compactor truck live location markers, and clickable hotspot popups displaying ticket summaries.
- **Main User Action / Workflow:** Supervisor toggles category and status filters to identify systemic overflow corridors, evaluates spatial density clusters, and coordinates inter-ward resource rebalancing.

[INSERT FIGURE HERE: Figure 5.11]
*Figure 5.11: UrbanClean City-Wide Waste Monitoring and GIS Map Prototype*

### 5.2.12 Prototype 12 — Monthly Compliance Report / Data Export
- **Figure Number:** Figure 5.12
- **Prototype Title:** UrbanClean Monthly Compliance Tracking and Data Export Prototype
- **Purpose of the Screen:** Enables municipal officers to audit 30-day operational compliance, evaluate SLA adherence, and export structured records for external reporting.
- **Intended User / Role:** Municipal Administrators and Executive Auditors.
- **Main UI Components:** 30-day compliance data grid (Date, Total Filed, Resolved within 24h, Resolved within 48h, SLA Compliance Rate %), driver fuel efficiency summaries, and "Export to Excel / Download CSV" action button.
- **Main User Action / Workflow:** Administrator reviews 30-day historical redressal percentages, verifies SLA compliance figures, and clicks "Export to Excel" to download a clean, formatted CSV spreadsheet for administrative documentation.

[INSERT FIGURE HERE: Figure 5.12]
*Figure 5.12: UrbanClean Monthly Compliance Tracking and Data Export Prototype*

---

## 5.3 Prototype–Architecture Mapping
To establish complete traceability between the user-facing prototype designs and the underlying software engineering implementation, Table 5.1 maps each prototype interface to its corresponding frontend components, backend RESTful endpoints, and persistent database entities.

### Table 5.1: Prototype–Architecture Mapping
| Prototype Feature | Frontend Component | Backend / API Endpoint | Database Table |
| :--- | :--- | :--- | :--- |
| **Landing Page** | `index.html` + Glassmorphism CSS | Static Web Server (`GET /`) | — |
| **Multi-Role Login** | `login.html` (Tabbed RBAC Form) | `POST /api/login` | `accounts` |
| **Citizen Registration** | `login.html` (Registration Modal) | `POST /api/register` | `accounts` |
| **Complaint Form** | `citizen.html` (Reporting Form) | `POST /api/complaints` (Multer) | `complaints` |
| **GPS Location Selection** | Leaflet.js Canvas + Nominatim API | W3C Geolocation + `POST /api/complaints` | `complaints` (`lat`, `lng`, `area`) |
| **Complaint Tracking** | `citizen.html` ('My Reports' Table) | `GET /api/complaints?userId=CIT-XXX` | `complaints` |
| **Driver Dashboard** | `driver.html` (Duty Toggle & Roster) | `GET /api/driver/route/today` | `drivers`, `driver_routes` |
| **Route Optimization** | Leaflet Map + TSP Controller | `POST /api/route-optimize` + OSRM API | `driver_routes` |
| **Proof-of-Cleanup** | `driver.html` (Resolution Modal) | `PUT /api/complaints/:id/resolve` (Multer) | `complaints` (`photo_after`, `status`) |
| **Admin Dashboard** | `admin.html` (KPI Counter Cards) | `GET /api/admin/stats`, `GET /api/drivers` | `accounts`, `complaints`, `drivers` |
| **GIS Monitoring Map** | `admin.html` (Spatial Leaflet Map) | `GET /api/complaints` (All Municipal) | `complaints` (`lat`, `lng`, `status`) |
| **Compliance Report** | `admin.html` (Compliance Table) | Client CSV Generation / Admin API | `complaints`, `driver_routes` |

---

## 5.4 Backend Architecture
The backend application (`backend/server.js`) operates on Node.js using the Express.js framework, structured as a modular, decoupled RESTful API gateway:
- **Port Binding & Network Gateway:** Listens on port 3000 by default (configurable via `PORT` environment variable), binding to `0.0.0.0` for local area network access across client devices.
- **Middleware Pipeline:** Configured with `cors()` for cross-origin access, `express.json()` and `express.urlencoded()` for request body parsing, and `multer` for multipart form-data handling with 5 MB file size caps and image MIME filtering (`image/jpeg`, `image/png`).
- **Modular Business Logic Services:** Encapsulates Authentication (PBKDF2/SHA-512 salting), Complaint Management, Driver Scheduling (Haversine 1.0 km proximity filter and Greedy TSP heuristic), and Municipal Analytics.
- **Physical Directory Tree & Pipeline Flow:** Figure 5.13 illustrates the physical codebase directory tree alongside the complete seven-stage transactional data flow pipeline.

[INSERT FIGURE HERE: Figure 5.13]
*Figure 5.13: UrbanClean Backend Structure and Data Flow Diagram*

### Explanation of Figure 5.13:
Figure 5.13 synthesizes the physical codebase structure and operational data flow of the UrbanClean backend platform. The left side (Part A) documents the physical directory tree, highlighting the application entry point (`backend/server.js`), the dual-persistence document store (`backend/db.json`), the SQLite synchronization daemon (`backend/sync_sqlite.py`), the relational database mirror (`backend/urban_clean.db`), and the uploaded media directory (`backend/uploads/`), alongside client-side assets in `frontend/`. 

The right side (Part B) details the seven-stage data processing pipeline:
1. *Client Request Ingestion:* Incoming HTTP requests enter via semantic REST endpoints.
2. *Middleware Validation:* CORS headers verified, JSON bodies parsed, and file MIME types whitelisted.
3. *Cryptographic Security & RBAC:* User sessions evaluated against PBKDF2/SHA-512 hashes.
4. *Geospatial Proximity Filtering:* Spherical Haversine distance evaluated against 1.0 km radius.
5. *Algorithmic Route Sequencing:* Greedy Nearest-Neighbor TSP orders waypoints, calling OSRM for street polylines.
6. *Dual-Layer Persistence Synchronization:* Write transactions update `db.json` and immediately invoke `sync_sqlite.py` via background child processes.
7. *Semantic HTTP Response:* Clean JSON payloads returned to client interfaces with appropriate HTTP status codes (200, 201, 400, 401, 403, 500).

---

## 5.5 Database Schema Design
UrbanClean implements a dual-persistence strategy designed for rapid development agility and robust relational integrity: an active file-backed JSON document store (`backend/db.json`) mirrored synchronously into a normalized SQLite relational database (`backend/urban_clean.db`) via `sync_sqlite.py`.

The structure of data is normalized into five core relational tables:

### Table 5.2: Data Dictionary — `accounts` Table
| Column Name | Data Type | Key Constraints | Field Description |
|---|---|---|---|
| id | VARCHAR(50) | PRIMARY KEY, NOT NULL | Unique user identifier (e.g., CIT-702, DRV-101, ADM-999) |
| name | VARCHAR(100) | NOT NULL | Full legal name of user |
| email | VARCHAR(150) | UNIQUE, NOT NULL | Primary login email address |
| role | VARCHAR(20) | NOT NULL, CHECK IN ('citizen','driver','admin') | Access control role tag |
| vehicle | VARCHAR(50) | NULLABLE | Assigned vehicle registration (Drivers only, e.g., MH-02-ES-4521) |
| state | VARCHAR(100) | DEFAULT 'Maharashtra' | State administrative jurisdiction |
| district | VARCHAR(100) | NULLABLE | District administrative jurisdiction (e.g., Thane, Mumbai) |
| city | VARCHAR(100) | NULLABLE | Assigned municipal city (e.g., Kalyan, Bandra) |
| password_hash | TEXT | NOT NULL | PBKDF2/SHA-512 salted cryptographic hash string |

### Table 5.3: Data Dictionary — `complaints` Table
| Column Name | Data Type | Key Constraints | Field Description |
|---|---|---|---|
| id | VARCHAR(20) | PRIMARY KEY, NOT NULL | Unique complaint ticket code (e.g., COMP-001) |
| category | VARCHAR(50) | NOT NULL | Waste classification (e.g., Garbage Pile, Overflowing Bin, Other) |
| title | VARCHAR(255) | NOT NULL | Short summary title of issue |
| description | TEXT | NULLABLE | Detailed landmark and site accessibility notes |
| lat | FLOAT | NOT NULL | WGS84 GPS latitude coordinate (e.g., 19.0544) |
| lng | FLOAT | NOT NULL | WGS84 GPS longitude coordinate (e.g., 72.8295) |
| area | VARCHAR(100) | NULLABLE | Municipal neighborhood (e.g., Bandra West, Kalyan Sector-3) |
| photo_before | TEXT | NULLABLE | Local file path to citizen's uploaded evidence photo |
| photo_after | TEXT | NULLABLE | Local file path to driver's cleanup verification photo |
| status | VARCHAR(50) | DEFAULT 'Pending' | Lifecycle state (Pending, Assigned, In Progress, Completed) |

### Table 5.4: Data Dictionary — `driver_routes` Table
| Column Name | Data Type | Key Constraints | Field Description |
|---|---|---|---|
| id | INTEGER | PRIMARY KEY, AUTOINCREMENT | Unique waypoint index entry |
| driverId | VARCHAR(50) | FOREIGN KEY -> drivers.id | Identifier of driver who pinned waypoint |
| pointIndex | INTEGER | NOT NULL | Sequential index of waypoint in route |
| label | VARCHAR(100) | DEFAULT 'Point N' | Display label (e.g., Point 1, Depot, Disposal Site) |
| lat | FLOAT | NOT NULL | Pinned latitude coordinate |
| lng | FLOAT | NOT NULL | Pinned longitude coordinate |
| savedAt | DATETIME | DEFAULT CURRENT_TIMESTAMP | Timestamp when waypoint was saved |

### Table 5.5: Data Dictionary — `drivers` Table
| Column Name | Data Type | Key Constraints | Field Description |
|---|---|---|---|
| id | VARCHAR(50) | PRIMARY KEY, NOT NULL | Driver unique code (e.g., DRV-101) |
| name | VARCHAR(100) | NOT NULL | Driver full name (e.g., Ramesh Kumar) |
| status | VARCHAR(20) | DEFAULT 'Off-Duty' | Operational status (Active, Off-Duty) |
| vehicle | VARCHAR(100) | NOT NULL | Assigned truck model & plate (e.g., Eicher Pro Dump Truck MH-02-ES-4521) |
| efficiency | INTEGER | DEFAULT 0 | Calculated route fuel savings percentage (e.g., 28%) |
| distance | VARCHAR(20) | DEFAULT '0.0 km' | Total planned driving distance (e.g., 12.4 km) |
| assignedComplaints | TEXT | DEFAULT '[]' | JSON array string of assigned ticket IDs |

### Table 5.6: Data Dictionary — `notifications` Table
| Column Name | Data Type | Key Constraints | Field Description |
|---|---|---|---|
| id | VARCHAR(20) | PRIMARY KEY, NOT NULL | Unique alert ID (e.g., NT-001) |
| type | VARCHAR(20) | NOT NULL | Notification category (info, warning, success) |
| message | TEXT | NOT NULL | Human-readable system log message |
| timeStr | VARCHAR(50) | NOT NULL | Relative event timestamp (e.g., 10 mins ago) |

The relational structure and verified records of the database are supported by the live SQLite environment screenshots below:

[INSERT FIGURE HERE: Figure 5.14]
*Figure 5.14: DB Browser for SQLite — accounts & complaints Tables*

### Explanation of Figure 5.14:
Figure 5.14 displays the live records of the `accounts` and `complaints` tables in DB Browser for SQLite, confirming PBKDF2/SHA-512 salted password hashes, multi-role separation, WGS84 geographic coordinates, and ticket lifecycle states (`Open`, `Completed`).

[INSERT FIGURE HERE: Figure 5.15]
*Figure 5.15: DB Browser for SQLite — driver_routes & notifications Tables*

### Explanation of Figure 5.15:
Figure 5.15 documents sequential collection stop waypoints configured by collection driver DRV-101 (`Point 1` through `Point 12`) with high-precision coordinates, alongside system-wide notification broadcasts.

[INSERT FIGURE HERE: Figure 5.16]
*Figure 5.16: DB Browser for SQLite — drivers Fleet Roster Table*

### Explanation of Figure 5.16:
Figure 5.16 demonstrates the driver fleet roster showing active driver states, vehicle assignments (`Eicher Pro Dump Truck`), route distance metrics (`12.4 km`), and assigned complaint arrays.

---

## 5.6 Security Considerations
Security architecture is enforced across client, server, and storage layers:
- **Authentication & Password Protection:** User passwords are cryptographically salted using a 16-byte random salt and hashed with PBKDF2/SHA-512 over 10,000 iterations. Plaintext passwords are never logged, transmitted, or persisted.
- **Role-Based Access Control (RBAC):** Portal pages evaluate client session roles, redirecting unauthorized users. Server endpoints validate caller identity, returning HTTP 403 Forbidden on privilege violations.
- **Horizontal Citizen Data Isolation:** Queries to `GET /api/complaints` filter records by caller ID, ensuring citizens can access only their own filed tickets.
- **File Upload Protection:** Multer limits uploaded images to a maximum of 5 MB and whitelists MIME types (`image/jpeg`, `image/png`), blocking executable files and arbitrary script uploads.
- **Input Sanitization:** All user inputs (descriptions, titles, names) are sanitized to neutralize Cross-Site Scripting (XSS) and injection attacks.
- **API Protection & Error Suppression:** Centralized error-handling middleware intercepts runtime exceptions, suppressing internal stack traces and directory paths to return clean, standardized JSON error responses.
- **Database Protection:** Relational database operations utilize parameterized SQL statements within `sync_sqlite.py`, preventing SQL injection vulnerabilities.

---

# CHAPTER 6 — APPLICATION DEVELOPMENT

## 6.1 Frontend Implementation
The frontend is implemented as lightweight, modular Single-Page Application (SPA) views using vanilla HTML5, CSS3, JavaScript ES6+, and Leaflet.js v1.9.4. Figures 6.1 through 6.7 provide authentic screenshots of the actual running application interfaces:

[INSERT FIGURE HERE: Figure 6.1]
*Figure 6.1: Public Landing Page, Multi-Role Login & Citizen Registration Views*

### Explanation of Figure 6.1:
Figure 6.1 documents the public landing page with live cleanliness KPI counters, the multi-role tabbed login interface (`login.html`), and the citizen account creation view.

[INSERT FIGURE HERE: Figure 6.2]
*Figure 6.2: Citizen Waste Reporting Interface & Interactive Map Pinning Views*

### Explanation of Figure 6.2:
Figure 6.2 showcases the citizen waste reporting form on `citizen.html`, featuring real-time photo dropzone staging, category classification, and interactive Leaflet map coordinate pinning.

[INSERT FIGURE HERE: Figure 6.3]
*Figure 6.3: GPS Geolocation Telemetry, Citizen Ticket Tracking & Driver Dashboard Views*

### Explanation of Figure 6.3:
Figure 6.3 displays high-precision GPS telemetry capture, the citizen real-time ticket tracking table ('My Reports') with color-coded status badges, and the collection driver workspace.

[INSERT FIGURE HERE: Figure 6.4]
*Figure 6.4: Driver Optimized Route Map (5 Stops) & Proof-of-Cleanup Upload Views*

### Explanation of Figure 6.4:
Figure 6.4 illustrates the driver route navigation map displaying five sequenced collection stops connected via OSRM turn-by-turn road polylines, alongside the proof-of-cleanup upload modal.

[INSERT FIGURE HERE: Figure 6.5]
*Figure 6.5: Municipal Administrator Command Center, Active Drivers & Daily Complaints Modal Views*

### Explanation of Figure 6.5:
Figure 6.5 documents the municipal administrator command center on `admin.html`, showing real-time KPI counter cards, active driver rosters, and daily complaint management modals.

[INSERT FIGURE HERE: Figure 6.6]
*Figure 6.6: City-Wide Waste Monitoring Map & Monthly Compliance Tracking Report with Excel Export Views*

### Explanation of Figure 6.6:
Figure 6.6 presents the administrator spatial monitoring map displaying city-wide complaint distributions, alongside the 30-day compliance report with one-click Excel CSV export.

[INSERT FIGURE HERE: Figure 6.7]
*Figure 6.7: Mobile Responsive Device View across Smartphone Viewport Views*

### Explanation of Figure 6.7:
Figure 6.7 demonstrates responsive layout adaptation on smartphone viewports (375×667), transitioning navigation into accessible bottom tab bars and touch-optimized controls.

## 6.2 Backend Implementation
The backend server (`backend/server.js`) is implemented using Express.js on Node.js. It encapsulates REST route handlers, controller logic, and algorithmic computation services:
- **Express Route Handlers:** Handles routing for authentication (`/api/register`, `/api/login`), complaint lifecycle (`/api/complaints`, `/api/complaints/:id/resolve`), driver route operations (`/api/driver/route/today`, `/api/driver/route/lock`), and municipal analytics (`/api/admin/dashboard`).
- **Haversine 1.0 km Proximity Engine:** Computes great-circle geodesic distances between driver collection points and active complaints using the spherical trigonometric formula:
  $$d = 2R \cdot \arcsin\left(\sqrt{\sin^2\left(\frac{\Delta\phi}{2}\right) + \cos(\phi_1)\cos(\phi_2)\sin^2\left(\frac{\Delta\lambda}{2}\right)}\right)$$
  Complaints where $d \le 1.0\text{ km}$ enter the driver's active candidate queue; distant complaints remain in the general unassigned pool.
- **Greedy TSP Route Optimization:** An internal Greedy Nearest-Neighbor heuristic iteratively selects the nearest unvisited waypoint in $O(N^2)$ time, generating an ordered stop sequence that is then projected onto real Mumbai road geometries via the Project-OSRM Driving API.

## 6.3 Database Integration
UrbanClean integrates an active JSON document store (`backend/db.json`) with an automated SQLite relational database mirror (`backend/urban_clean.db`):
- **CRUD Operations:** Read operations parse `db.json` asynchronously in under 8 ms. Write operations (`INSERT`, `UPDATE`) mutate the in-memory state and commit atomically to `db.json`.
- **Automated Synchronization Daemon:** Upon every write operation, `writeDB()` invokes `sync_sqlite.py` through a background child process: `exec('python sync_sqlite.py')`. The Python daemon parses `db.json` and updates the SQLite tables using transactional SQL statements (`CREATE TABLE IF NOT EXISTS`, `INSERT OR REPLACE`), ensuring 100% record parity without database locking.

## 6.4 Authentication & Validation
- **Multi-Role Authentication:** Users authenticate against role-specific records (citizen, driver, admin). Passwords are validated using PBKDF2 with SHA-512 over 10,000 iterations against a 16-byte random cryptographic salt.
- **Role-Based Access Control (RBAC):** Frontend page guards check user session roles, while backend REST endpoints enforce authorization checks before executing operations.
- **Input Validation:** Input strings are validated for length, email syntax (`@` check), coordinate bounds ($[-90, +90]$ lat, $[-180, +180]$ lng), and non-empty required fields.

## 6.5 Error Handling
A multi-tier error handling architecture ensures graceful failure handling:
- **Centralized Error-Handling Middleware:** Express interceptors catch unhandled exceptions, returning semantic HTTP 500 JSON responses without leaking stack traces or internal server paths.
- **Multer Upload Error Handling:** Dedicated 4-parameter error middleware (`(err, req, res, next)`) intercepts file upload rejections, returning a clean HTTP 400 Bad Request JSON response: `{"error": "Only image files are allowed!"}`.
- **External API Fallback:** If the external Project-OSRM service experiences network timeouts, the system degrades gracefully by falling back to straight-line Haversine routing polylines, preventing application crashes.
"""
