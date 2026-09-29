# -*- coding: utf-8 -*-
"""
Chapter 5 (System Architecture Design) & Chapter 6 (Application Development)
Restructured strictly to the required syllabus topics.
"""

CH5_CH6_TEXT = r"""# CHAPTER 5 — SYSTEM ARCHITECTURE DESIGN

## 5.1 Frontend Architecture — Prototype
The frontend architecture of UrbanClean is designed around a lightweight, responsive Single-Page Application (SPA) paradigm with a modern Glassmorphism visual design system. In place of heavy JavaScript application frameworks that induce high memory footprints on mobile client browsers, the interface utilizes modular semantic HTML5, CSS custom properties, and client DOM controllers (`script.js`) paired with the Leaflet.js (v1.9.4) vector mapping canvas.

To visualize the user interaction model and aesthetic layout across each stakeholder role prior to full-stack code implementation, high-fidelity prototypes were designed. Figures 5.1 through 5.12 showcase the twelve authoritative interface prototypes governing the UrbanClean platform:

[INSERT FIGURE HERE: Figure 5.1]
*Figure 5.1: Prototype — Public Landing Page & Cleanliness Statistics*

### Explanation of Figure 5.1:
Figure 5.1 illustrates the public visitor interface accessible to unauthenticated civic observers. It highlights the glassmorphic hero container, real-time KPI metrics (Issues Resolved, Active Reports, Happy Citizens), feature cards, and quick navigation anchors guiding citizens to report issues or log in.

[INSERT FIGURE HERE: Figure 5.2]
*Figure 5.2: Prototype — Multi-Role Unified Authentication Portal*

### Explanation of Figure 5.2:
Figure 5.2 showcases the unified authentication gateway supporting role-based access control. Distinct tab selectors allow Citizens, Drivers, and Municipal Administrators to authenticate with role validation and error feedback.

[INSERT FIGURE HERE: Figure 5.3]
*Figure 5.3: Prototype — Citizen Registration & Account Creation*

### Explanation of Figure 5.3:
Figure 5.3 displays the citizen registration interface. The form captures user full name, email address, password with validation rules, contact number, and residential municipal ward to establish jurisdictional boundaries.

[INSERT FIGURE HERE: Figure 5.4]
*Figure 5.4: Prototype — Citizen Waste Reporting & Incident Logging Form*

### Explanation of Figure 5.4:
Figure 5.4 details the primary civic incident reporting interface. Citizens select standardized waste categories, provide landmark descriptions, attach photographic evidence via drag-and-drop dropzones, and invoke geolocation detection.

[INSERT FIGURE HERE: Figure 5.5]
*Figure 5.5: Prototype — Interactive Geographic Location Selection & Map Canvas*

### Explanation of Figure 5.5:
Figure 5.5 demonstrates the Leaflet-powered interactive map selection canvas. Users can drop draggable coordinate pins or click 'Auto-Detect GPS' to capture high-precision coordinates with reverse geocoding.

[INSERT FIGURE HERE: Figure 5.6]
*Figure 5.6: Prototype — Citizen Real-Time Complaint Tracking & Lifecycle Dashboard*

### Explanation of Figure 5.6:
Figure 5.6 presents the citizen ticket tracking portal ('My Reports'). Each complaint displays its unique ID, waste category, timestamp, color-coded lifecycle status badge, and clickable details modal with before-and-after photographic comparisons.

[INSERT FIGURE HERE: Figure 5.7]
*Figure 5.7: Prototype — Waste Collection Driver Duty Dashboard*

### Explanation of Figure 5.7:
Figure 5.7 illustrates the field operator mobile workspace. Drivers toggle shift duty status (Active/Off-Duty), view assigned truck registrations, review scheduled stops, and inspect live distance metrics.

[INSERT FIGURE HERE: Figure 5.8]
*Figure 5.8: Prototype — Driver TSP Route Optimization & Real-Road Navigation Map*

### Explanation of Figure 5.8:
Figure 5.8 showcases the driver route optimization interface. The Leaflet map renders numbered collection waypoints ordered via the Greedy TSP heuristic and connected via turn-by-turn road polylines computed by OSRM.

[INSERT FIGURE HERE: Figure 5.9]
*Figure 5.9: Prototype — Proof-of-Cleanup Image Upload & Verification Interface*

### Explanation of Figure 5.9:
Figure 5.9 details the closed-loop resolution verification modal. Drivers must attach an after-cleanup photograph of the remediated site before the ticket status can transition to 'Completed'.

[INSERT FIGURE HERE: Figure 5.10]
*Figure 5.10: Prototype — Municipal Administrator Command Center & Analytics Dashboard*

### Explanation of Figure 5.10:
Figure 5.10 presents the executive command center. Real-time KPI counter cards display Reported Today, Pending, In Progress, and Solved Today, alongside quick management tables.

[INSERT FIGURE HERE: Figure 5.11]
*Figure 5.11: Prototype — City-Wide Waste Monitoring Map & GIS Filtering*

### Explanation of Figure 5.11:
Figure 5.11 illustrates the spatial monitoring console for municipal supervisors, plotting city-wide complaint distributions with status-based filtering and driver location tracking.

[INSERT FIGURE HERE: Figure 5.12]
*Figure 5.12: Prototype — Municipal Monthly Compliance Tracking & Data Export Report*

### Explanation of Figure 5.12:
Figure 5.12 showcases the compliance audit reporting interface. Supervisors can review 30-day ticket resolutions, evaluate driver performance metrics, and export data formatted as CSV.

### Table 5.1: Prototype–Architecture Tier Mapping
| Figure | Interface Prototype Name | Primary User Role | Architectural Layer & Technology | Core Interactivity & Functional Role |
| :---: | :--- | :--- | :--- | :--- |
| **5.1** | Public Landing & Statistics | Guest / Public | Tier 1: HTML5 / Glassmorphism CSS | Static metrics display, routing anchors |
| **5.2** | Multi-Role Authentication | All Roles | Tier 1 + Tier 2: Fetch API / Express Auth | Role toggle, PBKDF2 hash credential check |
| **5.3** | Citizen Registration | Citizen | Tier 1 + Tier 2: Express `/api/register` | Input sanitization, account creation |
| **5.4** | Waste Reporting Form | Citizen | Tier 1 + Tier 2: Multer File Upload | Category tagging, multipart payload submission |
| **5.5** | Map Canvas & Pin Drop | Citizen | Tier 1 + Tier 3: Leaflet.js / Nominatim | Click-to-pin, W3C GPS, reverse geocoding |
| **5.6** | Citizen Ticket Tracker | Citizen | Tier 1 + Tier 2: Express `/api/complaints` | Real-time status lifecycle badges, modal view |
| **5.7** | Driver Duty Dashboard | Collection Driver | Tier 1 + Tier 2: Driver REST Endpoints | Duty toggle, vehicle roster, shift metrics |
| **5.8** | TSP Navigation Map | Collection Driver | Tier 1 + Tier 3: Leaflet / Greedy TSP / OSRM | Turn-by-turn road polyline, waypoint sequence |
| **5.9** | Proof-of-Cleanup Modal | Collection Driver | Tier 1 + Tier 2: Multer Resolution Upload | Photo proof validation, ticket completion |
| **5.10** | Admin Command Center | Municipal Admin | Tier 1 + Tier 2: Admin Dashboard Gateway | Real-time KPI aggregates, roster oversight |
| **5.11** | GIS Monitoring Map | Municipal Admin | Tier 1 + Tier 3: Leaflet MarkerCluster / OSM | City-wide geospatial distribution, filtering |
| **5.12** | Compliance Export Report | Municipal Admin | Tier 1 + Tier 2: CSV Generation Engine | 30-day SLA compliance auditing, CSV export |

## 5.2 Backend Architecture
The backend application (`backend/server.js`) operates on Node.js using the Express.js framework, structured as a modular, decoupled RESTful API gateway:
- **Port Binding & Network Gateway:** Listens on port 3000 by default (configurable via `PORT` environment variable), binding to `0.0.0.0` for local area network access.
- **Middleware Pipeline:** Configured with `cors()` for cross-origin access, `express.json()` and `express.urlencoded()` for request body parsing, and `multer` for multipart form-data handling with 5 MB file size caps and image MIME filtering (`image/jpeg`, `image/png`).
- **Modular Business Logic Services:** Encapsulates Authentication (PBKDF2/SHA-512 salting), Complaint Management, Driver Scheduling (Haversine 1.0 km proximity filter and Greedy TSP heuristic), and Municipal Analytics.
- **Physical Directory Tree & Pipeline Flow:** Figure 5.13 illustrates the physical codebase directory tree alongside the complete seven-stage transactional data flow pipeline.

[INSERT FIGURE HERE: Figure 5.13]
*Figure 5.13: UrbanClean Backend Structure and Data Flow*

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

## 5.3 Database Schema Design — Structure of Data
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

## 5.4 API Structure
The API follows semantic RESTful conventions, exposing versioned endpoints structured around JSON request and response payloads:
- `POST /api/register` — Public user registration for Citizens and Drivers with validation.
- `POST /api/login` — Credential authentication, PBKDF2 hash verification, and session token generation.
- `GET /api/complaints` — Retrieve complaints filtered by user ID or municipal jurisdiction.
- `POST /api/complaints` — Multipart complaint submission with photo attachment, GPS coordinates, and category.
- `PUT /api/complaints/:id/resolve` — Driver cleanup resolution with mandatory proof-of-cleanup photo upload.
- `GET /api/driver/route/today` — Retrieve today's locked route snapshot and eligible 1.0 km complaints.
- `POST /api/driver/route/lock` — Freeze today's driver route snapshot, deferring new complaints to tomorrow's queue.
- `GET /api/driver/route/tomorrow` — Retrieve complaints deferred to tomorrow's shift queue.
- `GET /api/admin/dashboard` — Fetch aggregated municipal KPIs, complaint hotspot markers, and active driver rosters.

## 5.5 Security Considerations
Security architecture is enforced across client, server, and storage layers:
- **Authentication & Password Protection:** User passwords are cryptographically salted using a 16-byte random salt and hashed with PBKDF2/SHA-512 over 10,000 iterations. Plaintext passwords are never logged, transmitted, or persisted.
- **Role-Based Access Control (RBAC):** Portal pages evaluate client session roles, redirecting unauthorized users. Server endpoints validate caller identity, returning HTTP 403 Forbidden on privilege violations.
- **Horizontal Citizen Data Isolation:** Queries to `GET /api/complaints` filter records by caller ID, ensuring citizens can access only their own filed tickets.
- **File Upload Protection:** Multer limits uploaded images to a maximum of 5 MB and whitelists MIME types (`image/jpeg`, `image/png`), blocking executable files and arbitrary script uploads.
- **Input Sanitization:** All user inputs (descriptions, titles, names) are sanitized to neutralize Cross-Site Scripting (XSS) and injection attacks.

---

# CHAPTER 6 — APPLICATION DEVELOPMENT

## 6.1 Frontend Implementation
The frontend is implemented as lightweight, modular Single-Page Application (SPA) views using vanilla HTML5, CSS3, JavaScript ES6+, and Leaflet.js v1.9.4. Figures 6.1 through 6.7 provide authentic screenshots of the actual running application interfaces:

[INSERT FIGURE HERE: Figure 6.1]
*Figure 6.1: Public Landing Page, Multi-Role Login & Citizen Registration*

### Explanation of Figure 6.1:
Figure 6.1 documents the public landing page with live cleanliness KPI counters, the multi-role tabbed login interface (`login.html`), and the citizen account creation view.

[INSERT FIGURE HERE: Figure 6.2]
*Figure 6.2: Citizen Waste Reporting Interface & Interactive Map Pinning*

### Explanation of Figure 6.2:
Figure 6.2 showcases the citizen waste reporting form on `citizen.html`, featuring real-time photo dropzone staging, category classification, and interactive Leaflet map coordinate pinning.

[INSERT FIGURE HERE: Figure 6.3]
*Figure 6.3: GPS Geolocation Telemetry, Citizen Ticket Tracking & Driver Dashboard*

### Explanation of Figure 6.3:
Figure 6.3 displays high-precision GPS telemetry capture, the citizen real-time ticket tracking table ('My Reports') with color-coded status badges, and the collection driver workspace.

[INSERT FIGURE HERE: Figure 6.4]
*Figure 6.4: Driver Optimized Route Map (5 Stops) & Proof-of-Cleanup Upload*

### Explanation of Figure 6.4:
Figure 6.4 illustrates the driver route navigation map displaying five sequenced collection stops connected via OSRM turn-by-turn road polylines, alongside the proof-of-cleanup upload modal.

[INSERT FIGURE HERE: Figure 6.5]
*Figure 6.5: Municipal Administrator Command Center, Active Drivers & Daily Complaints Modal*

### Explanation of Figure 6.5:
Figure 6.5 documents the municipal administrator command center on `admin.html`, showing real-time KPI counter cards, active driver rosters, and daily complaint management modals.

[INSERT FIGURE HERE: Figure 6.6]
*Figure 6.6: City-Wide Waste Monitoring Map & Monthly Compliance Tracking Report with Excel Export*

### Explanation of Figure 6.6:
Figure 6.6 presents the administrator spatial monitoring map displaying city-wide complaint distributions, alongside the 30-day compliance report with one-click Excel CSV export.

[INSERT FIGURE HERE: Figure 6.7]
*Figure 6.7: Mobile Responsive Device View across Smartphone Viewport*

### Explanation of Figure 6.7:
Figure 6.7 demonstrates responsive layout adaptation on smartphone viewports (375×667), transitioning navigation into accessible bottom tab bars and touch-optimized controls.

## 6.2 Backend Implementation
The backend server (`backend/server.js`) is implemented using Express.js on Node.js. It encapsulates REST route handlers, controller logic, and algorithmic computation services:
- **Express Route Handlers:** Handles routing for authentication (`/api/register`, `/api/login`), complaint lifecycle (`/api/complaints`, `/api/complaints/:id/resolve`), driver route operations (`/api/driver/route/today`, `/api/driver/route/lock`), and municipal analytics (`/api/admin/dashboard`).
- **Haversine 1.0 km Proximity Engine:** Computes great-circle geodesic distances between driver collection points and active complaints using the spherical trigonometric formula:
  $$d = 2R \arcsin\left(\sqrt{\sin^2\left(\frac{\Delta\phi}{2}\right) + \cos(\phi_1)\cos(\phi_2)\sin^2\left(\frac{\Delta\lambda}{2}\right)}\right)$$
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
