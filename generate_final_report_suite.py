# -*- coding: utf-8 -*-
"""
UrbanClean Master Academic Project Report Generator
Compiles the authoritative, syllabus-compliant 10-chapter academic project report:
- Times New Roman throughout
- 16pt Chapter titles, 14pt Headings, 13pt Subheadings, 12pt Body text
- Page 1 starting at Chapter 1, Bottom Center
- Embedded 35 figures with captions
- Perfect right-aligned Table of Contents, List of Figures, and List of Tables with dot leaders
- Converts cleanly to UrbanClean_Final_Project_Report.pdf via docx2pdf
"""

import os
import re
import sys
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_TAB_ALIGNMENT, WD_TAB_LEADER
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn

sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(r'd:\Urban clean\report_chapters')
import prelim, ch1_ch2, ch3_ch4, ch5_ch6, ch7_ch8, ch9_ch10
import formatted_lists

WORKSPACE_DIR = r"d:\Urban clean"
REPORT_ASSETS = os.path.join(WORKSPACE_DIR, "screenshots", "report_assets")
EVIDENCE_ASSETS = os.path.join(WORKSPACE_DIR, "screenshots", "evidence")
LOGO_PATH = os.path.join(WORKSPACE_DIR, "college_logo.jpg")
GANTT_PATH = os.path.join(WORKSPACE_DIR, "gantt_chart.png")

# All 35 image mappings
IMAGE_MAP = {
    "COLLEGE_LOGO": LOGO_PATH,
    "FIG_3_1": GANTT_PATH,
    "FIG_4_1": os.path.join(REPORT_ASSETS, "uml_diagram_p1.png"),
    "FIG_4_2": os.path.join(REPORT_ASSETS, "uml_diagram_p2.png"),
    "FIG_4_3": os.path.join(REPORT_ASSETS, "uml_diagram_p3.png"),
    "FIG_4_4": os.path.join(REPORT_ASSETS, "uml_diagram_p4.png"),
    "FIG_4_5": os.path.join(REPORT_ASSETS, "uml_diagram_p5.png"),
    "FIG_4_6": os.path.join(REPORT_ASSETS, "uml_diagram_p6.png"),
    "FIG_4_7": os.path.join(REPORT_ASSETS, "uml_diagram_p7.png"),
    "FIG_4_8": os.path.join(REPORT_ASSETS, "uml_diagram_p8.png"),
    "FIG_5_1": os.path.join(REPORT_ASSETS, "uml_diagram_p7.png"), # Deployment / Layered Arch
    "FIG_5_2": os.path.join(REPORT_ASSETS, "db_screenshot_p1.png"),
    "FIG_5_3": os.path.join(REPORT_ASSETS, "db_screenshot_p2.png"),
    "FIG_5_4": os.path.join(REPORT_ASSETS, "db_screenshot_p3.png"),
    "FIG_5_5": os.path.join(REPORT_ASSETS, "proto_landing.png"),
    "FIG_5_6": os.path.join(REPORT_ASSETS, "proto_login.png"),
    "FIG_5_7": os.path.join(REPORT_ASSETS, "proto_registration.png"),
    "FIG_5_8": os.path.join(REPORT_ASSETS, "proto_complaint_form.png"),
    "FIG_5_9": os.path.join(REPORT_ASSETS, "proto_map_selection.png"),
    "FIG_5_10": os.path.join(REPORT_ASSETS, "proto_complaint_tracking.png"),
    "FIG_5_11": os.path.join(REPORT_ASSETS, "proto_driver_dashboard.png"),
    "FIG_5_12": os.path.join(REPORT_ASSETS, "proto_driver_route.png"),
    "FIG_5_13": os.path.join(REPORT_ASSETS, "proto_proof_upload.png"),
    "FIG_5_14": os.path.join(REPORT_ASSETS, "proto_admin_dashboard.png"),
    "FIG_5_15": os.path.join(REPORT_ASSETS, "proto_monitoring_map.png"),
    "FIG_5_16": os.path.join(REPORT_ASSETS, "proto_compliance_report.png"),
    "FIG_6_1": os.path.join(REPORT_ASSETS, "app_screenshot_p1.png"),
    "FIG_6_2": os.path.join(REPORT_ASSETS, "app_screenshot_p2.png"),
    "FIG_6_3": os.path.join(REPORT_ASSETS, "app_screenshot_p3.png"),
    "FIG_6_4": os.path.join(REPORT_ASSETS, "app_screenshot_p4.png"),
    "FIG_6_5": os.path.join(REPORT_ASSETS, "app_screenshot_p5.png"),
    "FIG_6_6": os.path.join(REPORT_ASSETS, "app_screenshot_p6.png"),
    "FIG_6_7": os.path.join(REPORT_ASSETS, "app_screenshot_p7.png"),
    "FIG_7_1": os.path.join(EVIDENCE_ASSETS, "S23.png"),
    "FIG_7_2": os.path.join(EVIDENCE_ASSETS, "S24.png"),
    "FIG_7_3": os.path.join(EVIDENCE_ASSETS, "S25.png"),
    "FIG_8_1": os.path.join(EVIDENCE_ASSETS, "S44.png"),
    "FIG_8_2": os.path.join(EVIDENCE_ASSETS, "S45.png"),
    "FIG_8_3": os.path.join(EVIDENCE_ASSETS, "S46.png"),
    "FIG_8_4": os.path.join(EVIDENCE_ASSETS, "S47.png"),
    "FIG_9_1": os.path.join(EVIDENCE_ASSETS, "S37.png"),
    "FIG_9_2": os.path.join(EVIDENCE_ASSETS, "S38.png"),
    "FIG_9_3": os.path.join(EVIDENCE_ASSETS, "S39.png"),
    "FIG_9_4": os.path.join(EVIDENCE_ASSETS, "S36.png"),
    "FIG_9_5": os.path.join(EVIDENCE_ASSETS, "S30.png"),
    "FIG_9_6": os.path.join(EVIDENCE_ASSETS, "S32.png"),
    "FIG_9_7": os.path.join(EVIDENCE_ASSETS, "S40.png"),
    "FIG_9_8": os.path.join(EVIDENCE_ASSETS, "S41.png"),
}

def xml_safe(text):
    if not text:
        return ""
    text = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    return text.replace('"', "&quot;").replace("'", "&apos;")

def set_cell_background(cell, fill_hex):
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    cell._tc.get_or_add_tcPr().append(shd)

def set_table_borders(table):
    tblPr = table._tbl.tblPr
    borders = parse_xml(
        f'<w:tblBorders {nsdecls("w")}>\n'
        f'  <w:top w:val="single" w:sz="6" w:space="0" w:color="B0C4DE"/>\n'
        f'  <w:left w:val="none" w:sz="0" w:space="0" w:color="auto"/>\n'
        f'  <w:bottom w:val="single" w:sz="6" w:space="0" w:color="B0C4DE"/>\n'
        f'  <w:right w:val="none" w:sz="0" w:space="0" w:color="auto"/>\n'
        f'  <w:insideH w:val="single" w:sz="4" w:space="0" w:color="E0E6ED"/>\n'
        f'  <w:insideV w:val="none" w:sz="0" w:space="0" w:color="auto"/>\n'
        f'</w:tblBorders>'
    )
    tblPr.append(borders)

doc = Document()

# Default styles
style_normal = doc.styles['Normal']
style_normal.font.name = 'Times New Roman'
style_normal.font.size = Pt(12)
style_normal.font.color.rgb = RGBColor(0x22, 0x22, 0x22)

# ══════════════════════════════════════════════════════════════════════════════
# SECTION 1: TITLE / COVER PAGE
# ══════════════════════════════════════════════════════════════════════════════
s1 = doc.sections[0]
s1.top_margin = Inches(0.8)
s1.bottom_margin = Inches(0.8)
s1.left_margin = Inches(0.8)
s1.right_margin = Inches(0.8)

s1._sectPr.append(parse_xml(
    f'<w:pgBorders {nsdecls("w")} w:offsetFrom="page">\n'
    f'  <w:top w:val="double" w:sz="24" w:space="24" w:color="1F4E79"/>\n'
    f'  <w:left w:val="double" w:sz="24" w:space="24" w:color="1F4E79"/>\n'
    f'  <w:bottom w:val="double" w:sz="24" w:space="24" w:color="1F4E79"/>\n'
    f'  <w:right w:val="double" w:sz="24" w:space="24" w:color="1F4E79"/>\n'
    f'</w:pgBorders>'
))

def add_title_p(text, font_size=12, bold=False, italic=False, color=RGBColor(0,0,0),
                space_before=0, space_after=4, alignment=WD_ALIGN_PARAGRAPH.CENTER):
    p = doc.add_paragraph()
    p.alignment = alignment
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.space_after = Pt(space_after)
    run = p.add_run(text)
    run.font.name = "Times New Roman"
    run.font.size = Pt(font_size)
    run.font.bold = bold
    run.font.italic = italic
    run.font.color.rgb = color
    return p

add_title_p("A PROJECT REPORT", font_size=18, bold=True, color=RGBColor(0x0F, 0x2C, 0x59), space_before=14, space_after=4)
add_title_p("On", font_size=13, italic=True, space_after=6)
add_title_p("UrbanClean: Geospatial Smart City Waste Management &\nRoute Optimization System",
            font_size=17, bold=True, color=RGBColor(0xC0, 0x00, 0x00), space_after=14)
add_title_p("Submitted by", font_size=12, italic=True, space_after=4)
add_title_p("Mr. AYUSH SANTOSH TORASKAR", font_size=14, bold=True, color=RGBColor(0x1F, 0x4E, 0x79), space_after=2)
add_title_p("(Roll No. CS-9147 | Class: TY B.Sc. CS / II)", font_size=11, bold=True, space_after=12)

add_title_p("in partial fulfillment for the award of the degree of", font_size=11, italic=True, space_after=3)
add_title_p("BACHELOR OF SCIENCE", font_size=14, bold=True, color=RGBColor(0x0F, 0x2C, 0x59), space_after=2)
add_title_p("in", font_size=11, italic=True, space_after=2)
add_title_p("COMPUTER SCIENCE", font_size=14, bold=True, color=RGBColor(0x0F, 0x2C, 0x59), space_after=12)

add_title_p("under the guidance of", font_size=11, italic=True, space_after=3)
add_title_p("PROF. AARTI GAWAI", font_size=13, bold=True, color=RGBColor(0xC0, 0x00, 0x00), space_after=2)
add_title_p("Department of Computer Science", font_size=12, space_after=12)

if os.path.exists(LOGO_PATH):
    p_logo = doc.add_paragraph()
    p_logo.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_logo.paragraph_format.space_before = Pt(4)
    p_logo.paragraph_format.space_after = Pt(8)
    p_logo.add_run().add_picture(LOGO_PATH, width=Inches(1.5))

add_title_p("Modern Education Society's", font_size=13, bold=True, color=RGBColor(0x0F, 0x2C, 0x59), space_after=2)
add_title_p("The D. G. Ruparel College of Arts, Science & Commerce", font_size=14, bold=True, color=RGBColor(0x0F, 0x2C, 0x59), space_after=2)
add_title_p("(Sem - V)", font_size=12, bold=True, space_after=2)
add_title_p("(2026 – 2027)", font_size=12, bold=True, space_after=4)

# ══════════════════════════════════════════════════════════════════════════════
# SECTION 2: CERTIFICATE PAGE
# ══════════════════════════════════════════════════════════════════════════════
s2 = doc.add_section()
s2.top_margin = Inches(0.8)
s2.bottom_margin = Inches(0.8)
s2.left_margin = Inches(0.8)
s2.right_margin = Inches(0.8)

s2._sectPr.append(parse_xml(
    f'<w:pgBorders {nsdecls("w")} w:offsetFrom="page">\n'
    f'  <w:top w:val="double" w:sz="24" w:space="24" w:color="1F4E79"/>\n'
    f'  <w:left w:val="double" w:sz="24" w:space="24" w:color="1F4E79"/>\n'
    f'  <w:bottom w:val="double" w:sz="24" w:space="24" w:color="1F4E79"/>\n'
    f'  <w:right w:val="double" w:sz="24" w:space="24" w:color="1F4E79"/>\n'
    f'</w:pgBorders>'
))

if os.path.exists(LOGO_PATH):
    p_logo2 = doc.add_paragraph()
    p_logo2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_logo2.paragraph_format.space_before = Pt(8)
    p_logo2.paragraph_format.space_after = Pt(4)
    p_logo2.add_run().add_picture(LOGO_PATH, width=Inches(1.2))

add_title_p("Modern Education Society's", font_size=13, bold=True, color=RGBColor(0x0F, 0x2C, 0x59), space_after=2)
add_title_p("The D. G. Ruparel College of Arts, Science & Commerce,", font_size=14, bold=True, color=RGBColor(0x0F, 0x2C, 0x59), space_after=2)
add_title_p("senapati bapat marg, opp. Matunga road station (w.r.), mahim, mumbai 400 016", font_size=10, italic=True, space_after=4)
add_title_p("Department of Computer Science", font_size=13, bold=True, color=RGBColor(0x1F, 0x4E, 0x79), space_after=14)

add_title_p("CERTIFICATE", font_size=18, bold=True, color=RGBColor(0x0F, 0x2C, 0x59), space_after=18)

p_cert = doc.add_paragraph()
p_cert.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
p_cert.paragraph_format.line_spacing = 1.3
p_cert.paragraph_format.space_after = Pt(14)

def add_cert_run(text, bold=False, italic=False, color=RGBColor(0,0,0), underline=False):
    run = p_cert.add_run(text)
    run.font.name = "Times New Roman"
    run.font.size = Pt(11.5)
    run.font.bold = bold
    run.font.italic = italic
    run.font.underline = underline
    run.font.color.rgb = color

add_cert_run("This is to certify that Mr./Ms.  ")
add_cert_run("Mr. TORASKAR AYUSH SANTOSH", bold=True, color=RGBColor(0xC0, 0x00, 0x00), underline=True)
add_cert_run("\n\nSeat no: ________________ of ")
add_cert_run("T.Y.B.Sc. (Sem V)", bold=True)
add_cert_run(" class has satisfactorily completed the project report entitled ")
add_cert_run("UrbanClean: Geospatial Smart City Waste Management & Route Optimization System", bold=True, color=RGBColor(0xC0, 0x00, 0x00))
add_cert_run(" , to be submitted in the partial fulfillment for the award of ")
add_cert_run("Bachelor of Science in Computer Science", bold=True)
add_cert_run(" during the academic year ")
add_cert_run("2026 – 2027.", bold=True)

p_date = doc.add_paragraph()
p_date.paragraph_format.space_before = Pt(20)
p_date.paragraph_format.space_after = Pt(24)
r_date = p_date.add_run("Date of Submission: ____________________")
r_date.font.name = "Times New Roman"
r_date.font.size = Pt(11.5)
r_date.font.bold = True

tbl_sig = doc.add_table(rows=2, cols=2)
tbl_sig.alignment = WD_TABLE_ALIGNMENT.CENTER
tbl_sig.autofit = False
for row in tbl_sig.rows:
    for cell in row.cells:
        cell.width = Inches(3.2)

c00 = tbl_sig.cell(0, 0).paragraphs[0]
c00.paragraph_format.space_after = Pt(40)
r00 = c00.add_run("_________________________\nProject Guide\n(Prof. Aarti Gawai)")
r00.font.name = "Times New Roman"
r00.font.size = Pt(11)
r00.font.bold = True

c01 = tbl_sig.cell(0, 1).paragraphs[0]
c01.alignment = WD_ALIGN_PARAGRAPH.RIGHT
c01.paragraph_format.space_after = Pt(40)
r01 = c01.add_run("_________________________\nHead / Incharge,\nDepartment Computer Science")
r01.font.name = "Times New Roman"
r01.font.size = Pt(11)
r01.font.bold = True

c10 = tbl_sig.cell(1, 0).paragraphs[0]
r10 = c10.add_run("_________________________\nCollege Seal")
r10.font.name = "Times New Roman"
r10.font.size = Pt(11)
r10.font.bold = True

c11 = tbl_sig.cell(1, 1).paragraphs[0]
c11.alignment = WD_ALIGN_PARAGRAPH.RIGHT
r11 = c11.add_run("_________________________\nSignature of Examiner")
r11.font.name = "Times New Roman"
r11.font.size = Pt(11)
r11.font.bold = True

# ══════════════════════════════════════════════════════════════════════════════
# SECTION 3: PRELIMINARY SECTION
# ══════════════════════════════════════════════════════════════════════════════
s3 = doc.add_section()
s3.top_margin = Inches(1.0)
s3.bottom_margin = Inches(1.0)
s3.left_margin = Inches(1.0)
s3.right_margin = Inches(1.0)

s3._sectPr.append(parse_xml(
    f'<w:pgBorders {nsdecls("w")} w:offsetFrom="page">\n'
    f'  <w:top w:val="none"/>\n'
    f'  <w:left w:val="none"/>\n'
    f'  <w:bottom w:val="none"/>\n'
    f'  <w:right w:val="none"/>\n'
    f'</w:pgBorders>'
))

# Parser helper function for markdown sections
def render_markdown_section(doc_target, text_content):
    lines = text_content.split('\n')
    i = 0
    in_code_block = False
    code_lines = []
    table_lines = []

    def process_table(tbl_lines):
        if len(tbl_lines) < 2:
            return
        rows_data = []
        for line in tbl_lines:
            cells = [c.strip() for c in line.split('|')[1:-1]]
            if cells and not all(re.match(r'^:?-+:?$', c) for c in cells):
                rows_data.append(cells)
        if not rows_data:
            return
        num_cols = max(len(r) for r in rows_data)
        tbl = doc_target.add_table(rows=len(rows_data), cols=num_cols)
        tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
        tbl.autofit = True
        set_table_borders(tbl)

        for r_idx, row in enumerate(rows_data):
            for c_idx, cell_value in enumerate(row):
                if c_idx < num_cols:
                    cell = tbl.cell(r_idx, c_idx)
                    cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
                    p = cell.paragraphs[0]
                    p.paragraph_format.space_before = Pt(3)
                    p.paragraph_format.space_after = Pt(3)
                    p.paragraph_format.line_spacing = 1.05
                    clean_val = xml_safe(cell_value.replace('**', '').replace('`', ''))
                    run = p.add_run(clean_val)
                    run.font.name = 'Times New Roman'
                    if r_idx == 0:
                        set_cell_background(cell, "1F4E79")
                        run.font.size = Pt(9.5)
                        run.font.bold = True
                        run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
                    else:
                        if r_idx % 2 == 1:
                            set_cell_background(cell, "F9FBFD")
                        else:
                            set_cell_background(cell, "FFFFFF")
                        run.font.size = Pt(9)
                        run.font.color.rgb = RGBColor(0x33, 0x33, 0x33)

        p_space = doc_target.add_paragraph()
        p_space.paragraph_format.space_after = Pt(6)

    while i < len(lines):
        line = lines[i]

        # Check for image insertion markers
        matched_image = None

        if "[INSERT FIGURE HERE:" in line:
            m = re.search(r'\[INSERT FIGURE HERE:\s*([^\]]+)\]', line)
            if m:
                fig_tag = m.group(1).strip()
                num_m = re.search(r'Figure\s*(\d+\.\d+)', fig_tag, re.IGNORECASE)
                if num_m:
                    ch_num, fig_num = num_m.group(1).split('.')
                    img_key = f"FIG_{ch_num}_{fig_num}"
                    if img_key in IMAGE_MAP:
                        matched_image = IMAGE_MAP[img_key]

        if matched_image and os.path.exists(matched_image):
            p_img = doc_target.add_paragraph()
            p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_img.paragraph_format.space_before = Pt(8)
            p_img.paragraph_format.space_after = Pt(4)
            p_img.add_run().add_picture(matched_image, width=Inches(6.2))

            # Look ahead for caption
            if i + 1 < len(lines) and (lines[i+1].strip().startswith('*Figure') or lines[i+1].strip().startswith('_Figure')):
                caption_line = lines[i+1].strip().strip('*_')
                p_cap = doc_target.add_paragraph()
                p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
                p_cap.paragraph_format.space_before = Pt(2)
                p_cap.paragraph_format.space_after = Pt(8)
                r_cap = p_cap.add_run(caption_line)
                r_cap.font.name = "Times New Roman"
                r_cap.font.size = Pt(10.5)
                r_cap.font.bold = True
                r_cap.font.italic = True
                r_cap.font.color.rgb = RGBColor(0x1F, 0x4E, 0x79)
                i += 2
                continue
            i += 1
            continue

        # Code block handling
        if line.strip().startswith('```') or line.strip().startswith('===='):
            if in_code_block:
                in_code_block = False
                code_text = xml_safe("\n".join(code_lines))
                code_lines = []
                p = doc_target.add_paragraph()
                p.paragraph_format.left_indent = Inches(0.2)
                p.paragraph_format.right_indent = Inches(0.2)
                p.paragraph_format.space_before = Pt(4)
                p.paragraph_format.space_after = Pt(6)
                run = p.add_run(code_text)
                run.font.name = 'Consolas'
                run.font.size = Pt(8.5)
                run.font.color.rgb = RGBColor(0x1F, 0x29, 0x37)
            else:
                in_code_block = True
                code_lines = []
            i += 1
            continue

        if in_code_block:
            code_lines.append(line)
            i += 1
            continue

        # Table block handling
        if line.strip().startswith('|') and '|' in line:
            table_lines.append(line)
            i += 1
            continue
        else:
            if table_lines:
                process_table(table_lines)
                table_lines = []

        # Headings
        stripped = line.strip()
        if stripped.startswith('# '):
            p = doc_target.add_paragraph()
            p.paragraph_format.space_before = Pt(18)
            p.paragraph_format.space_after = Pt(8)
            run = p.add_run(xml_safe(stripped[2:]))
            run.font.name = 'Times New Roman'
            run.font.size = Pt(16)
            run.font.bold = True
            run.font.color.rgb = RGBColor(0x11, 0x3F, 0x67)
        elif stripped.startswith('## '):
            p = doc_target.add_paragraph()
            p.paragraph_format.space_before = Pt(14)
            p.paragraph_format.space_after = Pt(6)
            run = p.add_run(xml_safe(stripped[3:]))
            run.font.name = 'Times New Roman'
            run.font.size = Pt(14)
            run.font.bold = True
            run.font.color.rgb = RGBColor(0x1F, 0x4E, 0x79)
        elif stripped.startswith('### '):
            p = doc_target.add_paragraph()
            p.paragraph_format.space_before = Pt(10)
            p.paragraph_format.space_after = Pt(4)
            run = p.add_run(xml_safe(stripped[4:]))
            run.font.name = 'Times New Roman'
            run.font.size = Pt(13)
            run.font.bold = True
            run.font.color.rgb = RGBColor(0x2E, 0x75, 0xB6)
        elif stripped.startswith('#### '):
            p = doc_target.add_paragraph()
            p.paragraph_format.space_before = Pt(8)
            p.paragraph_format.space_after = Pt(2)
            run = p.add_run(xml_safe(stripped[5:]))
            run.font.name = 'Times New Roman'
            run.font.size = Pt(12)
            run.font.bold = True
            run.font.color.rgb = RGBColor(0x33, 0x33, 0x33)
        elif stripped.startswith('- ') or stripped.startswith('* '):
            p = doc_target.add_paragraph(style='List Bullet')
            p.paragraph_format.space_after = Pt(2)
            p.paragraph_format.line_spacing = 1.15
            clean_text = xml_safe(stripped[2:].replace('**', ''))
            run = p.add_run(clean_text)
            run.font.name = 'Times New Roman'
            run.font.size = Pt(12)
        elif re.match(r'^\d+\.\s', stripped):
            p = doc_target.add_paragraph(style='List Number')
            p.paragraph_format.space_after = Pt(2)
            p.paragraph_format.line_spacing = 1.15
            clean_text = xml_safe(re.sub(r'^\d+\.\s', '', stripped).replace('**', ''))
            run = p.add_run(clean_text)
            run.font.name = 'Times New Roman'
            run.font.size = Pt(12)
        elif stripped == '---':
            pass
        elif stripped == '<br>' or stripped == '<br><br>':
            p = doc_target.add_paragraph()
            p.paragraph_format.space_after = Pt(4)
        elif stripped:
            p = doc_target.add_paragraph()
            p.paragraph_format.space_after = Pt(4)
            p.paragraph_format.line_spacing = 1.15
            clean_text = xml_safe(stripped.replace('**', '').replace('`', ''))
            run = p.add_run(clean_text)
            run.font.name = 'Times New Roman'
            run.font.size = Pt(12)
            run.font.color.rgb = RGBColor(0x22, 0x22, 0x22)

        i += 1

    if table_lines:
        process_table(table_lines)

# Split prelim text to render Declaration, Ack, Abstract first
prelim_full = prelim.PRELIM_TEXT
idx_toc = prelim_full.find('## TABLE OF CONTENTS / INDEX')
idx_abbrev = prelim_full.find('## LIST OF ABBREVIATIONS')

prelim_head = prelim_full[:idx_toc]
abbrev_text = prelim_full[idx_abbrev:]

print("Rendering Preliminary Header (Declaration, Acknowledgement, Abstract)...")
render_markdown_section(doc, prelim_head)

# ══════════════════════════════════════════════════════════════════════════════
# FORMATTED SECTION: TABLE OF CONTENTS (Right-Aligned Tab Stops with Dot Leaders)
# ══════════════════════════════════════════════════════════════════════════════
print("Rendering Formatted Table of Contents with Right-Aligned Dot Leaders...")
p_toc_head = doc.add_paragraph()
p_toc_head.paragraph_format.space_before = Pt(16)
p_toc_head.paragraph_format.space_after = Pt(8)
r_th = p_toc_head.add_run("TABLE OF CONTENTS / INDEX")
r_th.font.name = "Times New Roman"
r_th.font.size = Pt(14)
r_th.font.bold = True
r_th.font.color.rgb = RGBColor(0x1F, 0x4E, 0x79)

for level, title, page_str in formatted_lists.TOC_ITEMS:
    p = doc.add_paragraph()
    p.paragraph_format.tab_stops.add_tab_stop(Inches(6.5), WD_TAB_ALIGNMENT.RIGHT, WD_TAB_LEADER.DOTS)
    p.paragraph_format.left_indent = Inches(0.0 if level == 0 else 0.25 if level == 1 else 0.45)
    p.paragraph_format.space_before = Pt(2.5 if level == 0 else 1.0)
    p.paragraph_format.space_after = Pt(1.5)
    p.paragraph_format.line_spacing = 1.15

    r_txt = p.add_run(title)
    r_txt.font.name = "Times New Roman"
    r_txt.font.size = Pt(11.5 if level == 0 else 11.0 if level == 1 else 10.5)
    r_txt.font.bold = (level == 0)
    if level == 0:
        r_txt.font.color.rgb = RGBColor(0x11, 0x3F, 0x67)

    r_tab = p.add_run("\t")
    r_tab.font.name = "Times New Roman"

    r_page = p.add_run(page_str)
    r_page.font.name = "Times New Roman"
    r_page.font.size = Pt(11.5 if level == 0 else 11.0 if level == 1 else 10.5)
    r_page.font.bold = (level == 0)
    if level == 0:
        r_page.font.color.rgb = RGBColor(0x11, 0x3F, 0x67)

# ══════════════════════════════════════════════════════════════════════════════
# FORMATTED SECTION: LIST OF FIGURES (Right-Aligned Tab Stops with Dot Leaders)
# ══════════════════════════════════════════════════════════════════════════════
print("Rendering Formatted List of Figures with Right-Aligned Dot Leaders...")
p_fig_head = doc.add_paragraph()
p_fig_head.paragraph_format.space_before = Pt(18)
p_fig_head.paragraph_format.space_after = Pt(8)
r_fh = p_fig_head.add_run("LIST OF FIGURES")
r_fh.font.name = "Times New Roman"
r_fh.font.size = Pt(14)
r_fh.font.bold = True
r_fh.font.color.rgb = RGBColor(0x1F, 0x4E, 0x79)

for fig_title, fig_page in formatted_lists.FIGURE_ITEMS:
    p = doc.add_paragraph()
    p.paragraph_format.tab_stops.add_tab_stop(Inches(6.5), WD_TAB_ALIGNMENT.RIGHT, WD_TAB_LEADER.DOTS)
    p.paragraph_format.left_indent = Inches(0.0)
    p.paragraph_format.space_before = Pt(1.5)
    p.paragraph_format.space_after = Pt(1.5)
    p.paragraph_format.line_spacing = 1.15

    r_txt = p.add_run(fig_title)
    r_txt.font.name = "Times New Roman"
    r_txt.font.size = Pt(11)

    r_tab = p.add_run("\t")
    r_tab.font.name = "Times New Roman"

    r_page = p.add_run(fig_page)
    r_page.font.name = "Times New Roman"
    r_page.font.size = Pt(11)
    r_page.font.bold = True

# ══════════════════════════════════════════════════════════════════════════════
# FORMATTED SECTION: LIST OF TABLES (Right-Aligned Tab Stops with Dot Leaders)
# ══════════════════════════════════════════════════════════════════════════════
print("Rendering Formatted List of Tables with Right-Aligned Dot Leaders...")
p_tbl_head = doc.add_paragraph()
p_tbl_head.paragraph_format.space_before = Pt(18)
p_tbl_head.paragraph_format.space_after = Pt(8)
r_th = p_tbl_head.add_run("LIST OF TABLES")
r_th.font.name = "Times New Roman"
r_th.font.size = Pt(14)
r_th.font.bold = True
r_th.font.color.rgb = RGBColor(0x1F, 0x4E, 0x79)

for tbl_title, tbl_page in formatted_lists.TABLE_ITEMS:
    p = doc.add_paragraph()
    p.paragraph_format.tab_stops.add_tab_stop(Inches(6.5), WD_TAB_ALIGNMENT.RIGHT, WD_TAB_LEADER.DOTS)
    p.paragraph_format.left_indent = Inches(0.0)
    p.paragraph_format.space_before = Pt(1.5)
    p.paragraph_format.space_after = Pt(1.5)
    p.paragraph_format.line_spacing = 1.15

    r_txt = p.add_run(tbl_title)
    r_txt.font.name = "Times New Roman"
    r_txt.font.size = Pt(11)

    r_tab = p.add_run("\t")
    r_tab.font.name = "Times New Roman"

    r_page = p.add_run(tbl_page)
    r_page.font.name = "Times New Roman"
    r_page.font.size = Pt(11)
    r_page.font.bold = True

# Render Abbreviations
print("Rendering List of Abbreviations...")
render_markdown_section(doc, abbrev_text)

# ══════════════════════════════════════════════════════════════════════════════
# SECTION 4: CHAPTERS 1 ONWARDS (Page numbering starts at 1, Bottom Center)
# ══════════════════════════════════════════════════════════════════════════════
s4 = doc.add_section()
s4.top_margin = Inches(1.0)
s4.bottom_margin = Inches(1.0)
s4.left_margin = Inches(1.0)
s4.right_margin = Inches(1.0)

s4._sectPr.append(parse_xml(
    f'<w:pgBorders {nsdecls("w")} w:offsetFrom="page">\n'
    f'  <w:top w:val="none"/>\n'
    f'  <w:left w:val="none"/>\n'
    f'  <w:bottom w:val="none"/>\n'
    f'  <w:right w:val="none"/>\n'
    f'</w:pgBorders>'
))

s4_footer = s4.footer
s4_footer.is_linked_to_previous = False
f_p = s4_footer.paragraphs[0]
f_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
f_run = f_p.add_run()
f_run.font.name = "Times New Roman"
f_run.font.size = Pt(11)
fld = parse_xml(r'<w:fldSimple %s w:instr="PAGE"/>' % nsdecls('w'))
f_p._p.append(fld)
s4._sectPr.append(parse_xml(r'<w:pgNumType %s w:start="1"/>' % nsdecls('w')))

# Combine all 10 chapters
all_chapters_text = "\n\n".join([
    ch1_ch2.CH1_CH2_TEXT,
    ch3_ch4.CH3_CH4_TEXT,
    ch5_ch6.CH5_CH6_TEXT,
    ch7_ch8.CH7_CH8_TEXT,
    ch9_ch10.CH9_CH10_TEXT
])

print("Rendering Chapters 1 to 10...")
render_markdown_section(doc, all_chapters_text)

# Save DOCX
docx_final_path = os.path.join(WORKSPACE_DIR, "UrbanClean_Final_Project_Report.docx")
doc.save(docx_final_path)
print(f"[SUCCESS] Master Final Project Report DOCX saved to:\n   {docx_final_path}")
print(f"Total Document Sections: {len(doc.sections)}")

# Copy to docs/
docs_docx_path = os.path.join(WORKSPACE_DIR, "docs", "UrbanClean_Final_Project_Report.docx")
import shutil
shutil.copy2(docx_final_path, docs_docx_path)
print(f"[SUCCESS] Copied DOCX to docs/:\n   {docs_docx_path}")

# Convert to PDF via docx2pdf
pdf_final_path = os.path.join(WORKSPACE_DIR, "UrbanClean_Final_Project_Report.pdf")
print("Converting DOCX to PDF via Microsoft Word...")
try:
    from docx2pdf import convert
    convert(docx_final_path, pdf_final_path)
    print(f"[SUCCESS] Final Academic Project Report PDF created at:\n   {pdf_final_path}")
    print(f"PDF File Size: {os.path.getsize(pdf_final_path)} bytes")

    # Copy to docs/
    docs_pdf_path = os.path.join(WORKSPACE_DIR, "docs", "UrbanClean_Final_Project_Report.pdf")
    shutil.copy2(pdf_final_path, docs_pdf_path)
    print(f"[SUCCESS] Copied PDF to docs/:\n   {docs_pdf_path}")
except Exception as e:
    print(f"[ERROR] PDF conversion failed: {e}")
