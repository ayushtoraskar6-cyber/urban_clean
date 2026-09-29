# -*- coding: utf-8 -*-
"""
Chapter 3 (SDLC Planning) & Chapter 4 (System Modeling Using UML)
Restructured strictly to the required syllabus topics.
"""

CH3_CH4_TEXT = """# CHAPTER 3 — SOFTWARE DEVELOPMENT LIFE CYCLE (SDLC) PLANNING

## 3.1 Selection of SDLC Model
For the engineering of UrbanClean, an **Iterative Agile Development Model** was selected. While the broader academic milestones adhered to sequential deliverables (Proposal, SRS, Architecture, Working Code, Final Submission), the actual technical development was organized into rapid, two-week iterative sprints.

The Iterative Agile methodology was chosen due to several critical project dynamics:
1. **Algorithm Refinement & Empirical Tuning:** The route optimization pipeline required continuous empirical tuning of the spherical Haversine formula and Greedy TSP sequencing against realistic Mumbai road networks before final locking.
2. **Decoupled Architectural Sprints:** Allowed the team to build and stabilize the backend RESTful API and JSON persistence store independently while frontend Glassmorphism UI components were being refined.
3. **Continuous Stakeholder Feedback:** Regular weekly review meetings with faculty guide Prof. Aarti Gawai enabled prompt requirement adjustments without costly retrofits.
4. **Early Risk Mitigation:** High-risk integrations—such as public OSRM API response handling and W3C geolocation permissions—were implemented and stress-tested in early iterations.

## 3.2 Work Breakdown Structure (WBS)
The project activities were decomposed hierarchically into defined work packages and deliverables:

### Table 3.1: Work Breakdown Structure (WBS)
| WBS Code | Phase / Task Name | Work Package Details | Primary Deliverable |
|---|---|---|---|
| 1.0 | Project Initiation | Problem identification, feasibility study, literature review | Approved Synopsis & Project Proposal |
| 2.0 | Requirements Analysis | Functional (FR-01 to FR-28) and Non-Functional (NFR-01 to NFR-19) drafting | Software Requirements Specification (SRS) |
| 3.0 | System Modeling & Design | UML design suite (7 core diagrams) and relational schema design | Architecture Design Document (ADD) |
| 4.0 | Frontend Engineering | Glassmorphism CSS3 styling, Leaflet map canvas, DOM controllers (script.js) | Functional Single-Page Application Views |
| 5.0 | Backend & Algorithm Dev | REST API gateway (server.js), Multer photo uploads, TSP + OSRM routing | Node.js Express REST API Server |
| 6.0 | Data Persistence & Sync | Document store (db.json) and automated SQLite mirror (sync_sqlite.py) | Dual Data Storage Architecture |
| 7.0 | Testing & Verification | Test case design, execution of TC-01 to TC-52, performance benchmarking | STQA Test Case Execution Log |
| 8.0 | Final Delivery | Report generation, PowerPoint viva deck, code repository freeze | Final Project Report & Demonstration |

## 3.3 Project Timeline / Gantt Chart
The project execution timeline strictly adhered to the academic schedule established by the Department of Computer Science (Sem-V 2026-27):

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

[INSERT FIGURE HERE: Figure 3.1]
*Figure 3.1: Project Gantt Chart (Sem-V 2026-27 Milestones & Timeline)*

The Gantt chart visually illustrates the linear milestone transitions across the project duration, ensuring timely completion of all deliverables leading to the final university demonstration.

## 3.4 Resource Planning
Resource allocation was structured across three essential dimensions to ensure uninterrupted execution:
- **Human Resources:** Ayush Santosh Toraskar (Sole Full-Stack Developer & Researcher); Prof. Aarti Gawai (Project Guide & Technical Mentor).
- **Software Resources:** Visual Studio Code IDE, Git/GitHub Version Control, Node.js runtime, DB Browser for SQLite, Postman REST Client.
- **Hardware Resources:** Laptop (Intel Core i5, 16 GB RAM, 512 GB NVMe SSD, Windows 11 64-bit); Android smartphone for mobile responsive testing and live GPS telemetry.

Key operational risks were actively managed throughout resource deployment:
- *External API Latency:* Decoupled TSP waypoint ordering from road geometry; system computes Euclidean/Haversine fallback if OSRM is unreachable.
- *Browser Geolocation Permissions:* Implemented interactive map click-to-pin fallback, allowing manual pin dropping on default city coordinates.
- *Persistence Fault-Tolerance:* Automated background SQLite mirroring (`sync_sqlite.py`) executes synchronously on every file-backed JSON write to prevent in-memory state loss.
- *File Upload Boundaries:* Multer middleware enforces strict 5 MB file size limit and whitelists image MIME types (`image/jpeg`, `image/png`).

---

# CHAPTER 4 — SYSTEM MODELING USING UML

## 4.1 Event Table
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

## 4.2 Use Case Diagram
The Use Case Diagram delineates the system functional boundary, modeling the external actors and their authorized behavioral interactions with system use cases.

[INSERT FIGURE HERE: Figure 4.2]
*Figure 4.2: UrbanClean Use Case Diagram — Actors, Use Cases, and System Boundary*

### Explanation of Use Case Diagram:
Figure 4.2 illustrates functional interactions across the four primary system actors:
- **Citizen:** Executes `Register / Login`, `Report Waste Complaint` (which mandatorily `<<includes>>` `Geotag Location` and `Upload Photo`), `Track Complaint Status`, and `View Public Guest Dashboard`.
- **Driver:** Executes `View Assigned Route`, `Navigate Optimized Route`, and `Update Collection Status` (which mandatorily `<<includes>>` `Upload Photo`).
- **Admin:** Executes `View Analytics Dashboard`, `Monitor Driver Roster`, `Manage Complaints / Assign Driver`, and `View Zone Reports`.
- **Guest:** Executes `View Cleanliness Statistics` and `Browse Public Reports`.

## 4.3 Class Diagram
The Class Diagram captures the static structural blueprint of the system, defining domain model classes, structural attributes, operations, visibility constraints, and relationships.

[INSERT FIGURE HERE: Figure 4.3]
*Figure 4.3: UrbanClean UML Class Diagram*

### Explanation of Class Diagram:
Figure 4.3 details the object-oriented schema of the platform:
- **Base Class `User`:** Encapsulates shared attributes (`userId`, `name`, `email`, `passwordHash`, `role`, `city`, `createdAt`) and common operations (`login()`, `logout()`, `updateProfile()`).
- **Inheritance Hierarchy:** Three specialized subclasses extend `User`:
  - `Citizen`: Extends `User` with `phone` and `complaints` list, providing `submitReport()`, `trackStatus()`, and `viewHistory()`.
  - `Driver`: Extends `User` with `vehicleId`, `dutyStatus`, `assignedStops`, and `efficiency`, providing `toggleDuty()`, `pinStop()`, `generateRoute()`, `lockShift()`, and `uploadProof()`.
  - `Admin`: Extends `User` with `municipality` and `adminLevel`, providing `viewAnalytics()`, `assignDriver()`, `manageRoster()`, and `exportReportCSV()`.
- **Domain Entities & Associations:**
  - `Complaint`: Holds ticket details (`complaintId`, `latitude`, `longitude`, `photoUrl`, `wasteCategory`, `status`, `createdAt`), associated to `Citizen` (1-to-Many submission) and `Driver` (1-to-Many resolution).
  - `Zone`: Represents municipal administrative boundaries (`zoneId`, `zoneName`), partitioning complaints and dispatch workloads.
  - `Route`: Owned by a `Driver` (1-to-1 daily link), aggregating ordered waypoints (`routeId`, `totalDistance`, `computeTSP()`, `addWaypoint()`).

## 4.4 Sequence Diagram
The Sequence Diagram documents the chronological sequence of message transmissions across architectural tiers throughout the end-to-end complaint lifecycle.

[INSERT FIGURE HERE: Figure 4.4]
*Figure 4.4: UML Sequence Diagram — End-to-End Complaint Lifecycle*

### Explanation of Sequence Diagram:
Figure 4.4 traces the complete operational workflow across six lifelines (`Citizen`, `Citizen Frontend`, `Backend REST API`, `PostgreSQL/SQLite`, `OSRM Routing Engine`, `Admin Console`, `Driver App`):
1. Citizen drops a pin, attaches a photo, and submits to `POST /complaints`.
2. Backend REST API validates payload, stores image to disk, and executes SQL insert (`status = 'Pending'`).
3. Backend notifies Admin Console of the new complaint.
4. Admin dispatches the complaint to a driver matching the ward.
5. Backend requests route optimization from OSRM Routing Engine and returns the optimized TSP road polyline.
6. Driver app receives updated route and task; driver navigates to site, cleans waste, and uploads proof photo.
7. Backend updates complaint status to 'Completed', refreshes zone analytics, and updates citizen ticket status to Green.

## 4.5 Activity Diagram
The Activity Diagram models the procedural control flow, branching logic, and decision gates governing complaint reporting, proximity evaluation, route optimization, and proof verification.

[INSERT FIGURE HERE: Figure 4.5]
*Figure 4.5: UrbanClean Activity Diagram — Complaint Processing, Routing, and Resolution Flow*

### Explanation of Activity Diagram:
Figure 4.5 models algorithmic decision paths:
1. Citizen opens reporting interface, captures coordinates, and selects waste photo.
2. Decision Gate: Validates geotag and photo presence; if invalid, displays error toast and prompts resubmission.
3. If valid, ticket is created (`status = 'Pending'`).
4. Decision Gate: Evaluates Haversine distance ($d \\le 1.0\\text{ km}$); nearby complaints enter candidate queue; distant complaints remain in unassigned pool.
5. Driver executes Greedy TSP and OSRM calculates road polyline; driver locks shift route.
6. Driver clears waste site and uploads after-cleanup photograph.
7. Decision Gate: Verifies proof photo acceptance; if valid, marks ticket 'Completed' and logs resolution timestamp.

## 4.6 ER Diagram
The Entity-Relationship (ER) Diagram models the conceptual and logical data architecture of UrbanClean, illustrating the primary persistent entities, their structural attributes, unique primary keys, referential foreign key constraints, and relational cardinalities. While the Class Diagram defines the object-oriented abstractions and behavioral methods of the runtime application tier, the ER Diagram establishes the concrete data modeling foundation governing the SQLite relational database and the mirrored JSON document store.

[INSERT FIGURE HERE: Figure 4.6]
*Figure 4.6: Entity-Relationship Diagram of UrbanClean*

### ER Diagram Description
Figure 4.6 represents the relational data model underpinning the UrbanClean smart waste management ecosystem. The data model is structured around five core persistent entities: `ACCOUNT`, `COMPLAINT`, `DRIVER`, `DRIVER_ROUTE`, and `NOTIFICATION`. Each entity is normalized to Third Normal Form (3NF) to prevent insertion, update, and deletion anomalies while maintaining strict referential integrity across the application's multi-role workflows.

The foundational identity store is captured by the `ACCOUNT` entity (`accounts` table), uniquely identified by primary key `id` (e.g., `CIT-702`, `DRV-101`, `ADM-999`). It maintains core user credentials and jurisdictional attributes including `name`, `email` (enforcing a unique constraint), `role` (partitioned across `citizen`, `driver`, and `admin`), administrative geographic tags (`state`, `district`, `city`), and `password_hash` (storing salted cryptographic digests). The `DRIVER` entity (`drivers` table) shares a 1:1 specialization relationship with `ACCOUNT` for users designated with the `driver` role, storing fleet-specific telemetry such as `status` (`Active` or `Off-Duty`), assigned vehicle description (`vehicle`), algorithmic route fuel efficiency (`efficiency`), cumulative travel distance (`distance`), and active assignment queues (`assignedComplaints`).

The core transactional workload of the platform is centered on the `COMPLAINT` entity (`complaints` table), identified by primary key `id` (e.g., `COMP-001`). It establishes a 1:N relationship with `ACCOUNT` through foreign key `reportedBy` (or `userId`), linking each filed ticket to the submitting citizen. A second 1:N operational relationship connects `DRIVER` to `COMPLAINT` via foreign key `assignedDriverId`, designating the field operator responsible for physical remediation. The entity captures essential geospatial and verification attributes including WGS84 coordinates (`lat`, `lng`), `area`, `city`, categorization (`category`), descriptive notes (`title`, `description`), ticket lifecycle status (`status`: `Pending`, `Assigned`, `In Progress`, `Completed`), and visual audit trails stored as relative disk paths (`photo_before` for citizen evidence and `photo_after` for driver proof-of-cleanup).

Driver navigation and route scheduling are modeled by the `DRIVER_ROUTE` entity (`driver_routes` table), which holds an auto-incrementing integer primary key `id` and maintains a 1:N relationship with `DRIVER` via foreign key `driverId`. This entity stores sequential waypoints (`pointIndex`, `label`, `lat`, `lng`, `savedAt`) generated during Greedy TSP optimization and locked daily shifts. Finally, the `NOTIFICATION` entity (`notifications` table), identified by primary key `id`, records system-wide operational alerts, task assignments, and citizen resolution broadcasts (`type`, `message`, `timeStr`). Together, these entities and relationships provide comprehensive data persistence supporting real-time civic reporting, automated proximity filtering, route navigation, and municipal governance.

## 4.7 Deployment Diagram
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
"""
