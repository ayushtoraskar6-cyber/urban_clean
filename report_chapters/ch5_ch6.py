# -*- coding: utf-8 -*-
"""
Chapter 5 (System Architecture Design) & Chapter 6 (Application Development)
"""

CH5_CH6_TEXT = """# CHAPTER 5 — SYSTEM ARCHITECTURE DESIGN

## 5.1 Introduction & Overall System Architecture
System Architecture Design specifies the structural blueprints, modular subsystems, data flows, and communication contracts that govern UrbanClean. The platform is designed around a decoupled, 3-tier Client-Server architecture ensuring responsive client interactions, secure backend business logic execution, and resilient data persistence.

[INSERT FIGURE HERE: Figure 5.1]
*Figure 5.1: High-Level Layered System Architecture of UrbanClean*

### Explanation of Layered System Architecture:
Figure 5.1 illustrates the three-tier architectural hierarchy:
- **Tier 1 (Presentation Layer):** Responsive single-page interfaces (`index.html`, `login.html`, `citizen.html`, `driver.html`, `admin.html`) built with Glassmorphism CSS3, Leaflet.js v1.9.4, and the client application controller (`script.js`).
- **Tier 2 (Application & Logic Layer):** Node.js runtime and Express.js REST API gateway (`server.js`) on Port 3000, managing middleware (CORS, Multer photo ingestion), core business services (PBKDF2/SHA-512 authentication, RBAC, Haversine 1.0 km filter, Greedy TSP sequencer, Daily Route-Lock manager, and 30-day data retention).
- **Tier 3 (Persistence & External Services Layer):** Dual persistence storage engine (`backend/db.json` mirrored via `sync_sqlite.py` to `backend/urban_clean.db`) and external HTTPS queries to OpenStreetMap tile servers, OSM Nominatim reverse geocoding, and Project-OSRM road routing API.

## 5.2 Frontend Architecture
The presentation layer is implemented as modular single-page views without heavy frontend framework dependencies (such as React or Angular), minimizing memory overhead on mobile devices:
- **Centralized Client State (`STATE`):** Manages user authentication tokens, active geographic coordinates, loaded complaint arrays, driver collection stops, map instances, and route lock flags.
- **Leaflet.js Mapping Engine (v1.9.4):** Lightweight (42 KB) vector engine rendering OpenStreetMap tiles, custom SVG status markers, and route polylines.
- **Glassmorphic Design Framework (`styles.css`):** Utilizes CSS custom variables, translucent backdrop blur filters (`backdrop-filter: blur(12px)`), high-contrast typography, and fluid responsive grid layouts.

## 5.3 Backend Architecture
The backend application (`backend/server.js`) operates on Node.js using the Express.js framework:
- **Port Binding:** Listens on port 3000 by default (configurable via `PORT` environment variable).
- **Middleware Pipeline:** Configured with `cors()` for cross-origin resource access, `express.json()` and `express.urlencoded()` for payload parsing, and `multer` for multipart form file storage.
- **Stateless Handlers:** Exposes standardized REST endpoints adhering strictly to HTTP verb semantics (`GET`, `POST`, `PUT`, `DELETE`).

## 5.4 Database Architecture & Dual-Persistence Strategy
UrbanClean utilizes a dual-persistence strategy designed for rapid development agility and robust relational inspection:
1. **Active File-Backed JSON Store (`backend/db.json`):** Serves as the primary operational document store, allowing non-blocking I/O reads and agile schema evolution.
2. **Automated SQLite Relational Mirror (`backend/urban_clean.db`):** Mirrored synchronously upon every write operation via `sync_sqlite.py`, structuring document arrays into normalized relational SQL tables (`accounts`, `complaints`, `drivers`, `driver_routes`, `notifications`).
3. **Synchronization Mechanism:** Every write operation in `server.js` updates `db.json`. Upon completion of file writing, `writeDB()` triggers a background child process: `exec('python sync_sqlite.py')`. `sync_sqlite.py` parses `db.json` and updates the SQLite database tables using transactional SQL statements (`CREATE TABLE IF NOT EXISTS`, `INSERT OR REPLACE`).

## 5.5 Database Schema & Data Dictionaries
The relational database models five core tables as verified in the project's SQLite environment:

### Table 5.1: Data Dictionary — `accounts` Table
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

### Table 5.2: Data Dictionary — `complaints` Table
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

### Table 5.3: Data Dictionary — `driver_routes` Table
| Column Name | Data Type | Key Constraints | Field Description |
|---|---|---|---|
| id | INTEGER | PRIMARY KEY, AUTOINCREMENT | Unique waypoint index entry |
| driverId | VARCHAR(50) | FOREIGN KEY -> drivers.id | Identifier of driver who pinned waypoint |
| pointIndex | INTEGER | NOT NULL | Sequential index of waypoint in route |
| label | VARCHAR(100) | DEFAULT 'Point N' | Display label (e.g., Point 1, Depot, Disposal Site) |
| lat | FLOAT | NOT NULL | Pinned latitude coordinate |
| lng | FLOAT | NOT NULL | Pinned longitude coordinate |
| savedAt | DATETIME | DEFAULT CURRENT_TIMESTAMP | Timestamp when waypoint was saved |

### Table 5.4: Data Dictionary — `drivers` Table
| Column Name | Data Type | Key Constraints | Field Description |
|---|---|---|---|
| id | VARCHAR(50) | PRIMARY KEY, NOT NULL | Driver unique code (e.g., DRV-101) |
| name | VARCHAR(100) | NOT NULL | Driver full name (e.g., Ramesh Kumar) |
| status | VARCHAR(20) | DEFAULT 'Off-Duty' | Operational status (Active, Off-Duty) |
| vehicle | VARCHAR(100) | NOT NULL | Assigned truck model & plate (e.g., Eicher Pro Dump Truck MH-02-ES-4521) |
| efficiency | INTEGER | DEFAULT 0 | Calculated route fuel savings percentage (e.g., 28%) |
| distance | VARCHAR(20) | DEFAULT '0.0 km' | Total planned driving distance (e.g., 12.4 km) |
| assignedComplaints | TEXT | DEFAULT '[]' | JSON array string of assigned ticket IDs |

### Table 5.5: Data Dictionary — `notifications` Table
| Column Name | Data Type | Key Constraints | Field Description |
|---|---|---|---|
| id | VARCHAR(20) | PRIMARY KEY, NOT NULL | Unique alert ID (e.g., NT-001) |
| type | VARCHAR(20) | NOT NULL | Notification category (info, warning, success) |
| message | TEXT | NOT NULL | Human-readable system log message |
| timeStr | VARCHAR(50) | NOT NULL | Relative event timestamp (e.g., 10 mins ago) |

## 5.6 Database Schema Inspection via DB Browser for SQLite
The database implementation was visually verified in the SQLite environment using DB Browser for SQLite:

[INSERT FIGURE HERE: Figure 5.2]
*Figure 5.2: DB Browser for SQLite — `accounts` & `complaints` Tables*

### Explanation of Figure 5.2:
Figure 5.2 shows the live records of the `accounts` and `complaints` tables. It verifies PBKDF2/SHA-512 salted password hashes, multi-role user segregation (`citizen`, `driver`, `admin`), exact WGS84 coordinates for complaints, and ticket lifecycle states (`Open`, `Completed`).

[INSERT FIGURE HERE: Figure 5.3]
*Figure 5.3: DB Browser for SQLite — `driver_routes` & `notifications` Tables*

### Explanation of Figure 5.3:
Figure 5.3 documents sequential collection stop waypoints configured by collection driver DRV-101 (`Point 1` through `Point 12`) with high-precision decimal degrees, as well as real-time system event logs capturing shift starts and task updates.

[INSERT FIGURE HERE: Figure 5.4]
*Figure 5.4: DB Browser for SQLite — `drivers` Fleet Roster Table*

### Explanation of Figure 5.4:
Figure 5.4 demonstrates the driver fleet roster showing active driver states, vehicle assignments (`Eicher Pro Dump Truck`, `Tata Ace Garbage Tipper`), route distance metrics (`12.4 km`), and assigned complaint arrays.

## 5.7 API Structure
The API follows semantic RESTful conventions:
- `POST /api/register` — Public user registration (Citizen and Driver).
- `POST /api/login` — Credential authentication and session token generation.
- `GET /api/complaints` — Retrieve complaints filtered by user ID or city jurisdiction.
- `POST /api/complaints` — Multipart complaint submission with photo attachment.
- `PUT /api/complaints/:id/resolve` — Driver cleanup resolution with proof photo upload.
- `GET /api/driver/route/today` — Retrieve today's locked route snapshot and eligible 1.0 km complaints.
- `POST /api/driver/route/lock` — Lock today's driver route snapshot.
- `GET /api/driver/route/tomorrow` — Retrieve complaints deferred to tomorrow's shift queue.
- `GET /api/admin/dashboard` — Fetch aggregated municipal KPIs and active driver rosters.

## 5.8 Authentication and Authorization
- **Cryptographic Salting & Hashing:** Passwords are never stored in plaintext. Credentials are secured using PBKDF2 with SHA-512 hashing across 10,000 iterations, bound to a unique 16-byte cryptographically random hex salt.
- **Role-Based Access Control (RBAC):** Users belong strictly to one role (`citizen`, `driver`, `admin`). Administrative endpoints evaluate session tokens and caller headers, rejecting unauthorized access with HTTP 403 Forbidden.
- **Client Session Management:** Authenticated user profiles are serialized into browser `localStorage.setItem('urban_clean_user', ...)`. View protection is enforced via `verifyPageSecurity()` on every view load.

## 5.9 Security Considerations
- **Cross-Site Scripting (XSS) Prevention:** User text inputs (descriptions, landmarks, names) are sanitized and escaped prior to DOM injection.
- **File Ingestion Restrictions:** Multer enforces a 5 MB file size limit and inspects MIME types to reject executables and non-image files.
- **Strict Citizen Data Isolation:** Backend complaint queries inspect `x-user-id` headers; citizens can never inspect or modify complaints filed by other residents.
- **Administrative Jurisdiction Locking:** Administrator viewports are locked to their assigned municipal territory (e.g., Kalyan, Bandra), preventing cross-jurisdictional interference.

## 5.10 Data Flow Architecture
The operational information flows across the platform are illustrated by Context-Level (Level 0) and Detailed (Level 1) Data Flow Diagrams:
- **Level 0 (Context Diagram):** Citizens inject complaints and photos and receive status tracking; Drivers receive assignments and route navigation and return cleanup proof; Administrators receive KPIs and audit data and transmit driver assignments.
- **Level 1 (Core Module Data Exchanges):** Traces data flow from (1.0 Registration & Login) to Accounts Store, (2.0 Complaint Submission) to Complaints Store, (3.0 Proximity & TSP Engine) calculating routes, (4.0 Route Lock & Dispatch) freezing driver queues, (5.0 Resolution Verification) storing proof photos, and (6.0 Municipal Analytics & CSV Export) serving administrative oversight.

## 5.11 Prototype / User Interface Design
The prototype design phase serves as a vital bridge between abstract architectural specifications and concrete software implementation. In modern software engineering lifecycles, user interface prototyping validates interaction paradigms, navigational flow, screen hierarchy, and information density prior to full-scale frontend development. The conceptual prototypes for UrbanClean were formulated using a user-centered design (UCD) approach, prioritizing accessibility, minimal cognitive load for citizens reporting incidents in field conditions, streamlined workflow efficiency for field collection drivers, and comprehensive operational situational awareness for municipal administrators.

### UI/UX Design Methodology
The design of UrbanClean's interfaces follows four foundational design principles:
1. **User-Centered Role Separation:** Interface layouts are strictly partitioned across three primary user roles—Citizens, Drivers, and Municipal Administrators—alongside a public guest experience. Each portal exposes exclusively the controls, telemetric cards, and navigational actions relevant to the logged-in actor's functional responsibilities.
2. **Visual Hierarchy and Glassmorphic Styling:** A modern aesthetic employing high-contrast typography, distinctive visual cards, crisp data tables, and translucent glassmorphism accents ensures legibility under diverse lighting environments, including outdoor handheld usage.
3. **Responsive and Device-Agnostic Layouts:** Viewports are engineered with fluid CSS grid and flexbox constructs, guaranteeing functional fidelity across desktop workstations (1920x1080), administrative dashboard displays, tablets, and mobile smartphone displays (360x640 to 414x896).
4. **GIS Map Usability and Spatial Interaction:** Geospatial mapping components utilize intuitive pan-and-zoom controls, distinctive color-coded markers representing incident urgency, interactive location pinning, and dynamic polyline overlays for turn-by-turn routing visualization.

*Distinction Note:* The wireframe interface mockups presented in this section (Figures 5.5 through 5.16) illustrate the conceptual architectural UI designs and layout schematics formulated during the design phase. These prototype models contrast with the actual production execution screenshots documented in Chapter 6 (Figures 6.1 through 6.7), which capture the fully realized, styled runtime application running on live local servers.

[INSERT FIGURE HERE: Figure 5.5]
*Figure 5.5: Prototype — Public Landing Page & Cleanliness Statistics*

### Explanation of Figure 5.5:
Figure 5.5 illustrates the conceptual wireframe prototype for the public guest landing page. The interface features a prominent navigation header with direct login routing, a hero section detailing municipal cleanliness objectives, three live statistical counter cards summarizing city-wide cleanliness impact (Issues Resolved, Active Complaints, and Registered Citizens), and a read-only interactive map overview displaying resolved and pending waste incidents across municipal zones.

[INSERT FIGURE HERE: Figure 5.6]
*Figure 5.6: Prototype — Multi-Role Unified Authentication Portal*

### Explanation of Figure 5.6:
Figure 5.6 displays the prototype design for the unified multi-role authentication interface. To minimize authentication friction while enforcing strict role separation, the interface incorporates segmented tab selectors allowing users to switch between Citizen, Driver, and Municipal Administrator login modes, each paired with username/email and password credential fields, client-side validation triggers, and direct registration redirects.

[INSERT FIGURE HERE: Figure 5.7]
*Figure 5.7: Prototype — Citizen Registration & Account Creation*

### Explanation of Figure 5.7:
Figure 5.7 depicts the architectural mockup of the citizen registration interface. The form captures essential citizen identity attributes—including full name, phone number, residential municipal ward, email address, and secure password credentials—with immediate client-side format validation before submitting user payload objects to the backend cryptographic salting and hashing service.

[INSERT FIGURE HERE: Figure 5.8]
*Figure 5.8: Prototype — Citizen Waste Reporting & Incident Logging Form*

### Explanation of Figure 5.8:
Figure 5.8 presents the prototype wireframe for the citizen waste complaint reporting form. Designed for rapid incident logging, the interface provides dropdown categorization (Household, Hazardous, Recyclable, Construction, Electronic), detailed landmark input fields, a W3C GPS auto-detection button, photographic evidence upload controls with 5 MB file constraint indicators, and an interactive submission action invoking the REST complaint ingestion pipeline.

[INSERT FIGURE HERE: Figure 5.9]
*Figure 5.9: Prototype — Interactive Geographic Location Selection & Map Canvas*

### Explanation of Figure 5.9:
Figure 5.9 illustrates the conceptual design for the interactive Leaflet map canvas embedded within the citizen reporting view. When automated GPS satellite positioning is unavailable or imprecise, citizens can pan across the cartographic tile layer and click directly on the canvas to drop a repositionable marker, automatically extracting latitude and longitude coordinates and triggering reverse-geocoding to resolve street-level landmark text.

[INSERT FIGURE HERE: Figure 5.10]
*Figure 5.10: Prototype — Citizen Real-Time Complaint Tracking & Lifecycle Dashboard*

### Explanation of Figure 5.10:
Figure 5.10 delineates the prototype design for the citizen complaint tracking dashboard. The screen presents a filterable tabular overview of all historical complaints submitted by the authenticated citizen account, showcasing ticket identifier badges, submission dates, waste category chips, thumbnail evidence previews, and color-coded lifecycle status tags (Pending, Assigned, In Progress, Completed).

[INSERT FIGURE HERE: Figure 5.11]
*Figure 5.11: Prototype — Waste Collection Driver Duty Dashboard*

### Explanation of Figure 5.11:
Figure 5.11 showcases the prototype layout for the waste collection driver operational dashboard. The interface equips collection drivers with essential field telemetry, including assigned vehicle identifiers, active duty shift status, daily collection quotas, and an interactive queue of assigned waste collection stops populated through administrative dispatch.

[INSERT FIGURE HERE: Figure 5.12]
*Figure 5.12: Prototype — Driver TSP Route Optimization & Real-Road Navigation Map*

### Explanation of Figure 5.12:
Figure 5.12 displays the architectural mockup for the driver route optimization and navigation workspace. The prototype demonstrates the integration of the Greedy Nearest-Neighbor Traveling Salesperson Problem (TSP) algorithm with OSRM routing services, projecting sequenced collection waypoints, road-following navigation polylines, cumulative driving distance, and estimated transit times across the interactive map viewport.

[INSERT FIGURE HERE: Figure 5.13]
*Figure 5.13: Prototype — Proof-of-Cleanup Image Upload & Verification Interface*

### Explanation of Figure 5.13:
Figure 5.13 illustrates the prototype wireframe for the post-collection verification and proof upload interface. To maintain accountability and prevent premature ticket closure, the form requires drivers to capture an on-site completion photograph, select the resolved ticket ID, enter operational notes, and transmit the multipart form to transition the ticket lifecycle to Completed.

[INSERT FIGURE HERE: Figure 5.14]
*Figure 5.14: Prototype — Municipal Administrator Command Center & Analytics Dashboard*

### Explanation of Figure 5.14:
Figure 5.14 presents the prototype layout for the municipal administrator command center. The dashboard provides executive situational awareness through high-level metric cards (Total Complaints, Solved Today, Pending Action, Active Field Drivers), real-time incident activity feeds, driver fleet status monitors, and administrative dispatch controls.

[INSERT FIGURE HERE: Figure 5.15]
*Figure 5.15: Prototype — City-Wide Waste Monitoring Map & GIS Filtering*

### Explanation of Figure 5.15:
Figure 5.15 showcases the conceptual prototype for the city-wide administrative GIS monitoring map. The viewport displays all reported municipal waste incidents mapped across geographic wards with status-distinctive marker clusters, accompanied by category and status filtering panels, interactive popups detailing complaint specifics, and driver location overlays.

[INSERT FIGURE HERE: Figure 5.16]
*Figure 5.16: Prototype — Municipal Monthly Compliance Tracking & Data Export Report*

### Explanation of Figure 5.16:
Figure 5.16 details the prototype design for the municipal compliance reporting and data export interface. The view aggregates monthly incident resolution metrics, SLA compliance percentages, driver performance statistics, and ward-level distribution tables, featuring an integrated 'Export to CSV / Excel' tool facilitating external municipal auditing and regulatory archiving.

## 5.12 Prototype–Architecture Mapping
To validate the architectural integrity of the system design, each prototype interface is systematically mapped to corresponding functional components across the three architectural tiers: Presentation Layer, Application/Business Logic Layer, and Data Persistence Layer. Table 5.6 outlines this structural correspondence.

Table 5.6: Prototype–Architecture Tier Mapping
| Interface Screen Prototype | Presentation Layer Artifact | Application Tier Services & Endpoints | Data Layer Entities & Tables |
| :--- | :--- | :--- | :--- |
| Landing Page (Fig 5.5) | index.html, Glassmorphic CSS | GET /api/complaints, Statistics Aggregator | complaints (read-only count) |
| Multi-Role Login (Fig 5.6) | login.html, Role Tabs, DOM Handler | POST /api/auth/login, PBKDF2 Verifier | accounts (role, passwordHash, salt) |
| Citizen Registration (Fig 5.7) | login.html (Register Tab), Regex Validator | POST /api/auth/register, Salt Generator | accounts (Insert new user row) |
| Complaint Form (Fig 5.8) | citizen.html, Multer Form, GPS Button | POST /api/complaints, Multer Ingestion | complaints (status='Pending', photo path) |
| Map Selection (Fig 5.9) | Leaflet Canvas, OSM Tile Layer | OSM Nominatim Geocoder API | Geo-coordinates (lat, lng, landmark) |
| Complaint Tracking (Fig 5.10) | citizen.html, Dynamic Table Renderer | GET /api/complaints, User Filter | complaints (userId indexed query) |
| Driver Dashboard (Fig 5.11) | driver.html, Telemetry Cards, Shift Toggle | GET /api/driver/routes, Roster Service | drivers, driverRoutes |
| Route Navigation (Fig 5.12) | Leaflet Polylines, OSRM Renderer | POST /api/routes/optimize, TSP Engine | driverRoutes, complaints (lat, lng) |
| Proof Upload (Fig 5.13) | driver.html, Cleanup Modal, File Upload | POST /api/complaints/:id/resolve, Multer | complaints (proofPhoto, status='Completed') |
| Admin Command Center (Fig 5.14) | admin.html, KPI Metric Cards, Activity Feed | GET /api/admin/metrics, Dispatcher | accounts, complaints, drivers |
| Monitoring Map (Fig 5.15) | Leaflet GIS Layer, Category Filter Drawer | GET /api/complaints/all, GeoJSON Stream | complaints (All active & solved rows) |
| Compliance Report (Fig 5.16) | admin.html, Reporting Grid, CSV Exporter | GET /api/admin/export-csv, Analytics Engine | dailyRouteSnapshots, complaints audit |

This systematic alignment ensures that every graphical control exposed to end users is directly backed by robust RESTful routing logic, deterministic business rules, and synchronized dual-persistence database stores.

---

# CHAPTER 6 — APPLICATION DEVELOPMENT

## 6.1 Introduction & Development Environment
The Implementation phase translates architectural models and database schemas into functional software artifacts. UrbanClean is implemented using modular JavaScript across both client and server tiers.
- **Operating System:** Windows 11 Home (64-bit) / Ubuntu 22.04 LTS.
- **IDE:** Visual Studio Code (v1.85+) with ESLint, Prettier, and REST Client extensions.
- **Runtime Environment:** Node.js v20.x LTS with npm package manager.
- **Database Tools:** DB Browser for SQLite (v3.12.x) for database schema inspection and verification.
- **Testing Tools:** Google Chrome DevTools, Postman v10.x, Puppeteer Core.

## 6.2 Technology Stack Implementation Details
- **Frontend:** HTML5 Semantic Elements, CSS3 (Glassmorphism design system), Vanilla JavaScript ES6+, Leaflet.js v1.9.4.
- **Backend:** Node.js, Express.js v4.19.2, Multer v1.4.5-lts.1, CORS, Child Process.
- **Database:** JSON Document Store (`db.json`) and SQLite3 (`urban_clean.db`).
- **External Geospatial APIs:** OpenStreetMap Tile Server, OSM Nominatim Geocoder, Project-OSRM Routing API.

## 6.3 Frontend Implementation
Implemented as a high-performance Single Page Application (SPA) architecture across five modular HTML files:
- `index.html`: Public homepage featuring city cleanliness counters (12,459 Issues Resolved, 349 Active Complaints, 9,876 Happy Citizens) and a read-only live complaint map.
- `login.html`: Multi-role authentication interface with dedicated tabs for Citizen, Driver, and Admin.
- `citizen.html`: Citizen workspace with auto-detect GPS, Leaflet pin placement, category selection, and 'My Reports' tracking table.
- `driver.html`: Route optimization workspace with collection stop pinning, 1.0 km proximity filtering, TSP route generation, and cleanup verification forms.
- `admin.html`: Municipal command dashboard displaying live KPI cards, city-wide complaint map, driver roster, and CSV export.

## 6.4 Backend Implementation
The backend application (`backend/server.js`) operates on Node.js using Express:
- Implements RESTful routes for user registration, authentication, complaint ingestion, and route optimization.
- Manages file ingestion via Multer, saving validated images to `backend/uploads/`.
- Executes synchronous `sync_sqlite.py` calls on every database write operation.

## 6.5 Database Integration
- **Active Document Store:** `backend/db.json` structures entities into top-level keys: `accounts`, `complaints`, `drivers`, `driverRoutes`, `dailyRouteSnapshots`.
- **Relational Tables:** Synchronized automatically into `backend/urban_clean.db` with structured schemas matching Tables 5.1 through 5.5.

## 6.6 Authentication & Validation Implementation
- User passwords are encrypted using PBKDF2 with SHA-512 and unique 16-byte random salts.
- Authenticated user state is persisted in client `localStorage` under key `'urban_clean_user'`.
- Page access security is enforced via `verifyPageSecurity()`, which inspects role permissions on every page load.

## 6.7 Complaint Management & Geospatial Algorithms
- **Complaint Submission:** Citizens submit complaints via multipart form submission to `POST /api/complaints`. Backend initializes ticket status to `'Pending'`, persists coordinates, and stores photo path. Tickets progress through deterministic states: `Pending` -> `Assigned` -> `In Progress` -> `Completed`.
- **GPS Coordinates Acquisition:** Citizens acquire coordinates via `navigator.geolocation.getCurrentPosition()` or by clicking on the Leaflet map canvas. Coordinates are reverse-geocoded via OSM Nominatim API to populate human-readable address names.
- **Haversine 1.0 km Proximity Filter:** Proximity calculations utilize the spherical Haversine formula:
  $$d = 2R \\arcsin\\left(\\sqrt{\\sin^2\\left(\\frac{\\Delta \\phi}{2}\\right) + \\cos(\\phi_1)\\cos(\\phi_2)\\sin^2\\left(\\frac{\\Delta \\lambda}{2}\\right)}\\right)$$
  where $R = 6371\\text{ km}$. Complaints with $d \\le 1.0\\text{ km}$ from collection points are marked eligible for driver collection.
- **Greedy TSP & OSRM Road Routing:** Driver waypoints are sequenced in $O(N^2)$ time using the Greedy Nearest-Neighbor heuristic, and the ordered coordinates are submitted to OSRM to render real-road navigation polylines.

## 6.8 Error Handling Architecture
- **Multer Middleware Error Handling:** Implemented a 4-parameter Express error-handling middleware catching `MulterError` and custom validation rejections, ensuring invalid file uploads (such as non-image files or payloads exceeding 5 MB) return clean JSON responses (`{"error": "Only image files are allowed!"}`) rather than raw HTML stack traces.
- **OSRM Network Fallback:** If the external OSRM demonstration server experiences network timeouts or rate throttling, the platform degrades gracefully by rendering straight-line Haversine geodesic paths between ordered waypoints, ensuring driver workflow continuity.

## 6.9 Screen Walkthrough & Implemented Features
The screenshots below capture actual working execution states of the UrbanClean platform:

[INSERT FIGURE HERE: Figure 6.1]
*Figure 6.1: Public Landing Page, Multi-Role Login & Citizen Registration*

### Explanation of Figure 6.1:
Figure 6.1 illustrates the public entry points of UrbanClean: the public landing page with live city cleanliness metrics (12,458 issues resolved, 346 active complaints), the unified multi-role login interface supporting Citizen, Driver, and Admin credentials, and the citizen account registration form.

[INSERT FIGURE HERE: Figure 6.2]
*Figure 6.2: Citizen Waste Reporting Interface & Interactive Map Pinning*

### Explanation of Figure 6.2:
Figure 6.2 showcases the citizen waste reporting workspace. Citizens can select waste categories from a dropdown, enter landmark descriptions, acquire exact GPS coordinates, or place an interactive marker directly on the Leaflet map canvas.

[INSERT FIGURE HERE: Figure 6.3]
*Figure 6.3: GPS Geolocation Telemetry, Citizen Ticket Tracking & Driver Dashboard*

### Explanation of Figure 6.3:
Figure 6.3 displays the acquired W3C GPS location (`19.157006, 73.238692 - Badlapur, Thane`), the citizen 'Track Your Complaints' table showing ticket `COMP-492` with live status progression, and the collection driver route optimization workspace.

[INSERT FIGURE HERE: Figure 6.4]
*Figure 6.4: Driver Optimized Route Map (5 Stops) & Proof-of-Cleanup Upload*

### Explanation of Figure 6.4:
Figure 6.4 demonstrates the driver field workspace where 5 collection waypoints are sequenced and projected onto real streets using OSRM, alongside the cleanup progress update form requiring an after-cleanup photo upload before marking a ticket completed.

[INSERT FIGURE HERE: Figure 6.5]
*Figure 6.5: Municipal Administrator Command Center, Active Drivers & Daily Complaints Modal*

### Explanation of Figure 6.5:
Figure 6.5 documents the municipal command dashboard displaying live KPI cards (5 Reported Today, 4 Pending Collection, 1 Solved Today), active driver fleet status, and the detailed complaints modal.

[INSERT FIGURE HERE: Figure 6.6]
*Figure 6.6: City-Wide Waste Monitoring Map & Monthly Compliance Tracking Report with Excel Export*

### Explanation of Figure 6.6:
Figure 6.6 illustrates the interactive city-wide waste monitoring map with color-coded status pins and the comprehensive 30-day compliance tracking table with one-click 'Export to Excel' CSV download capability.

[INSERT FIGURE HERE: Figure 6.7]
*Figure 6.7: Mobile Responsive Device View across Smartphone Viewport*

### Explanation of Figure 6.7:
Figure 6.7 validates the mobile responsive design of UrbanClean rendered on a smartphone viewport via local Wi-Fi LAN access (`http://192.168.1.7:3000`), demonstrating full functionality across handheld devices.
"""
