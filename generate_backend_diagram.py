# -*- coding: utf-8 -*-
"""
Generate a professional, publication-ready academic diagram:
"Figure 5.2: UrbanClean Backend Structure and Data Flow"
Saved to: screenshots/report_assets/backend_structure_dataflow.png
"""

import os
from PIL import Image, ImageDraw, ImageFont

WIDTH = 2000
HEIGHT = 1350

img = Image.new("RGB", (WIDTH, HEIGHT), "#FFFFFF")
draw = ImageDraw.Draw(img)

# Fonts
font_title = ImageFont.truetype("C:/Windows/Fonts/calibri.ttf", 32)
font_subtitle = ImageFont.truetype("C:/Windows/Fonts/calibri.ttf", 20)
font_sec_hdr = ImageFont.truetype("C:/Windows/Fonts/calibri.ttf", 22)
font_box_title = ImageFont.truetype("C:/Windows/Fonts/calibri.ttf", 18)
font_box_sub = ImageFont.truetype("C:/Windows/Fonts/calibri.ttf", 15)
font_mono = ImageFont.truetype("C:/Windows/Fonts/consola.ttf", 16)
font_mono_small = ImageFont.truetype("C:/Windows/Fonts/consola.ttf", 14)
font_flow_title = ImageFont.truetype("C:/Windows/Fonts/calibri.ttf", 17)
font_flow_text = ImageFont.truetype("C:/Windows/Fonts/calibri.ttf", 14)

# ─────────────────────────────────────────────────────────────────────────────
# 1. TOP HEADER BANNER
# ─────────────────────────────────────────────────────────────────────────────
draw.rectangle([(20, 20), (WIDTH - 20, 100)], fill="#F0F4F8", outline="#1F4E79", width=2)
draw.text((40, 30), "UrbanClean™ — Backend Architecture, Directory Structure & Data Flow", fill="#113F67", font=font_title)
draw.text((42, 68), "System Architecture Design Specification | Node.js Express REST API, Dual-Persistence Engine & Modular Services", fill="#4A6572", font=font_subtitle)

# Outer decorative frame
draw.rectangle([(20, 115), (WIDTH - 20, HEIGHT - 20)], outline="#B0C4DE", width=2)

# Dividing vertical line between Left (Structure) and Right (Data Flow)
draw.line([(880, 115), (880, HEIGHT - 20)], fill="#B0C4DE", width=2)

# ─────────────────────────────────────────────────────────────────────────────
# 2. LEFT PANEL: BACKEND & PROJECT DIRECTORY STRUCTURE
# ─────────────────────────────────────────────────────────────────────────────
draw.rectangle([(35, 125), (865, 165)], fill="#E8EEF5", outline="#2E75B6", width=1)
draw.text((45, 133), "PART A: Physical Backend Directory & Component Structure", fill="#1F4E79", font=font_sec_hdr)

# Draw Root Folder Box
root_box = [(50, 180), (320, 225)]
draw.rectangle(root_box, fill="#1F4E79", outline="#113F67", width=2)
draw.text((65, 190), "📁 UrbanClean/ (Project Root)", fill="#FFFFFF", font=font_box_title)

# Tree connector lines
draw.line([(90, 225), (90, 1280)], fill="#7F8C8D", width=2)

def draw_tree_item(x, y, is_folder, name, desc, width=730, height=48, fill_col="#FFFFFF", border_col="#95A5A6", icon="📄"):
    # Horizontal branch line from main stem at x=90
    draw.line([(90, y + height // 2), (x, y + height // 2)], fill="#7F8C8D", width=2)
    
    # Item box
    box = [(x, y), (x + width, y + height)]
    draw.rectangle(box, fill=fill_col, outline=border_col, width=1)
    
    prefix = "📁 " if is_folder else f"{icon} "
    draw.text((x + 10, y + 6), f"{prefix}{name}", fill="#2C3E50", font=font_mono)
    draw.text((x + 12, y + 26), desc, fill="#555555", font=font_flow_text)

# Backend Root Sub-branch
backend_box = [(120, 245), (420, 290)]
draw.line([(90, 267), (120, 267)], fill="#7F8C8D", width=2)
draw.rectangle(backend_box, fill="#2E75B6", outline="#1F4E79", width=2)
draw.text((135, 255), "📁 backend/ (Application Server)", fill="#FFFFFF", font=font_box_title)

# Secondary stem for backend children
draw.line([(150, 290), (150, 830)], fill="#7F8C8D", width=2)

backend_files = [
    ("server.js", "Express REST API Gateway, Routing, Multer Upload, RBAC, TSP Route Engine", "#F9FBFD", "#2E75B6", "⚡"),
    ("db.json", "Active JSON Document Store (accounts, complaints, drivers, driverRoutes)", "#FEF9E7", "#D4AC0D", "🗄️"),
    ("sync_sqlite.py", "Background Real-Time SQLite Sync Daemon (triggered via child_process)", "#E8F8F5", "#16A085", "🔄"),
    ("urban_clean.db", "Relational SQLite Mirror Database (5 normalized ACID tables for audit/reporting)", "#EAF2F8", "#2980B9", "💾"),
    ("models.py / schemas.py", "FastAPI / SQLAlchemy ORM Schemas & DDL definitions", "#F4F6F6", "#7F8C8D", "📜"),
    ("database.py / seed.py", "SQLite session engine configuration and baseline demographic seed data", "#F4F6F6", "#7F8C8D", "⚙️"),
    ("uploads/", "Physical disk storage directory for uploaded complaints and resolution proof photos", "#FDEDEC", "#E74C3C", "📁"),
    ("package.json", "Node.js dependencies: express (v4.19), multer (v1.4), cors, crypto", "#F9EBEA", "#C0392B", "📦"),
]

curr_y = 305
for fname, fdesc, bg, border, icon in backend_files:
    is_f = fname.endswith("/")
    draw.line([(150, curr_y + 24), (180, curr_y + 24)], fill="#7F8C8D", width=2)
    draw_tree_item(180, curr_y, is_f, fname, fdesc, width=670, height=48, fill_col=bg, border_col=border, icon=icon)
    curr_y += 58

# Frontend Sub-branch
curr_y = 810
draw.line([(90, curr_y + 24), (120, curr_y + 24)], fill="#7F8C8D", width=2)
draw.rectangle([(120, curr_y), (420, curr_y + 45)], fill="#34495E", outline="#2C3E50", width=2)
draw.text((135, curr_y + 10), "📁 frontend/ (Client Presentation)", fill="#FFFFFF", font=font_box_title)

draw.line([(150, curr_y + 45), (150, 1140)], fill="#7F8C8D", width=2)

frontend_files = [
    ("index.html / login.html", "Public landing portal with live statistics & unified multi-role authentication", "#FDFEFE", "#BDC3C7", "🌐"),
    ("citizen.html / driver.html / admin.html", "Role-dedicated SPAs: Geotagged reporting, route optimization, command center", "#FDFEFE", "#BDC3C7", "🌐"),
    ("script.js", "Client State Manager, Leaflet GIS Engine, REST fetcher, TSP Greedy Router", "#FEFDE8", "#F1C40F", "📜"),
    ("styles.css", "Glassmorphic responsive UI design system with CSS custom properties", "#EBF5FB", "#3498DB", "🎨"),
]

curr_y += 55
for fname, fdesc, bg, border, icon in frontend_files:
    draw.line([(150, curr_y + 24), (180, curr_y + 24)], fill="#7F8C8D", width=2)
    draw_tree_item(180, curr_y, False, fname, fdesc, width=670, height=48, fill_col=bg, border_col=border, icon=icon)
    curr_y += 56

# Supporting Directories
supporting = [
    ("docs/", "Academic report PDFs, UML diagrams, complete testing documentation", "#EAFAF1", "#2ECC71", "📁"),
    ("test_suite/", "Automated unit, integration, latency benchmarks and DB sync test scripts", "#F5EEF8", "#9B59B6", "📁"),
]
curr_y = 1130
for fname, fdesc, bg, border, icon in supporting:
    draw.line([(90, curr_y + 24), (120, curr_y + 24)], fill="#7F8C8D", width=2)
    draw_tree_item(120, curr_y, True, fname, fdesc, width=730, height=48, fill_col=bg, border_col=border, icon=icon)
    curr_y += 56


# ─────────────────────────────────────────────────────────────────────────────
# 3. RIGHT PANEL: BACKEND DATA FLOW & PROCESSING PIPELINE
# ─────────────────────────────────────────────────────────────────────────────
draw.rectangle([(895, 125), (WIDTH - 35, 165)], fill="#E8EEF5", outline="#2E75B6", width=1)
draw.text((905, 133), "PART B: End-to-End Backend Data Flow & Processing Pipeline", fill="#1F4E79", font=font_sec_hdr)

def draw_arrow_down(x, y_start, y_end, label=""):
    draw.line([(x, y_start), (x, y_end)], fill="#2E75B6", width=3)
    # Arrow head
    draw.polygon([(x - 6, y_end - 10), (x + 6, y_end - 10), (x, y_end)], fill="#2E75B6")
    if label:
        draw.text((x + 12, (y_start + y_end) // 2 - 8), label, fill="#1B4F72", font=font_mono_small)

# STAGE 1: Client Layer
s1_y = 180
draw.rectangle([(910, s1_y), (1960, s1_y + 70)], fill="#F8FAFC", outline="#34495E", width=2)
draw.text((925, s1_y + 10), "1. CLIENT INTERACTION LAYER (Frontend Viewports & Browser Telemetry)", fill="#2C3E50", font=font_box_title)
draw.text((925, s1_y + 38), "• Citizen: Geotagged waste incident + photo | Driver: Collection stops, route optimize | Admin: KPI dashboard & CSV export", fill="#555555", font=font_box_sub)

draw_arrow_down(1435, s1_y + 70, s1_y + 105, "HTTP POST/GET/PUT (JSON / Multipart)")

# STAGE 2: REST API Gateway & Routing
s2_y = s1_y + 105
draw.rectangle([(910, s2_y), (1960, s2_y + 80)], fill="#EBF5FB", outline="#2980B9", width=2)
draw.text((925, s2_y + 10), "2. EXPRESS.JS REST API ROUTING GATEWAY (backend/server.js on Port 3000)", fill="#1B4F72", font=font_box_title)
draw.text((925, s2_y + 36), "Endpoints: POST /api/login, POST /api/signup, POST /api/complaints, GET /api/complaints", fill="#2C3E50", font=font_mono_small)
draw.text((925, s2_y + 56), "POST /api/route-optimize, POST /api/driver/route/lock, PUT /api/complaints/:id/resolve, GET /api/admin/stats", fill="#2C3E50", font=font_mono_small)

draw_arrow_down(1435, s2_y + 80, s2_y + 115, "Payload stream")

# STAGE 3: Middleware & Security Filters
s3_y = s2_y + 115
draw.rectangle([(910, s3_y), (1960, s3_y + 75)], fill="#FDEDEC", outline="#E74C3C", width=2)
draw.text((925, s3_y + 10), "3. MIDDLEWARE & SECURITY VALIDATION STACK", fill="#922B21", font=font_box_title)
draw.text((925, s3_y + 36), "• CORS Policy | express.json() Body Parser | Multer Multipart Ingestion (5 MB max, MIME image verification)", fill="#4A148C", font=font_box_sub)
draw.text((925, s3_y + 54), "• PBKDF2/SHA-512 Cryptographic Hashing | verifyPageSecurity() & Role-Based Access Control (RBAC)", fill="#C0392B", font=font_box_sub)

draw_arrow_down(1435, s3_y + 75, s3_y + 110, "Validated parameters")

# STAGE 4: Business Logic & Processing Services
s4_y = s3_y + 110
draw.rectangle([(910, s4_y), (1960, s4_y + 90)], fill="#FEF9E7", outline="#F39C12", width=2)
draw.text((925, s4_y + 10), "4. CONTROLLER & CORE BUSINESS LOGIC SERVICES", fill="#7D6608", font=font_box_title)
draw.text((925, s4_y + 36), "• Complaint Ingestion Service: Assigns COMP-XXX, tags W3C GPS coords, sets status='Pending'", fill="#555555", font=font_box_sub)
draw.text((925, s4_y + 54), "• Geolocation Engine: Haversine 1.0 km Proximity Filter for collection driver assignment", fill="#555555", font=font_box_sub)
draw.text((925, s4_y + 72), "• Optimization Engine: Greedy Nearest-Neighbor TSP + Project-OSRM Road Polyline Navigation", fill="#555555", font=font_box_sub)

draw_arrow_down(1435, s4_y + 90, s4_y + 125, "Synchronous write triggers")

# STAGE 5: Dual-Persistence Data Layer
s5_y = s4_y + 125
draw.rectangle([(910, s5_y), (1960, s5_y + 110)], fill="#E8F8F5", outline="#16A085", width=2)
draw.text((925, s5_y + 10), "5. DUAL-PERSISTENCE DATA STORAGE & DISK PERSISTENCE", fill="#0E6251", font=font_box_title)

# Draw sub-boxes for JSON and SQLite
draw.rectangle([(930, s5_y + 38), (1410, s5_y + 98)], fill="#FFFFFF", outline="#16A085", width=1)
draw.text((940, s5_y + 44), "Active Document Store (backend/db.json)", fill="#117A65", font=font_box_title)
draw.text((940, s5_y + 68), "Non-blocking CRUD operations on JSON collections", fill="#555555", font=font_flow_text)

# Arrow from JSON to SQLite
draw.line([(1410, s5_y + 68), (1460, s5_y + 68)], fill="#16A085", width=2)
draw.polygon([(1460, s5_y + 68), (1452, s5_y + 64), (1452, s5_y + 72)], fill="#16A085")
draw.text((1416, s5_y + 48), "sync_sqlite.py", fill="#0E6251", font=font_mono_small)

draw.rectangle([(1470, s5_y + 38), (1940, s5_y + 98)], fill="#FFFFFF", outline="#2980B9", width=1)
draw.text((1480, s5_y + 44), "Relational Mirror (backend/urban_clean.db)", fill="#1B4F72", font=font_box_title)
draw.text((1480, s5_y + 68), "ACID Relational SQL Tables: accounts, complaints...", fill="#555555", font=font_flow_text)

draw_arrow_down(1435, s5_y + 110, s5_y + 145, "Formatted JSON Response + HTTP Status")

# STAGE 6: Client Response & UI Update
s6_y = s5_y + 145
draw.rectangle([(910, s6_y), (1960, s6_y + 70)], fill="#F4ECF7", outline="#8E44AD", width=2)
draw.text((925, s6_y + 10), "6. CLIENT RESPONSE RECEPTION & DOM/GIS UPDATE", fill="#512E5F", font=font_box_title)
draw.text((925, s6_y + 38), "• HTTP 200/201/400/401/403 | DOM update, Leaflet marker animation, toast alerts, localStorage update", fill="#555555", font=font_box_sub)

# STAGE 7: Concrete Operational Workflows (3-column comparison at bottom)
s7_y = s6_y + 90
draw.rectangle([(910, s7_y), (1960, s7_y + 280)], fill="#FAFAFA", outline="#7F8C8D", width=1)
draw.text((925, s7_y + 10), "7. CONCRETE ROLE WORKFLOWS EXECUTED THROUGH BACKEND", fill="#1F4E79", font=font_sec_hdr)

col_w = 330
col_gap = 20

# Workflow 1: Citizen
w1_x = 925
draw.rectangle([(w1_x, s7_y + 40), (w1_x + col_w, s7_y + 265)], fill="#FFFFFF", outline="#2980B9", width=1)
draw.text((w1_x + 10, s7_y + 48), "Citizen Incident Flow", fill="#1F4E79", font=font_flow_title)
flow1 = [
    "1. Citizen fills reporting form",
    "2. Auto-Detect GPS coordinates",
    "3. Attach before-cleanup photo",
    "4. POST /api/complaints",
    "5. Multer validates image (<5MB)",
    "6. Issue ticket COMP-XXX",
    "7. Status set to 'Pending'",
    "8. Real-time sync to SQLite",
    "9. Ticket appears in 'My Reports'"
]
for i, line in enumerate(flow1):
    draw.text((w1_x + 12, s7_y + 75 + i * 20), line, fill="#333333", font=font_flow_text)

# Workflow 2: Driver
w2_x = w1_x + col_w + col_gap
draw.rectangle([(w2_x, s7_y + 40), (w2_x + col_w, s7_y + 265)], fill="#FFFFFF", outline="#D4AC0D", width=1)
draw.text((w2_x + 10, s7_y + 48), "Driver Route & Shift Flow", fill="#7D6608", font=font_flow_title)
flow2 = [
    "1. Driver logs in with vehicle ID",
    "2. Toggle On-Duty shift status",
    "3. Haversine 1.0 km proximity filter",
    "4. POST /api/route-optimize",
    "5. Greedy TSP sequences stops",
    "6. OSRM projects road polyline",
    "7. POST /api/driver/route/lock",
    "8. PUT /api/complaints/:id/resolve",
    "9. Ticket marked 'Completed'"
]
for i, line in enumerate(flow2):
    draw.text((w2_x + 12, s7_y + 75 + i * 20), line, fill="#333333", font=font_flow_text)

# Workflow 3: Admin
w3_x = w2_x + col_w + col_gap
draw.rectangle([(w3_x, s7_y + 40), (w3_x + col_w, s7_y + 265)], fill="#FFFFFF", outline="#27AE60", width=1)
draw.text((w3_x + 10, s7_y + 48), "Admin Governance Flow", fill="#1E8449", font=font_flow_title)
flow3 = [
    "1. Admin logs in with ward lock",
    "2. GET /api/admin/stats",
    "3. Real-time KPI counters render",
    "4. Ward complaint distribution map",
    "5. Driver roster duty monitoring",
    "6. Manual assignment override",
    "7. SLA breach detection (>48h)",
    "8. GET /api/admin/export-csv",
    "9. 30-Day compliance CSV export"
]
for i, line in enumerate(flow3):
    draw.text((w3_x + 12, s7_y + 75 + i * 20), line, fill="#333333", font=font_flow_text)

# Save image
out_dir = os.path.join("screenshots", "report_assets")
os.makedirs(out_dir, exist_ok=True)
out_path = os.path.join(out_dir, "backend_structure_dataflow.png")
img.save(out_path, dpi=(300, 300))
print(f"Backend structure and data flow diagram successfully generated at: {out_path}")
