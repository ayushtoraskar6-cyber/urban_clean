# -*- coding: utf-8 -*-
"""
Chapter 1 (Problem Identification & Feasibility Study) & Chapter 2 (Requirement Engineering)
Structured strictly according to the required academic format.
"""

CH1_CH2_TEXT = r"""# CHAPTER 1 — PROBLEM IDENTIFICATION & FEASIBILITY STUDY

## 1.1 Identification of a Real-World Problem
Urban solid waste management constitutes one of the most critical civic responsibilities maintained by municipal corporations and urban local bodies (ULBs). Across rapidly urbanizing metropolitan regions such as Mumbai (MCGM), Thane (TMC), and Kalyan-Dombivli (KDMC), exponential commercial expansion and high population density generate thousands of metric tons of municipal solid waste daily. Operational municipal expenditure on waste collection consumes millions of rupees annually in vehicular fuel, personnel work-hours, and equipment maintenance.

### Nature and Classification of the Problem:
The waste-management crisis addressed by **UrbanClean** is fundamentally a **Municipal and Social Civic Problem**:
- **Municipal Operational Bottleneck:** Traditional waste management operates on static, historical collection routes without real-world telemetry or awareness of actual dumpster fill levels. Sanitation compactor trucks follow fixed weekly timetables, visiting half-empty bins while overflowing dumpsters in adjacent neighborhoods remain unserviced for days. This causes excessive diesel fuel waste, unnecessary vehicular wear, and severe labor misallocation.
- **Social and Environmental Hazard:** Unattended waste heaps create immediate public health hazards, including groundwater leaching, foul odors, vector-borne disease proliferation (dengue, malaria, cholera), stray animal scavenging, and blocked municipal stormwater drains during heavy monsoon seasons.
- **Civic Trust Deficit:** Citizens encounter significant friction when attempting to lodge civic grievances. Traditional helplines and paper-based ward registers are unresponsive, lack tracking transparency, and offer zero accountability, breeding public cynicism toward local governance bodies.

Through comprehensive analysis of municipal solid waste management operations, four critical structural bottlenecks were identified:
1. **Ambiguous Landmark Descriptions:** Citizens lodge complaints using vague physical landmarks (e.g., "near corner temple" or "behind general store"), leaving field drivers unable to pinpoint exact dumpster coordinates.
2. **Civic Opacity ("Black Hole" Redressal):** Citizens have zero visibility into complaint resolution progress once a report is submitted, breeding distrust between the public and urban local bodies.
3. **Redundant Fleet Mileage & Fuel Waste:** Sanitation trucks drive unoptimized, circuitous paths, idling in heavy urban traffic and burning excessive diesel fuel.
4. **Administrative Data Fragmentation:** Municipal officers lack a centralized real-time dashboard to monitor zone-wide complaint hotspots, track on-duty driver workforce availability, and enforce service level agreements (SLAs).

In the conventional municipal setup, street sweepers gather waste into unmonitored dumpsters, compactor trucks follow static weekly schedules regardless of bin fill levels, and citizens must visit ward offices or call landlines to register complaints. Verbal dispatches and unverified paper checkmarks leave complaints marked "resolved" without proof, resulting in abandoned tickets, massive fuel waste, and severe data loss.

## 1.2 Problem Justification and Scope Definition
There is an urgent requirement for an integrated, multi-role web platform that captures precise GPS-geotagged waste reports with photographic evidence, isolates nearby complaints using spatial proximity algorithms, optimizes collection routes for field drivers using road-network routing engines, and provides municipal directors with live administrative governance tools.

**UrbanClean** replaces the obsolete conventional workflow with a unified, cloud-accessible, geospatial web architecture designed to achieve clear operational objectives:
1. **Digitize Civic Grievance Lodgment:** Citizens drop a pin directly onto a live Leaflet map canvas or click "Auto-Detect GPS" to obtain high-precision W3C geolocation coordinates with mandatory photographic attachments.
2. **Algorithmic Proximity Filtering:** On-duty drivers see only active complaints situated within a 1.0 km spherical radius of their collection points, preventing cognitive overload.
3. **Turn-by-Turn Route Optimization:** Waypoints are ordered mathematically using a Greedy Nearest-Neighbor Traveling Salesperson Problem (TSP) heuristic and projected onto real streets using OSRM, generating turn-by-turn road geometry and calculating realistic fuel savings (22% to 32%).
4. **Operational Shift Stability:** A Daily Route-Lock engine prevents driver task overload by locking today's route snapshot and automatically queuing overflow complaints for tomorrow.
5. **Closed-Loop Resolution Verification:** A ticket cannot be closed until the driver captures and uploads an after-cleanup photograph of the cleared location.
6. **Centralized Municipal Governance:** Real-time administrative command dashboards provide live KPI statistics, jurisdiction auto-locking, and downloadable 30-day compliance CSV exports.

### Scope of the System:
To maintain rigorous engineering focus and deliver a robust solution within academic project boundaries, the system's operational scope is explicitly delineated:

**What the System Covers (In Scope):**
- **Multi-Role Web Application:** Dedicated, role-segregated portals for Guests, Citizens, Collection Drivers, and Municipal Administrators.
- **Geospatial Reporting Canvas:** Interactive Leaflet.js map with OpenStreetMap cartography, draggable pin placement, and W3C device GPS auto-detection.
- **Closed-Loop Photographic Audit Trail:** Mandatory citizen photo submission before ticket creation, and mandatory driver after-cleanup photo upload before ticket closure.
- **Algorithmic Fleet Optimization:** Client-side and server-side Haversine geodesic distance filtering (1.0 km threshold) and Greedy TSP stop sequencing paired with OSRM driving network polylines.
- **Shift Stability Protection:** Daily Route-Lock engine that snapshots active stops and queues late submissions into tomorrow's dispatch roster.
- **Administrative Command Center:** Ward-locked municipal monitoring dashboards with real-time KPI counter cards and 30-day CSV compliance auditing exports.
- **Dual-Layer Persistence:** Operational file-backed JSON document store (`db.json`) mirrored synchronously to an embedded SQLite relational database (`urban_clean.db`).

**What the System Does NOT Cover (Out of Scope):**
- **Hardware Bin Sensors:** Does not require ultrasonic physical IoT level sensors mounted on public dumpsters (eliminating hardware capital expenditure and battery maintenance overhead).
- **Automated Computer Vision Classification:** Does not perform server-side deep learning AI image classification to verify waste composition.
- **Native Mobile App Store Packaging:** Does not provide standalone compiled Android APK or iOS IPA application packages; operates exclusively as a mobile-responsive web application accessible via modern mobile browsers.
- **Financial Gateway Integration:** Does not incorporate civic fine billing, waste taxation, or payment gateway processing.

## 1.3 Stakeholder Identification
The platform serves four primary stakeholder groups documented across the project lifecycle:

### Table 1.1: Stakeholder Identification and System Expectations
| Stakeholder Group | Role in System | Key Needs & Expectations | Primary Benefit Received |
| :--- | :--- | :--- | :--- |
| **Citizens / Residents** | Incident Reporters | Fast reporting (<1 min), GPS pin-pointing, live ticket tracking | Clean neighborhoods, transparent civic response |
| **Collection Drivers** | On-Field Operators | Clear route instructions, optimized stops, workload stability | Reduced driving distance, predictable daily shifts |
| **Municipal Administrators** | Governance & Supervisors | City-wide KPI visibility, driver tracking, compliance auditing | Data-driven decision making, fuel budget savings |
| **General Public / Guests** | Unauthenticated Visitors | Transparent cleanliness metrics, pickup schedules | Public awareness, municipal trust building |

## 1.4 Feasibility Analysis
A rigorous three-dimensional feasibility analysis was conducted to evaluate the viability of UrbanClean:

### 1.4.1 Technical Feasibility
UrbanClean is built upon mature, industry-standard web technologies. The frontend uses standard HTML5, CSS3, and JavaScript ES6+ alongside Leaflet.js (a lightweight 42 KB open-source mapping engine). The backend utilizes Node.js and Express.js, providing an event-driven, non-blocking asynchronous architecture capable of handling thousands of concurrent requests. Geospatial data is acquired via the browser W3C Geolocation API, and real-road driving calculations leverage the Open Source Routing Machine (OSRM) public API. Data persistence uses an active JSON store (`db.json`) mirrored synchronously to SQLite (`urban_clean.db`). All components operate on open-source licenses without proprietary software dependencies, confirming high technical feasibility.

### 1.4.2 Economic Feasibility
Traditional smart-waste initiatives propose installing ultrasonic IoT sensors on thousands of municipal dumpsters, entailing prohibitive hardware costs ($50–$150 per bin), battery maintenance, and cellular SIM subscriptions. UrbanClean achieves crowdsourced waste detection and route optimization using smartphones and web browsers already possessed by citizens and drivers. The total hardware expenditure is **zero**. Software infrastructure costs are minimal, utilizing open-source frameworks and free OpenStreetMap cartography. The projected economic return is compelling: documented project models estimate a **22% to 32% reduction in fleet fuel consumption**, generating immediate recurring operational savings for municipal corporations.

### 1.4.3 Operational Feasibility
The platform addresses deeply felt, real-world operational challenges for municipal authorities. For citizens, the reporting workflow requires under one minute across three intuitive steps (Locate, Categorize, Submit). For drivers, the 1.0 km Haversine proximity filter and Daily Route-Lock system eliminate route chaos and task overload. For administrators, the dashboard presents instant visual KPIs without manual spreadsheet collation. The user interface employs an intuitive Glassmorphism design system that requires zero specialized technical training, ensuring high operational acceptance.

---

# CHAPTER 2 — REQUIREMENT ENGINEERING

## 2.1 Functional Requirements Specification
The functional requirements define the explicit system capabilities, user actions, and algorithmic behaviors supported by the platform. The complete catalog of 28 functional requirements across the system modules is specified below:

### Table 2.1: Functional Requirements Specification (FR-01 to FR-28)
| ID | Functional Requirement | Description | Priority |
| :--- | :--- | :--- | :--- |
| **FR-01** | Multi-Role Registration | The system shall allow Citizens and Drivers to register using role-specific fields (name, email, password, city, vehicle ID for drivers). Admin public signup is prohibited. | High |
| **FR-02** | Credential Authentication | The system shall authenticate users against cryptographically salted and hashed passwords stored in the database. | High |
| **FR-03** | Role-Based Access Control | The system shall enforce role-based access control (RBAC), restricting portal pages and API endpoints strictly to authorized roles. | High |
| **FR-04** | Public Guest Dashboard | The system shall allow unauthenticated visitors to view city-wide cleanliness metrics, recent reports, and read-only map previews. | Medium |
| **FR-05** | Session Invalidation | The system shall provide a secure logout mechanism that invalidates browser session tokens and prevents back-button view restoration. | High |
| **FR-06** | Session Inactivity Timeout | The system shall automatically terminate user sessions after a configurable period of client inactivity. | Low |
| **FR-07** | GPS Geolocation Capture | The system shall allow citizens to capture exact coordinates via the browser W3C Geolocation API or by dropping a draggable pin on a Leaflet map. | High |
| **FR-08** | Mandatory Photo Evidence | The system shall require at least one photographic attachment as visual evidence before a complaint can be lodged. | High |
| **FR-09** | Waste Categorization | The system shall allow citizens to classify complaints under standardized categories (Overflowing Bin, Garbage Heap, Hazardous Waste, Dead Animal). | Medium |
| **FR-10** | Reverse Geocoding | The system shall query the OSM Nominatim API to convert captured latitude and longitude coordinates into human-readable street addresses. | High |
| **FR-11** | Unique Ticket Generation | The system shall persist every complaint with a unique ticket identifier (e.g., COMP-001), submission timestamp, and initial status 'Pending'. | High |
| **FR-12** | Live Ticket Tracking | The system shall display the live status of submitted complaints (Pending → Assigned → In Progress → Completed) on the citizen's personal dashboard. | High |
| **FR-13** | Strict Citizen Data Isolation | The system shall ensure citizens can view and query only their own submitted complaints, completely isolating records between different residents. | High |
| **FR-14** | Haversine Proximity Filter | The system shall compute the spherical geodesic distance between driver collection points and active complaints, filtering only complaints within 1.0 km. | High |
| **FR-15** | Automated Driver Assignment | The system shall automatically associate open complaints in a municipal zone with on-duty drivers assigned to that jurisdiction. | High |
| **FR-16** | Greedy TSP Route Optimization | The system shall execute an internal Greedy Nearest-Neighbor Traveling Salesperson Problem heuristic to calculate the optimal stop sequence. | High |
| **FR-17** | OSRM Road Path Rendering | The system shall query the OSRM Driving API with ordered waypoints to render true street-level navigation polylines and road travel distances. | High |
| **FR-18** | Daily Route-Lock System | The system shall allow drivers to freeze their daily route snapshot ('Start Shift / Lock Route'), routing subsequent complaints into Tomorrow's Queue. | High |
| **FR-19** | Driver Shift Duty Toggle | The system shall allow drivers to toggle their operational shift status between On-Duty and Off-Duty, dynamically updating driver rosters. | High |
| **FR-20** | Stop Sequence Navigation | The system shall display sequenced collection stops to drivers on an interactive map with turn-by-turn order and distance metrics. | High |
| **FR-21** | Proof-of-Cleanup Upload | The system shall require drivers to upload an after-cleanup photograph before a complaint ticket can be transitioned to 'Completed'. | High |
| **FR-22** | Closed-Loop Resolution | The system shall update the ticket status to 'Completed' and record an immutable resolution timestamp upon proof acceptance. | High |
| **FR-23** | Driver Notification Dispatch | The system shall push real-time alerts to drivers when new stops are assigned or routes re-optimized. | Low |
| **FR-24** | Real-Time Admin KPI Cards | The system shall present administrators with live counters showing Total Reported Today, Pending Collection, In Progress, and Solved Today. | High |
| **FR-25** | Driver Roster Management | The system shall allow administrators to view and filter driver rosters by active status, vehicle number, and completed task counts. | High |
| **FR-26** | Manual Task Reassignment | The system shall allow administrators to manually override automated assignments and reassign complaints to another driver. | Medium |
| **FR-27** | 30-Day CSV Report Export | The system shall allow administrators to generate and download a comprehensive 30-day compliance report formatted as an Excel-compatible CSV. | Medium |
| **FR-28** | SLA Breach Escalation | The system shall visually flag complaints that remain unresolved beyond a configurable SLA threshold (default 48 hours). | Medium |

## 2.2 Non-Functional Requirements
The non-functional requirements govern the platform's operational qualities, performance thresholds, security standards, and system reliability:

### Table 2.2: Non-Functional Requirements Specification (NFR-01 to NFR-19)
| ID | Requirement Area | Requirement Statement & Target Metric |
| :--- | :--- | :--- |
| **NFR-01** | Performance | The system shall return map queries, complaint searches, and dashboard metrics within 2.0 seconds under normal load (up to 200 concurrent users). |
| **NFR-02** | Performance | The TSP route optimization computation shall complete within 3.0 seconds for driver routes containing up to 25 collection waypoints. |
| **NFR-03** | Performance | The server shall sustain at least 500 concurrent active users without response latency exceeding 3.0 seconds. |
| **NFR-04** | Usability | The citizen complaint submission workflow shall be completable in three steps or fewer: Locate on map, Categorize, and Submit. |
| **NFR-05** | Usability | The interface shall present a consistent, mobile-responsive layout verified across modern desktop, tablet, and smartphone viewports. |
| **NFR-06** | Usability | The system shall provide distinct, standardized color-coded status badges: Yellow (Pending), Blue (Assigned), Orange (In Progress), Green (Completed). |
| **NFR-07** | Security | All user passwords shall be stored using PBKDF2/SHA-512 cryptographic salting and hashing; plaintext passwords shall never be persisted. |
| **NFR-08** | Security | The system shall enforce role-based access control (RBAC) on every API endpoint, rejecting unauthorized requests with HTTP 403 Forbidden. |
| **NFR-09** | Security | All client-server communication shall be secured in transit using HTTPS / TLS 1.2+ encryption. |
| **NFR-10** | Security | The system shall validate and sanitize all user input (text, coordinates, file MIME types) to prevent XSS and injection attacks. |
| **NFR-11** | Reliability | The platform shall maintain 99.5% uptime during municipal operating hours (6:00 AM – 10:00 PM). |
| **NFR-12** | Reliability | The system shall ensure zero data loss during server restarts via automated real-time SQLite synchronization of all JSON writes. |
| **NFR-13** | Reliability | The system shall degrade gracefully—falling back to straight-line Haversine routing—if the external OSRM service is temporarily unreachable. |
| **NFR-14** | Maintainability | The backend shall be structured as modular Express.js services (Auth, Complaint, Driver, Admin) allowing component updates without system redeployment. |
| **NFR-15** | Scalability | The data architecture shall support scalable migration to PostgreSQL (v16.x) with PostGIS (v3.x) spatial indexing beyond 100,000 complaint rows. |
| **NFR-16** | Maintainability | The API shall follow versioned RESTful conventions with semantic JSON request and response payloads. |
| **NFR-17** | Data Integrity | The database shall enforce referential integrity between users, complaints, drivers, and routes via structured foreign key relationships. |
| **NFR-18** | Data Integrity | The system shall log status transition history with timestamps and actor IDs to guarantee complete auditability. |
| **NFR-19** | Portability | The web application shall operate seamlessly on Windows 10/11, macOS 12+, and Ubuntu 20.04 LTS+ without environment-specific code paths. |

## 2.3 Use Case Analysis and Actor Profiles
System privileges, functional access boundaries, and operational scopes are partitioned across four primary actors:
1. **Guest (Unauthenticated Public):** Public civic observers accessing the platform via `index.html`. Privileges include viewing aggregate municipal cleanliness KPI counters (resolved issues, active complaints, registered citizen metrics), inspecting recent localized waste complaints, and viewing scheduled municipal collection routes without credentials.
2. **Citizen (Civic Resident):** Registered community members authenticated via `login.html`. Capabilities include acquiring meter-precision W3C device coordinates or placing an interactive Leaflet map pin, selecting categorical waste types, attaching mandatory binary photographic evidence, submitting complaint tickets to `POST /api/complaints`, and tracking real-time status under an isolated 'My Reports' view.
3. **Collection Driver (Municipal Field Operator):** Sanitation truck operators operating vehicle hardware. Authenticated via `login.html`, drivers toggle shift duty status (Active / Off-Duty), inspect assigned collection stops, filter nearby complaints within a 1.0 km geodesic radius, execute the Greedy TSP heuristic to calculate optimal stop sequences, project road polylines via OSRM, freeze shifts via the Daily Route-Lock Engine, and upload after-cleanup proof photos.
4. **Municipal Administrator (Ward Supervisor):** Municipal executive personnel exercising jurisdictional governance. Authenticated with territorial locking (e.g., Kalyan, Bandra), administrators monitor real-time KPI command cards, inspect zone-wide Leaflet complaint distributions, manage driver duty rosters, override task assignments, and export comprehensive 30-day compliance audits formatted as CSV.

## 2.4 Requirement Prioritization – MoSCoW
Requirements were prioritized using the industry-standard **MoSCoW** framework:
- **Must Have (Essential Core):** Multi-role authentication (FR-01, FR-02, FR-03); Geotagged complaint reporting with mandatory photo proof (FR-07, FR-08, FR-11); 1.0 km Haversine proximity filter (FR-14); Greedy TSP + OSRM road route optimization (FR-16, FR-17); Daily Route-Lock system (FR-18); Closed-loop proof-of-resolution upload (FR-21); Admin command KPI dashboard (FR-24).
- **Should Have (High Value):** Automated GPS coordinate capture (FR-10); Reverse geocoding via Nominatim (FR-10); Strict citizen data isolation (FR-13); 30-day compliance CSV export (FR-27); Driver shift duty toggle (FR-19).
- **Could Have (Desirable):** SLA breach visual escalation flag (FR-28); Real-time driver reroute notification alert (FR-23); Public guest preview dashboard (FR-04).
- **Won't Have (Deferred to Future Scope):** Ultrasonic IoT physical bin sensors; Computer vision AI waste classification; Native mobile apps for iOS/Android.

## 2.5 Constraints and Assumptions
The operational and architectural constraints and foundational assumptions governing the UrbanClean project comprise:

**Project Constraints:**
- **Network Dependency:** Real-time map tile streaming from OpenStreetMap and turn-by-turn road geometry generation via OSRM require active internet connectivity.
- **Client Geolocation Accuracy:** GPS precision is subject to client hardware limitations, satellite visibility, and urban canyon signal reflection; interactive map pin placement serves as an essential manual fallback.
- **File Upload Limitations:** Photograph uploads are capped at 5 MB per image and strictly whitelisted to JPEG and PNG image MIME types to mitigate storage exhaustion and code execution risks.
- **Collection Stop Threshold:** Driver collection routes are computationally bounded at a maximum of 40 collection waypoints per shift to maintain sub-second Greedy TSP execution times.
- **Single Production Branch:** Version control workflows adhere strictly to a single `main` trunk on GitHub.

**Project Assumptions:**
- Citizens, drivers, and administrators access the platform through modern web browsers supporting HTML5 Geolocation, Canvas, and CSS Grid.
- Collection truck drivers operate vehicles equipped with internet-connected mobile smartphones or dashboard tablets.
- OpenStreetMap tile servers and Project-OSRM routing services maintain continuous availability over HTTPS.
- In compliance with civic record policies, complaint records follow an automated 30-day retention policy before archiving.

### Table 2.3: Hardware Requirements Specification
| Parameter | Minimum Client Specification | Recommended Development / Server Specification |
| :--- | :--- | :--- |
| **Processor** | Dual-Core 1.8 GHz (Intel / ARM) | Quad-Core 2.5 GHz+ (Intel Core i5 10th Gen+ / AMD Ryzen 5) |
| **Memory (RAM)** | 2 GB RAM (Smartphone) / 4 GB (PC) | 8 GB – 16 GB DDR4 RAM |
| **Storage** | 500 MB free browser cache space | 20 GB free SSD storage |
| **Display Resolution** | 375 × 667 (Mobile) / 1366 × 768 (Desktop) | 1920 × 1080 Full HD |
| **Network Interface** | 3G / 4G / Wi-Fi (min 1 Mbps) | Broadband Internet (min 10 Mbps) |

### Table 2.4: Software Technology Stack Specifications
| Layer / Component | Technology Used | Version / Specification | Purpose in Project |
| :--- | :--- | :--- | :--- |
| **Operating System** | Windows / Linux / macOS | Windows 11 (64-bit) / Ubuntu 22.04 LTS | Development and host environment |
| **Backend Runtime** | Node.js | v18.x – v20.x LTS | Server-side JavaScript event-driven engine |
| **Web Framework** | Express.js | v4.19.x | RESTful HTTP API routing and middleware |
| **File Handling** | Multer | v1.4.5-lts.1 | Multipart form-data and image disk storage |
| **Database Engine** | JSON Store + SQLite | `db.json` + SQLite v3.x (`urban_clean.db`) | Dual-persistence active store and relational mirror |
| **Database Sync Script** | Python | Python 3.11 – 3.13 (`sync_sqlite.py`) | Automated real-time SQLite mirroring |
| **Database Inspection** | DB Browser for SQLite | v3.12.x+ | Visual relational schema and table inspection |
| **Frontend Languages** | HTML5, CSS3, JavaScript | Modern W3C Standard, ES6+ | Single-page client presentation and controllers |
| **UI Design System** | Glassmorphism CSS | Custom `styles.css` / CSS custom properties | Translucent frosted-glass aesthetic |
| **Mapping Engine** | Leaflet.js | v1.9.4 | Interactive cartography and marker rendering |
| **Map Tiles** | OpenStreetMap | Standard Carto Tile Server (HTTPS) | Global open-source road network basemaps |
| **Geocoding Service** | OSM Nominatim | RESTful JSON API | Reverse geocoding of coordinates to street names |
| **Road Routing Engine** | Project-OSRM | v5.x Driving API (`router.project-osrm.org`) | Real-road polyline and road driving distance |
| **Development IDE** | Visual Studio Code | v1.85+ | Source code editing, debugging, terminal control |
| **Web Browsers** | Chrome, Edge, Firefox | Latest 2 versions | Client-side application execution |
"""
