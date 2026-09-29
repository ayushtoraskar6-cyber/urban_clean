# -*- coding: utf-8 -*-
"""
Preliminary Pages for UrbanClean Report
"""

PRELIM_TEXT = """
# A PROJECT REPORT
## On
# UrbanClean: Geospatial Smart City Waste Management & Route Optimization System

Submitted by
**Mr. AYUSH SANTOSH TORASKAR**  
*(Roll No. CS-9147 | Class: TY B.Sc. CS / II)*  

in partial fulfillment for the award of the degree of  
**BACHELOR OF SCIENCE IN COMPUTER SCIENCE**  

under the guidance of  
**PROF. AARTI GAWAI**  
*Department of Computer Science*  

**Modern Education Society’s**  
**The D. G. Ruparel College of Arts, Science & Commerce**  
*Senapati Bapat Marg, Opp. Matunga Road Station (W.R.), Mahim, Mumbai – 400 016*  
*(Academic Year: 2026 – 2027)*  

---

## CERTIFICATE

**Modern Education Society’s The D. G. Ruparel College of Arts, Science & Commerce**  
*Senapati Bapat Marg, Opp. Matunga Road Station (W.R.), Mahim, Mumbai – 400 016*  
**Department of Computer Science**  

This is to certify that **Mr. TORASKAR AYUSH SANTOSH**, Seat No.: **________________**, of **T.Y.B.Sc. (Sem V)** class has satisfactorily completed the project report entitled:  
**“UrbanClean: Geospatial Smart City Waste Management & Route Optimization System”**  
to be submitted in partial fulfillment for the award of **Bachelor of Science in Computer Science** during the academic year **2026 – 2027**.

<br>

**Date of Submission:** ____________________  

<br>

_________________________ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; _________________________  
**Project Guide** &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **Head / Incharge**  
*(Prof. Aarti Gawai)* &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; *Department of Computer Science*  

<br><br>

_________________________ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; _________________________  
**College Seal** &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **Signature of Examiner**  

---

## DECLARATION

I, **AYUSH SANTOSH TORASKAR**, student of **TY B.Sc. Computer Science (Class II, Roll No. CS-9147)** at **Modern Education Society’s The D. G. Ruparel College of Arts, Science & Commerce**, hereby declare that the project report entitled:  
**“URBANCLEAN: GEOSPATIAL SMART CITY WASTE MANAGEMENT & ROUTE OPTIMIZATION SYSTEM”**  
is submitted by me in partial fulfillment of the requirements for the degree of **Bachelor of Science in Computer Science** to the University of Mumbai for the academic year **2026–2027**.

I declare that this work is original, has been formulated by me based on authentic research, architectural design, software requirements specification, and algorithmic modeling under the supervision of my faculty project guide, **Prof. Aarti Gawai**. It has not formed the basis for the award of any previous degree, diploma, associate-ship, or fellowship of any other university or examining body.

All sources, open-source libraries, routing services (OSRM), geospatial APIs (Leaflet.js, OpenStreetMap), and reference specifications utilized during this study have been duly acknowledged.

<br>

**Date:** September 2026  
**Place:** Mumbai, Maharashtra  
<br>
_________________________________  
**AYUSH SANTOSH TORASKAR**  
Roll No.: CS-9147 | Class: TY B.Sc. CS / II  
Modern Education Society’s The D. G. Ruparel College  

---

## ACKNOWLEDGEMENT

I express my deepest gratitude and sincere appreciation to my respected Project Guide, **Prof. Aarti Gawai**, whose insightful suggestions, constructive criticism, and consistent technical mentorship steered this project from conceptual formulation to successful architectural design, implementation, and documentation.

I extend my profound thanks to the **Head of the Department of Computer Science** and the respected faculty members of the Department of Computer Science at **Modern Education Society’s The D. G. Ruparel College of Arts, Science & Commerce**, for providing access to computing facilities, academic software environments, and administrative support essential for completing this project.

I am immensely thankful to the **Principal** of the college for providing an encouraging academic environment and infrastructure.

Lastly, I owe deep gratitude to my family and peers for their continuous moral encouragement, patience, and assistance throughout the duration of this B.Sc. Computer Science project.

<br>
**AYUSH SANTOSH TORASKAR**  
(Roll No. CS-9147)  

---

## ABSTRACT

Municipal Solid Waste Management (MSWM) across rapidly expanding urban centers faces profound operational bottlenecks: static collection truck schedules independent of real-world waste accumulation, vague text-based address forms that obscure dump locations, complete absence of tracking transparency for citizens, unoptimized collection routes causing severe fuel expenditure and carbon emissions, and uncoordinated administrative oversight.

**UrbanClean** is an end-to-end, web-based geospatial smart city waste management and route optimization platform engineered to bridge the operational gap between civic waste reporting, driver fleet dispatching, and municipal governance. The system integrates four interconnected user roles:
1. **Guests**, who can inspect public city cleanliness metrics, recent complaints, and pickup schedules without authentication.
2. **Citizens**, who report waste accumulation incidents in real time by capturing exact GPS latitude and longitude coordinates through the W3C Geolocation API or an interactive Leaflet map canvas, selecting waste categories, and uploading mandatory binary photograph evidence.
3. **Collection Drivers**, who manage assigned complaint queues, configure custom collection waypoints (up to 40 pins), filter nearby complaints using a **1.0 km Haversine geodesic spatial filter**, lock active shifts via a **Daily Route-Lock Engine**, and follow fuel-optimized navigation sequences computed using an internal **Greedy Nearest-Neighbor Traveling Salesperson Problem (TSP)** heuristic paired with the **Open Source Routing Machine (OSRM)** road driving API.
4. **Municipal Administrators**, who exercise centralized operational oversight via a real-time command dashboard auto-locked to their assigned municipality (e.g., Kalyan, Bandra), monitor ward-level complaint aggregates, track driver duty rosters, reassign tasks, and export 30-day compliance reports in CSV format.

The platform establishes an automated complaint lifecycle (**Pending → Assigned → In Progress → Completed**) verified by mandatory proof-of-resolution photographs uploaded by drivers upon site clearance. The software architecture encompasses a modular Express.js / Node.js backend (with an active JSON document store `db.json` mirrored in real time to SQLite `urban_clean.db` via `sync_sqlite.py`), Leaflet.js mapping, OpenStreetMap raster tiles, and client session state management. Evaluation confirms sub-minute complaint logging, strict data privacy, zero IoT hardware capital expense, and an estimated **22% to 32% reduction in fleet driving distance**, presenting an efficient, scalable smart city framework.

---

## TABLE OF CONTENTS / INDEX

- **Preliminary Pages**
  - Title Page
  - Certificate of Authenticity
  - Candidate Declaration
  - Acknowledgement
  - Abstract
  - Table of Contents / Index
  - List of Figures
  - List of Tables
  - List of Abbreviations
- **Chapter 1 — Problem Identification & Feasibility Study**
  - 1.1 Identification of a Real-World Problem
  - 1.2 Problem Context & Urban Realities
  - 1.3 Problem Statement
  - 1.4 Scope of the Problem
  - 1.5 Stakeholder Identification & Expectations
  - 1.6 Feasibility Analysis (Technical, Economic, Operational, Schedule)
  - 1.7 Project Constraints & Assumptions
  - 1.8 Expected Project Outcomes
- **Chapter 2 — Requirement Engineering**
  - 2.1 Introduction & Requirement Gathering
  - 2.2 Stakeholder Requirements
  - 2.3 Functional Requirements (FR-01 to FR-28)
  - 2.4 Non-Functional Requirements (NFR-01 to NFR-19)
  - 2.5 Use-Case Analysis Across Actors
  - 2.6 Requirement Prioritization (MoSCoW Framework)
  - 2.7 Project Constraints & Assumptions
  - 2.8 Hardware & Software Requirements
- **Chapter 3 — Software Development Life Cycle (SDLC) Planning**
  - 3.1 Selected SDLC Model (Iterative Agile)
  - 3.2 Reasons for Selecting the Iterative Agile Model
  - 3.3 SDLC Phases & Milestones
  - 3.4 Work Breakdown Structure (WBS)
  - 3.5 Project Activities Deconstruction
  - 3.6 Project Timeline & Milestone Schedule
  - 3.7 Resource Planning (Human, Software, Hardware)
  - 3.8 Risk Identification, Assessment, and Mitigation
  - 3.9 Project Gantt Chart (Figure 3.1)
- **Chapter 4 — System Modeling Using UML**
  - 4.1 UML Overview & Visual Modeling Rationale
  - 4.2 System Actors & Privilege Boundaries
  - 4.3 UML Event Table (Figure 4.1)
  - 4.4 Class Diagram (Figure 4.2)
  - 4.5 Object Diagram — Runtime Snapshot (Figure 4.3)
  - 4.6 Use Case Diagram (Figure 4.4)
  - 4.7 Sequence Diagram — Complaint Lifecycle (Figure 4.5)
  - 4.8 Component Diagram (Figure 4.6)
  - 4.9 Deployment Diagram (Figure 4.7)
  - 4.10 Activity Diagram — Operational Logic (Figure 4.8)
- **Chapter 5 — System Architecture Design**
  - 5.1 Layered System Architecture Overview (Figure 5.1)
  - 5.2 Frontend Architecture & Client State Model
  - 5.3 Backend Architecture & RESTful Pipeline
  - 5.4 Database Architecture & Dual-Persistence Strategy
  - 5.5 Database Schema & Data Dictionaries (Tables 5.1 to 5.5)
  - 5.6 Database Schema Inspection via DB Browser for SQLite (Figures 5.2 to 5.4)
  - 5.7 API Structure & Contract Specifications
  - 5.8 Authentication, Session Security & RBAC Enforcement
  - 5.9 Security Considerations & Data Isolation
  - 5.10 Data Flow Architecture (Context Diagram & Level 1 DFD)
- **Chapter 6 — Application Development**
  - 6.1 Development Environment & Tooling
  - 6.2 Technology Stack Implementation Details
  - 6.3 Frontend Implementation (Modular SPA Views)
  - 6.4 Backend Implementation (Express REST Handlers)
  - 6.5 Database Integration & Real-Time SQLite Synchronization
  - 6.6 Authentication & Validation Implementation
  - 6.7 Complaint Management & Geospatial Algorithms (Haversine & TSP)
  - 6.8 Error Handling Architecture (Multer Middleware & OSRM Fallback)
  - 6.9 Screen Walkthrough & Implemented Features (Figures 6.1 to 6.7)
- **Chapter 7 — Integration & System Testing**
  - 7.1 Testing Objectives & Quality Goals
  - 7.2 Comprehensive Testing Strategy
  - 7.3 Unit Testing & Mathematical Verification (Figure 7.1)
  - 7.4 Black-Box & Form Validation Testing
  - 7.5 Integration Testing & API Verification (Figures 7.2 & 7.3)
  - 7.6 Master Software Testing Test Case Log (Table 7.1: TC-01 to TC-52)
  - 7.7 Defect & Bug Management (BUG-01 Fix & Minor Defects)
  - 7.8 Test Execution Summary & Verification Metrics (Table 7.2)
- **Chapter 8 — Deployment**
  - 8.1 Local Hosting & Runtime Deployment
  - 8.2 APK Build Analysis (Web-First Architectural Rationale)
  - 8.3 Server Configuration & Network Topography
  - 8.4 Version Control Using GitHub (Repository Structure & Branch Architecture)
  - 8.5 GitHub Working Tree & Commit Provenance Inspection (Figures 8.1 to 8.4)
- **Chapter 9 — Performance & Security Testing**
  - 9.1 Basic Load Testing & Concurrency Analysis (Figures 9.1 to 9.3)
  - 9.2 REST API Response Time & Latency Benchmarking (Figure 9.4)
  - 9.3 Input Validation & Boundary Checks (Figure 9.5)
  - 9.4 Security Validation & Access Control Verification (Figure 9.6)
  - 9.5 Identified Vulnerabilities & Implemented Resolutions (Figures 9.7 & 9.8)
  - 9.6 Performance & Security Verification Summary
- **Chapter 10 — Final Documentation**
  - 10.1 Project Implementation Results
  - 10.2 Empirical Observations
  - 10.3 Discussion of Algorithmic & Operational Results (Table 10.1)
  - 10.4 System Limitations & Edge Constraints
  - 10.5 Future Research & Development Scope
  - 10.6 Conclusion & Achievement of Objectives (Table 10.2)
- **References**
- **Appendices**
  - Appendix A: Important Source Code
  - Appendix B: Additional Screenshots
  - Appendix C: Master Test Cases List
  - Appendix D: Database Structure DDL
  - Appendix E: User Manual & Operations Guide
- **Syllabus Requirements Compliance Checklist**

---

## LIST OF FIGURES

- Figure 3.1: Project Gantt Chart (Sem-V 2026-27 Milestones & Timeline)
- Figure 4.1: UML Event Table — System Triggers, Sources, and Responses
- Figure 4.2: UrbanClean UML Class Diagram
- Figure 4.3: UrbanClean Object Diagram — Runtime Snapshot
- Figure 4.4: UrbanClean Use Case Diagram — Actors, Use Cases, and System Boundary
- Figure 4.5: UML Sequence Diagram — End-to-End Complaint Lifecycle
- Figure 4.6: UrbanClean Component Diagram
- Figure 4.7: UrbanClean Deployment Diagram
- Figure 4.8: UrbanClean Activity Diagram — Complaint Processing, Routing, and Resolution Flow
- Figure 5.1: High-Level Layered System Architecture of UrbanClean
- Figure 5.2: DB Browser for SQLite — `accounts` & `complaints` Tables
- Figure 5.3: DB Browser for SQLite — `driver_routes` & `notifications` Tables
- Figure 5.4: DB Browser for SQLite — `drivers` Fleet Roster Table
- Figure 6.1: Public Landing Page, Multi-Role Login & Citizen Registration (`index.html` & `login.html`)
- Figure 6.2: Citizen Waste Reporting Interface & Interactive Map Pinning (`citizen.html`)
- Figure 6.3: GPS Geolocation Telemetry, Citizen Ticket Tracking & Driver Dashboard
- Figure 6.4: Driver Optimized Route Map (5 Stops) & Proof-of-Cleanup Upload (`driver.html`)
- Figure 6.5: Municipal Administrator Command Center, Active Drivers & Daily Complaints Modal (`admin.html`)
- Figure 6.6: City-Wide Waste Monitoring Map & Monthly Compliance Tracking Report with Excel Export
- Figure 6.7: Mobile Responsive Device View across Smartphone Viewport (`http://192.168.1.7:3000`)
- Figure 7.1: Unit Testing Suite Execution Output (`unit_tests.js` — S23)
- Figure 7.2: REST API & Component Integration Verification (`integration_tests.js` — S24)
- Figure 7.3: Dual Persistence (db.json <-> SQLite) Sync Verification (`verify_db_sync.py` — S25)
- Figure 8.1: GitHub Repository Remote & Branch Configuration (S44)
- Figure 8.2: GitHub Project Directory Structure (`git ls-tree` — S45)
- Figure 8.3: Source Code Tracking & Working Tree Commit Inspection (`git log -n 1 --stat` — S46)
- Figure 8.4: Git Commit History Timeline & Provenance Audit (`git log --graph --oneline` — S47)
- Figure 9.1: Autocannon Basic Load Testing Configuration (S37)
- Figure 9.2: Autocannon Live Concurrency Load Execution Progress (S38)
- Figure 9.3: Autocannon Concurrency Load Test Final Results (S39)
- Figure 9.4: REST API Response Time & Latency Benchmark (`benchmark_latency.js` — S36)
- Figure 9.5: Input Validation Failure — Duplicate Account & Password Constraints (S30)
- Figure 9.6: Cryptographic Session Authentication — `POST /api/login` (S32)
- Figure 9.7: Defect BUG-01: Raw 500 Stack Trace on Invalid File MIME Upload (S40)
- Figure 9.8: Defect BUG-01 Retest: Graceful HTTP 400 Bad Request JSON Response (S41)

---

## LIST OF TABLES

- Table 1.1: Stakeholder Identification and System Expectations
- Table 2.1: Functional Requirements Specification (FR-01 to FR-28)
- Table 2.2: Non-Functional Requirements Specification (NFR-01 to NFR-19)
- Table 2.3: Hardware Requirements Specification
- Table 2.4: Software Technology Stack Specifications
- Table 3.1: Work Breakdown Structure (WBS)
- Table 3.2: Project Milestone Schedule (Project Gantt Chart Sem-V 2026-27)
- Table 3.3: Risk Identification, Assessment, and Mitigation Matrix
- Table 5.1: Data Dictionary — `accounts` Table
- Table 5.2: Data Dictionary — `complaints` Table
- Table 5.3: Data Dictionary — `driver_routes` Table
- Table 5.4: Data Dictionary — `drivers` Table
- Table 5.5: Data Dictionary — `notifications` Table
- Table 7.1: Master Software Testing Test Case Log (TC-01 through TC-52)
- Table 7.2: Test Cases Category Breakdown and Execution Metrics
- Table 10.1: Evaluated Operational Fuel Savings Across Municipal Fleets
- Table 10.2: Comparison of Project Objectives with Implementation Results

---

## LIST OF ABBREVIATIONS

- **API:** Application Programming Interface
- **B2G:** Business to Government
- **BVA:** Boundary Value Analysis
- **CORS:** Cross-Origin Resource Sharing
- **CRUD:** Create, Read, Update, Delete
- **CSV:** Comma-Separated Values
- **CSS:** Cascading Style Sheets
- **DBMS:** Database Management System
- **DFD:** Data Flow Diagram
- **DOM:** Document Object Model
- **EPSG:** European Petroleum Survey Group (Geodetic Parameter Dataset)
- **ER:** Entity-Relationship
- **FCM:** Firebase Cloud Messaging
- **GIS:** Geographic Information System
- **GPS:** Global Positioning System
- **HTML:** HyperText Markup Language
- **HTTP / HTTPS:** HyperText Transfer Protocol / Secure
- **IEEE:** Institute of Electrical and Electronics Engineers
- **IoT:** Internet of Things
- **JSON:** JavaScript Object Notation
- **KDMC:** Kalyan-Dombivli Municipal Corporation
- **KPI:** Key Performance Indicator
- **MCGM:** Municipal Corporation of Greater Mumbai
- **MIME:** Multipurpose Internet Mail Extensions
- **MSWM:** Municipal Solid Waste Management
- **NFR:** Non-Functional Requirement
- **OSM:** OpenStreetMap
- **OSRM:** Open Source Routing Machine
- **PBKDF2:** Password-Based Key Derivation Function 2
- **PII:** Personally Identifiable Information
- **RAM:** Random Access Memory
- **RBAC:** Role-Based Access Control
- **REST:** Representational State Transfer
- **SDLC:** Software Development Life Cycle
- **SHA:** Secure Hash Algorithm
- **SLA:** Service Level Agreement
- **SPA:** Single Page Application
- **SQL:** Structured Query Language
- **SRS:** Software Requirements Specification
- **SSD:** Solid State Drive
- **STQA:** Software Testing and Quality Assurance
- **TMC:** Thane Municipal Corporation
- **TSP:** Traveling Salesperson Problem
- **UI / UX:** User Interface / User Experience
- **ULB:** Urban Local Body
- **UML:** Unified Modeling Language
- **URI / URL:** Uniform Resource Identifier / Uniform Resource Locator
- **W3C:** World Wide Web Consortium
- **WBS:** Work Breakdown Structure
- **WGS84:** World Geodetic System 1984
- **XSS:** Cross-Site Scripting
"""
