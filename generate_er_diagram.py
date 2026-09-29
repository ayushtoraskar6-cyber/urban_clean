# -*- coding: utf-8 -*-
"""
Generate a publication-grade academic Entity-Relationship (ER) Diagram:
"Figure 4.8: Entity-Relationship Diagram of UrbanClean"
Saved to: screenshots/report_assets/er_diagram.png
"""

import os
from PIL import Image, ImageDraw, ImageFont

WIDTH = 2200
HEIGHT = 1500

img = Image.new("RGB", (WIDTH, HEIGHT), "#FFFFFF")
draw = ImageDraw.Draw(img)

# Fonts
font_title = ImageFont.truetype("C:/Windows/Fonts/calibri.ttf", 34)
font_subtitle = ImageFont.truetype("C:/Windows/Fonts/calibri.ttf", 20)
font_ent_title = ImageFont.truetype("C:/Windows/Fonts/calibrib.ttf", 22)
font_ent_type = ImageFont.truetype("C:/Windows/Fonts/calibrii.ttf", 15)
font_attr_pk = ImageFont.truetype("C:/Windows/Fonts/consola.ttf", 16)
font_attr_fk = ImageFont.truetype("C:/Windows/Fonts/consola.ttf", 16)
font_attr_reg = ImageFont.truetype("C:/Windows/Fonts/consola.ttf", 15)
font_rel_label = ImageFont.truetype("C:/Windows/Fonts/calibrib.ttf", 16)
font_card = ImageFont.truetype("C:/Windows/Fonts/calibrib.ttf", 18)
font_legend_title = ImageFont.truetype("C:/Windows/Fonts/calibrib.ttf", 18)
font_legend_txt = ImageFont.truetype("C:/Windows/Fonts/calibri.ttf", 15)

# 1. TOP HEADER BANNER
draw.rectangle([(25, 20), (WIDTH - 25, 95)], fill="#F0F4F8", outline="#1F4E79", width=2)
draw.text((45, 28), "UrbanClean™ — Entity-Relationship (ER) Relational Data Model", fill="#113F67", font=font_title)
draw.text((47, 65), "System Modeling Design Specification | Relational SQLite Schema, Dual-Persistence Mapping & Referential Integrity", fill="#4A6572", font=font_subtitle)

# Outer decorative border
draw.rectangle([(25, 110), (WIDTH - 25, HEIGHT - 25)], outline="#B0C4DE", width=2)

# Helper function to draw an entity box
def draw_entity(x, y, w, title, subtitle, attributes, header_bg="#1F4E79"):
    header_h = 52
    row_h = 26
    total_h = header_h + len(attributes) * row_h + 14
    
    # Entity Box Outer Shadow/Border
    draw.rectangle([(x + 3, y + 3), (x + w + 3, y + total_h + 3)], fill="#EAECEE")
    draw.rectangle([(x, y), (x + w, y + total_h)], fill="#FFFFFF", outline="#1F4E79", width=2)
    
    # Header
    draw.rectangle([(x, y), (x + w, y + header_h)], fill=header_bg)
    draw.line([(x, y + header_h), (x + w, y + header_h)], fill="#1F4E79", width=2)
    
    draw.text((x + 16, y + 8), title, fill="#FFFFFF", font=font_ent_title)
    draw.text((x + 16, y + 31), subtitle, fill="#D0E1FD", font=font_ent_type)
    
    # Draw separator line between PK and other attributes if desired, or render each attribute
    cur_y = y + header_h + 8
    for item in attributes:
        prefix, col_name, data_type, is_key = item
        
        # Background highlight for PK / FK
        if is_key == "PK":
            draw.rectangle([(x + 6, cur_y - 2), (x + w - 6, cur_y + row_h - 4)], fill="#FEF9E7")
            badge_color = "#B7950B"
            txt_color = "#7D6608"
            fnt = font_attr_pk
        elif is_key == "FK":
            draw.rectangle([(x + 6, cur_y - 2), (x + w - 6, cur_y + row_h - 4)], fill="#F5EEF8")
            badge_color = "#7D3C98"
            txt_color = "#5B2C6F"
            fnt = font_attr_fk
        else:
            badge_color = "#566573"
            txt_color = "#2C3E50"
            fnt = font_attr_reg
            
        draw.text((x + 14, cur_y), prefix, fill=badge_color, font=fnt)
        draw.text((x + 65, cur_y), col_name, fill=txt_color, font=fnt)
        draw.text((x + w - 145, cur_y), data_type, fill="#7F8C8D", font=font_attr_reg)
        
        cur_y += row_h
        
    return (x, y, w, total_h)

# Helper function to draw relationship diamond
def draw_diamond(cx, cy, rw, rh, label, fill="#EBF5FB", outline="#2E75B6"):
    pts = [(cx, cy - rh), (cx + rw, cy), (cx, cy + rh), (cx - rw, cy)]
    draw.polygon(pts, fill=fill, outline=outline)
    
    # Text in center
    bbox = font_rel_label.getbbox(label)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    draw.text((cx - tw // 2, cy - th // 2 - 2), label, fill="#1B4F72", font=font_rel_label)

# ─────────────────────────────────────────────────────────────────────────────
# ENTITY DEFINITIONS & LAYOUT
# ─────────────────────────────────────────────────────────────────────────────

# 1. ACCOUNT Entity (Top Left)
acc_attrs = [
    ("[PK]", "id", "VARCHAR(50)", "PK"),
    ("    ", "name", "VARCHAR(100)", ""),
    ("    ", "email", "VARCHAR(150)", ""),
    ("    ", "role", "VARCHAR(20)", ""),
    ("    ", "vehicle", "VARCHAR(50)", ""),
    ("    ", "state", "VARCHAR(100)", ""),
    ("    ", "district", "VARCHAR(100)", ""),
    ("    ", "city", "VARCHAR(100)", ""),
    ("    ", "password_hash", "TEXT", ""),
    ("    ", "createdAt", "DATETIME", ""),
]
acc_box = draw_entity(60, 160, 470, "ACCOUNT (accounts)", "User Profile & Identity Store", acc_attrs, header_bg="#1F4E79")

# 2. DRIVER Entity (Top Center-Right)
drv_attrs = [
    ("[PK]", "id", "VARCHAR(50)", "PK"),
    ("    ", "name", "VARCHAR(100)", ""),
    ("    ", "status", "VARCHAR(20)", ""),
    ("    ", "vehicle", "VARCHAR(100)", ""),
    ("    ", "efficiency", "INTEGER", ""),
    ("    ", "distance", "VARCHAR(20)", ""),
    ("    ", "assignedComplaints", "TEXT [JSON]", ""),
]
drv_box = draw_entity(840, 160, 480, "DRIVER (drivers)", "Fleet Operator Roster & Telemetry", drv_attrs, header_bg="#1B4F72")

# 3. NOTIFICATION Entity (Far Right)
notif_attrs = [
    ("[PK]", "id", "VARCHAR(20)", "PK"),
    ("    ", "type", "VARCHAR(20)", ""),
    ("    ", "message", "TEXT", ""),
    ("    ", "timeStr", "VARCHAR(50)", ""),
]
notif_box = draw_entity(1620, 160, 490, "NOTIFICATION (notifications)", "System Alerts & Audit Broadcasts", notif_attrs, header_bg="#283747")

# 4. COMPLAINT Entity (Bottom Left/Center)
comp_attrs = [
    ("[PK]", "id", "VARCHAR(20)", "PK"),
    ("[FK]", "reportedBy (userId)", "VARCHAR(50)", "FK"),
    ("[FK]", "assignedDriverId", "VARCHAR(50)", "FK"),
    ("    ", "category", "VARCHAR(50)", ""),
    ("    ", "title", "VARCHAR(255)", ""),
    ("    ", "description", "TEXT", ""),
    ("    ", "lat", "FLOAT (WGS84)", ""),
    ("    ", "lng", "FLOAT (WGS84)", ""),
    ("    ", "area", "VARCHAR(100)", ""),
    ("    ", "city", "VARCHAR(100)", ""),
    ("    ", "status", "VARCHAR(50)", ""),
    ("    ", "photo_before", "TEXT [PATH]", ""),
    ("    ", "photo_after", "TEXT [PATH]", ""),
    ("    ", "timestamp", "BIGINT", ""),
]
comp_box = draw_entity(180, 720, 520, "COMPLAINT (complaints)", "Civic Waste Reporting Ticket Store", comp_attrs, header_bg="#114B5F")

# 5. DRIVER_ROUTE Entity (Bottom Right)
route_attrs = [
    ("[PK]", "id", "INTEGER (AUTO)", "PK"),
    ("[FK]", "driverId", "VARCHAR(50)", "FK"),
    ("    ", "pointIndex", "INTEGER", ""),
    ("    ", "label", "VARCHAR(100)", ""),
    ("    ", "lat", "FLOAT (WGS84)", ""),
    ("    ", "lng", "FLOAT (WGS84)", ""),
    ("    ", "savedAt", "DATETIME", ""),
]
route_box = draw_entity(1040, 720, 480, "DRIVER_ROUTE (driver_routes)", "Geospatial TSP Stops & Waypoints", route_attrs, header_bg="#1A5276")

# ─────────────────────────────────────────────────────────────────────────────
# RELATIONSHIP CONNECTORS & DIAMONDS
# ─────────────────────────────────────────────────────────────────────────────

# Relationship 1: ACCOUNT (1) ---- [Submits] ---- (N) COMPLAINT
# Vertical connection from bottom of ACCOUNT (x=295, y=490) to top of COMPLAINT (x=300, y=720)
rel1_diamond_y = 590
draw.line([(295, 490), (295, rel1_diamond_y - 28)], fill="#2E75B6", width=2)
draw_diamond(295, rel1_diamond_y, 80, 28, "Submits / Files")
draw.line([(295, rel1_diamond_y + 28), (295, 720)], fill="#2E75B6", width=2)

# Cardinality 1 at ACCOUNT end, N at COMPLAINT end
draw.text((310, 505), "1", fill="#1F4E79", font=font_card)
draw.text((310, 685), "N", fill="#1F4E79", font=font_card)
draw.text((200, 545), "FK: reportedBy", fill="#7D3C98", font=font_attr_fk)

# Relationship 2: DRIVER (1) ---- [Assigned / Cleans] ---- (N) COMPLAINT
# Line from bottom-left of DRIVER (x=920, y=410) down to top-right of COMPLAINT (x=580, y=720)
rel2_x, rel2_y = 750, 570
draw.line([(920, 410), (920, 570)], fill="#2E75B6", width=2)
draw.line([(920, 570), (rel2_x + 95, 570)], fill="#2E75B6", width=2)
draw_diamond(rel2_x, rel2_y, 95, 28, "Assigned / Cleans")
draw.line([(rel2_x - 95, 570), (580, 570)], fill="#2E75B6", width=2)
draw.line([(580, 570), (580, 720)], fill="#2E75B6", width=2)

draw.text((930, 425), "1", fill="#1F4E79", font=font_card)
draw.text((595, 685), "N", fill="#1F4E79", font=font_card)
draw.text((615, 620), "FK: assignedDriverId", fill="#7D3C98", font=font_attr_fk)

# Relationship 3: DRIVER (1) ---- [Navigates / Plans] ---- (N) DRIVER_ROUTE
# Line from bottom-right of DRIVER (x=1150, y=410) down to top of DRIVER_ROUTE (x=1240, y=720)
rel3_y = 560
draw.line([(1180, 410), (1180, rel3_y - 28)], fill="#2E75B6", width=2)
draw_diamond(1180, rel3_y, 90, 28, "Plans / Navigates")
draw.line([(1180, rel3_y + 28), (1180, 720)], fill="#2E75B6", width=2)

draw.text((1195, 425), "1", fill="#1F4E79", font=font_card)
draw.text((1195, 685), "N", fill="#1F4E79", font=font_card)
draw.text((1200, 605), "FK: driverId", fill="#7D3C98", font=font_attr_fk)

# Relationship 4: ACCOUNT (1) ---- [Operates As] ---- (1) DRIVER
# Horizontal connection between ACCOUNT (x=530, y=280) and DRIVER (x=840, y=280)
rel4_x = 685
rel4_y = 280
draw.line([(530, rel4_y), (rel4_x - 75, rel4_y)], fill="#2E75B6", width=2)
draw_diamond(rel4_x, rel4_y, 75, 26, "Operates As")
draw.line([(rel4_x + 75, rel4_y), (840, rel4_y)], fill="#2E75B6", width=2)

draw.text((545, 255), "1", fill="#1F4E79", font=font_card)
draw.text((815, 255), "1", fill="#1F4E79", font=font_card)
draw.text((620, 235), "Role = 'driver'", fill="#1E8449", font=font_ent_type)

# Relationship 5: ACCOUNT (1) ---- [Broadcasts / Logs] ---- (N) NOTIFICATION
# Line connecting ACCOUNT / System to NOTIFICATION
rel5_x = 1470
rel5_y = 260
draw.line([(1320, 260), (rel5_x - 85, 260)], fill="#7F8C8D", width=2, joint="curve")
draw_diamond(rel5_x, rel5_y, 85, 26, "Receives / Logs", fill="#F2F4F4", outline="#7F8C8D")
draw.line([(rel5_x + 85, 260), (1620, 260)], fill="#7F8C8D", width=2)

draw.text((1335, 235), "1", fill="#566573", font=font_card)
draw.text((1595, 235), "N", fill="#566573", font=font_card)

# ─────────────────────────────────────────────────────────────────────────────
# LEGEND & ARCHITECTURAL SUMMARY BOX (Bottom Right)
# ─────────────────────────────────────────────────────────────────────────────
leg_x, leg_y, leg_w, leg_h = 1620, 720, 490, 480
draw.rectangle([(leg_x + 3, leg_y + 3), (leg_x + leg_w + 3, leg_y + leg_h + 3)], fill="#EAECEE")
draw.rectangle([(leg_x, leg_y), (leg_x + leg_w, leg_y + leg_h)], fill="#FDFEFE", outline="#2C3E50", width=2)

# Legend Header
draw.rectangle([(leg_x, leg_y), (leg_x + leg_w, leg_y + 44)], fill="#2C3E50")
draw.text((leg_x + 16, leg_y + 12), "ER MODEL NOTATION & KEY SPECIFICATION", fill="#FFFFFF", font=font_legend_title)

cur_ly = leg_y + 60

# Legend items
legend_items = [
    ("[PK]", "Primary Key (Unique entity identifier, Indexed)", "#B7950B", "#FEF9E7"),
    ("[FK]", "Foreign Key (Maintains Referential Integrity)", "#7D3C98", "#F5EEF8"),
    ("1 : N", "One-to-Many Cardinality Relationship", "#1F4E79", "#EBF5FB"),
    ("1 : 1", "One-to-One Specialization / Profile Link", "#1E8449", "#EAFAF1"),
]

for tag, desc, fg, bg in legend_items:
    draw.rectangle([(leg_x + 16, cur_ly), (leg_x + 80, cur_ly + 28)], fill=bg, outline=fg, width=1)
    draw.text((leg_x + 22, cur_ly + 5), tag, fill=fg, font=font_ent_title)
    draw.text((leg_x + 95, cur_ly + 5), desc, fill="#2C3E50", font=font_legend_txt)
    cur_ly += 42

cur_ly += 10
draw.line([(leg_x + 16, cur_ly), (leg_x + leg_w - 16, cur_ly)], fill="#BDC3C7", width=1)
cur_ly += 14

draw.text((leg_x + 16, cur_ly), "RELATIONAL INTEGRITY RULES:", fill="#1B4F72", font=font_ent_title)
cur_ly += 26

rules = [
    "• ON DELETE CASCADE: When driver removed, routes deleted.",
    "• ACCOUNT SEGREGATION: Role attribute enforces RBAC.",
    "• GEOSPATIAL STORAGE: WGS84 decimal coords (lat, lng).",
    "• DUAL PERSISTENCE: Synchronous write to db.json mirror.",
    "• PROOF STORAGE: photo_before and photo_after URLs.",
    "• HISTORICAL LOGS: Notifications maintain audit trails.",
]

for r in rules:
    draw.text((leg_x + 16, cur_ly), r, fill="#34495E", font=font_legend_txt)
    cur_ly += 25

# Save image
out_dir = r"d:\Urban clean\screenshots\report_assets"
os.makedirs(out_dir, exist_ok=True)
out_path = os.path.join(out_dir, "er_diagram.png")
img.save(out_path, dpi=(300, 300))
print(f"[SUCCESS] ER Diagram saved to: {out_path}")
print(f"Dimensions: {img.size}")
