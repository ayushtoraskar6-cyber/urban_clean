# -*- coding: utf-8 -*-
"""
Chapter 3 (SDLC Planning) & Chapter 4 (System Modeling Using UML)
"""

CH3_CH4_TEXT = """# CHAPTER 3 — SOFTWARE DEVELOPMENT LIFE CYCLE (SDLC) PLANNING

## 3.1 Introduction
The Software Development Life Cycle (SDLC) provides a systematic framework for structuring, planning, and executing the engineering phases required to build UrbanClean. Solid waste management systems involve multifaceted interdependencies between client-side geolocation APIs, real-time map tile rendering, mathematical optimization heuristics, and dual-layer database persistence. A structured lifecycle methodology guarantees high software quality, timely risk mitigation, and disciplined delivery.

## 3.2 Selected SDLC Model
For the development of UrbanClean, an **Iterative Agile Development Model** was selected. While the broader academic milestones adhered to sequential deliverables (Proposal, SRS, Architecture, Working Code, Final Submission), the actual technical development was organized into rapid, two-week iterative sprints.

## 3.3 Reason for Selecting the SDLC Model
The Iterative Agile methodology was chosen due to several critical project dynamics:
1. **Algorithm Refinement & Prototyping:** The route optimization pipeline required continuous empirical tuning of the spherical Haversine formula and Greedy TSP sequencing against realistic Mumbai road networks before final locking.
2. **Decoupled Architectural Sprints:** Allowed the team to build and stabilize the backend RESTful API and JSON persistence store independently while frontend Glassmorphism UI components were being refined.
3. **Continuous Stakeholder Feedback:** Regular weekly review meetings with faculty guide Prof. Aarti Gawai enabled prompt requirement adjustments without costly retrofits.
4. **Early Risk Mitigation:** High-risk integrations—such as public OSRM API response handling and W3C geolocation permissions—were implemented and stress-tested in early iterations.

## 3.4 SDLC Phases
Development was partitioned into five distinct, sequential phases:
- **Phase 1: Problem Identification & Requirements Engineering (Weeks 1–2):** Feasibility analysis, stakeholder interviews, user requirement prioritization, and drafting the formal SRS document.
- **Phase 2: Architectural & System Design (Weeks 3–4):** High-level 3-tier architecture design, UML modeling (Use Case, Class, Sequence, Activity, Component, Deployment diagrams), database schema modeling, and API contract specification.
- **Phase 3: Core Implementation & Algorithm Coding (Weeks 5–6):** Express.js REST server implementation, Leaflet.js mapping integration, Haversine 1.0 km proximity engine, Greedy TSP heuristic, and Daily Route-Lock mechanisms.
- **Phase 4: Verification, Testing & Bug Fixing (Week 7):** Comprehensive test execution (TC-01 through TC-52) across Functional, Boundary, Security, Database, and UI categories, followed by edge-case bug fixes.
- **Phase 5: Deployment, Demonstration & Documentation (Week 8):** Final GitHub repository freeze, academic project report compilation, viva presentation deck preparation, and final project demonstration.

## 3.5 Work Breakdown Structure (WBS)
The project activities were decomposed hierarchically:

### Table 3.1: Work Breakdown Structure (WBS)
| WBS Code | Phase / Task Name | Work Package Details | Primary Deliverable |
|---|---|---|---|
| 1.0 | Project Initiation | Problem identification, feasibility study, literature review | Approved Synopsis & Project Proposal |
| 2.0 | Requirements Analysis | Functional (FR-01 to FR-28) and Non-Functional (NFR-01 to NFR-19) drafting | Software Requirements Specification (SRS) |
| 3.0 | System Modeling & Design | UML design suite (8 diagrams) and relational schema design | Architecture Design Document (ADD) |
| 4.0 | Frontend Engineering | Glassmorphism CSS3 styling, Leaflet map canvas, DOM controllers (script.js) | Functional Single-Page Application Views |
| 5.0 | Backend & Algorithm Dev | REST API gateway (server.js), Multer photo uploads, TSP + OSRM routing | Node.js Express REST API Server |
| 6.0 | Data Persistence & Sync | Document store (db.json) and automated SQLite mirror (sync_sqlite.py) | Dual Data Storage Architecture |
| 7.0 | Testing & Verification | Test case design, execution of TC-01 to TC-52, performance benchmarking | STQA Test Case Execution Log |
| 8.0 | Final Delivery | Report generation, PowerPoint viva deck, code repository freeze | Final Project Report & Demonstration |

## 3.6 Project Activities
- **Activity A1 (01 Aug 2026):** Project topic formulation and Synopsis submission.
- **Activity A2 (02 Aug – 08 Aug 2026):** Feasibility analysis, stakeholder analysis, and Project Proposal defense.
- **Activity A3 (09 Aug – 24 Aug 2026):** Requirements engineering, drafting FRs/NFRs, and UML diagram modeling.
- **Activity A4 (25 Aug – 03 Sep 2026):** Technical architecture design, database schema formulation, and API specification.
- **Activity A5 (04 Sep – 15 Sep 2026):** Core full-stack coding: HTML/CSS frontend, Node.js backend, Leaflet maps, and TSP routing.
- **Activity A6 (16 Sep – 21 Sep 2026):** System integration testing, bug fixing, GitHub repository packaging, and report writing.
- **Activity A7 (22 Sep – 24 Sep 2026):** Viva presentation creation, demonstration rehearsing, and final project viva.

## 3.7 Project Timeline & Milestones
The project execution timeline strictly adhered to the academic schedule established by the Department of Computer Science:

### Table 3.2: Project Milestone Schedule (Project Gantt Chart Sem-V 2026-27)
| Deliverable / Milestone | Start Date | Completion Date | Duration | Status |
|---|---|---|---|---|
| Synopsis Submission | 01 Aug 2026 | 01 Aug 2026 | 1 Day | Completed |
| Project Proposal | 02 Aug 2026 | 08 Aug 2026 | 7 Days | Completed |
| SRS & UML Diagrams | 09 Aug 2026 | 24 Aug 2026 | 16 Days | Completed |
| Architecture Design Document | 25 Aug 2026 | 03 Sep 2026 | 10 Days | Completed |
| Working Application Development | 04 Sep 2026 | 15 Sep 2026 | 12 Days | Completed |
| GitHub Repository & Final Report | 16 Sep 2026 | 21 Sep 2026 | 6 Days | Completed |
| Presentation & Final Demonstration | 22 Sep 2026 | 24 Sep 2026 | 3 Days | Completed |

## 3.8 Resource Planning
- **Human Resources:** Ayush Santosh Toraskar (Sole Full-Stack Developer & Researcher); Prof. Aarti Gawai (Project Guide & Technical Mentor).
- **Software Resources:** Visual Studio Code IDE, Git/GitHub Version Control, Node.js runtime, DB Browser for SQLite, Postman REST Client.
- **Hardware Resources:** Laptop (Intel Core i5, 16 GB RAM, 512 GB NVMe SSD, Windows 11 64-bit); Android smartphone for mobile responsive testing and live GPS telemetry.

## 3.9 Risk Identification and Management
### Table 3.3: Risk Identification, Assessment, and Mitigation Matrix
| Risk ID | Identified Risk Event | Probability | Impact | Mitigation Strategy Implemented |
|---|---|---|---|---|
| RSK-01 | Public OSRM API network latency or rate throttling | Medium | High | Decoupled TSP waypoint ordering from road geometry; system computes Euclidean/Haversine fallback if OSRM is unreachable. |
| RSK-02 | Citizen GPS permission denial on client browsers | High | Medium | Implemented interactive map click-to-pin fallback, allowing manual pin dropping on default city coordinates. |
| RSK-03 | Server crash causing in-memory state loss | Low | High | Automated background SQLite mirroring (sync_sqlite.py) executes synchronously on every file-backed JSON write. |
| RSK-04 | Malicious file upload / arbitrary script execution | Medium | High | Multer middleware enforces strict 5 MB file size limit and whitelists image MIME types (image/jpeg, image/png). |
| RSK-05 | Unauthorized access to administrative command features | Low | High | Strict Role-Based Access Control (RBAC) enforced across frontend page guards and backend API endpoints. |

## 3.10 Project Gantt Chart (Sem-V 2026-27)
[INSERT FIGURE HERE: Figure 3.1]
*Figure 3.1: Project Gantt Chart (Sem-V 2026-27 Milestones & Timeline)*

The Gantt chart visually illustrates the linear milestone transitions across the project duration, ensuring timely completion of all deliverables leading to the final university demonstration.

---

# CHAPTER 4 — SYSTEM MODELING USING UML

## 4.1 Introduction & UML Overview
Unified Modeling Language (UML) represents the industry standard visual specification language used to specify, visualize, construct, and document the structural blueprints and dynamic operational behaviors of software systems. In the engineering of UrbanClean, system modeling serves as the vital bridge linking formal Software Requirements Specifications (SRS) with concrete full-stack architectural implementation.

The UrbanClean UML design suite models both structural architecture (static class relationships, runtime object snapshots, and physical deployment nodes) and dynamic behavioral interactions (user use-case boundaries, chronological inter-tier sequence flows, component interfaces, and procedural decision activities). All diagrams are sourced authoritatively from the validated system design specification (*UrbanClean UML & System Design Diagram Suite*).

## 4.2 Actors of the System
System privileges, functional access boundaries, and operational scopes are partitioned across four core actors:
1. **Guest (Unauthenticated Public):** Public civic observers accessing the platform via `index.html`. Privileges include viewing aggregate municipal cleanliness KPI counters (resolved issues, active complaints, registered citizen metrics), inspecting recent localized waste complaints, and viewing scheduled municipal collection routes without credentials.
2. **Citizen (Civic Resident):** Registered community members authenticated via `login.html`. Capabilities include acquiring meter-precision W3C device coordinates or placing an interactive Leaflet map pin, selecting categorical waste types, attaching mandatory binary photographic evidence, submitting complaint tickets to `POST /api/complaints`, and tracking real-time status under an isolated 'My Reports' view.
3. **Collection Driver (Municipal Field Operator):** Sanitation truck operators operating vehicle hardware. Authenticated via `login.html`, drivers toggle shift duty status (Active / Off-Duty), inspect assigned collection stops, filter nearby complaints within a 1.0 km geodesic radius, execute the Greedy TSP heuristic to calculate optimal stop sequences, project road polylines via OSRM, freeze shifts via the Daily Route-Lock Engine, and upload after-cleanup proof photos.
4. **Municipal Administrator (Ward Supervisor):** Municipal executive personnel exercising jurisdictional governance. Authenticated with territorial locking (e.g., Kalyan, Bandra), administrators monitor real-time KPI command cards, inspect zone-wide Leaflet complaint distributions, manage driver duty rosters, override task assignments, and export comprehensive 30-day compliance audits formatted as CSV.

## 4.3 UML Event Table
The Event Table models every fundamental transactional trigger within the UrbanClean ecosystem, detailing the event stimulus, its initiator, the system processing activity, the generated response, and the destination endpoint.

[INSERT FIGURE HERE: Figure 4.1]
*Figure 4.1: UML Event Table — System Triggers, Sources, and Responses*

### Explanation of Event Table:
Figure 4.1 enumerates the operational lifecycle events that drive the system:
- **Complaint Submission:** Initiated by a Citizen clicking 'Submit' with GPS coordinates and photo evidence; the system validates the payload, creates a ticket (`status = 'Pending'`), stores the photo to disk, and notifies the Admin Console.
- **User Authentication:** Initiated by any user role submitting email and password; the system validates the PBKDF2/SHA-512 salted hash, establishes an isolated client session, and redirects to the role-specific dashboard.
- **Task Assignment:** Initiated by the Admin dispatch engine; maps pending complaints to the nearest on-duty driver covering that municipal ward.
- **Route Optimization:** Initiated when waypoints are added to a driver schedule; the internal TSP heuristic and OSRM engine recompute the shortest road path and update the Leaflet map polyline.
- **Duty Status Toggle:** Initiated by the Driver marking shift state; updates the active driver roster and availability metrics on the Admin dashboard.
- **Complaint Resolution:** Initiated by the Driver uploading proof-of-cleanup photo; validates the image, transitions ticket status to 'Completed', logs the immutable resolution timestamp, and updates both Citizen Tracker and Admin Console.

## 4.4 Class Diagram
The Class Diagram captures the static structural blueprint of the system, defining domain model classes, structural attributes, operations, visibility constraints, and relationships.

[INSERT FIGURE HERE: Figure 4.2]
*Figure 4.2: UrbanClean UML Class Diagram*

### Explanation of Class Diagram:
Figure 4.2 details the object-oriented schema of the platform:
- **Base Class `User`:** Encapsulates shared attributes (`userId`, `name`, `email`, `passwordHash`, `role`, `city`, `createdAt`) and common operations (`login()`, `logout()`, `updateProfile()`).
- **Inheritance Hierarchy:** Three specialized subclasses extend `User`:
  - `Citizen`: Extends `User` with `phone` and `complaints` list, providing `submitReport()`, `trackStatus()`, and `viewHistory()`.
  - `Driver`: Extends `User` with `vehicleId`, `dutyStatus`, `assignedStops`, and `efficiency`, providing `toggleDuty()`, `pinStop()`, `generateRoute()`, `lockShift()`, and `uploadProof()`.
  - `Admin`: Extends `User` with `municipality` and `adminLevel`, providing `viewAnalytics()`, `assignDriver()`, `manageRoster()`, and `exportReportCSV()`.
- **Domain Entities & Associations:**
  - `Complaint`: Holds ticket details (`complaintId`, `latitude`, `longitude`, `photoUrl`, `wasteCategory`, `status`, `createdAt`), associated to `Citizen` (1-to-Many submission) and `Driver` (1-to-Many resolution).
  - `Zone`: Represents municipal administrative boundaries (`zoneId`, `zoneName`), partitioning complaints and dispatch workloads.
  - `Route`: Owned by a `Driver` (1-to-1 daily link), aggregating ordered waypoints (`routeId`, `totalDistance`, `computeTSP()`, `addWaypoint()`).

## 4.5 Object Diagram (Runtime Snapshot)
The Object Diagram illustrates an empirical runtime state instance of the UrbanClean object model, capturing concrete attribute values and active instance links during an operational shift.

[INSERT FIGURE HERE: Figure 4.3]
*Figure 4.3: UrbanClean Object Diagram — Runtime Snapshot*

### Explanation of Object Diagram:
Figure 4.3 documents an active system snapshot:
- `citizen1: Citizen` (`userId = 101`, `name = "Ayush Toraskar"`, `email = "ayush@mail.com"`, `role = "Citizen"`) has submitted `complaint1: Complaint`.
- `complaint1: Complaint` (`complaintId = 5001`, `latitude = 21.1458`, `longitude = 79.0882`, `wasteCategory = "Organic"`, `status = "Assigned"`, `photoUrl = "img_5001.jpg"`) belongs to `zone1: Zone` (`zoneId = 3`, `zoneName = "Ward 12 - Dharampeth"`).
- `driver1: Driver` (`userId = 205`, `name = "Ramesh Kale"`, `vehicleId = "MH31AB1234"`, `dutyStatus = "On Duty"`) resolves `complaint1` and follows `route1: Route`.
- `route1: Route` (`routeId = 77`, `totalDistance = 4.8 km`, `waypoints = [complaint1, complaint2]`) includes `complaint1` within its sequenced stops.

## 4.6 Use Case Diagram
The Use Case Diagram delineates the system functional boundary, modeling the four external actors and their authorized behavioral interactions with system use cases.

[INSERT FIGURE HERE: Figure 4.4]
*Figure 4.4: UrbanClean Use Case Diagram — Actors, Use Cases, and System Boundary*

### Explanation of Use Case Diagram:
Figure 4.4 illustrates functional interactions:
- **Citizen:** Executes `Register / Login`, `Report Waste Complaint` (which mandatorily `<<includes>>` `Geotag Location` and `Upload Photo`), `Track Complaint Status`, and `View Public Guest Dashboard`.
- **Driver:** Executes `View Assigned Route`, `Navigate Optimized Route`, and `Update Collection Status` (which mandatorily `<<includes>>` `Upload Photo`).
- **Admin:** Executes `View Analytics Dashboard`, `Monitor Driver Roster`, `Manage Complaints / Assign Driver`, and `View Zone Reports`.

## 4.7 Sequence Diagram
The Sequence Diagram documents the chronological sequence of message transmissions across architectural tiers throughout the end-to-end complaint lifecycle.

[INSERT FIGURE HERE: Figure 4.5]
*Figure 4.5: UML Sequence Diagram — End-to-End Complaint Lifecycle*

### Explanation of Sequence Diagram:
Figure 4.5 traces the complete operational workflow across six lifelines (`Citizen`, `Citizen Frontend`, `Backend REST API`, `PostgreSQL/SQLite`, `OSRM Routing Engine`, `Admin Console`, `Driver App`):
1. Citizen drops a pin, attaches a photo, and submits to `POST /complaints`.
2. Backend REST API validates payload, stores image to disk, and executes SQL insert (`status = 'Pending'`).
3. Backend notifies Admin Console of the new complaint.
4. Admin dispatches the complaint to a driver matching the ward.
5. Backend requests route optimization from OSRM Routing Engine and returns the optimized TSP road polyline.
6. Driver app receives updated route and task; driver navigates to site, cleans waste, and uploads proof photo.
7. Backend updates complaint status to 'Completed', refreshes zone analytics, and updates citizen ticket status to Green.

## 4.8 Component Diagram
The Component Diagram illustrates the high-level structural decomposition of UrbanClean into independent, modular software components and service contracts.

[INSERT FIGURE HERE: Figure 4.6]
*Figure 4.6: UrbanClean Component Diagram*

### Explanation of Component Diagram:
Figure 4.6 displays modular structural components:
- **Presentation Components:** `Citizen Portal`, `Driver Portal`, and `Admin Portal` implemented using HTML5, CSS3, JavaScript, and Leaflet.js, streaming map tiles from external `OpenStreetMap Tile API`.
- **API Gateway Component:** Node.js + Express.js handling authentication routing, request validation, and payload distribution.
- **Service Components:**
  - `Authentication Service`: Salted hash verification and session management.
  - `Complaint Service`: Ticket lifecycle management and photo disk storage.
  - `Dispatch & TSP Service`: 1.0 km Haversine spatial filter and Greedy Nearest-Neighbor TSP solver.
  - `Admin Analytics Service`: Zone aggregation, KPI counters, and CSV generation.
- **Infrastructure Services:** External `OSRM Engine` for real-road driving directions and `PostgreSQL+PostGIS / SQLite` database persistence.

## 4.9 Deployment Diagram
The Deployment Diagram models the physical network topography and runtime hardware nodes hosting the UrbanClean software tiers.

[INSERT FIGURE HERE: Figure 4.7]
*Figure 4.7: UrbanClean Deployment Diagram*

### Explanation of Deployment Diagram:
Figure 4.7 details hardware and network nodes:
- `Client Device`: Smartphone, Desktop, or Tablet running modern web browsers (Chrome, Edge, Safari) with HTML5 Geolocation API, communicating over HTTPS (REST/JSON) to Port 3000.
- `Application Server (Ubuntu 20.04 LTS+ / Windows 11)`: Hosts the Node.js runtime environment and Express.js REST API server managing Auth, Complaint, Dispatch, and Analytics services.
- `Database Server`: Hosts relational storage (PostgreSQL v16.x / SQLite3) connected via TCP Port 5432 / local native connector.
- `Routing Server`: Dedicated OSRM Engine processing road network routing graphs.
- `External Service`: OpenStreetMap tile servers providing basemap cartography over HTTPS.

## 4.10 Activity Diagram
The Activity Diagram models the procedural control flow, branching logic, and decision gates governing complaint reporting, proximity evaluation, route optimization, and proof verification.

[INSERT FIGURE HERE: Figure 4.8]
*Figure 4.8: UrbanClean Activity Diagram — Complaint Processing, Routing, and Resolution Flow*

### Explanation of Activity Diagram:
Figure 4.8 models algorithmic decision paths:
1. Citizen opens reporting interface, captures coordinates, and selects waste photo.
2. Decision Gate: Validates geotag and photo presence; if invalid, displays error toast and prompts resubmission.
3. If valid, ticket is created (`status = 'Pending'`).
4. Decision Gate: Evaluates Haversine distance ($d \\le 1.0\\text{ km}$); nearby complaints enter candidate queue; distant complaints remain in unassigned pool.
5. Driver executes Greedy TSP and OSRM calculates road polyline; driver locks shift route.
6. Driver clears waste site and uploads after-cleanup photograph.
7. Decision Gate: Verifies proof photo acceptance; if valid, marks ticket 'Completed' and logs resolution timestamp.
"""
