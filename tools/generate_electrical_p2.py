#!/usr/bin/env python3
"""Generate the CRTFE P2 concept electrical drawing set and integrated manual."""

from __future__ import annotations

import math
from pathlib import Path

from pypdf import PdfReader, PdfWriter
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A3, landscape, letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch, mm
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfgen import canvas
from reportlab.platypus import (
    KeepTogether,
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path(__file__).resolve().parents[1]
BLUEPRINT = ROOT / "docs/blueprints/CRTFE_V2_Electrical_Wiring_Schematic_Set_P2.pdf"
MANUAL = ROOT / "docs/manuals/CRTFE_V2_Integrated_Engineering_Assembly_Manual_P2.pdf"
MANUAL_CORE = ROOT / "tmp/CRTFE_V2_P2_manual_core.pdf"
OLD_MANUAL = ROOT / "docs/manuals/CRTFE_V5_Energy_Sled_Preliminary_Engineering_Manual.pdf"

BLUE = colors.HexColor("#184A8B")
PALE_BLUE = colors.HexColor("#DDEAF8")
GRID_BLUE = colors.HexColor("#B8D2EC")
DARK = colors.HexColor("#132A3A")
GREEN = colors.HexColor("#77A51B")
RED = colors.HexColor("#A52A2A")
GRAY = colors.HexColor("#52606D")
LIGHT = colors.HexColor("#F4F7FA")


def safe(text: str) -> str:
    return (
        text.replace("\u2013", "-")
        .replace("\u2014", "-")
        .replace("\u2212", "-")
        .replace("\u2265", ">=")
        .replace("\u2264", "<=")
        .replace("\u00b2", "^2")
        .replace("\u03c3", "sigma")
        .replace("\u0394", "Delta")
    )


def wrap_lines(text: str, font: str, size: float, width: float) -> list[str]:
    words = safe(text).split()
    lines: list[str] = []
    current = ""
    for word in words:
        proposed = f"{current} {word}".strip()
        if not current or stringWidth(proposed, font, size) <= width:
            current = proposed
        else:
            lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def graph_paper(c: canvas.Canvas, width: float, height: float) -> None:
    c.saveState()
    c.setStrokeColor(GRID_BLUE)
    c.setLineWidth(0.25)
    step = 5 * mm
    x = 0
    while x <= width:
        c.line(x, 0, x, height)
        x += step
    y = 0
    while y <= height:
        c.line(0, y, width, y)
        y += step
    c.setStrokeColor(colors.HexColor("#7FABD6"))
    c.setLineWidth(0.6)
    step = 25 * mm
    x = 0
    while x <= width:
        c.line(x, 0, x, height)
        x += step
    y = 0
    while y <= height:
        c.line(0, y, width, y)
        y += step
    c.restoreState()


def blueprint_title(c: canvas.Canvas, sheet: str, title: str, subtitle: str = "") -> None:
    width, height = landscape(A3)
    c.saveState()
    c.setFillColor(colors.white)
    c.rect(12 * mm, 10 * mm, width - 24 * mm, 24 * mm, fill=1, stroke=0)
    c.setStrokeColor(BLUE)
    c.setLineWidth(1.1)
    c.rect(12 * mm, 10 * mm, width - 24 * mm, 24 * mm, fill=0, stroke=1)
    c.line(width - 83 * mm, 10 * mm, width - 83 * mm, 34 * mm)
    c.line(width - 43 * mm, 10 * mm, width - 43 * mm, 34 * mm)
    c.setFillColor(BLUE)
    c.setFont("Helvetica-Bold", 13)
    c.drawString(17 * mm, 24 * mm, safe(title))
    c.setFont("Helvetica", 8)
    c.drawString(17 * mm, 15 * mm, safe(subtitle))
    c.setFont("Helvetica-Bold", 10)
    c.drawString(width - 79 * mm, 24 * mm, f"SHEET {sheet}")
    c.setFont("Helvetica", 8)
    c.drawString(width - 79 * mm, 15 * mm, "REV P2 | 2026-08-24")
    c.setFont("Helvetica-Bold", 10)
    c.drawString(width - 39 * mm, 24 * mm, "CRTFE V-2")
    c.setFont("Helvetica", 6.5)
    c.drawString(width - 39 * mm, 15 * mm, "CONCEPT ONLY")
    c.restoreState()


def header(c: canvas.Canvas, title: str, note: str) -> None:
    width, height = landscape(A3)
    c.saveState()
    c.setFillColor(colors.white)
    c.rect(12 * mm, height - 32 * mm, width - 24 * mm, 20 * mm, fill=1, stroke=0)
    c.setStrokeColor(BLUE)
    c.setLineWidth(1.0)
    c.rect(12 * mm, height - 32 * mm, width - 24 * mm, 20 * mm, fill=0, stroke=1)
    c.setFillColor(BLUE)
    c.setFont("Helvetica-Bold", 15)
    c.drawString(17 * mm, height - 21 * mm, safe(title))
    c.setFont("Helvetica", 8)
    c.drawRightString(width - 17 * mm, height - 21 * mm, safe(note))
    c.restoreState()


def box(
    c: canvas.Canvas,
    x: float,
    y: float,
    w: float,
    h: float,
    title: str,
    lines: list[str] | tuple[str, ...] = (),
    *,
    fill=colors.white,
    stroke=BLUE,
    title_fill=PALE_BLUE,
    dashed: bool = False,
) -> None:
    c.saveState()
    c.setStrokeColor(stroke)
    c.setFillColor(fill)
    c.setLineWidth(1.1)
    if dashed:
        c.setDash(4, 3)
    c.roundRect(x, y, w, h, 2.5 * mm, fill=1, stroke=1)
    c.setDash()
    c.setFillColor(title_fill)
    c.roundRect(x, y + h - 10 * mm, w, 10 * mm, 2.5 * mm, fill=1, stroke=0)
    c.rect(x, y + h - 10 * mm, w, 5 * mm, fill=1, stroke=0)
    c.setFillColor(stroke)
    c.setFont("Helvetica-Bold", 9)
    title_lines = wrap_lines(title, "Helvetica-Bold", 9, w - 6 * mm)
    ty = y + h - 6.7 * mm
    for line in title_lines[:2]:
        c.drawCentredString(x + w / 2, ty, line)
        ty -= 3.6 * mm
    c.setFillColor(DARK)
    c.setFont("Helvetica", 7.5)
    ty = y + h - 15 * mm
    for raw in lines:
        for line in wrap_lines(raw, "Helvetica", 7.5, w - 7 * mm):
            if ty < y + 4 * mm:
                break
            c.drawString(x + 3.5 * mm, ty, line)
            ty -= 3.5 * mm
    c.restoreState()


def wire(
    c: canvas.Canvas,
    points: list[tuple[float, float]],
    label: str = "",
    *,
    color=BLUE,
    width: float = 1.3,
    arrow: bool = True,
    dashed: bool = False,
) -> None:
    c.saveState()
    c.setStrokeColor(color)
    c.setFillColor(color)
    c.setLineWidth(width)
    if dashed:
        c.setDash(5, 3)
    path = c.beginPath()
    path.moveTo(*points[0])
    for point in points[1:]:
        path.lineTo(*point)
    c.drawPath(path, fill=0, stroke=1)
    if arrow and len(points) >= 2:
        x1, y1 = points[-2]
        x2, y2 = points[-1]
        angle = math.atan2(y2 - y1, x2 - x1)
        length = 3.2 * mm
        for delta in (2.55, -2.55):
            c.line(x2, y2, x2 + length * math.cos(angle + delta), y2 + length * math.sin(angle + delta))
    if label:
        mid = points[len(points) // 2]
        c.setFillColor(color)
        c.setFont("Helvetica-Bold", 7)
        c.drawCentredString(mid[0], mid[1] + 2 * mm, safe(label))
    c.restoreState()


def sheet_note(c: canvas.Canvas, text: str, x: float, y: float, w: float, *, color=RED) -> None:
    c.saveState()
    c.setFillColor(colors.white)
    c.setStrokeColor(color)
    c.setLineWidth(0.9)
    lines = wrap_lines(text, "Helvetica-Bold", 7.5, w - 8 * mm)
    h = (len(lines) * 3.4 + 7) * mm
    c.roundRect(x, y, w, h, 2 * mm, fill=1, stroke=1)
    c.setFillColor(color)
    c.setFont("Helvetica-Bold", 7.5)
    ty = y + h - 5 * mm
    for line in lines:
        c.drawString(x + 4 * mm, ty, safe(line))
        ty -= 3.4 * mm
    c.restoreState()


def new_sheet(c: canvas.Canvas, sheet: str, title: str, note: str = "") -> tuple[float, float]:
    width, height = landscape(A3)
    graph_paper(c, width, height)
    header(c, title, note)
    blueprint_title(c, sheet, title, "UNITS: functional connection architecture | values marked TBD require engineering release")
    return width, height


def draw_sheet_001(c: canvas.Canvas) -> None:
    width, height = new_sheet(c, "E-001", "ELECTRICAL DRAWING INDEX AND CONTROL BOUNDARY", "P2 ground-research package")
    x0, y0 = 20 * mm, 52 * mm
    rows = [
        ("E-101", "V0.3 SYSTEM INTERCONNECT", "Airflow, enclosed plasma subsystem, instruments, DAQ and safety"),
        ("E-102", "V0.3 HARDWIRED SAFETY CHAIN", "Dual-channel concept, manual reset and monitored contactor feedback"),
        ("E-201", "G2B STATOR VALIDATION ONE-LINE", "Polyphase source, phase measurement, field mapping and force stand"),
        ("E-301", "G2D HTS / STATOR INTEGRATION", "Independent HTS protection and traveling-wave source"),
        ("E-401", "V5 ENERGY-SLED SINGLE-LINE", "HV functional order, BMS, IMD, branch isolation and LV boundary"),
        ("E-501", "ARC POWER / DATA / SAFETY", "Reasoning, mediation and independent protective paths"),
        ("E-601", "HARNESS ZONES / INTERFACES", "Cable classes, routing separation, connector IDs and hold points"),
    ]
    table_x = x0
    table_y_top = height - 52 * mm
    c.setFillColor(colors.white)
    c.setStrokeColor(BLUE)
    c.rect(table_x, y0, 250 * mm, table_y_top - y0, fill=1, stroke=1)
    col = [25, 95, 130]
    x = table_x
    for w in col[:-1]:
        x += w * mm
        c.line(x, y0, x, table_y_top)
    row_h = (table_y_top - y0) / (len(rows) + 1)
    c.setFillColor(PALE_BLUE)
    c.rect(table_x, table_y_top - row_h, 250 * mm, row_h, fill=1, stroke=0)
    c.setFillColor(BLUE)
    c.setFont("Helvetica-Bold", 8)
    c.drawString(table_x + 4 * mm, table_y_top - 7 * mm, "SHEET")
    c.drawString(table_x + 29 * mm, table_y_top - 7 * mm, "DRAWING")
    c.drawString(table_x + 124 * mm, table_y_top - 7 * mm, "PURPOSE")
    y = table_y_top - row_h
    for sheet, drawing, purpose in rows:
        c.line(table_x, y - row_h, table_x + 250 * mm, y - row_h)
        c.setFillColor(DARK)
        c.setFont("Helvetica-Bold", 8)
        c.drawString(table_x + 4 * mm, y - 7 * mm, sheet)
        c.setFont("Helvetica", 7.2)
        for idx, line in enumerate(wrap_lines(drawing, "Helvetica", 7.2, 88 * mm)):
            c.drawString(table_x + 29 * mm, y - (6 + idx * 3.2) * mm, line)
        for idx, line in enumerate(wrap_lines(purpose, "Helvetica", 7.2, 121 * mm)):
            c.drawString(table_x + 124 * mm, y - (6 + idx * 3.2) * mm, line)
        y -= row_h
    box(
        c,
        282 * mm,
        145 * mm,
        118 * mm,
        82 * mm,
        "P2 RELEASES",
        [
            "Functional connections and independent safety boundaries",
            "Equipment and connector identifiers",
            "Cable-service classes and separation rules",
            "De-energized assembly and inspection sequence",
        ],
    )
    box(
        c,
        282 * mm,
        62 * mm,
        118 * mm,
        72 * mm,
        "P2 DOES NOT RELEASE",
        [
            "Bus voltage or hazardous-energy limits",
            "Power-wire gauge, fuse, contactor or coil rating",
            "Plasma-pulser construction or energized procedure",
            "Flight hardware, fabrication or certification approval",
        ],
        stroke=RED,
        title_fill=colors.HexColor("#F6DDDD"),
    )
    sheet_note(c, "CORE RULE: ARC, DAQ AND ORDINARY SOFTWARE NEVER CARRY THE HARDWIRED EMERGENCY-STOP OR PROTECTIVE-TRIP FUNCTION.", 282 * mm, 45 * mm, 118 * mm)
    c.showPage()


def draw_sheet_101(c: canvas.Canvas) -> None:
    width, height = new_sheet(c, "E-101", "V0.3 MOVING-AIR TEST RIG - SYSTEM INTERCONNECT", "100 x 100 mm duct | 10 / 20 / 30 m/s")
    y_mid = 148 * mm
    box(c, 20 * mm, y_mid, 42 * mm, 48 * mm, "FACILITY POWER", ["Approved receptacle / source", "Branch protection by facility", "PE / bond"])
    box(c, 78 * mm, y_mid, 50 * mm, 48 * mm, "LOCKABLE ISOLATION", ["Main disconnect", "LOTO point", "Absence-of-voltage boundary"])
    box(c, 145 * mm, y_mid, 55 * mm, 48 * mm, "SAFETY CONTACTOR", ["K1 / K2 as designed", "Monitored feedback", "Manual reset only"])
    box(c, 217 * mm, y_mid + 26 * mm, 55 * mm, 48 * mm, "BLOWER DRIVE", ["Variable speed", "Finger guard", "10 / 20 / 30 m/s baselines"])
    box(c, 217 * mm, y_mid - 32 * mm, 55 * mm, 48 * mm, "ENCLOSED PLASMA SOURCE", ["Qualified laboratory subsystem", "J-V03-HV", "No P2 internal schematic"], stroke=RED, title_fill=colors.HexColor("#F6DDDD"))
    box(c, 292 * mm, y_mid, 58 * mm, 48 * mm, "CLEAR TEST DUCT", ["Flow straightener", "T1 / plasma cassette / T2", "Z20 / Z50 / Z80"])
    box(c, 368 * mm, y_mid, 40 * mm, 48 * mm, "EXHAUST", ["XY traverse", "5 x 5 grid", "Camera"])
    wire(c, [(62 * mm, y_mid + 24 * mm), (78 * mm, y_mid + 24 * mm)], "POWER")
    wire(c, [(128 * mm, y_mid + 24 * mm), (145 * mm, y_mid + 24 * mm)], "ISOLATION")
    wire(c, [(200 * mm, y_mid + 24 * mm), (208 * mm, y_mid + 24 * mm), (208 * mm, y_mid + 50 * mm), (217 * mm, y_mid + 50 * mm)], "ENABLE")
    wire(c, [(200 * mm, y_mid + 24 * mm), (208 * mm, y_mid + 24 * mm), (208 * mm, y_mid - 8 * mm), (217 * mm, y_mid - 8 * mm)], "ENABLE", color=RED)
    wire(c, [(272 * mm, y_mid + 50 * mm), (282 * mm, y_mid + 50 * mm), (282 * mm, y_mid + 30 * mm), (292 * mm, y_mid + 30 * mm)], "AIR")
    wire(c, [(272 * mm, y_mid - 8 * mm), (282 * mm, y_mid - 8 * mm), (282 * mm, y_mid + 18 * mm), (292 * mm, y_mid + 18 * mm)], "IONIZED ZONE", color=RED)
    wire(c, [(350 * mm, y_mid + 24 * mm), (368 * mm, y_mid + 24 * mm)], "FLOW")

    box(c, 32 * mm, 62 * mm, 67 * mm, 52 * mm, "24 VDC SAFETY / CONTROL", ["J-V03-CTRL", "E-stop channels", "Guard interlocks", "Reset / status lights"])
    box(c, 122 * mm, 62 * mm, 64 * mm, 52 * mm, "INSTRUMENTATION", ["T1 / T2", "Impedance fixture", "Velocity probe", "Ambient sensors"])
    box(c, 210 * mm, 62 * mm, 64 * mm, 52 * mm, "ISOLATED DAQ", ["J-V03-DAQ", "Synchronized channels", "Calibration IDs", "Raw data preserved"])
    box(c, 298 * mm, 62 * mm, 60 * mm, 52 * mm, "OPERATOR CONSOLE", ["Test-plan state", "Display / record", "No safety authority", "No automatic restart"])
    box(c, 377 * mm, 62 * mm, 31 * mm, 52 * mm, "ARC", ["Read-only approved data", "Non-executable analysis"], dashed=True)
    wire(c, [(99 * mm, 88 * mm), (145 * mm, 88 * mm), (145 * mm, y_mid)], "HARDWIRED", color=GREEN, arrow=False)
    wire(c, [(186 * mm, 88 * mm), (210 * mm, 88 * mm)], "C2/C3")
    wire(c, [(274 * mm, 88 * mm), (298 * mm, 88 * mm)], "DATA")
    wire(c, [(358 * mm, 88 * mm), (377 * mm, 88 * mm)], "APPROVED COPY", dashed=True)
    wire(c, [(321 * mm, 114 * mm), (321 * mm, 132 * mm), (175 * mm, 132 * mm), (175 * mm, y_mid)], "START REQUEST ONLY", dashed=True, color=GRAY)
    sheet_note(c, "NO PLASMA-ON TEST UNTIL THE ENCLOSED SOURCE, INTERLOCKS, LOTO, INSTRUMENTATION AND HOST-LAB PROCEDURE PASS THE READINESS REVIEW.", 20 * mm, 43 * mm, 388 * mm)
    c.showPage()


def draw_sheet_102(c: canvas.Canvas) -> None:
    width, height = new_sheet(c, "E-102", "V0.3 HARDWIRED SAFETY CHAIN - CONCEPT", "24 VDC low-energy logic shown; component category/rating TBD")
    box(c, 20 * mm, 178 * mm, 42 * mm, 40 * mm, "PS-SAFE", ["24 VDC candidate", "Branch fuse F-C1", "Monitored supply"])
    box(c, 82 * mm, 178 * mm, 55 * mm, 40 * mm, "CHANNEL A", ["E-STOP A", "GUARD 1A", "GUARD 2A"])
    box(c, 82 * mm, 115 * mm, 55 * mm, 40 * mm, "CHANNEL B", ["E-STOP B", "GUARD 1B", "GUARD 2B"])
    box(c, 160 * mm, 144 * mm, 62 * mm, 52 * mm, "SAFETY RELAY SR1", ["Dual-channel inputs", "Cross-fault monitoring", "Manual reset input", "EDM feedback"])
    box(c, 250 * mm, 178 * mm, 52 * mm, 40 * mm, "K1 ENABLE CONTACTOR", ["Force-guided / monitored auxiliary contact", "De-energize to trip"])
    box(c, 250 * mm, 115 * mm, 52 * mm, 40 * mm, "K2 ENABLE CONTACTOR", ["Architecture by qualified integrator", "De-energize to trip"])
    box(c, 330 * mm, 144 * mm, 70 * mm, 52 * mm, "HAZARDOUS-ENERGY ENABLE", ["Blower and plasma-source enable as approved", "No direct power shown", "Manual reset required"])
    wire(c, [(62 * mm, 198 * mm), (82 * mm, 198 * mm)], "+24V")
    wire(c, [(62 * mm, 190 * mm), (72 * mm, 190 * mm), (72 * mm, 135 * mm), (82 * mm, 135 * mm)], "+24V")
    wire(c, [(137 * mm, 198 * mm), (150 * mm, 198 * mm), (150 * mm, 180 * mm), (160 * mm, 180 * mm)], "IN-A")
    wire(c, [(137 * mm, 135 * mm), (150 * mm, 135 * mm), (150 * mm, 160 * mm), (160 * mm, 160 * mm)], "IN-B")
    wire(c, [(222 * mm, 180 * mm), (250 * mm, 198 * mm)], "O1")
    wire(c, [(222 * mm, 160 * mm), (250 * mm, 135 * mm)], "O2")
    wire(c, [(302 * mm, 198 * mm), (318 * mm, 198 * mm), (318 * mm, 180 * mm), (330 * mm, 180 * mm)], "K1")
    wire(c, [(302 * mm, 135 * mm), (318 * mm, 135 * mm), (318 * mm, 160 * mm), (330 * mm, 160 * mm)], "K2")
    wire(c, [(276 * mm, 115 * mm), (276 * mm, 96 * mm), (191 * mm, 96 * mm), (191 * mm, 144 * mm)], "EDM K1/K2", arrow=False, dashed=True, color=GREEN)
    box(c, 52 * mm, 58 * mm, 58 * mm, 34 * mm, "MANUAL RESET", ["Keyed / guarded", "Outside hazard zone"])
    wire(c, [(110 * mm, 75 * mm), (191 * mm, 75 * mm), (191 * mm, 144 * mm)], "RESET", color=GREEN)
    box(c, 132 * mm, 58 * mm, 68 * mm, 34 * mm, "PROTECTIVE TRIPS", ["Overtemperature", "Smoke / arc", "Facility stop"])
    wire(c, [(200 * mm, 75 * mm), (222 * mm, 75 * mm), (222 * mm, 151 * mm)], "TRIP", color=RED)
    box(c, 224 * mm, 58 * mm, 80 * mm, 34 * mm, "STATUS ONLY", ["Safe / tripped / guard open", "To DAQ and ARC - read only"])
    wire(c, [(222 * mm, 151 * mm), (236 * mm, 151 * mm), (236 * mm, 92 * mm)], "AUX", dashed=True, color=GRAY)
    sheet_note(c, "THIS IS A FUNCTIONAL SAFETY CONCEPT, NOT A CLAIM OF PERFORMANCE LEVEL, SIL OR CODE COMPLIANCE. THE QUALIFIED INTEGRATOR SELECTS AND VALIDATES THE FINAL ARCHITECTURE.", 320 * mm, 58 * mm, 80 * mm)
    c.showPage()


def draw_sheet_201(c: canvas.Canvas) -> None:
    width, height = new_sheet(c, "E-201", "G2B PLASMA-OFF POLYPHASE STATOR VALIDATION - ONE-LINE", "125-point vector field map minimum")
    y = 160 * mm
    box(c, 18 * mm, y, 42 * mm, 50 * mm, "FACILITY SOURCE", ["Voltage / frequency TBD", "PE and branch protection", "Qualified lab"])
    box(c, 75 * mm, y, 48 * mm, 50 * mm, "LOCKABLE DISCONNECT", ["LOTO", "Pre-use inspection", "Absence-of-voltage test"])
    box(c, 138 * mm, y, 52 * mm, 50 * mm, "SAFETY ENABLE", ["E-stop / guards", "K1 / K2 monitored", "Manual reset"])
    box(c, 205 * mm, y, 58 * mm, 50 * mm, "ISOLATED 3-PHASE SOURCE", ["Programmable amplitude / frequency", "Phase sequence A-B-C", "No P2 internal design"])
    box(c, 280 * mm, y, 55 * mm, 50 * mm, "PHASE MEASUREMENT", ["IA / IB / IC", "VA / VB / VC", "Real / reactive / apparent power"])
    box(c, 350 * mm, y, 58 * mm, 50 * mm, "SEGMENTED STATOR", ["Finite winding", "End turns included", "Temperature sensors", "J-G2-PH"])
    for x1, x2, label in [(60, 75, "SOURCE"), (123, 138, "ISOLATED"), (190, 205, "ENABLE"), (263, 280, "A/B/C"), (335, 350, "A/B/C")]:
        wire(c, [(x1 * mm, (y + 25 * mm)), (x2 * mm, (y + 25 * mm))], label)
    box(c, 42 * mm, 74 * mm, 60 * mm, 54 * mm, "FIELD PROBE SYSTEM", ["Bx / By / Bz / |B|", "Amplitude and phase", "5 axial x 5 x 5 grid", "Calibrated orientation"])
    box(c, 128 * mm, 74 * mm, 60 * mm, 54 * mm, "IMPEDANCE MATRIX", ["Zij(f) = Rij + jXij", "Mutual inductance", "Harmonics / PF", "Temperature rise"])
    box(c, 214 * mm, 74 * mm, 60 * mm, 54 * mm, "FORCE / REACTION STAND", ["External load path", "Blank and phase reversal", "No plasma for G2B", "Uncertainty recorded"])
    box(c, 300 * mm, 74 * mm, 60 * mm, 54 * mm, "SYNCHRONIZED DAQ", ["Timebase", "Calibration IDs", "Raw waveforms", "Model release hash"])
    wire(c, [(379 * mm, y), (379 * mm, 138 * mm), (72 * mm, 138 * mm), (72 * mm, 128 * mm)], "FIELD", dashed=True, color=GREEN)
    wire(c, [(307 * mm, y), (307 * mm, 138 * mm), (158 * mm, 138 * mm), (158 * mm, 128 * mm)], "V/I")
    wire(c, [(379 * mm, y), (379 * mm, 144 * mm), (244 * mm, 144 * mm), (244 * mm, 128 * mm)], "REACTION", dashed=True)
    wire(c, [(102 * mm, 101 * mm), (300 * mm, 101 * mm)], "DATA", dashed=True, color=GRAY)
    wire(c, [(188 * mm, 94 * mm), (300 * mm, 94 * mm)], "DATA", dashed=True, color=GRAY)
    wire(c, [(274 * mm, 87 * mm), (300 * mm, 87 * mm)], "DATA", dashed=True, color=GRAY)
    sheet_note(c, "PASS REQUIRES MODEL-TO-MEASUREMENT AGREEMENT AGAINST PRE-REGISTERED UNCERTAINTY-BASED LIMITS. COMMANDED CURRENT OR AN IDEAL FIELD PLOT IS NOT VALIDATION.", 42 * mm, 45 * mm, 318 * mm)
    c.showPage()


def draw_sheet_301(c: canvas.Canvas) -> None:
    width, height = new_sheet(c, "E-301", "G2D COMBINED HTS BIAS AND TRAVELING-WAVE STATOR", "plasma off | protection independent")
    box(c, 18 * mm, 165 * mm, 52 * mm, 46 * mm, "HTS DC SUPPLY", ["Vendor / engineer controlled", "Current and ramp TBD", "Remote inhibit"])
    box(c, 90 * mm, 165 * mm, 52 * mm, 46 * mm, "HTS CURRENT LEADS", ["J-HTS-DC", "Thermal intercepts", "Cryogenic feedthrough"])
    box(c, 162 * mm, 165 * mm, 54 * mm, 46 * mm, "HTS BIAS MAGNET", ["Static field", "Temperature margin", "Stored energy TBD"])
    box(c, 90 * mm, 92 * mm, 52 * mm, 46 * mm, "QUENCH DETECTOR", ["Independent hardware", "J-HTS-QD", "No ARC dependency"], stroke=RED, title_fill=colors.HexColor("#F6DDDD"))
    box(c, 162 * mm, 92 * mm, 54 * mm, 46 * mm, "DUMP / PROTECTION", ["Energy extraction TBD", "Voltage / thermal analysis", "Validated protective response"], stroke=RED, title_fill=colors.HexColor("#F6DDDD"))
    wire(c, [(70 * mm, 188 * mm), (90 * mm, 188 * mm)], "C6 TBD")
    wire(c, [(142 * mm, 188 * mm), (162 * mm, 188 * mm)], "C6 TBD")
    wire(c, [(189 * mm, 165 * mm), (189 * mm, 138 * mm)], "SENSE", color=RED)
    wire(c, [(142 * mm, 115 * mm), (162 * mm, 115 * mm)], "TRIP", color=RED)
    wire(c, [(162 * mm, 108 * mm), (70 * mm, 108 * mm), (70 * mm, 175 * mm)], "INHIBIT", color=RED)

    box(c, 246 * mm, 165 * mm, 52 * mm, 46 * mm, "3-PHASE SOURCE", ["Separate isolation", "A-B-C phase sequence", "Amplitude / frequency TBD"])
    box(c, 318 * mm, 165 * mm, 54 * mm, 46 * mm, "TRAVELING STATOR", ["Segmented winding", "Installed with passive hardware", "Temperature / field sensors"])
    wire(c, [(298 * mm, 188 * mm), (318 * mm, 188 * mm)], "C5 A/B/C")
    box(c, 246 * mm, 92 * mm, 52 * mm, 46 * mm, "CRYOCOOLER", ["Cold-stage load TBD", "Wall-plug power measured", "Independent alarms"])
    box(c, 318 * mm, 92 * mm, 54 * mm, 46 * mm, "COMBINED TEST VOLUME", ["Static + traveling field map", "Passive loss / heating", "No plasma for G2D"])
    wire(c, [(298 * mm, 115 * mm), (318 * mm, 115 * mm)], "THERMAL")
    wire(c, [(345 * mm, 165 * mm), (345 * mm, 138 * mm)], "FIELD")
    wire(c, [(216 * mm, 188 * mm), (230 * mm, 188 * mm), (230 * mm, 126 * mm), (318 * mm, 126 * mm)], "BIAS FIELD", dashed=True, color=GREEN)
    box(c, 382 * mm, 120 * mm, 28 * mm, 66 * mm, "DAQ / ARC STATUS", ["Read-only copies", "No quench trip", "No direct drive"], dashed=True)
    wire(c, [(372 * mm, 188 * mm), (382 * mm, 174 * mm)], "DATA", dashed=True, color=GRAY)
    wire(c, [(372 * mm, 115 * mm), (382 * mm, 132 * mm)], "DATA", dashed=True, color=GRAY)
    sheet_note(c, "STOP ON UNEXPLAINED HEATING, AC LOSS, FIELD DISTORTION, LOSS OF HTS TEMPERATURE MARGIN OR ANY QUENCH-PROTECTION ANOMALY.", 18 * mm, 46 * mm, 392 * mm)
    c.showPage()


def draw_sheet_401(c: canvas.Canvas) -> None:
    width, height = new_sheet(c, "E-401", "V5 TARGET ENERGY SLED - FUNCTIONAL SINGLE-LINE", "1450 x 1050 x 340 mm envelope | 120 kg allowance")
    y = 171 * mm
    boxes = [
        (18, 48, "SEGMENTED MODULES", ["Cell chemistry / count TBD", "Module sensing", "Independent isolation concept"]),
        (82, 44, "SERVICE DISCONNECT", ["Manual / visible state", "Tool controlled", "HVIL candidate"]),
        (142, 42, "MAIN FUSE", ["Rating TBD", "Fault coordination required", "Pyro option not released"]),
        (200, 48, "MAIN CONTACTORS", ["K+ and K-", "Aux feedback", "Weld detection"]),
        (264, 48, "PRECHARGE / DISCHARGE", ["R and Kp TBD", "Bus capacitance required", "Safe discharge verified"]),
        (328, 44, "DC LINK", ["Voltage TBD", "Laminated bus candidate", "Touch-safe barriers"]),
    ]
    for x, w, title, lines in boxes:
        box(c, x * mm, y, w * mm, 48 * mm, title, lines)
    for (x1, w1, *_), (x2, *_rest) in zip(boxes, boxes[1:]):
        wire(c, [((x1 + w1) * mm, y + 24 * mm), (x2 * mm, y + 24 * mm)], "C7 TBD", color=RED)
    branch_y = 93 * mm
    for idx, x in enumerate((244, 286, 328, 370), start=1):
        box(c, x * mm, branch_y, 35 * mm, 42 * mm, f"BRANCH {idx}", ["Fuse / contactor as designed", f"Lift module {idx}", "Rating TBD"], stroke=RED, title_fill=colors.HexColor("#F6DDDD"))
        wire(c, [(350 * mm, y), (350 * mm, 146 * mm), ((x + 17.5) * mm, 146 * mm), ((x + 17.5) * mm, 135 * mm)], f"M{idx}", color=RED)
    box(c, 18 * mm, branch_y, 52 * mm, 42 * mm, "BMS", ["Cell V / T", "Contactor state", "Independent shutdown path"])
    box(c, 86 * mm, branch_y, 52 * mm, 42 * mm, "ISOLATION MONITOR", ["HV-to-chassis", "Threshold TBD", "Independent trip input"])
    box(c, 154 * mm, branch_y, 52 * mm, 42 * mm, "ESSENTIAL LV", ["Isolated supply", "Recorder / shutdown", "J-SLED-LV"])
    wire(c, [(44 * mm, 135 * mm), (44 * mm, y)], "MODULE DATA", dashed=True, color=GRAY)
    wire(c, [(112 * mm, 135 * mm), (112 * mm, 146 * mm), (350 * mm, 146 * mm)], "IMD", dashed=True, color=GREEN)
    wire(c, [(206 * mm, 114 * mm), (232 * mm, 114 * mm), (232 * mm, 154 * mm), (224 * mm, 154 * mm), (224 * mm, y)], "K+/K-/Kp REQUEST", dashed=True, color=GRAY)
    box(c, 18 * mm, 48 * mm, 188 * mm, 28 * mm, "HARDWIRED PROTECTION", ["BMS / IMD / contactor / fuse / service disconnect remain outside ARC authority; exact circuit and ratings TBD."], stroke=GREEN, title_fill=colors.HexColor("#E6F0D3"))
    box(c, 226 * mm, 48 * mm, 182 * mm, 28 * mm, "CONNECTOR BOUNDARY", ["J-SLED-HV touch-safe/keyed/HVIL candidate; J-SLED-LV carries status and shutdown request only. Pinouts are not released."], stroke=BLUE)
    sheet_note(c, "NO LIVE-CELL OR HV BUILD IS AUTHORIZED BY THIS DRAWING. A SELECTED CHEMISTRY, BUS, FAULT STUDY, THERMAL PROPAGATION TEST AND RESPONSIBLE-ENGINEER RELEASE ARE REQUIRED.", 18 * mm, 40 * mm, 390 * mm)
    c.showPage()


def draw_sheet_501(c: canvas.Canvas) -> None:
    width, height = new_sheet(c, "E-501", "ARC / T.A.R. POWER, DATA AND SAFETY SEPARATION", "ARC Revision 1.4 | all plans non-executable")
    box(c, 20 * mm, 167 * mm, 55 * mm, 48 * mm, "ISOLATED AVIONICS A", ["Converter A TBD", "Compute A / storage", "Network A"])
    box(c, 20 * mm, 96 * mm, 55 * mm, 48 * mm, "ISOLATED AVIONICS B", ["Converter B TBD", "Compute B / storage", "Network B"])
    box(c, 102 * mm, 132 * mm, 62 * mm, 56 * mm, "THE ARC / T.A.R.", ["Signed knowledge", "Evidence reasoning", "Digital-twin comparison", "Non-executable intent"])
    wire(c, [(75 * mm, 191 * mm), (102 * mm, 171 * mm)], "POWER / DATA")
    wire(c, [(75 * mm, 120 * mm), (102 * mm, 149 * mm)], "POWER / DATA")
    box(c, 191 * mm, 132 * mm, 64 * mm, 56 * mm, "INDEPENDENT SAFETY GATEWAY", ["Authoritative coarse state", "Policy / envelope binding", "Veto capable", "No raw setpoints from ARC"], stroke=GREEN, title_fill=colors.HexColor("#E6F0D3"))
    wire(c, [(164 * mm, 160 * mm), (191 * mm, 160 * mm)], "TYPED INTENT", dashed=True)
    box(c, 282 * mm, 132 * mm, 58 * mm, 56 * mm, "DETERMINISTIC CONTROLS", ["Released procedures", "Local limits", "Setpoint calculation", "Safe-state logic"], stroke=GREEN, title_fill=colors.HexColor("#E6F0D3"))
    wire(c, [(255 * mm, 160 * mm), (282 * mm, 160 * mm)], "PERMISSION / CONTEXT", color=GREEN)
    box(c, 367 * mm, 132 * mm, 43 * mm, 56 * mm, "MODULE CONTROLLERS", ["Power stages", "Actuators", "Local protection", "No ARC API"])
    wire(c, [(340 * mm, 160 * mm), (367 * mm, 160 * mm)], "BOUNDED CONTROL", color=GREEN)
    box(c, 20 * mm, 52 * mm, 68 * mm, 40 * mm, "ESSENTIAL SAFETY SOURCE", ["Separately protected", "Hold-up TBD", "Not controlled by ARC"], stroke=RED, title_fill=colors.HexColor("#F6DDDD"))
    box(c, 115 * mm, 52 * mm, 76 * mm, 40 * mm, "HARDWIRED PROTECTION", ["E-stop / guard / BMS", "Quench / dump / fire", "Never waits for network or signing"], stroke=RED, title_fill=colors.HexColor("#F6DDDD"))
    box(c, 218 * mm, 52 * mm, 64 * mm, 40 * mm, "INDEPENDENT SENSING", ["Hazard trips", "Local thresholds", "Direct protective path"], stroke=RED, title_fill=colors.HexColor("#F6DDDD"))
    wire(c, [(88 * mm, 72 * mm), (115 * mm, 72 * mm)], "POWER", color=RED)
    wire(c, [(191 * mm, 72 * mm), (218 * mm, 72 * mm)], "TRIP INPUT", color=RED)
    wire(c, [(282 * mm, 72 * mm), (345 * mm, 72 * mm), (345 * mm, 132 * mm)], "DIRECT TRIP", color=RED)
    wire(c, [(191 * mm, 80 * mm), (223 * mm, 80 * mm), (223 * mm, 132 * mm)], "STATUS COPY", dashed=True, color=GRAY)
    box(c, 310 * mm, 52 * mm, 100 * mm, 40 * mm, "LOSS-OF-ARC REQUIREMENT", ["Deterministic controls remain available or reach the predefined safe state. ARC loss cannot block shutdown."], stroke=BLUE)
    c.showPage()


def draw_sheet_601(c: canvas.Canvas) -> None:
    width, height = new_sheet(c, "E-601", "HARNESS ZONES, CABLE CLASSES AND RELEASE EVIDENCE", "separate routing | controlled crossings | no inferred ratings")
    zones = [
        ("ZONE A", "C0 / C1", "Protective bond and 24 V safety/control", GREEN),
        ("ZONE B", "C2 / C3", "Analog sensors and thermocouples", BLUE),
        ("ZONE C", "C4", "Data/time; fiber preferred across noisy boundaries", GRAY),
        ("ZONE D", "C5", "Polyphase stator power; symmetric routing", colors.HexColor("#8B5A18")),
        ("ZONE E", "C6", "HTS DC/current leads and quench wiring", colors.HexColor("#6B2F8A")),
        ("ZONE F", "C7 / C8", "Propulsion HV and special disconnect circuits", RED),
    ]
    x = 22 * mm
    y = 171 * mm
    for idx, (zone, cls, desc, color) in enumerate(zones):
        box(c, x, y, 58 * mm, 44 * mm, f"{zone} - {cls}", [desc, "Rating / spacing by released design"], stroke=color, title_fill=colors.Color(color.red, color.green, color.blue, alpha=0.12))
        x += 65 * mm
    c.setFillColor(DARK)
    c.setFont("Helvetica-Bold", 10)
    c.drawString(22 * mm, 148 * mm, "CONTROLLED CROSSING RULE")
    c.setFont("Helvetica", 8)
    for idx, line in enumerate(
        wrap_lines(
            "Cross power and sensor/data harnesses only at documented locations, preferably near 90 degrees. Maintain the released separation, shielding, bonding and enclosure-feedthrough design. Do not bundle unlike classes for convenience.",
            "Helvetica",
            8,
            365 * mm,
        )
    ):
        c.drawString(22 * mm, (139 - idx * 4) * mm, line)
    data = [
        ["INTERFACE", "SERVICE", "MANDATORY FEATURES", "RELEASE EVIDENCE"],
        ["J-V03-CTRL", "V0.3 low-voltage control", "Keyed; status/control only", "Netlist + low-energy test"],
        ["J-V03-DAQ", "Sensors / DAQ", "Shielded pairs; no hazardous energy", "Calibration + channel map"],
        ["J-V03-HV", "Enclosed plasma source", "Lab-owned; touch-safe; interlocked", "Facility approval"],
        ["J-G2-PH", "Stator A/B/C", "Phase ID; symmetric routing", "Impedance / thermal analysis"],
        ["J-HTS-DC/QD", "HTS current / quench", "Independent protection", "Magnet safety review"],
        ["J-SLED-HV/LV", "Energy sled", "Keyed; HVIL candidate; LV segregated", "Fault + insulation + FMEA"],
        ["J-ARC-A/B", "ARC redundant data/power", "Isolated; no actuator pins", "Interface control review"],
    ]
    tx, ty, tw, th = 22 * mm, 55 * mm, 365 * mm, 73 * mm
    c.setFillColor(colors.white)
    c.setStrokeColor(BLUE)
    c.rect(tx, ty, tw, th, fill=1, stroke=1)
    row_h = th / len(data)
    cols = [34, 54, 139, 138]
    x_positions = [tx]
    running = tx
    for val in cols[:-1]:
        running += val * mm
        x_positions.append(running)
        c.line(running, ty, running, ty + th)
    for r_idx, row in enumerate(data):
        ry = ty + th - (r_idx + 1) * row_h
        if r_idx == 0:
            c.setFillColor(PALE_BLUE)
            c.rect(tx, ry, tw, row_h, fill=1, stroke=0)
        if r_idx:
            c.line(tx, ry, tx + tw, ry)
        c.setFillColor(DARK)
        c.setFont("Helvetica-Bold" if r_idx == 0 else "Helvetica", 6.4)
        for col_idx, cell in enumerate(row):
            cell_x = x_positions[col_idx] + 2 * mm
            cell_w = cols[col_idx] * mm - 4 * mm
            lines = wrap_lines(cell, "Helvetica-Bold" if r_idx == 0 else "Helvetica", 6.4, cell_w)
            for line_idx, line in enumerate(lines[:2]):
                c.drawString(cell_x, ry + row_h - (3.5 + line_idx * 2.7) * mm, line)
    sheet_note(c, "WIRE SIZE, OVERCURRENT PROTECTION, CONTACTOR RATINGS, CREEPAGE/CLEARANCE AND CONNECTOR PINOUTS REMAIN TBD UNTIL HARDWARE AND ELECTRICAL LOADS ARE SELECTED.", 22 * mm, 42 * mm, 365 * mm)
    c.showPage()


def generate_blueprint() -> None:
    BLUEPRINT.parent.mkdir(parents=True, exist_ok=True)
    c = canvas.Canvas(str(BLUEPRINT), pagesize=landscape(A3), pageCompression=1)
    c.setTitle("CRTFE V-2 Electrical Wiring Schematic Set P2")
    c.setAuthor("CRTFE Project")
    c.setSubject("Concept-level ground-research electrical architecture")
    for draw in (
        draw_sheet_001,
        draw_sheet_101,
        draw_sheet_102,
        draw_sheet_201,
        draw_sheet_301,
        draw_sheet_401,
        draw_sheet_501,
        draw_sheet_601,
    ):
        draw(c)
    c.save()


def manual_styles():
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name="CoverTitle", fontName="Helvetica-Bold", fontSize=28, leading=32, textColor=DARK, alignment=TA_CENTER, spaceAfter=18))
    styles.add(ParagraphStyle(name="CoverSub", fontName="Helvetica", fontSize=13, leading=18, textColor=GRAY, alignment=TA_CENTER, spaceAfter=12))
    styles.add(ParagraphStyle(name="H1X", parent=styles["Heading1"], fontName="Helvetica-Bold", fontSize=18, leading=22, textColor=DARK, spaceBefore=8, spaceAfter=10))
    styles.add(ParagraphStyle(name="H2X", parent=styles["Heading2"], fontName="Helvetica-Bold", fontSize=13, leading=16, textColor=BLUE, spaceBefore=8, spaceAfter=6))
    styles.add(ParagraphStyle(name="BodyX", parent=styles["BodyText"], fontName="Helvetica", fontSize=9.3, leading=13, textColor=DARK, spaceAfter=6))
    styles.add(ParagraphStyle(name="SmallX", parent=styles["BodyText"], fontName="Helvetica", fontSize=7.5, leading=10, textColor=GRAY, spaceAfter=4))
    styles.add(ParagraphStyle(name="Callout", parent=styles["BodyText"], fontName="Helvetica-Bold", fontSize=9.5, leading=13, textColor=RED, borderColor=RED, borderWidth=0.8, borderPadding=8, backColor=colors.HexColor("#FFF6F6"), spaceBefore=8, spaceAfter=8))
    styles.add(ParagraphStyle(name="CenterX", parent=styles["BodyText"], fontName="Helvetica", fontSize=9, leading=13, alignment=TA_CENTER, textColor=DARK))
    return styles


def manual_header_footer(c: canvas.Canvas, doc) -> None:
    width, height = letter
    c.saveState()
    c.setStrokeColor(GRID_BLUE)
    c.setLineWidth(0.5)
    c.line(0.55 * inch, height - 0.48 * inch, width - 0.55 * inch, height - 0.48 * inch)
    c.setFont("Helvetica-Bold", 7.5)
    c.setFillColor(BLUE)
    c.drawString(0.58 * inch, height - 0.35 * inch, "CRTFE V-2 P2 ELECTRICAL INTEGRATION MANUAL")
    c.setFont("Helvetica", 7)
    c.setFillColor(GRAY)
    c.drawRightString(width - 0.58 * inch, height - 0.35 * inch, "CONCEPT - NOT BUILD OR ENERGIZED-WORK RELEASE")
    c.line(0.55 * inch, 0.48 * inch, width - 0.55 * inch, 0.48 * inch)
    c.drawString(0.58 * inch, 0.30 * inch, "Controlled revision P2 - 2026-08-24")
    c.drawRightString(width - 0.58 * inch, 0.30 * inch, f"Page {doc.page}")
    c.restoreState()


def para(text: str, style) -> Paragraph:
    return Paragraph(safe(text), style)


def bullet_list(items: list[str], style) -> list[Paragraph]:
    return [Paragraph(safe(item), style, bulletText="-") for item in items]


def styled_table(data: list[list[str]], widths: list[float], styles, font_size: float = 7.4) -> Table:
    rows = []
    for r_idx, row in enumerate(data):
        row_style = styles["SmallX"]
        rows.append([Paragraph(f"<b>{safe(cell)}</b>" if r_idx == 0 else safe(cell), row_style) for cell in row])
    table = Table(rows, colWidths=widths, repeatRows=1, hAlign="LEFT")
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), PALE_BLUE),
                ("TEXTCOLOR", (0, 0), (-1, 0), BLUE),
                ("GRID", (0, 0), (-1, -1), 0.35, colors.HexColor("#9BB9D7")),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 4),
                ("RIGHTPADDING", (0, 0), (-1, -1), 4),
                ("TOPPADDING", (0, 0), (-1, -1), 4),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
                ("FONTSIZE", (0, 0), (-1, -1), font_size),
            ]
        )
    )
    return table


def generate_manual_core() -> None:
    MANUAL_CORE.parent.mkdir(parents=True, exist_ok=True)
    styles = manual_styles()
    doc = SimpleDocTemplate(
        str(MANUAL_CORE),
        pagesize=letter,
        rightMargin=0.62 * inch,
        leftMargin=0.62 * inch,
        topMargin=0.66 * inch,
        bottomMargin=0.62 * inch,
        title="CRTFE V-2 Integrated Engineering and Assembly Manual P2",
        author="CRTFE Project",
    )
    story = [
        Spacer(1, 0.65 * inch),
        para("CRTFE V-2", styles["CoverTitle"]),
        para("INTEGRATED ENGINEERING, WIRING AND ASSEMBLY MANUAL", styles["CoverTitle"]),
        para("Revision P2 - Ground-Research Electrical Architecture", styles["CoverSub"]),
        Spacer(1, 0.25 * inch),
        para("Includes the P2 eight-sheet electrical schematic set and the retained V5 P0 energy-sled mechanical/fastener baseline.", styles["CenterX"]),
        Spacer(1, 0.25 * inch),
        para("CONCEPT ONLY - NOT A FABRICATION DRAWING - NOT FLIGHT READY - NO ENERGIZED WORK AUTHORIZED", styles["Callout"]),
        Spacer(1, 0.6 * inch),
        styled_table(
            [
                ["Document", "Controlled value"],
                ["Configuration", "V0.3 / V-2 G2 ground articles plus V5 target-vehicle interface"],
                ["Revision", "P2 - 2026-08-24"],
                ["Maturity", "DRAFT concept-level integration"],
                ["Authority", "No flight, fabrication, live-cell, HV-source construction or energized-test authority"],
            ],
            [1.5 * inch, 5.1 * inch],
            styles,
        ),
        PageBreak(),
        para("1. Revision P2 change summary", styles["H1X"]),
        para("P2 adds the missing connection architecture and makes the trust and energy boundaries explicit.", styles["BodyX"]),
        *bullet_list(
            [
                "Eight-sheet blue-pencil/graph-paper electrical schematic set.",
                "V0.3 system interconnect and hardwired safety-chain concept.",
                "G2B plasma-off polyphase stator validation one-line.",
                "G2D combined HTS-bias/stator wiring and independent quench boundary.",
                "V5 energy-sled functional single-line and ARC power/data/safety separation.",
                "Cable-class, interface, inspection, assembly and staged-commissioning schedules.",
                "Existing P0 structural, shield, fastener and inert-mockup manual retained as a controlled appendix.",
            ],
            styles["BodyX"],
        ),
        para("P2 does not invent values that the project has not earned. Power conductor sizes, HV ratings, contactor/fuse ratings, coil turns/current, quench dump values, creepage/clearance and live test limits remain TBD pending selected hardware and professional engineering.", styles["Callout"]),
        para("Document organization", styles["H2X"]),
        styled_table(
            [
                ["Section", "Contents"],
                ["Part I", "P2 electrical integration, wiring, assembly, inspection and commissioning"],
                ["Appendix A", "Retained V5 P0 energy-sled structural/fastener/assembly manual"],
                ["Appendix B", "P2 electrical wiring schematic set E-001 through E-601"],
            ],
            [1.2 * inch, 5.4 * inch],
            styles,
        ),
        PageBreak(),
        para("2. System purpose in plain language", styles["H1X"]),
        para("The first job is not to build an aircraft. The first job is to test one hard question: can moving air be made electrically conductive enough, without unacceptable power or heat, to justify the next experiment?", styles["BodyX"]),
        styled_table(
            [
                ["Article", "Simple purpose", "What it can prove"],
                ["V0.3", "Move air through a small duct; measure conductivity, power, heat, decay and flow.", "Whether the assumed conductive-air state exists in the selected regime."],
                ["G2B", "Power the bare traveling-wave stator with no plasma; map field and coil power.", "Whether the finite-coil model predicts the real winding."],
                ["G2D", "Combine the HTS bias magnet and stator with no plasma.", "Whether they coexist without unacceptable loss, heating or margin loss."],
                ["V5 interface", "Preserve a target-vehicle packaging and safety boundary.", "Nothing about flight until every prior gate is passed."],
            ],
            [0.8 * inch, 3.0 * inch, 2.8 * inch],
            styles,
        ),
        para("The source files use CRFTE and CRTFE. No approved letter-by-letter expansion is present, so this manual does not invent one. The controlled plain-language name is CRTFE Experimental Aerospace Research Project.", styles["Callout"]),
        PageBreak(),
        para("3. Electrical architecture and responsibility", styles["H1X"]),
        styled_table(
            [
                ["Layer", "Function", "Responsible authority"],
                ["Facility power", "Branch protection, LOTO, grounding and safe work condition", "Host laboratory / qualified electrical personnel"],
                ["Hardwired safety", "E-stop, guards, protective trips, manual reset", "Qualified safety/electrical integrator"],
                ["Test power", "Blower, plasma subsystem, stator source and HTS supply", "Equipment owner and responsible engineer"],
                ["Instrumentation", "Calibrated V/I/Z, field, temperature, velocity and time", "Test engineer"],
                ["DAQ", "Synchronized raw data and configuration records", "Test engineer; no protective authority"],
                ["ARC/T.A.R.", "Evidence retrieval, analysis and non-executable planning", "Authenticated human review; no actuator authority"],
            ],
            [1.15 * inch, 3.15 * inch, 2.3 * inch],
            styles,
        ),
        para("The hardwired safety chain is independent of ARC, T.A.R., the DAQ computer, ordinary software and network availability. Opening a guarded energized compartment must remove the applicable hazardous-energy enable using a validated architecture. Manual reset and no automatic restart are required.", styles["Callout"]),
        para("Safety references", styles["H2X"]),
        *bullet_list(
            [
                "OSHA 29 CFR 1910.147: energy isolation and lockout/tagout.",
                "OSHA 29 CFR 1910.333: electrical safe work practices.",
                "OSHA 29 CFR 1910.306: interlock precedent for access panels on specific equipment.",
                "NFPA 70E: electrical safety program and shock/arc-flash risk framework.",
            ],
            styles["BodyX"],
        ),
        PageBreak(),
        para("4. Cable-class schedule", styles["H1X"]),
        styled_table(
            [
                ["Class", "Service", "P2 planning rule", "Release"],
                ["C0", "Protective earth/bonding", "Dedicated studs; no signal-current return", "TBD by fault/code study"],
                ["C1", "24 VDC safety/control", "Twisted stranded copper; separately fused", "18 AWG bench candidate only"],
                ["C2", "Analog sensors", "Shielded twisted pair", "22-24 AWG bench candidate only"],
                ["C3", "Thermocouple", "Correct alloy extension wire", "24 AWG bench candidate only"],
                ["C4", "Data/time", "Fiber preferred across noisy boundaries", "By network/EMC design"],
                ["C5", "Stator A/B/C", "Symmetric phase routing", "TBD after frequency/current/thermal study"],
                ["C6", "HTS DC/leads", "Vendor-qualified cryogenic interfaces", "TBD by magnet design"],
                ["C7/C8", "Propulsion HV/special disconnect", "Segregated, touch-safe, guarded", "Not released in P2"],
            ],
            [0.55 * inch, 1.45 * inch, 2.6 * inch, 2.0 * inch],
            styles,
        ),
        para("Small-wire gauges are bench candidates only. The responsible engineer must verify branch protection, voltage drop, temperature, bundle derating, flexing, connector compatibility and the host facility's rules before use.", styles["Callout"]),
        PageBreak(),
        para("5. Interface and connector schedule", styles["H1X"]),
        styled_table(
            [
                ["ID", "Interface", "Mandatory feature"],
                ["J-V03-CTRL", "V0.3 control box", "Keyed low-voltage; control/status only"],
                ["J-V03-DAQ", "V0.3 instruments", "Shielded pairs; no hazardous-energy conductors"],
                ["J-V03-HV", "Enclosed plasma subsystem", "Lab-owned, touch-safe, interlocked; pinout not released"],
                ["J-G2-PH", "G2 phase interface", "A/B/C identity; protective bonding as designed"],
                ["J-G2-SENSE", "G2 measurement", "Finger-safe lab-selected V/I/temperature interface"],
                ["J-HTS-DC", "HTS supply/current leads", "Vendor/engineer controlled; no P2 pinout"],
                ["J-HTS-QD", "Quench/dump", "Independent protection; ARC gets status only"],
                ["J-SLED-HV", "Energy-sled propulsion HV", "Touch-safe, keyed, HVIL candidate; rating TBD"],
                ["J-SLED-LV", "Energy-sled essential LV", "BMS/IMD/status and shutdown request"],
                ["J-ARC-A/B", "ARC power/data", "Isolated paths; no direct actuator pins"],
            ],
            [1.0 * inch, 2.25 * inch, 3.35 * inch],
            styles,
        ),
        para("Connector manufacturer, family, shell, insert, pin assignment, sealing, mating cycles and keying remain configuration-controlled selections. Never infer a pinout from a concept drawing.", styles["Callout"]),
        PageBreak(),
        para("6. Wire identification and workmanship", styles["H1X"]),
        *bullet_list(
            [
                "Assign every conductor a unique wire ID and show the same ID on schematic, wire list and both physical ends.",
                "Record from/to equipment, connector and pin, service class, conductor/cable part number, gauge, length, shield rule, protection and inspection status.",
                "Use controlled crimp tooling matched to the terminal and conductor. Record tool identification and inspection status.",
                "Provide strain relief, bend-radius control, chafe protection, environmental sealing and a service loop where removal requires it.",
                "Keep protective bonding separate from signal return and shield termination.",
                "Do not splice hazardous-energy wiring unless the released design and facility procedure explicitly permit it.",
                "Inspect 100 percent of safety-chain, HTS-protection and propulsion-HV terminations.",
            ],
            styles["BodyX"],
        ),
        para("NASA-STD-8739.4 is used as a workmanship reference for cable and harness assemblies. FAA AC 43.13-1B may inform aviation workmanship only where applicable and legally permitted. Neither reference is a substitute for the selected component manufacturer's instructions or a project-specific engineering release.", styles["BodyX"]),
        PageBreak(),
        para("7. Grounding, bonding, shielding and field compatibility", styles["H1X"]),
        styled_table(
            [
                ["Topic", "P2 rule", "Verification"],
                ["Protective bond", "Dedicated low-impedance path; no hinge-only bond", "Low-resistance measurement and visual inspection"],
                ["Signal reference", "Defined by instrument/DAQ architecture", "Noise and common-mode test"],
                ["Cable shield", "Terminate per EMC plan; avoid improvised pigtails", "Continuity and transfer-impedance review"],
                ["Conductive enclosure", "Segment/slot/insulate where analysis requires", "G2B/G2C field-loss and heating comparison"],
                ["Carbon/composite", "Control galvanic and bonding interfaces", "Coupon and environmental test"],
                ["Crossings", "Documented locations, preferably near 90 degrees", "Harness-zone inspection"],
            ],
            [1.25 * inch, 3.15 * inch, 2.2 * inch],
            styles,
        ),
        para("A shield that protects against impact or fire can become a conductive shorted turn near a changing magnetic field. G2C must measure field distortion, induced loss and heating with the installed shield, seams and representative fasteners.", styles["Callout"]),
        PageBreak(),
        para("8. Assembly sequence - drawings and enclosure", styles["H1X"]),
        *bullet_list(
            [
                "Freeze configuration ID, schematic revision, test plan and approved equipment list.",
                "Create the complete wire list and connector schedule before cutting wire.",
                "Complete fault-current, ampacity, insulation, creepage/clearance, stored-energy and EMC analyses before hazardous-energy release.",
                "Install enclosure, DIN rail, terminal blocks, protective-earth bar and labeled cable-entry plates.",
                "Install the hardwired safety components before ordinary control or DAQ hardware.",
                "Install separate routing zones for C0/C1, C2/C3/C4 and C5/C6/C7.",
                "Bond the enclosure and mounting panels first; document the hardware stack and measured bond.",
                "Build and label low-voltage harnesses to the controlled cut list.",
                "Install hazardous-energy harnesses only after engineering and host-laboratory release.",
            ],
            styles["BodyX"],
        ),
        para("No work beneath an unsupported energy sled. No live cells, charged capacitors, HTS stored energy or plasma-source connection during mechanical fit check.", styles["Callout"]),
        PageBreak(),
        para("9. De-energized inspection and verification", styles["H1X"]),
        styled_table(
            [
                ["Step", "Evidence"],
                ["Point-to-point", "Every net agrees with schematic/wire list; checker signs"],
                ["Isolation", "No unintended continuity among power, control, sensor, shield and chassis"],
                ["Bonding", "Recorded low-resistance result using approved method"],
                ["Connector", "Keying, polarization, backshell, strain relief and labels correct"],
                ["Harness", "Separation, bend radius, clamps, chafe and service loops correct"],
                ["Safety logic", "E-stop/guard/manual-reset tested with low-energy supply"],
                ["Restart", "Power cycle cannot cause automatic hazardous-energy restart"],
                ["Data", "Channel map, calibration IDs, timebase and raw-data path verified"],
            ],
            [1.45 * inch, 5.15 * inch],
            styles,
        ),
        para("Insulation-resistance or hipot testing can damage electronics or create hazardous stored charge. The responsible engineer must define the method, disconnected components, test voltage, discharge and acceptance criteria. P2 does not invent them.", styles["Callout"]),
        PageBreak(),
        para("10. Staged commissioning", styles["H1X"]),
        styled_table(
            [
                ["Stage", "Allowed activity", "Stop condition"],
                ["C0", "Mechanical fit and labels; all sources disconnected", "Any interference, chafe or connector error"],
                ["C1", "Low-energy safety-chain test", "Any trip/reset/feedback discrepancy"],
                ["C2", "DAQ, sensors and time synchronization", "Missing calibration or time integrity"],
                ["C3", "Blower and V0.3 plasma-OFF baselines", "Unstable flow, vibration, leak or data gap"],
                ["C4", "G2B stator at lowest approved energy; no plasma", "Unexpected imbalance, heating or field"],
                ["C5", "G2C passive hardware installed", "Shorted-turn signature or unexplained loss"],
                ["C6", "G2D HTS + stator; no plasma", "Margin loss, quench anomaly or excessive AC loss"],
                ["C7", "Plasma-loaded test under host procedure", "Arc, excessive heat, interlock or data anomaly"],
            ],
            [0.65 * inch, 3.4 * inch, 2.55 * inch],
            styles,
        ),
        para("Advancement is evidence-gated. Passing a wiring inspection does not validate propulsion, and passing a field-map test does not validate thrust.", styles["Callout"]),
        PageBreak(),
        para("11. V0.3 operating record", styles["H1X"]),
        para("Every plasma-ON run must cite a matching plasma-OFF baseline at the same nominal 10, 20 or 30 m/s flow point. The minimum run record includes:", styles["BodyX"]),
        *bullet_list(
            [
                "Run, configuration, operator, facility, date/time and calibration IDs.",
                "Complete 5 x 5 XY velocity plane and axial location.",
                "T1/T2 and ambient temperature/pressure/humidity where available.",
                "Z20, Z50 and Z80 complex impedance records.",
                "Plasma-source electrical input from the qualified facility instrumentation.",
                "Synchronized video and discharge classification: diffuse, filamentary, thermal/arc or uncertain.",
                "Raw data preserved separately from derived conductivity and model output.",
                "Stop/pivot decision against the pre-committed conductivity, power, heat and morphology gates.",
            ],
            styles["BodyX"],
        ),
        para("No V0.3 data become vehicle-scale proof. The 0.01 m^2 duct is approximately 60 times smaller than the earlier 0.60 m^2 module model and is a screening article only.", styles["Callout"]),
        PageBreak(),
        para("12. G2 electromagnetic validation record", styles["H1X"]),
        *bullet_list(
            [
                "Mesh-converged finite-coil/circuit model with reproducible inputs and hashes.",
                "Bare-coil vector map: at least five axial stations and 5 x 5 cross-section grid per station.",
                "Field amplitude and phase, complete coil impedance matrix, real/reactive/apparent power, power factor, harmonics and temperature rise.",
                "Installed passive hardware repeat with duct, cryostat, supports, shield, seams and representative fasteners.",
                "Combined HTS/stator repeat with temperature margin, AC loss, stored energy and protection response.",
                "Pre-registered acceptance limits derived from calibrated uncertainty and design sensitivity.",
            ],
            styles["BodyX"],
        ),
        para("Preliminary comparison objectives in the project record are <=5 percent field-amplitude RMS error, <=10 percent maximum local field error, <=5 degrees phase error and <=10 percent real-power error. They are not final released acceptance criteria.", styles["Callout"]),
        PageBreak(),
        para("13. Energy sled and ARC interface", styles["H1X"]),
        para("The V5 energy sled remains a target-vehicle packaging and safety study: 1450 x 1050 x 340 mm maximum envelope and 120 kg battery-system allowance. Chemistry, bus voltage, cell count, fault current and live hardware are not selected.", styles["BodyX"]),
        styled_table(
            [
                ["Function", "Required order/boundary"],
                ["HV path", "Segmented modules -> service disconnect -> main fuse -> K+/K- -> precharge/discharge -> DC link -> isolated branches"],
                ["Protection", "BMS, IMD, fuse, contactor feedback and service disconnect remain independent of ARC"],
                ["Low voltage", "Isolated essential supply supports recorder and shutdown functions"],
                ["ARC", "Receives approved status and may submit non-executable intent; no contactor-drive or actuator pins"],
                ["Shield", "Impact/fire protection must also pass electromagnetic loss/heating tests"],
            ],
            [1.25 * inch, 5.35 * inch],
            styles,
        ),
        PageBreak(),
        para("14. Hold points and release evidence", styles["H1X"]),
        styled_table(
            [
                ["Hold point", "Evidence", "Authority"],
                ["HP-E1", "Approved schematic, wire list, component data", "Responsible electrical engineer"],
                ["HP-E2", "Bond/enclosure inspection", "Engineer / facility safety"],
                ["HP-E3", "Netlist verification and insulation test plan", "Independent checker"],
                ["HP-E4", "Low-energy E-stop/interlock/manual-reset test", "Facility safety representative"],
                ["HP-E5", "DAQ calibration and time synchronization", "Test engineer"],
                ["HP-E6", "V0.3 and G2 plasma-OFF baselines", "Test director"],
                ["HP-E7", "HTS quench/dump validation", "Magnet/cryogenic engineer"],
                ["HP-E8", "Energized-test readiness review", "Host laboratory authority"],
            ],
            [0.8 * inch, 3.75 * inch, 2.05 * inch],
            styles,
        ),
        para("A signature at one hold point does not waive another discipline's authority. Safety, facility and test authorities remain independently veto-capable.", styles["Callout"]),
        PageBreak(),
        para("15. Stop-work and discrepancy control", styles["H1X"]),
        *bullet_list(
            [
                "Unexpected continuity, insulation or protective-bond result.",
                "Missing or incorrect conductor, connector or equipment label.",
                "Guard opening does not remove the relevant enable.",
                "Automatic restart after control-power restoration.",
                "Welded/inconsistent contactor feedback or loss of protective bond.",
                "Uncommanded phase sequence, current imbalance or unexplained heating.",
                "Field distortion or shorted-turn signature after passive hardware installation.",
                "HTS temperature-margin loss or quench-protection anomaly.",
                "DAQ time, calibration or configuration mismatch.",
                "Arc, smoke, odor, coolant leak, abnormal sound or unexpected temperature rise.",
            ],
            styles["BodyX"],
        ),
        para("Tag the discrepancy, preserve raw data, isolate affected hardware, identify configuration and obtain documented disposition before resuming.", styles["Callout"]),
        PageBreak(),
        para("16. Sources and controlled references", styles["H1X"]),
        *bullet_list(
            [
                "CRTFE V0.3 Prototype Test Rig Revision 1.2.",
                "CRTFE V-2 Hybrid MHD Research Baseline P1.2.",
                "CRTFE V-2 G2 Electromagnetic Verification and Validation P1.",
                "CRTFE V-2 ARC and Akashic Record Vessel Integration Revision 1.4.",
                "CRTFE V5 Energy Sled Preliminary Engineering Manual P0.",
                "OSHA 29 CFR 1910.147: https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.147",
                "OSHA 29 CFR 1910.333: https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.333",
                "OSHA 29 CFR 1910.306: https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.306",
                "NASA-STD-8739.4: https://standards.nasa.gov/standard/NASA/NASA-STD-87394",
                "FAA AC 43.13-1B: https://www.faa.gov/regulations_policies/advisory_circulars/index.cfm/go/document.information/documentid/99861",
                "NFPA 70E: https://www.nfpa.org/codes-and-standards/nfpa-70e-standard-development/70e",
            ],
            styles["BodyX"],
        ),
        para("References inform the safety and workmanship basis. They do not turn this preliminary project package into a code-compliant installation, flight release or certification approval.", styles["Callout"]),
        PageBreak(),
        para("APPENDIX A", styles["CoverTitle"]),
        para("Retained V5 P0 Energy-Sled Mechanical, Shield, Fastener and Inert-Assembly Baseline", styles["CoverSub"]),
        para("The following P0 manual pages are incorporated without changing their original claims or candidate values. P2 electrical architecture controls where the two documents overlap.", styles["Callout"]),
        PageBreak(),
    ]
    doc.build(story, onFirstPage=manual_header_footer, onLaterPages=manual_header_footer)


def merge_manual() -> None:
    writer = PdfWriter()
    writer.append(str(MANUAL_CORE), outline_item="Part I - P2 electrical integration")
    writer.append(str(OLD_MANUAL), outline_item="Appendix A - Retained V5 P0 manual")
    writer.append(str(BLUEPRINT), outline_item="Appendix B - P2 wiring schematics")
    metadata = {
        "/Title": "CRTFE V-2 Integrated Engineering, Wiring and Assembly Manual P2",
        "/Author": "CRTFE Project",
        "/Subject": "Ground-research electrical integration, retained energy-sled baseline and schematic package",
    }
    writer.add_metadata(metadata)
    MANUAL.parent.mkdir(parents=True, exist_ok=True)
    with MANUAL.open("wb") as stream:
        writer.write(stream)


def main() -> None:
    generate_blueprint()
    generate_manual_core()
    merge_manual()
    print(BLUEPRINT)
    print(MANUAL)


if __name__ == "__main__":
    main()
