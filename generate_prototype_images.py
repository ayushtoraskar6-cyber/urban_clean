# -*- coding: utf-8 -*-
"""
Generator for 12 Academic Wireframe / Prototype Mockups for UrbanClean
Produces clean, professional UI mockup images suitable for university project documentation.
"""

import os
from PIL import Image, ImageDraw, ImageFont

OUT_DIR = r"d:\Urban clean\screenshots\report_assets"
os.makedirs(OUT_DIR, exist_ok=True)

# Standard dimensions
W, H = 1200, 750

# Color palette (Academic wireframe / clean SaaS UI)
BG_PAGE = (245, 247, 250)
CARD_BG = (255, 255, 255)
NAV_BG = (31, 78, 121)       # UrbanClean Navy #1F4E79
TEXT_DARK = (30, 41, 59)     # Slate 800
TEXT_MUTED = (100, 116, 139) # Slate 500
BORDER_COLOR = (203, 213, 225) # Slate 300
PRIMARY = (2, 132, 199)      # Sky 600
SUCCESS = (16, 185, 129)     # Emerald 500
WARNING = (245, 158, 11)     # Amber 500
DANGER = (239, 68, 68)       # Red 500
INPUT_BG = (248, 250, 252)

# Load fonts
try:
    font_title = ImageFont.truetype("arialbd.ttf", 24)
    font_heading = ImageFont.truetype("arialbd.ttf", 18)
    font_bold = ImageFont.truetype("arialbd.ttf", 14)
    font_regular = ImageFont.truetype("arial.ttf", 13)
    font_small = ImageFont.truetype("arial.ttf", 11)
    font_badge = ImageFont.truetype("arialbd.ttf", 11)
except Exception:
    font_title = ImageFont.load_default()
    font_heading = font_title
    font_bold = font_title
    font_regular = font_title
    font_small = font_title
    font_badge = font_title

def draw_window_frame(draw, title_text):
    # Base background
    draw.rectangle([0, 0, W, H], fill=BG_PAGE)
    
    # Outer browser window container
    draw.rounded_rectangle([30, 25, W - 30, H - 25], radius=10, fill=CARD_BG, outline=BORDER_COLOR, width=2)
    
    # Browser titlebar
    draw.rounded_rectangle([30, 25, W - 30, 70], radius=10, fill=(241, 245, 249))
    draw.rectangle([30, 60, W - 30, 70], fill=(241, 245, 249)) # flatten bottom
    draw.line([30, 70, W - 30, 70], fill=BORDER_COLOR, width=1)
    
    # Window dots
    draw.ellipse([50, 42, 62, 54], fill=(255, 95, 86))
    draw.ellipse([70, 42, 82, 54], fill=(255, 189, 46))
    draw.ellipse([90, 42, 102, 54], fill=(39, 201, 63))
    
    # Title text
    draw.text((120, 39), f"UrbanClean System Prototype — {title_text}", fill=TEXT_DARK, font=font_bold)
    
    # Navigation bar inside mockup
    draw.rectangle([30, 70, W - 30, 120], fill=NAV_BG)
    draw.text((55, 82), "🌱 UrbanClean", fill=(255, 255, 255), font=font_heading)
    draw.text((210, 86), "Smart City Waste Management & Route Optimization", fill=(203, 213, 225), font=font_small)
    
    # Nav links
    nav_links = ["Home", "Report Waste", "Track Status", "Driver Workspace", "Admin Portal", "Help"]
    nx = 580
    for link in nav_links:
        draw.text((nx, 86), link, fill=(224, 242, 254), font=font_regular)
        nx += 100

def draw_button(draw, xy, text, bg=PRIMARY, fg=(255, 255, 255), font=font_bold):
    draw.rounded_rectangle(xy, radius=6, fill=bg, outline=bg)
    bbox = draw.textbbox((0, 0), text, font=font)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    bx = (xy[0] + xy[2] - tw) / 2
    by = (xy[1] + xy[3] - th) / 2 - 2
    draw.text((bx, by), text, fill=fg, font=font)

def draw_input(draw, xy, label, value=""):
    # Label above
    draw.text((xy[0], xy[1] - 18), label, fill=TEXT_DARK, font=font_bold)
    # Box
    draw.rounded_rectangle(xy, radius=5, fill=INPUT_BG, outline=BORDER_COLOR, width=1)
    if value:
        draw.text((xy[0] + 12, xy[1] + 10), value, fill=TEXT_DARK, font=font_regular)

# ─── 1. LANDING PAGE PROTOTYPE ───────────────────────────────────────────────
def make_proto_1():
    img = Image.new("RGB", (W, H), BG_PAGE)
    d = ImageDraw.Draw(img)
    draw_window_frame(d, "Public Landing / Home Page")
    
    # Hero section
    d.rounded_rectangle([60, 140, W - 60, 310], radius=8, fill=(238, 242, 255), outline=(199, 210, 254))
    d.text((90, 165), "Clean Cities Begin with Informed Communities", fill=(17, 24, 39), font=font_title)
    d.text((90, 205), "Crowdsourced Geospatial Waste Reporting & Fuel-Optimized Municipal Fleet Collection", fill=TEXT_MUTED, font=font_regular)
    d.text((90, 225), "Report overflowing bins with meter GPS accuracy, track complaint lifecycles in real time, and empower municipal fleets.", fill=TEXT_MUTED, font=font_small)
    
    draw_button(d, [90, 255, 270, 295], "📢 Report Waste Issue", bg=PRIMARY)
    draw_button(d, [290, 255, 450, 295], "🗺️ View Live City Map", bg=(15, 118, 110))
    draw_button(d, [470, 255, 620, 295], "🔑 Multi-Role Login", bg=(79, 70, 229))
    
    # 3 Stat Cards
    stats = [
        ("12,458", "Complaints Resolved", "Verified through photographic proof", SUCCESS),
        ("346", "Active Municipal Tickets", "Currently in queue & in-progress", WARNING),
        ("28.1%", "Average Fuel Savings", "Achieved via Greedy TSP + OSRM routing", PRIMARY)
    ]
    sx = 60
    for val, lbl, desc, col in stats:
        d.rounded_rectangle([sx, 330, sx + 340, 440], radius=8, fill=CARD_BG, outline=BORDER_COLOR, width=1)
        d.text((sx + 20, 345), val, fill=col, font=font_title)
        d.text((sx + 20, 380), lbl, fill=TEXT_DARK, font=font_bold)
        d.text((sx + 20, 405), desc, fill=TEXT_MUTED, font=font_small)
        sx += 370
        
    # Bottom interactive map preview placeholder
    d.rounded_rectangle([60, 460, W - 60, 700], radius=8, fill=(241, 245, 249), outline=BORDER_COLOR)
    d.text((80, 475), "Public Waste Density Basemap (OpenStreetMap Preview)", fill=TEXT_DARK, font=font_bold)
    # Simulated map grid
    for gx in range(80, W - 80, 120):
        d.line([gx, 505, gx, 680], fill=(226, 232, 240), width=1)
    for gy in range(505, 680, 40):
        d.line([80, gy, W - 80, gy], fill=(226, 232, 240), width=1)
    # Sample markers
    d.text((250, 560), "📍 Kalyan West (14 Active)", fill=DANGER, font=font_bold)
    d.text((620, 580), "📍 Bandra Sector-3 (6 Active)", fill=WARNING, font=font_bold)
    d.text((850, 540), "📍 Kurla Industrial (18 Active)", fill=DANGER, font=font_bold)
    d.text((450, 620), "📍 Thane Sector-2 (Cleared ✔)", fill=SUCCESS, font=font_bold)
    
    img.save(os.path.join(OUT_DIR, "proto_landing.png"))

# ─── 2. LOGIN PROTOTYPE ───────────────────────────────────────────────────────
def make_proto_2():
    img = Image.new("RGB", (W, H), BG_PAGE)
    d = ImageDraw.Draw(img)
    draw_window_frame(d, "User Authentication Interface")
    
    # Centered login card
    cx1, cy1, cx2, cy2 = 380, 150, 820, 680
    d.rounded_rectangle([cx1, cy1, cx2, cy2], radius=10, fill=CARD_BG, outline=BORDER_COLOR, width=2)
    
    d.text((cx1 + 80, cy1 + 25), "UrbanClean Secure Portal", fill=NAV_BG, font=font_title)
    d.text((cx1 + 60, cy1 + 60), "Select your role to access authorized workspace", fill=TEXT_MUTED, font=font_small)
    
    # Role selector tabs
    d.rounded_rectangle([cx1 + 30, cy1 + 90, cx1 + 145, cy1 + 125], radius=6, fill=PRIMARY)
    d.text((cx1 + 55, cy1 + 99), "Citizen", fill=(255, 255, 255), font=font_bold)
    
    d.rounded_rectangle([cx1 + 155, cy1 + 90, cx1 + 270, cy1 + 125], radius=6, fill=INPUT_BG, outline=BORDER_COLOR)
    d.text((cx1 + 185, cy1 + 99), "Driver", fill=TEXT_DARK, font=font_bold)
    
    d.rounded_rectangle([cx1 + 280, cy1 + 90, cx1 + 395, cy1 + 125], radius=6, fill=INPUT_BG, outline=BORDER_COLOR)
    d.text((cx1 + 305, cy1 + 99), "Admin", fill=TEXT_DARK, font=font_bold)
    
    # Form fields
    draw_input(d, [cx1 + 30, cy1 + 165, cx2 - 30, cy1 + 205], "Email Address", "ayush@urbanclean.org")
    draw_input(d, [cx1 + 30, cy1 + 245, cx2 - 30, cy1 + 285], "Account Password", "••••••••••••")
    
    # Options
    d.rectangle([cx1 + 30, cy1 + 300, cx1 + 45, cy1 + 315], fill=PRIMARY)
    d.text((cx1 + 55, cy1 + 301), "Remember session (PBKDF2 encrypted token)", fill=TEXT_MUTED, font=font_small)
    
    draw_button(d, [cx1 + 30, cy1 + 335, cx2 - 30, cy1 + 380], "🔐 Secure Sign In", bg=PRIMARY)
    
    d.line([cx1 + 30, cy1 + 410, cx2 - 30, cy1 + 410], fill=BORDER_COLOR, width=1)
    
    # Demo credentials reference box
    d.rounded_rectangle([cx1 + 30, cy1 + 425, cx2 - 30, cy1 + 500], radius=6, fill=(248, 250, 252), outline=BORDER_COLOR)
    d.text((cx1 + 40, cy1 + 433), "Academic Demo Credentials (Preset in Prototype):", fill=NAV_BG, font=font_badge)
    d.text((cx1 + 40, cy1 + 450), "• Citizen: ayush@urbanclean.org  | Citizen@123", fill=TEXT_MUTED, font=font_small)
    d.text((cx1 + 40, cy1 + 466), "• Driver:  ramesh@urbanclean.org | Driver@123", fill=TEXT_MUTED, font=font_small)
    d.text((cx1 + 40, cy1 + 482), "• Admin:   admin@urbanclean.org  | Admin@123", fill=TEXT_MUTED, font=font_small)
    
    draw_button(d, [cx1 + 30, cy1 + 515, cx2 - 30, cy1 + 555], "Create New Citizen Account", bg=(241, 245, 249), fg=PRIMARY)
    
    img.save(os.path.join(OUT_DIR, "proto_login.png"))

# ─── 3. CITIZEN REGISTRATION PROTOTYPE ───────────────────────────────────────
def make_proto_3():
    img = Image.new("RGB", (W, H), BG_PAGE)
    d = ImageDraw.Draw(img)
    draw_window_frame(d, "Citizen Registration Interface")
    
    cx1, cy1, cx2, cy2 = 320, 140, 880, 710
    d.rounded_rectangle([cx1, cy1, cx2, cy2], radius=10, fill=CARD_BG, outline=BORDER_COLOR, width=2)
    
    d.text((cx1 + 110, cy1 + 20), "Register Citizen Account", fill=NAV_BG, font=font_title)
    d.text((cx1 + 80, cy1 + 55), "Create verified credentials to report & track neighborhood waste", fill=TEXT_MUTED, font=font_small)
    
    draw_input(d, [cx1 + 30, cy1 + 105, cx1 + 260, cy1 + 145], "First Name *", "Ayush")
    draw_input(d, [cx1 + 290, cy1 + 105, cx2 - 30, cy1 + 145], "Last Name *", "Toraskar")
    
    draw_input(d, [cx1 + 30, cy1 + 180, cx2 - 30, cy1 + 220], "Email Address (Login ID) *", "ayushtoraskar6@gmail.com")
    draw_input(d, [cx1 + 30, cy1 + 255, cx1 + 260, cy1 + 295], "Mobile Contact *", "+91 98765 43210")
    draw_input(d, [cx1 + 290, cy1 + 255, cx2 - 30, cy1 + 295], "Municipal Jurisdiction *", "Kalyan-Dombivli (KDMC) ▾")
    
    draw_input(d, [cx1 + 30, cy1 + 330, cx1 + 260, cy1 + 370], "Create Password (8+ chars) *", "••••••••••••")
    draw_input(d, [cx1 + 290, cy1 + 330, cx2 - 30, cy1 + 370], "Confirm Password *", "••••••••••••")
    
    # Password rules
    d.text((cx1 + 30, cy1 + 382), "✔ Minimum 8 characters  ✔ Salted SHA-512 hashing  ✔ Cross-site data privacy enforced", fill=SUCCESS, font=font_small)
    
    # Checkbox
    d.rectangle([cx1 + 30, cy1 + 415, cx1 + 45, cy1 + 430], fill=PRIMARY)
    d.text((cx1 + 55, cy1 + 416), "I agree to civic terms of service and genuine waste evidence reporting policy", fill=TEXT_MUTED, font=font_small)
    
    draw_button(d, [cx1 + 30, cy1 + 455, cx2 - 30, cy1 + 500], "📝 Complete Citizen Registration", bg=PRIMARY)
    
    d.text((cx1 + 160, cy1 + 520), "Already registered? Return to Login Portal", fill=PRIMARY, font=font_bold)
    
    img.save(os.path.join(OUT_DIR, "proto_registration.png"))

# ─── 4. CITIZEN COMPLAINT REPORTING PROTOTYPE ────────────────────────────────
def make_proto_4():
    img = Image.new("RGB", (W, H), BG_PAGE)
    d = ImageDraw.Draw(img)
    draw_window_frame(d, "Citizen Waste Reporting Interface")
    
    # Left column: Form
    d.rounded_rectangle([50, 140, 620, 710], radius=8, fill=CARD_BG, outline=BORDER_COLOR)
    d.text((70, 160), "Lodge a Waste Accumulation Incident", fill=NAV_BG, font=font_heading)
    d.text((70, 188), "Provide location, category, and photograph evidence for driver dispatch", fill=TEXT_MUTED, font=font_small)
    
    # Waste Category Dropdown
    draw_input(d, [70, 235, 600, 275], "Waste Category *", "Garbage Overflow / Dumpster Full ▾")
    
    # Description Textarea
    d.text((70, 295), "Landmark & Proximity Description *", fill=TEXT_DARK, font=font_bold)
    d.rounded_rectangle([70, 315, 600, 385], radius=5, fill=INPUT_BG, outline=BORDER_COLOR)
    d.text((85, 325), "Severe garbage overflow near municipal school corner. Waste has spilled onto road.", fill=TEXT_DARK, font=font_regular)
    d.text((85, 345), "Blocks pedestrian pavement. Requires compactor truck clearance.", fill=TEXT_MUTED, font=font_small)
    
    # Geolocation controls
    d.text((70, 405), "Geospatial Coordinates & Street Address *", fill=TEXT_DARK, font=font_bold)
    draw_button(d, [70, 425, 280, 460], "🎯 Auto-Detect GPS", bg=(15, 118, 110))
    d.text((295, 435), "Lat: 19.157006  |  Lng: 73.238692", fill=TEXT_DARK, font=font_badge)
    
    draw_input(d, [70, 485, 600, 525], "Reverse-Geocoded Address (OSM Nominatim)", "Station Road, Kalyan West, Thane, Maharashtra 421301")
    
    # Photo Upload dropzone
    d.text((70, 545), "Mandatory Photographic Evidence (Max 5 MB) *", fill=TEXT_DARK, font=font_bold)
    d.rounded_rectangle([70, 565, 600, 635], radius=6, fill=(241, 245, 249), outline=PRIMARY, width=1)
    d.text((200, 585), "📷 photo_kalyan_overflow_01.jpg (1.8 MB)", fill=PRIMARY, font=font_bold)
    d.text((220, 605), "✔ JPEG format validated by Multer middleware", fill=SUCCESS, font=font_small)
    
    draw_button(d, [70, 655, 600, 695], "🚀 Submit Complaint to Municipal Dispatch", bg=PRIMARY)
    
    # Right column: Mini map locator
    d.rounded_rectangle([640, 140, W - 50, 710], radius=8, fill=CARD_BG, outline=BORDER_COLOR)
    d.text((660, 160), "Interactive Location Verification", fill=NAV_BG, font=font_heading)
    d.text((660, 188), "Click map canvas to fine-tune pin position", fill=TEXT_MUTED, font=font_small)
    
    d.rounded_rectangle([660, 220, W - 70, 650], radius=6, fill=(241, 245, 249), outline=BORDER_COLOR)
    # Simulated map grid
    for gx in range(680, W - 80, 80):
        d.line([gx, 230, gx, 640], fill=(226, 232, 240), width=1)
    for gy in range(230, 640, 40):
        d.line([660, gy, W - 70, gy], fill=(226, 232, 240), width=1)
    # Pinned location
    d.ellipse([880, 410, 910, 440], fill=DANGER)
    d.rounded_rectangle([820, 365, 970, 405], radius=4, fill=(30, 41, 59))
    d.text((830, 375), "Pinned Dumpster Site", fill=(255, 255, 255), font=font_badge)
    
    draw_button(d, [660, 665, W - 70, 695], "Confirm Pinned Location (19.1570, 73.2386)", bg=(15, 118, 110))
    
    img.save(os.path.join(OUT_DIR, "proto_complaint_form.png"))

# ─── 5. INTERACTIVE MAP PROTOTYPE ─────────────────────────────────────────────
def make_proto_5():
    img = Image.new("RGB", (W, H), BG_PAGE)
    d = ImageDraw.Draw(img)
    draw_window_frame(d, "Interactive Location Selection & Map Canvas")
    
    # Top controls bar
    d.rounded_rectangle([50, 135, W - 50, 185], radius=6, fill=CARD_BG, outline=BORDER_COLOR)
    d.text((70, 150), "Search Area / Landmark:", fill=TEXT_DARK, font=font_bold)
    d.rounded_rectangle([250, 142, 600, 178], radius=4, fill=INPUT_BG, outline=BORDER_COLOR)
    d.text((260, 152), "Kalyan West Station Road...", fill=TEXT_MUTED, font=font_regular)
    draw_button(d, [615, 142, 730, 178], "Search", bg=PRIMARY)
    draw_button(d, [745, 142, 910, 178], "🎯 Use My GPS", bg=(15, 118, 110))
    d.text((930, 152), "Zoom: 16x | WGS84 Datum", fill=TEXT_MUTED, font=font_small)
    
    # Large Map Canvas
    d.rounded_rectangle([50, 195, W - 50, 650], radius=8, fill=(241, 245, 249), outline=BORDER_COLOR)
    
    # Simulated roads
    d.line([80, 300, W - 80, 480], fill=(203, 213, 225), width=12) # main road
    d.line([400, 200, 500, 640], fill=(203, 213, 225), width=8)   # cross street
    d.line([750, 200, 720, 640], fill=(203, 213, 225), width=8)   # cross street 2
    d.text((120, 320), "Shivaji Chowk", fill=TEXT_MUTED, font=font_small)
    d.text((420, 220), "Station Road", fill=TEXT_MUTED, font=font_small)
    d.text((760, 220), "Agra Road", fill=TEXT_MUTED, font=font_small)
    
    # Map controls
    d.rounded_rectangle([70, 215, 105, 285], radius=4, fill=CARD_BG, outline=BORDER_COLOR)
    d.text((82, 222), "+", fill=TEXT_DARK, font=font_heading)
    d.line([70, 250, 105, 250], fill=BORDER_COLOR)
    d.text((84, 255), "−", fill=TEXT_DARK, font=font_heading)
    
    # Draggable Pin with popup
    d.ellipse([580, 380, 610, 410], fill=DANGER)
    d.rounded_rectangle([480, 290, 710, 370], radius=6, fill=(30, 41, 59), outline=(15, 23, 42))
    d.text((495, 300), "📍 Selected Incident Coordinates", fill=(255, 255, 255), font=font_bold)
    d.text((495, 322), "Lat: 19.157006  |  Lng: 73.238692", fill=(147, 197, 253), font=font_small)
    d.text((495, 340), "Click & drag pin to adjust exact dumpster spot", fill=(203, 213, 225), font=font_small)
    
    # Bottom status telemetry
    d.rounded_rectangle([50, 665, W - 50, 715], radius=6, fill=CARD_BG, outline=BORDER_COLOR)
    d.text((70, 680), "Selected: Badlapur / Kalyan Sector-3  •  Accuracy: ±4.8m (W3C High-Accuracy GPS)  •  Status: Ready", fill=TEXT_DARK, font=font_regular)
    draw_button(d, [W - 280, 672, W - 70, 708], "Apply Pinned Coordinates", bg=SUCCESS)
    
    img.save(os.path.join(OUT_DIR, "proto_map_selection.png"))

# ─── 6. CITIZEN COMPLAINT TRACKING PROTOTYPE ─────────────────────────────────
def make_proto_6():
    img = Image.new("RGB", (W, H), BG_PAGE)
    d = ImageDraw.Draw(img)
    draw_window_frame(d, "Citizen Complaint Tracking Interface")
    
    d.rounded_rectangle([50, 140, W - 50, 710], radius=8, fill=CARD_BG, outline=BORDER_COLOR)
    d.text((75, 160), "Track Your Reported Incidents ('My Reports')", fill=NAV_BG, font=font_title)
    d.text((75, 192), "Real-time transparent lifecycle progression with mandatory after-cleanup photo audit", fill=TEXT_MUTED, font=font_regular)
    
    # Active Ticket Detail Card
    d.rounded_rectangle([75, 220, W - 75, 450], radius=8, fill=(248, 250, 252), outline=BORDER_COLOR)
    d.text((95, 235), "Ticket # COMP-492  —  Garbage Overflow Reported", fill=NAV_BG, font=font_heading)
    d.text((95, 260), "Location: Kalyan Sector-5 (Near Police Station)  •  Submitted: 28 Sep 2026, 18:50", fill=TEXT_MUTED, font=font_small)
    
    # 4-Stage Progress Tracker
    stages = [
        ("1. Submitted", "Pending", SUCCESS, True),
        ("2. Assigned", "Driver Linked", SUCCESS, True),
        ("3. In-Progress", "Driver On-Site", PRIMARY, True),
        ("4. Completed", "Proof Verified", (148, 163, 184), False)
    ]
    px = 120
    for i, (stg, sub, col, done) in enumerate(stages):
        # Circle
        d.ellipse([px, 290, px + 36, 326], fill=col)
        d.text((px + 12, 298), str(i + 1), fill=(255, 255, 255), font=font_bold)
        d.text((px - 15, 335), stg, fill=TEXT_DARK, font=font_bold)
        d.text((px - 15, 352), sub, fill=TEXT_MUTED, font=font_small)
        # Connecting bar
        if i < 3:
            d.line([px + 45, 308, px + 185, 308], fill=SUCCESS if i < 2 else BORDER_COLOR, width=4)
        px += 220
        
    # Before / After Photo Comparison Cards
    d.rounded_rectangle([95, 380, 480, 435], radius=6, fill=CARD_BG, outline=BORDER_COLOR)
    d.text((110, 395), "📷 Citizen Photo Proof (Reported):", fill=TEXT_DARK, font=font_bold)
    d.text((110, 412), "photo-1789046772.jpg  (Garbage heap verified)", fill=TEXT_MUTED, font=font_small)
    
    d.rounded_rectangle([510, 380, 900, 435], radius=6, fill=CARD_BG, outline=BORDER_COLOR)
    d.text((525, 395), "📷 Driver Resolution Proof (Awaiting):", fill=WARNING, font=font_bold)
    d.text((525, 412), "Mandatory photo required before ticket closes", fill=TEXT_MUTED, font=font_small)
    
    # History Table Header
    d.text((75, 470), "Historical Submissions Log", fill=NAV_BG, font=font_heading)
    d.rounded_rectangle([75, 495, W - 75, 690], radius=6, fill=CARD_BG, outline=BORDER_COLOR)
    
    # Table header
    d.rectangle([75, 495, W - 75, 530], fill=NAV_BG)
    d.text((90, 506), "TICKET ID", fill=(255, 255, 255), font=font_badge)
    d.text((200, 506), "CATEGORY", fill=(255, 255, 255), font=font_badge)
    d.text((360, 506), "LOCATION", fill=(255, 255, 255), font=font_badge)
    d.text((560, 506), "SUBMITTED AT", fill=(255, 255, 255), font=font_badge)
    d.text((750, 506), "ASSIGNED DRIVER", fill=(255, 255, 255), font=font_badge)
    d.text((950, 506), "LIFECYCLE STATUS", fill=(255, 255, 255), font=font_badge)
    
    # Table rows
    rows = [
        ("COMP-492", "Garbage Overflow", "Kalyan Sector-5", "28 Sep 2026", "Ramesh Kumar (DRV-101)", "IN PROGRESS", WARNING),
        ("COMP-573", "Dustbin Full", "Kalyan Sector-1", "10 Sep 2026", "Ramesh Kumar (DRV-101)", "COMPLETED ✔", SUCCESS),
        ("COMP-264", "Garbage Overflow", "Kalyan Sector-3", "10 Sep 2026", "Amit Patel (DRV-102)", "COMPLETED ✔", SUCCESS),
        ("COMP-001", "Road Waste Pile", "Bandra West", "02 Sep 2026", "Sunil Shinde (DRV-103)", "COMPLETED ✔", SUCCESS),
    ]
    ry = 540
    for tid, cat, loc, sdate, drv, st, col in rows:
        d.text((90, ry), tid, fill=PRIMARY, font=font_bold)
        d.text((200, ry), cat, fill=TEXT_DARK, font=font_regular)
        d.text((360, ry), loc, fill=TEXT_MUTED, font=font_small)
        d.text((560, ry), sdate, fill=TEXT_MUTED, font=font_small)
        d.text((750, ry), drv, fill=TEXT_DARK, font=font_small)
        d.rounded_rectangle([945, ry - 3, 1070, ry + 17], radius=4, fill=col)
        d.text((955, ry), st, fill=(255, 255, 255), font=font_badge)
        d.line([75, ry + 25, W - 75, ry + 25], fill=BORDER_COLOR)
        ry += 35
        
    img.save(os.path.join(OUT_DIR, "proto_complaint_tracking.png"))

# ─── 7. DRIVER DASHBOARD PROTOTYPE ───────────────────────────────────────────
def make_proto_7():
    img = Image.new("RGB", (W, H), BG_PAGE)
    d = ImageDraw.Draw(img)
    draw_window_frame(d, "Driver Workspace & Shift Dashboard")
    
    # Header with driver details
    d.rounded_rectangle([50, 135, W - 50, 205], radius=8, fill=CARD_BG, outline=BORDER_COLOR)
    d.text((70, 148), "Driver Field Workspace — Ramesh Kumar (ID: DRV-101)", fill=NAV_BG, font=font_title)
    d.text((70, 178), "Vehicle: Eicher Pro Dump Truck (MH-02-ES-4521)  •  Assigned Ward: Kalyan Sector 1–5", fill=TEXT_MUTED, font=font_regular)
    
    # Duty status toggle
    d.rounded_rectangle([W - 270, 150, W - 70, 190], radius=20, fill=SUCCESS)
    d.text((W - 245, 162), "● SHIFT ACTIVE: ON-DUTY", fill=(255, 255, 255), font=font_badge)
    
    # 3 Route Metric KPI Cards
    kpis = [
        ("5 Stops", "Today's Collection Waypoints", "4 Pending clearance, 1 Resolved", PRIMARY),
        ("12.4 km", "Optimized TSP Driving Distance", "Calculated via OSRM road geometry", (15, 118, 110)),
        ("28.1%", "Fuel Efficiency Savings", "Compared to unoptimized manual tour", SUCCESS)
    ]
    kx = 50
    for val, lbl, desc, col in kpis:
        d.rounded_rectangle([kx, 220, kx + 345, 310], radius=8, fill=CARD_BG, outline=BORDER_COLOR)
        d.text((kx + 20, 232), val, fill=col, font=font_title)
        d.text((kx + 20, 264), lbl, fill=TEXT_DARK, font=font_bold)
        d.text((kx + 20, 285), desc, fill=TEXT_MUTED, font=font_small)
        kx += 370
        
    # Driver Controls Section
    d.rounded_rectangle([50, 325, 450, 710], radius=8, fill=CARD_BG, outline=BORDER_COLOR)
    d.text((70, 345), "Shift Route Engine Controls", fill=NAV_BG, font=font_heading)
    d.text((70, 372), "Manage collection waypoints and daily queue locking", fill=TEXT_MUTED, font=font_small)
    
    draw_button(d, [70, 405, 430, 445], "📍 Add Collection Waypoint (Pin on Map)", bg=(51, 65, 85))
    draw_button(d, [70, 460, 430, 500], "⚡ Run 1.0 km Haversine Geodesic Filter", bg=PRIMARY)
    draw_button(d, [70, 515, 430, 555], "🛣️ Compute Greedy TSP + OSRM Route", bg=(15, 118, 110))
    draw_button(d, [70, 570, 430, 610], "🔒 Lock Daily Route (Start Shift)", bg=(217, 119, 6))
    
    d.rounded_rectangle([70, 625, 430, 690], radius=6, fill=(254, 243, 199), outline=(245, 158, 11))
    d.text((80, 635), "⚠ Daily Route Lock Active:", fill=(180, 83, 9), font=font_badge)
    d.text((80, 652), "Today's shift queue is frozen. Complaints submitted", fill=(180, 83, 9), font=font_small)
    d.text((80, 668), "post-lock are automatically queued for tomorrow.", fill=(180, 83, 9), font=font_small)
    
    # Active Route Queue List
    d.rounded_rectangle([470, 325, W - 50, 710], radius=8, fill=CARD_BG, outline=BORDER_COLOR)
    d.text((490, 345), "Today's Assigned Collection Queue (5 Stops)", fill=NAV_BG, font=font_heading)
    
    stops = [
        ("1", "Kalyan Depot (Starting Point)", "0.0 km", "DEPARTURE", (100, 116, 139)),
        ("2", "COMP-492: Kalyan Sector-5", "2.1 km", "PENDING", DANGER),
        ("3", "COMP-573: Kalyan Sector-1", "4.8 km", "IN PROGRESS", WARNING),
        ("4", "COMP-392: Kalyan Sector-1", "7.3 km", "PENDING", DANGER),
        ("5", "COMP-763: Kalyan Sector-1", "10.2 km", "PENDING", DANGER),
        ("6", "Municipal Landfill Site", "12.4 km", "DISPOSAL", SUCCESS),
    ]
    sy = 380
    for idx, name, dist, st, col in stops:
        d.rounded_rectangle([490, sy, W - 70, sy + 44], radius=6, fill=INPUT_BG, outline=BORDER_COLOR)
        d.ellipse([505, sy + 10, 530, sy + 35], fill=NAV_BG)
        d.text((513, sy + 14), idx, fill=(255, 255, 255), font=font_badge)
        d.text((545, sy + 8), name, fill=TEXT_DARK, font=font_bold)
        d.text((545, sy + 25), f"Road Distance: {dist}", fill=TEXT_MUTED, font=font_small)
        d.rounded_rectangle([W - 190, sy + 10, W - 85, sy + 34], radius=4, fill=col)
        d.text((W - 180, sy + 15), st, fill=(255, 255, 255), font=font_badge)
        sy += 52
        
    img.save(os.path.join(OUT_DIR, "proto_driver_dashboard.png"))

# ─── 8. DRIVER ROUTE PROTOTYPE ───────────────────────────────────────────────
def make_proto_8():
    img = Image.new("RGB", (W, H), BG_PAGE)
    d = ImageDraw.Draw(img)
    draw_window_frame(d, "Driver Route Optimization & Road Polyline Navigation")
    
    # Left: Route Summary Sidebar
    d.rounded_rectangle([50, 135, 380, 710], radius=8, fill=CARD_BG, outline=BORDER_COLOR)
    d.text((70, 155), "Turn-by-Turn Route Navigation", fill=NAV_BG, font=font_heading)
    d.text((70, 180), "Greedy TSP Order with OSRM Road Geometry", fill=TEXT_MUTED, font=font_small)
    
    d.rounded_rectangle([70, 210, 360, 280], radius=6, fill=(238, 242, 255), outline=(199, 210, 254))
    d.text((85, 220), "Next Stop: Stop 3 (COMP-573)", fill=(67, 56, 202), font=font_bold)
    d.text((85, 240), "Kalyan Sector-1 (Near Municipal Garden)", fill=TEXT_DARK, font=font_small)
    d.text((85, 258), "ETA: 8 mins  •  Distance: 1.4 km", fill=TEXT_MUTED, font=font_small)
    
    draw_button(d, [70, 295, 360, 335], "🚗 Launch Google / OSRM Nav", bg=PRIMARY)
    draw_button(d, [70, 345, 360, 385], "📷 Upload Cleanup Proof", bg=SUCCESS)
    
    d.text((70, 405), "Active Tour Sequence:", fill=TEXT_DARK, font=font_bold)
    route_steps = [
        ("1. Kalyan Depot (08:00 AM)", "Departed ✔", SUCCESS),
        ("2. COMP-492 Sector-5", "Cleared (Proof Attached) ✔", SUCCESS),
        ("3. COMP-573 Sector-1", "Approaching Dumpster Site...", WARNING),
        ("4. COMP-392 Sector-1", "Queued (Within 1.0 km)", (100, 116, 139)),
        ("5. COMP-763 Sector-1", "Queued (Within 1.0 km)", (100, 116, 139)),
        ("6. Dumping Ground", "Final Disposal Waypoint", (100, 116, 139)),
    ]
    rty = 430
    for step, st, col in route_steps:
        d.text((70, rty), step, fill=TEXT_DARK, font=font_small)
        d.text((70, rty + 16), st, fill=col, font=font_badge)
        d.line([70, rty + 34, 360, rty + 34], fill=BORDER_COLOR)
        rty += 42
        
    # Right: Map with OSRM Polylines
    d.rounded_rectangle([400, 135, W - 50, 710], radius=8, fill=(241, 245, 249), outline=BORDER_COLOR)
    
    # Simulated roads
    d.line([430, 260, 1120, 580], fill=(226, 232, 240), width=16)
    d.line([600, 180, 750, 680], fill=(226, 232, 240), width=10)
    d.line([950, 180, 880, 680], fill=(226, 232, 240), width=10)
    
    # OSRM Driving Polyline (Blue route)
    route_pts = [(450, 270), (550, 320), (660, 370), (740, 410), (880, 480), (1050, 550)]
    for i in range(len(route_pts) - 1):
        d.line([route_pts[i], route_pts[i+1]], fill=(37, 99, 235), width=6)
        
    # Waypoint markers along route
    for i, (wx, wy) in enumerate(route_pts):
        d.ellipse([wx - 14, wy - 14, wx + 14, wy + 14], fill=(16, 185, 129) if i < 2 else (245, 158, 11) if i == 2 else NAV_BG)
        d.text((wx - 5, wy - 8), str(i + 1), fill=(255, 255, 255), font=font_badge)
        
    # Live truck marker
    d.ellipse([730, 400, 755, 425], fill=DANGER)
    d.rounded_rectangle([690, 435, 795, 465], radius=4, fill=(15, 23, 42))
    d.text((700, 442), "🚛 Truck Live", fill=(255, 255, 255), font=font_badge)
    
    img.save(os.path.join(OUT_DIR, "proto_driver_route.png"))

# ─── 9. PROOF OF CLEANUP UPLOAD PROTOTYPE ────────────────────────────────────
def make_proto_9():
    img = Image.new("RGB", (W, H), BG_PAGE)
    d = ImageDraw.Draw(img)
    draw_window_frame(d, "Driver Proof-of-Cleanup Resolution Protocol")
    
    cx1, cy1, cx2, cy2 = 320, 140, 880, 710
    d.rounded_rectangle([cx1, cy1, cx2, cy2], radius=10, fill=CARD_BG, outline=BORDER_COLOR, width=2)
    
    d.text((cx1 + 80, cy1 + 25), "Closed-Loop Ticket Resolution", fill=NAV_BG, font=font_title)
    d.text((cx1 + 55, cy1 + 60), "Upload photographic verification to authenticate waste site clearance", fill=TEXT_MUTED, font=font_small)
    
    # Ticket info card
    d.rounded_rectangle([cx1 + 30, cy1 + 95, cx2 - 30, cy1 + 175], radius=6, fill=INPUT_BG, outline=BORDER_COLOR)
    d.text((cx1 + 45, cy1 + 105), "Resolving Ticket: COMP-573", fill=NAV_BG, font=font_heading)
    d.text((cx1 + 45, cy1 + 130), "Category: Garbage Overflow  •  Location: Kalyan Sector-1 (Station Road)", fill=TEXT_DARK, font=font_small)
    d.text((cx1 + 45, cy1 + 148), "Reported By: Ayush (CIT-227356)  •  Assigned Vehicle: MH-02-ES-4521", fill=TEXT_MUTED, font=font_small)
    
    # Upload photo box
    d.text((cx1 + 30, cy1 + 195), "Mandatory Clean-Site Photograph *", fill=TEXT_DARK, font=font_bold)
    d.rounded_rectangle([cx1 + 30, cy1 + 215, cx2 - 30, cy1 + 395], radius=8, fill=(241, 245, 249), outline=SUCCESS, width=2)
    
    # Simulated thumbnail inside
    d.rounded_rectangle([cx1 + 150, cy1 + 235, cx1 + 370, cy1 + 340], radius=6, fill=(203, 213, 225))
    d.text((cx1 + 185, cy1 + 275), "📸 [Cleaned Dumpster Image]", fill=TEXT_DARK, font=font_bold)
    d.text((cx1 + 180, cy1 + 295), "photo-after-1789047006.jpg", fill=TEXT_MUTED, font=font_small)
    
    d.text((cx1 + 170, cy1 + 360), "✔ Image Captured via Device Camera (1.4 MB JPEG)", fill=SUCCESS, font=font_badge)
    
    # Resolution Notes
    draw_input(d, [cx1 + 30, cy1 + 435, cx2 - 30, cy1 + 485], "Supervisor / Driver Notes", "Entire roadway and bin perimeter swept. Dumpster emptied.")
    
    # Timestamp stamp
    d.text((cx1 + 30, cy1 + 510), "Immutable Timestamp: 28 Sep 2026, 11:42 AM  |  GPS Verified: 19.2325, 73.1356", fill=TEXT_MUTED, font=font_small)
    
    draw_button(d, [cx1 + 30, cy1 + 545, cx2 - 30, cy1 + 595], "✔ Complete Cleanup & Close Ticket", bg=SUCCESS)
    draw_button(d, [cx1 + 30, cy1 + 610, cx2 - 30, cy1 + 650], "Cancel / Postpone Stop", bg=(241, 245, 249), fg=TEXT_MUTED)
    
    img.save(os.path.join(OUT_DIR, "proto_proof_upload.png"))

# ─── 10. ADMIN DASHBOARD PROTOTYPE ───────────────────────────────────────────
def make_proto_10():
    img = Image.new("RGB", (W, H), BG_PAGE)
    d = ImageDraw.Draw(img)
    draw_window_frame(d, "Municipal Administrator Command Center")
    
    # Top Admin bar
    d.rounded_rectangle([50, 135, W - 50, 195], radius=8, fill=CARD_BG, outline=BORDER_COLOR)
    d.text((70, 148), "Administrator Command Center — Kalyan Municipal Corporation", fill=NAV_BG, font=font_title)
    d.text((70, 175), "Real-time fleet oversight, complaint dispatching, driver rosters, and compliance auditing", fill=TEXT_MUTED, font=font_small)
    d.rounded_rectangle([W - 280, 150, W - 70, 185], radius=6, fill=(238, 242, 255), outline=(199, 210, 254))
    d.text((W - 265, 160), "🔒 Locked Ward: Kalyan (KDMC)", fill=PRIMARY, font=font_badge)
    
    # 4 KPI Cards
    kpis = [
        ("5", "Total Reported Today", "Active civic grievances", DANGER),
        ("4", "Pending Collection", "In dispatch / driver route", WARNING),
        ("0", "Currently In Progress", "Drivers active on site", PRIMARY),
        ("1", "Resolved Today", "Verified by photo proof", SUCCESS)
    ]
    kx = 50
    for val, lbl, desc, col in kpis:
        d.rounded_rectangle([kx, 210, kx + 260, 295], radius=8, fill=CARD_BG, outline=BORDER_COLOR)
        d.text((kx + 20, 222), val, fill=col, font=font_title)
        d.text((kx + 20, 254), lbl, fill=TEXT_DARK, font=font_bold)
        d.text((kx + 20, 274), desc, fill=TEXT_MUTED, font=font_small)
        kx += 280
        
    # Left: Active Driver Fleet Roster
    d.rounded_rectangle([50, 310, 480, 710], radius=8, fill=CARD_BG, outline=BORDER_COLOR)
    d.text((70, 325), "Driver Workforce Roster (3 Registered)", fill=NAV_BG, font=font_heading)
    
    drivers = [
        ("Ramesh Kumar (DRV-101)", "Eicher Pro Dump (MH-02-ES-4521)", "5 Stops • 12.4 km", "ACTIVE", SUCCESS),
        ("Amit Patel (DRV-102)", "Tata Ace Tipper (MH-03-DF-8812)", "3 Stops • 8.6 km", "ACTIVE", SUCCESS),
        ("Sunil Shinde (DRV-103)", "Mahindra Bolero Picker (MH-01)", "0 Stops • Depot", "OFF-DUTY", (148, 163, 184)),
    ]
    dy = 360
    for name, veh, perf, st, col in drivers:
        d.rounded_rectangle([70, dy, 460, dy + 65], radius=6, fill=INPUT_BG, outline=BORDER_COLOR)
        d.text((85, dy + 8), name, fill=TEXT_DARK, font=font_bold)
        d.text((85, dy + 26), veh, fill=TEXT_MUTED, font=font_small)
        d.text((85, dy + 44), perf, fill=PRIMARY, font=font_badge)
        d.rounded_rectangle([365, dy + 12, 445, dy + 36], radius=4, fill=col)
        d.text((375, dy + 17), st, fill=(255, 255, 255), font=font_badge)
        dy += 75
        
    draw_button(d, [70, 600, 460, 640], "➕ Register New Municipal Driver", bg=PRIMARY)
    draw_button(d, [70, 650, 460, 690], "🔄 Auto-Balance Ward Dispatch Queues", bg=(15, 118, 110))
    
    # Right: Today's Complaints Queue Table
    d.rounded_rectangle([505, 310, W - 50, 710], radius=8, fill=CARD_BG, outline=BORDER_COLOR)
    d.text((525, 325), "Active Municipal Grievances — Dispatch Queue", fill=NAV_BG, font=font_heading)
    
    d.rectangle([525, 360, W - 70, 395], fill=NAV_BG)
    d.text((540, 370), "TICKET", fill=(255, 255, 255), font=font_badge)
    d.text((640, 370), "CATEGORY", fill=(255, 255, 255), font=font_badge)
    d.text((780, 370), "REPORTED BY", fill=(255, 255, 255), font=font_badge)
    d.text((910, 370), "AREA / WARD", fill=(255, 255, 255), font=font_badge)
    d.text((1040, 370), "ACTION", fill=(255, 255, 255), font=font_badge)
    
    q_rows = [
        ("COMP-492", "Garbage Overflow", "Ayush", "Kalyan Sec-5", "Assigned"),
        ("COMP-763", "Garbage Overflow", "Aarti", "Kalyan Sec-1", "Assign ▾"),
        ("COMP-392", "Garbage Overflow", "Ayush", "Kalyan Sec-1", "Assign ▾"),
        ("COMP-573", "Garbage Overflow", "Ayush", "Kalyan Sec-1", "Resolved"),
        ("COMP-264", "Garbage Overflow", "Ayush", "Kalyan Sec-3", "Assign ▾"),
    ]
    qy = 405
    for tid, cat, rep, ar, act in q_rows:
        d.text((540, qy), tid, fill=PRIMARY, font=font_bold)
        d.text((640, qy), cat, fill=TEXT_DARK, font=font_small)
        d.text((780, qy), rep, fill=TEXT_MUTED, font=font_small)
        d.text((910, qy), ar, fill=TEXT_DARK, font=font_small)
        d.rounded_rectangle([1030, qy - 4, 1110, qy + 18], radius=4, fill=(238, 242, 255), outline=PRIMARY)
        d.text((1040, qy), act, fill=PRIMARY, font=font_badge)
        d.line([525, qy + 26, W - 70, qy + 26], fill=BORDER_COLOR)
        qy += 40
        
    draw_button(d, [525, 650, W - 70, 690], "📊 Generate & Download 30-Day Compliance CSV", bg=SUCCESS)
    
    img.save(os.path.join(OUT_DIR, "proto_admin_dashboard.png"))

# ─── 11. MONITORING MAP PROTOTYPE ────────────────────────────────────────────
def make_proto_11():
    img = Image.new("RGB", (W, H), BG_PAGE)
    d = ImageDraw.Draw(img)
    draw_window_frame(d, "City-Wide Waste Monitoring Map")
    
    # Top legend & filters
    d.rounded_rectangle([50, 135, W - 50, 185], radius=6, fill=CARD_BG, outline=BORDER_COLOR)
    d.text((70, 150), "Status Filter:", fill=TEXT_DARK, font=font_bold)
    d.text((180, 150), "🔴 Pending (4)", fill=DANGER, font=font_bold)
    d.text((300, 150), "🟠 In-Progress (1)", fill=WARNING, font=font_bold)
    d.text((450, 150), "🟢 Resolved Today (1)", fill=SUCCESS, font=font_bold)
    d.text((630, 150), "🚚 Active Fleet Vehicles (2)", fill=PRIMARY, font=font_bold)
    
    draw_button(d, [W - 240, 142, W - 70, 178], "🔄 Refresh Live Pins", bg=PRIMARY)
    
    # Map area
    d.rounded_rectangle([50, 195, W - 50, 710], radius=8, fill=(241, 245, 249), outline=BORDER_COLOR)
    
    # River / geographic landmarks
    d.line([250, 200, 320, 700], fill=(186, 230, 253), width=45) # Ulhas river representation
    d.text((260, 420), "Ulhas River", fill=(14, 165, 233), font=font_badge)
    
    # Road network
    d.line([80, 350, W - 80, 420], fill=(226, 232, 240), width=14)
    d.line([500, 200, 620, 700], fill=(226, 232, 240), width=10)
    d.line([850, 200, 800, 700], fill=(226, 232, 240), width=10)
    d.text((120, 370), "Agra Road", fill=TEXT_MUTED, font=font_small)
    d.text((640, 300), "Kalyan-Shil Road", fill=TEXT_MUTED, font=font_small)
    
    # Pinned complaints with popup callout
    d.ellipse([580, 340, 606, 366], fill=DANGER)
    d.ellipse([720, 450, 746, 476], fill=DANGER)
    d.ellipse([880, 380, 906, 406], fill=DANGER)
    d.ellipse([450, 520, 476, 546], fill=WARNING)
    d.ellipse([920, 580, 946, 606], fill=SUCCESS)
    
    # Truck icons
    d.rounded_rectangle([630, 380, 690, 410], radius=4, fill=PRIMARY)
    d.text((635, 388), "🚛 DRV-1", fill=(255, 255, 255), font=font_badge)
    
    d.rounded_rectangle([820, 490, 880, 520], radius=4, fill=PRIMARY)
    d.text((825, 498), "🚛 DRV-2", fill=(255, 255, 255), font=font_badge)
    
    # Detailed inspection popup for selected pin
    d.rounded_rectangle([640, 220, 980, 340], radius=8, fill=(30, 41, 59), outline=(15, 23, 42))
    d.text((655, 230), "📍 Incident Ticket: COMP-492", fill=(255, 255, 255), font=font_bold)
    d.text((655, 250), "Ward: Kalyan Sector-5  •  Category: Overflowing Dumpster", fill=(147, 197, 253), font=font_small)
    d.text((655, 268), "Coordinates: 19.157006, 73.238692 (Validated)", fill=(203, 213, 225), font=font_small)
    d.text((655, 286), "Assigned: Ramesh Kumar (Eicher Dump MH-02-ES-4521)", fill=(203, 213, 225), font=font_small)
    d.rounded_rectangle([655, 305, 780, 330], radius=4, fill=DANGER)
    d.text((665, 310), "Status: PENDING", fill=(255, 255, 255), font=font_badge)
    d.rounded_rectangle([795, 305, 960, 330], radius=4, fill=PRIMARY)
    d.text((805, 310), "Dispatch Override ▾", fill=(255, 255, 255), font=font_badge)
    
    img.save(os.path.join(OUT_DIR, "proto_monitoring_map.png"))

# ─── 12. COMPLIANCE REPORT PROTOTYPE ─────────────────────────────────────────
def make_proto_12():
    img = Image.new("RGB", (W, H), BG_PAGE)
    d = ImageDraw.Draw(img)
    draw_window_frame(d, "Monthly Compliance & Audit Reporting")
    
    d.rounded_rectangle([50, 135, W - 50, 710], radius=8, fill=CARD_BG, outline=BORDER_COLOR)
    d.text((70, 155), "30-Day Municipal Waste Tracking & Compliance Audit", fill=NAV_BG, font=font_title)
    d.text((70, 185), "Comprehensive operational audit log formatted for municipal authority oversight and Excel export", fill=TEXT_MUTED, font=font_small)
    
    # Filter toolbar
    d.rounded_rectangle([70, 215, W - 70, 265], radius=6, fill=INPUT_BG, outline=BORDER_COLOR)
    d.text((85, 230), "Date Range: 01 Sep 2026 – 28 Sep 2026 ▾", fill=TEXT_DARK, font=font_bold)
    d.text((380, 230), "Ward: All Kalyan Sectors ▾", fill=TEXT_DARK, font=font_bold)
    d.text((620, 230), "SLA Compliance: 96.4% Met", fill=SUCCESS, font=font_bold)
    draw_button(d, [W - 270, 222, W - 85, 258], "📥 Export to Excel (CSV)", bg=SUCCESS)
    
    # Audit Table
    d.rounded_rectangle([70, 285, W - 70, 690], radius=6, fill=CARD_BG, outline=BORDER_COLOR)
    d.rectangle([70, 285, W - 70, 320], fill=NAV_BG)
    d.text((85, 296), "DATE", fill=(255, 255, 255), font=font_badge)
    d.text((180, 296), "TICKET ID", fill=(255, 255, 255), font=font_badge)
    d.text((280, 296), "CATEGORY", fill=(255, 255, 255), font=font_badge)
    d.text((450, 296), "REPORTED BY", fill=(255, 255, 255), font=font_badge)
    d.text((580, 296), "MUNICIPAL AREA", fill=(255, 255, 255), font=font_badge)
    d.text((750, 296), "DRIVER & VEHICLE", fill=(255, 255, 255), font=font_badge)
    d.text((940, 296), "LIFECYCLE STATUS", fill=(255, 255, 255), font=font_badge)
    d.text((1060, 296), "PHOTO", fill=(255, 255, 255), font=font_badge)
    
    table_rows = [
        ("28/09/2026", "COMP-492", "Garbage Overflow", "Ayush", "Kalyan Sector-5", "Ramesh Kumar (MH-02)", "OPEN", DANGER, "✔ Staged"),
        ("11/09/2026", "COMP-763", "Garbage Overflow", "Aarti", "Kalyan Sector-1", "Unassigned", "OPEN", DANGER, "✔ Staged"),
        ("10/09/2026", "COMP-392", "Garbage Overflow", "Ayush", "Kalyan Sector-1", "Ramesh Kumar (MH-02)", "OPEN", DANGER, "✔ Staged"),
        ("10/09/2026", "COMP-573", "Garbage Overflow", "Ayush", "Kalyan Sector-1", "Ramesh Kumar (MH-02)", "COMPLETED", SUCCESS, "✔ 2 Photos"),
        ("10/09/2026", "COMP-264", "Garbage Overflow", "Ayush", "Kalyan Sector-3", "Amit Patel (MH-03)", "OPEN", DANGER, "✔ Staged"),
        ("02/09/2026", "COMP-001", "Road Waste Pile", "Aarti", "Bandra West", "Sunil Shinde (MH-01)", "COMPLETED", SUCCESS, "✔ 2 Photos"),
        ("02/09/2026", "COMP-002", "Dustbin Overflow", "Ayush", "Khar West", "Ramesh Kumar (MH-02)", "COMPLETED", SUCCESS, "✔ 2 Photos"),
        ("01/09/2026", "COMP-003", "Commercial Dump", "Ayush", "Kurla West", "Amit Patel (MH-03)", "COMPLETED", SUCCESS, "✔ 2 Photos"),
    ]
    ty = 330
    for dt, tid, cat, rep, ar, drv, st, col, ph in table_rows:
        d.text((85, ty), dt, fill=TEXT_MUTED, font=font_small)
        d.text((180, ty), tid, fill=PRIMARY, font=font_bold)
        d.text((280, ty), cat, fill=TEXT_DARK, font=font_small)
        d.text((450, ty), rep, fill=TEXT_DARK, font=font_small)
        d.text((580, ty), ar, fill=TEXT_MUTED, font=font_small)
        d.text((750, ty), drv, fill=TEXT_DARK, font=font_small)
        d.rounded_rectangle([935, ty - 3, 1030, ty + 17], radius=4, fill=col)
        d.text((945, ty), st, fill=(255, 255, 255), font=font_badge)
        d.text((1060, ty), ph, fill=SUCCESS, font=font_badge)
        d.line([70, ty + 24, W - 70, ty + 24], fill=BORDER_COLOR)
        ty += 34
        
    d.text((85, 655), "Showing 8 of 8 active records • Automatic 30-day rolling purge active • Export format: RFC 4180 CSV", fill=TEXT_MUTED, font=font_small)
    
    img.save(os.path.join(OUT_DIR, "proto_compliance_report.png"))

print("Generating 12 academic prototype mockup images...")
make_proto_1()
make_proto_2()
make_proto_3()
make_proto_4()
make_proto_5()
make_proto_6()
make_proto_7()
make_proto_8()
make_proto_9()
make_proto_10()
make_proto_11()
make_proto_12()
print("All 12 prototype mockup images generated successfully in:", OUT_DIR)
