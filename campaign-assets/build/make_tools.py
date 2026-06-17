#!/usr/bin/env python3
"""Generate the campaign 'tools' arsenal: XLSX trackers, CSV templates, and an
importable .ics filing calendar. Run from build/. Outputs to ../tools/."""
import csv, datetime, pathlib
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.worksheet.datavalidation import DataValidation

TOOLS = pathlib.Path(__file__).resolve().parent.parent / "tools"
TOOLS.mkdir(exist_ok=True)

NAVY = "FF0A1F44"; RED = "FFC8102E"; MIST = "FFEEF2F7"; WHITE = "FFFFFFFF"
hdr_fill = PatternFill("solid", fgColor=NAVY)
hdr_font = Font(bold=True, color=WHITE, size=10)
title_font = Font(bold=True, color=NAVY, size=14)
note_font = Font(italic=True, color="FF64748B", size=9)
thin = Side(style="thin", color="FFD8DEE9")
border = Border(bottom=thin)

def style_header(ws, row, ncols, start=1):
    for c in range(start, start + ncols):
        cell = ws.cell(row=row, column=c)
        cell.fill = hdr_fill; cell.font = hdr_font
        cell.alignment = Alignment(horizontal="left", vertical="center", wrap_text=True)

def widths(ws, ws_widths):
    for col, w in ws_widths.items():
        ws.column_dimensions[col].width = w

def banner(ws, title, subtitle, ncols):
    ws.merge_cells(start_row=1, start_column=1, end_row=1, end_column=ncols)
    ws["A1"] = title; ws["A1"].font = title_font
    ws.merge_cells(start_row=2, start_column=1, end_row=2, end_column=ncols)
    ws["A2"] = subtitle; ws["A2"].font = note_font
    ws.row_dimensions[1].height = 20

# ---------------------------------------------------------------- 1. Contributions
def contribution_tracker():
    wb = Workbook(); ws = wb.active; ws.title = "Contributions"
    cols = ["Date","Donor Name","Address","City/State/ZIP","Occupation","Employer",
            "Amount","Election","Method","Aggregate to Date","Itemize? (>$200)","Refund/Redesig.","Notes"]
    banner(ws, "Contribution Tracker", "Grant for Congress (MO-02) — log every receipt. Itemize donors over $200 aggregate.", len(cols))
    hr = 4
    for i, c in enumerate(cols, 1): ws.cell(row=hr, column=i, value=c)
    style_header(ws, hr, len(cols))
    # formulas for 200 sample rows
    for r in range(hr+1, hr+201):
        ws.cell(row=r, column=10, value=f'=IF(B{r}="","",SUMIF($B${hr+1}:$B${hr+200},B{r},$G${hr+1}:$G${hr+200}))')
        ws.cell(row=r, column=11, value=f'=IF(J{r}="","",IF(J{r}>200,"YES",""))')
        ws.cell(row=r, column=7).number_format = '"$"#,##0.00'
        ws.cell(row=r, column=10).number_format = '"$"#,##0.00'
    # totals
    tr = hr + 201
    ws.cell(row=tr, column=6, value="TOTAL RAISED:").font = Font(bold=True, color=NAVY)
    tot = ws.cell(row=tr, column=7, value=f"=SUM(G{hr+1}:G{hr+200})")
    tot.font = Font(bold=True, color=NAVY); tot.number_format = '"$"#,##0.00'
    # validations
    dv_el = DataValidation(type="list", formula1='"Primary,General,Special,Runoff"', allow_blank=True)
    dv_m = DataValidation(type="list", formula1='"Check,Credit Card,Cash,In-Kind,ACH,Other"', allow_blank=True)
    ws.add_data_validation(dv_el); ws.add_data_validation(dv_m)
    dv_el.add(f"H{hr+1}:H{hr+200}"); dv_m.add(f"I{hr+1}:I{hr+200}")
    widths(ws, {"A":12,"B":22,"C":24,"D":20,"E":18,"F":18,"G":12,"H":12,"I":13,"J":16,"K":14,"L":15,"M":24})
    ws.freeze_panes = "A5"
    _instructions(wb, [
        "CONTRIBUTION TRACKER — how to use",
        "",
        "1. Log every contribution the day it is received.",
        "2. 'Aggregate to Date' auto-sums all gifts from the same donor name — match names exactly.",
        "3. When aggregate exceeds $200, the 'Itemize?' column flags YES: you must record",
        "   name, address, occupation, and employer for FEC itemized reporting.",
        "4. Track Primary and General separately — each has its own $3,300 individual limit (2025-26).",
        "5. Resolve any excessive contribution within 30 days (refund / redesignate / reattribute).",
        "",
        "Limits are for the 2025-2026 federal cycle. VERIFY current limits at fec.gov.",
        "Educational template, not legal advice. Never store SSNs or bank credentials here.",
    ])
    wb.save(TOOLS / "contribution-tracker.xlsx")
    _csv("contribution-tracker.csv", cols)
    print("  ✓ contribution-tracker.xlsx + .csv")

# ---------------------------------------------------------------- 2. Expenditures
def expenditure_tracker():
    wb = Workbook(); ws = wb.active; ws.title = "Expenditures"
    cols = ["Date","Payee","Address","Purpose","Category","Amount","Method","Itemize? (>$200)","Invoice #","Notes"]
    banner(ws, "Expenditure Tracker", "Grant for Congress (MO-02) — log every disbursement. Itemize payees over $200.", len(cols))
    hr = 4
    for i, c in enumerate(cols, 1): ws.cell(row=hr, column=i, value=c)
    style_header(ws, hr, len(cols))
    for r in range(hr+1, hr+201):
        ws.cell(row=r, column=8, value=f'=IF(F{r}="","",IF(F{r}>200,"YES",""))')
        ws.cell(row=r, column=6).number_format = '"$"#,##0.00'
    tr = hr + 201
    ws.cell(row=tr, column=5, value="TOTAL SPENT:").font = Font(bold=True, color=NAVY)
    tot = ws.cell(row=tr, column=6, value=f"=SUM(F{hr+1}:F{hr+200})")
    tot.font = Font(bold=True, color=NAVY); tot.number_format = '"$"#,##0.00'
    dv_cat = DataValidation(type="list", allow_blank=True,
        formula1='"Voter Contact,Mail,Digital Ads,Printing,Staff/Payroll,Consulting,Events,Office/Admin,Travel,Fundraising,Compliance,Other"')
    dv_m = DataValidation(type="list", formula1='"Check,Credit Card,Debit,ACH,Cash,Other"', allow_blank=True)
    ws.add_data_validation(dv_cat); ws.add_data_validation(dv_m)
    dv_cat.add(f"E{hr+1}:E{hr+200}"); dv_m.add(f"G{hr+1}:G{hr+200}")
    widths(ws, {"A":12,"B":24,"C":24,"D":26,"E":18,"F":12,"G":12,"H":14,"I":12,"J":24})
    ws.freeze_panes = "A5"
    # category summary sheet
    s = wb.create_sheet("By Category")
    s["A1"] = "Spending by Category"; s["A1"].font = title_font
    cats = ["Voter Contact","Mail","Digital Ads","Printing","Staff/Payroll","Consulting","Events","Office/Admin","Travel","Fundraising","Compliance","Other"]
    s.cell(row=3, column=1, value="Category"); s.cell(row=3, column=2, value="Total")
    style_header(s, 3, 2)
    for i, cat in enumerate(cats, 4):
        s.cell(row=i, column=1, value=cat)
        c = s.cell(row=i, column=2, value=f"=SUMIF(Expenditures!$E:$E,A{i},Expenditures!$F:$F)")
        c.number_format = '"$"#,##0.00'
    widths(s, {"A":20,"B":14})
    _instructions(wb, [
        "EXPENDITURE TRACKER — how to use",
        "",
        "1. Log every disbursement with payee, purpose, and category.",
        "2. Payments over $200 to a payee must be itemized in FEC reports ('Itemize?' = YES).",
        "3. The 'By Category' tab auto-totals spending so you can watch your budget mix.",
        "4. Reconcile this tracker to your bank statement before every reporting deadline.",
        "",
        "Educational template, not legal/financial advice. Verify itemization rules at fec.gov.",
    ])
    wb.save(TOOLS / "expenditure-tracker.xlsx")
    _csv("expenditure-tracker.csv", cols)
    print("  ✓ expenditure-tracker.xlsx + .csv (with category summary)")

# ---------------------------------------------------------------- 3. Donor limit checker
def donor_limit_checker():
    wb = Workbook(); ws = wb.active; ws.title = "Limit Checker"
    banner(ws, "Donor Limit Checker", "Enter what a donor has given per election; see remaining headroom. 2025-26 federal limits.", 4)
    ws["A4"] = "Donor / Entity type"; ws["A4"].font = hdr_font; ws["A4"].fill = hdr_fill
    ws["B4"] = "Election"; ws["B4"].font = hdr_font; ws["B4"].fill = hdr_fill
    ws["C4"] = "Given so far"; ws["C4"].font = hdr_font; ws["C4"].fill = hdr_fill
    ws["D4"] = "Limit"; ws["D4"].font = hdr_font; ws["D4"].fill = hdr_fill
    ws["E4"] = "Remaining"; ws["E4"].font = hdr_font; ws["E4"].fill = hdr_fill
    ws["F4"] = "Status"; ws["F4"].font = hdr_font; ws["F4"].fill = hdr_fill
    # limits reference (hidden helper area)
    limits = {"Individual":3300, "Multicandidate PAC":5000, "Party Committee":5000, "Non-Multicandidate PAC":2900}
    ws["H4"] = "Type"; ws["I4"] = "Per-election limit"
    for i,(k,v) in enumerate(limits.items(), 5):
        ws.cell(row=i, column=8, value=k); ws.cell(row=i, column=9, value=v).number_format='"$"#,##0'
    for r in range(5, 25):
        ws.cell(row=r, column=4, value=f'=IFERROR(VLOOKUP(A{r},$H$5:$I$8,2,FALSE),"")')
        ws.cell(row=r, column=5, value=f'=IF(OR(A{r}="",C{r}=""),"",D{r}-C{r})')
        ws.cell(row=r, column=6, value=f'=IF(OR(A{r}="",C{r}=""),"",IF(C{r}>D{r},"OVER LIMIT — refund/redesignate",IF(C{r}=D{r},"At max","OK")))')
        for col in (3,4,5): ws.cell(row=r, column=col).number_format = '"$"#,##0.00'
    dv = DataValidation(type="list", formula1='"Individual,Multicandidate PAC,Non-Multicandidate PAC,Party Committee"', allow_blank=True)
    dv2 = DataValidation(type="list", formula1='"Primary,General,Special,Runoff"', allow_blank=True)
    ws.add_data_validation(dv); ws.add_data_validation(dv2)
    dv.add("A5:A24"); dv2.add("B5:B24")
    widths(ws, {"A":24,"B":12,"C":14,"D":12,"E":14,"F":32,"G":3,"H":24,"I":16})
    ws["A26"] = "Corporations & unions: prohibited from direct contributions. Primary & general are separate elections."
    ws["A26"].font = note_font
    ws["A27"] = "Limits reflect the 2025-2026 cycle. VERIFY at fec.gov. Educational tool, not legal advice."
    ws["A27"].font = note_font
    wb.save(TOOLS / "donor-limit-checker.xlsx")
    print("  ✓ donor-limit-checker.xlsx")

# ---------------------------------------------------------------- 4. Voter contact tracker
def voter_contact_tracker():
    cols = ["Voter ID","Name","Address","Phone","Support (1-5)","Top Issue","Yard Sign?","Volunteer?","Voted?","Contact Date","Method","Notes"]
    wb = Workbook(); ws = wb.active; ws.title = "Voter Contacts"
    banner(ws, "Voter Contact Tracker", "Grant for Congress (MO-02) — ID every voter 1-5. Never contact confirmed opposition during GOTV.", len(cols))
    hr = 4
    for i, c in enumerate(cols, 1): ws.cell(row=hr, column=i, value=c)
    style_header(ws, hr, len(cols))
    dv_s = DataValidation(type="list", formula1='"1,2,3,4,5"', allow_blank=True)
    dv_yn = DataValidation(type="list", formula1='"Yes,No"', allow_blank=True)
    dv_m = DataValidation(type="list", formula1='"Door,Phone,Text,Email,Event"', allow_blank=True)
    for dv in (dv_s, dv_yn, dv_m): ws.add_data_validation(dv)
    dv_s.add(f"E{hr+1}:E{hr+500}"); dv_yn.add(f"G{hr+1}:H{hr+500}"); dv_yn.add(f"I{hr+1}:I{hr+500}"); dv_m.add(f"K{hr+1}:K{hr+500}")
    widths(ws, {"A":10,"B":22,"C":26,"D":14,"E":12,"F":18,"G":11,"H":11,"I":9,"J":12,"K":10,"L":24})
    ws.freeze_panes = "A5"
    # summary
    s = wb.create_sheet("Tally")
    s["A1"] = "Support Tally"; s["A1"].font = title_font
    rows = [("5 — Strong support",5),("4 — Lean support",4),("3 — Undecided",3),("2 — Lean opposed",2),("1 — Strong opposed",1)]
    s.cell(row=3,column=1,value="Level"); s.cell(row=3,column=2,value="Count"); style_header(s,3,2)
    for i,(lbl,val) in enumerate(rows,4):
        s.cell(row=i,column=1,value=lbl)
        s.cell(row=i,column=2,value=f"=COUNTIF('Voter Contacts'!$E:$E,{val})")
    widths(s, {"A":22,"B":10})
    wb.save(TOOLS / "voter-contact-tracker.xlsx")
    _csv("voter-contact-tracker.csv", cols)
    print("  ✓ voter-contact-tracker.xlsx + .csv (with tally)")

# ---------------------------------------------------------------- helpers
def _csv(name, cols):
    with open(TOOLS / name, "w", newline="") as f:
        csv.writer(f).writerow(cols)

def _instructions(wb, lines):
    ws = wb.create_sheet("Instructions")
    for i, line in enumerate(lines, 1):
        c = ws.cell(row=i, column=1, value=line)
        if i == 1: c.font = title_font
        else: c.font = Font(size=10, color="FF334155")
    ws.column_dimensions["A"].width = 95

# ---------------------------------------------------------------- 5. ICS filing calendar
def filing_calendar_ics():
    # Stable 2026 federal quarterly + year-end deadlines (House, quarterly filer).
    events = [
        ("July Quarterly Report (Apr 1–Jun 30)", "20260715"),
        ("October Quarterly Report (Jul 1–Sep 30)", "20261015"),
        ("Year-End Report (Oct 1–Dec 31)", "20270131"),
    ]
    now = datetime.datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
    lines = ["BEGIN:VCALENDAR","VERSION:2.0","PRODID:-//Grant for Congress//Filing Calendar//EN","CALSCALE:GREGORIAN"]
    for i,(summary, date) in enumerate(events,1):
        lines += [
            "BEGIN:VEVENT", f"UID:grant-filing-{i}-{date}@campaign", f"DTSTAMP:{now}",
            f"DTSTART;VALUE=DATE:{date}", f"SUMMARY:FEC FILING DUE — {summary}",
            "DESCRIPTION:Federal (FEC) reporting deadline. VERIFY exact date at fec.gov before relying on it. Pre-primary and pre-general reports are date-specific to your election and are NOT included here — add them manually. Educational reminder\\, not legal advice.",
            "BEGIN:VALARM","TRIGGER:-P14D","ACTION:DISPLAY","DESCRIPTION:FEC report due in 14 days","END:VALARM",
            "BEGIN:VALARM","TRIGGER:-P3D","ACTION:DISPLAY","DESCRIPTION:FEC report due in 3 days","END:VALARM",
            "END:VEVENT",
        ]
    lines.append("END:VCALENDAR")
    (TOOLS / "fec-filing-calendar.ics").write_text("\r\n".join(lines) + "\r\n")
    # companion CSV
    with open(TOOLS / "filing-deadline-calendar.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["Report","Period Covered","Due Date","14-day alarm","Filed?"])
        for summary, date in events:
            d = datetime.datetime.strptime(date, "%Y%m%d")
            w.writerow([summary.split(" (")[0], summary.split("(")[1].rstrip(")") if "(" in summary else "",
                        d.strftime("%Y-%m-%d"), (d - datetime.timedelta(days=14)).strftime("%Y-%m-%d"), ""])
        w.writerow(["Pre-Primary Report","through 20 days before primary","[ADD — 12 days before primary]","",""])
        w.writerow(["Pre-General Report","through 20 days before general","[ADD — 12 days before general]","",""])
        w.writerow(["Post-General Report","through 20 days after general","[ADD — 30 days after general]","",""])
    print("  ✓ fec-filing-calendar.ics + filing-deadline-calendar.csv")

if __name__ == "__main__":
    print("Building tools...")
    contribution_tracker(); expenditure_tracker(); donor_limit_checker()
    voter_contact_tracker(); filing_calendar_ics()
