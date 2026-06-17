# Grant for Congress (MO-02) — Campaign Asset Arsenal

A ready-to-use kit of campaign **documents (PDF)**, **tools (spreadsheets/calendar)**, and
**images** for *Matt Grant for Congress*, Missouri's 2nd District. Built from the **Get Elected**
skill templates. Packaged 2026-06-17.

> **Sample candidate.** "Matt Grant / MO-02" is a worked example. Bracketed fields like
> `[DATE]`, `[AMOUNT]`, `[WEBSITE]` are placeholders — find-and-replace them with your real
> details. Everything here is reusable for any U.S. House campaign.

---

## 📄 documents/ — 12 branded PDFs

| File | What it is |
|---|---|
| `campaign-plan.pdf` | Win-number math, vote goals, phases, budget frame, risk plan |
| `fundraising-plan.pdf` | Dollar goal, source breakdown, call-time discipline, ask ladder |
| `call-time-script.pdf` | Candidate finance-call script + per-prospect caller card |
| `stump-speech.pdf` | Fill-in-the-blank 5–7 min speech with delivery notes & variants |
| `press-release-launch.pdf` | One-page launch release + distribution checklist |
| `palm-card.pdf` | Print-ready 2-sided walk-piece copy + print specs |
| `candidate-onepager.pdf` | Bio/values leave-behind for press, donors, endorsers |
| `volunteer-onepager.pdf` | Recruitment handout with role menu + sign-up frame |
| `canvass-scripts.pdf` | Door, phone, and text scripts with data-capture fields |
| `gotv-plan.pdf` | Final-72-hours turnout plan, universe, vote-plan asks |
| `first-30-days.pdf` | Sequenced launch checklist (legal → money → team → launch) |
| `compliance-calendar.pdf` | Federal (FEC) registration + reporting schedule reference |

## 🧰 tools/ — trackers, calculators, calendar

| File | What it does |
|---|---|
| `contribution-tracker.xlsx` | Logs receipts; auto-sums per-donor aggregate; flags $200 itemization; Primary/General dropdowns; totals |
| `expenditure-tracker.xlsx` | Logs disbursements; "By Category" auto-summary tab; itemization flag |
| `donor-limit-checker.xlsx` | Enter a donor's giving → shows remaining headroom vs. 2025-26 federal limits + OVER-LIMIT warning |
| `voter-contact-tracker.xlsx` | 1–5 support ID, issue, sign/volunteer/voted flags; live support tally tab |
| `fec-filing-calendar.ics` | Importable calendar (Google/Apple/Outlook) with quarterly FEC deadlines + 14-day & 3-day alarms |
| `filing-deadline-calendar.csv` | Same deadlines as a spreadsheet, with pre-primary/general rows to fill |
| `*.csv` | Plain-CSV versions of each tracker for any database/CRM import |
| `disclaimer-generator.html` | Open in a browser → build a compliant "Paid for by…" disclaimer for any medium |

## 🖼️ images/

**`images/graphics/`** — social/web graphics (1280×720, navy + red brand):
- `launch-im-running.png` — "I'm Running for Congress" launch card
- `issue-cost-of-living.png` — "Lower the Cost of Living"
- `issue-stronger-schools.png` — "Stronger Schools"
- `issue-social-security-medicare.png` — "Social Security & Medicare"

**`images/thumbnails/`** — video thumbnails (candidate story):
- `thumbnail-v2-classroom-to-congress-score66.png` — **recommended final**
- `thumbnail-v1-classroom-to-congress-score48.png` — earlier draft (reference)

## 🛠️ build/ — reproducible source

`build/src/*.md` (document sources), `brand.css` + `md2pdf.py` (PDF pipeline), and
`make_tools.py` (spreadsheet/calendar generator). Re-run to regenerate everything after edits.

---

## Hosted in Canva (not bundled — network policy blocks Canva's export host)

- **Yard sign** — "Refined Navy Yard Sign with Spacious Design"
  - View: https://www.canva.com/d/fQ9aqVJUM8Oipx6 · Edit: https://www.canva.com/d/CNOwQkgzrs5hOTu

## Known gaps / next steps

- **Canva graphic generation** was down for this whole session (8 failed attempts) — the launch/issue
  graphics above were produced via the working image generator instead. Retry Canva when it recovers if
  you want square (1:1) IG-native versions.
- **Google Calendar** sync of deadlines needs re-auth.
- **Public website deploy (Vercel)** awaits your explicit go-ahead.

---

*This package contains campaign materials and educational templates only. Compliance content
(contribution limits, filing deadlines, disclaimers) is **educational information, not legal advice** —
verify all current rules with the FEC (fec.gov) and your state/local election authority, and consult a
campaign finance attorney for your situation. Limits shown reflect the 2025–2026 federal cycle. Handle
donor data securely; never store SSNs or bank credentials.*
