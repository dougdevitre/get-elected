#!/usr/bin/env python3
"""Render the Matt Grant (MO-02) Campaign Manager Playbook to a branded PDF.

Usage:  python3 build_pdf.py
Requires: weasyprint  (pip install weasyprint)
Output:   Matt-Grant-MO02-Campaign-Manager-Playbook.pdf
"""
import os
from weasyprint import HTML

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "Matt-Grant-MO02-Campaign-Manager-Playbook.pdf")

NAVY = "#0f1f3d"
RED = "#c8102e"
LIGHT = "#f4f6fa"
GREY = "#5b6472"

CSS = f"""
@page {{
  size: Letter;
  margin: 20mm 16mm 18mm 16mm;
  @bottom-center {{
    content: "Matt Grant for Congress · MO-02 · Campaign Manager Playbook";
    font-size: 8pt; color: {GREY};
  }}
  @bottom-right {{ content: "Page " counter(page); font-size: 8pt; color: {GREY}; }}
}}
@page cover {{ margin: 0; }}
* {{ box-sizing: border-box; }}
body {{ font-family: 'Helvetica Neue', Arial, sans-serif; color: #1a1a1a; font-size: 10pt; line-height: 1.5; }}
h1, h2, h3 {{ color: {NAVY}; line-height: 1.2; }}
h2 {{ font-size: 16pt; border-bottom: 3px solid {RED}; padding-bottom: 4px; margin-top: 26px; }}
h3 {{ font-size: 12pt; margin-top: 18px; color: {RED}; }}
p {{ margin: 6px 0; }}
a {{ color: {NAVY}; }}
.section {{ page-break-before: always; }}
table {{ width: 100%; border-collapse: collapse; margin: 10px 0; font-size: 8.6pt; }}
th {{ background: {NAVY}; color: #fff; text-align: left; padding: 6px 8px; }}
td {{ border-bottom: 1px solid #d8dde6; padding: 5px 8px; vertical-align: top; }}
tr:nth-child(even) td {{ background: {LIGHT}; }}
.small {{ font-size: 8.5pt; color: {GREY}; }}
ul {{ margin: 6px 0 6px 0; padding-left: 18px; }}
li {{ margin: 3px 0; }}
.callout {{ background: {LIGHT}; border-left: 5px solid {RED}; padding: 10px 14px; margin: 12px 0; font-size: 9pt; }}
.tag {{ display: inline-block; background: {RED}; color: #fff; font-size: 7.5pt; font-weight: bold;
        padding: 2px 7px; border-radius: 10px; letter-spacing: .5px; }}
.kpi {{ font-weight: bold; color: {NAVY}; }}

/* Cover */
.cover {{ page: cover; page-break-after: always; height: 100vh; background: {NAVY}; color: #fff;
         padding: 38mm 24mm; position: relative; }}
.cover .bar {{ width: 70px; height: 8px; background: {RED}; margin-bottom: 28px; }}
.cover h1 {{ color: #fff; font-size: 34pt; margin: 0 0 6px 0; }}
.cover .sub {{ font-size: 15pt; color: #c6d0e2; margin-bottom: 30px; }}
.cover .tagline {{ font-size: 13pt; color: {RED}; font-weight: bold; letter-spacing: .5px; }}
.cover .meta {{ position: absolute; bottom: 34mm; left: 24mm; right: 24mm; font-size: 9.5pt; color: #c6d0e2; }}
.cover .meta strong {{ color: #fff; }}
.cover .disc {{ position: absolute; bottom: 16mm; left: 24mm; right: 24mm; font-size: 7.8pt; color: #93a2bf; }}

/* Flow boxes (mermaid replacement that renders in PDF) */
.flow {{ display: flex; flex-wrap: wrap; gap: 8px; margin: 12px 0; }}
.node {{ flex: 1 1 0; min-width: 90px; background: {LIGHT}; border: 1px solid #cdd5e2;
         border-top: 4px solid {NAVY}; padding: 8px 10px; font-size: 8.4pt; text-align: center; }}
.node b {{ color: {NAVY}; display: block; font-size: 9pt; margin-bottom: 3px; }}
.arrow {{ align-self: center; color: {RED}; font-weight: bold; font-size: 14pt; }}
.cardgrid {{ display: flex; flex-wrap: wrap; gap: 10px; }}
.card {{ flex: 1 1 45%; border: 1px solid #d8dde6; border-top: 4px solid {RED};
         padding: 10px 12px; font-size: 8.6pt; }}
.card h4 {{ margin: 0 0 4px 0; color: {NAVY}; font-size: 10pt; }}
"""

def flow(*nodes):
    parts = []
    for i, n in enumerate(nodes):
        parts.append(f'<div class="node">{n}</div>')
        if i < len(nodes) - 1:
            parts.append('<div class="arrow">&rarr;</div>')
    return f'<div class="flow">{"".join(parts)}</div>'

cover = f"""
<div class="cover">
  <div class="bar"></div>
  <h1>Campaign Manager's<br>Field Manual</h1>
  <div class="sub">Matt Grant for Congress &middot; Missouri's 2nd District</div>
  <div class="tagline">Lower costs. Stronger schools. Showing up.</div>
  <div class="meta">
    <strong>End-to-end execution playbook</strong> &mdash; strategy, channels, apps &amp; integrations<br>
    Window: <strong>June 17 &rarr; August 4, 2026 (Primary)</strong> &middot; General: Nov 3, 2026<br>
    Win number: <strong>~16,500 votes</strong> &middot; Primary budget: <strong>$350,000</strong><br>
    Prepared for the campaign manager &middot; compliance facts verified <strong>2026-06-17</strong>
  </div>
  <div class="disc">
    Illustrative example. The candidate and dollar figures are fictional; district data, election
    dates, FEC contribution limits and reporting deadlines are real and web-sourced.
    Educational information, not legal advice &mdash; consult a campaign finance attorney or the FEC.
  </div>
</div>
"""

# ---- Section 1: Strategy snapshot ----
s1 = f"""
<div class="section">
<h2>1 &middot; The Race at a Glance</h2>
<p>You have been hired as campaign manager for <strong>Matt Grant</strong> with <span class="kpi">48 days</span>
to the <strong>August 4, 2026 Democratic primary</strong> for U.S. House, MO-02. August 4 is the
<em>primary</em> &mdash; winning it makes Matt the nominee for the <strong>November 3 general</strong>.
This manual is scoped to winning the primary.</p>

<table>
<tr><th>Item</th><th>Value</th><th>Item</th><th>Value</th></tr>
<tr><td>Office</td><td>U.S. House, MO-02</td><td>Jurisdiction</td><td>FEC + Missouri ballot access</td></tr>
<tr><td>Primary</td><td><b>Aug 4, 2026</b></td><td>District lean</td><td>Cook PVI R+4 (STL suburbs)</td></tr>
<tr><td>Win number (3-way)</td><td><b>~16,500 votes</b></td><td>Voter ID goal</td><td>35,000&ndash;40,000</td></tr>
<tr><td>Primary budget</td><td><b>$350,000</b></td><td>Cash-on-hand by Jul 23</td><td>$60,000+</td></tr>
<tr><td>Core message</td><td colspan="3">&ldquo;Lower costs, stronger schools, and a representative who actually shows up.&rdquo;</td></tr>
</table>

<h3>The four engines you run at once</h3>
{flow("<b>MONEY</b>Fundraising &amp; finance", "<b>MESSAGE</b>Content &amp; channels",
      "<b>FIELD</b>Voter contact &amp; GOTV", "<b>COMPLIANCE</b>FEC &amp; data")}

<div class="callout"><b>Theory of victory.</b> Consolidate the grassroots / electability share of the
small primary electorate &mdash; concentrated in St. Louis County &mdash; behind one credible local
candidate, while two opponents split the rest. Win it at the doors with the highest voter-contact
operation in the race, not on TV.</div>

<h3>Hard external dates (real, sourced &middot; verified 2026-06-17)</h3>
<table>
<tr><th>Date</th><th>Event</th><th>Owner</th></tr>
<tr><td>Jul 15, 2026</td><td><b>FEC July Quarterly report due</b> (covers Apr 1&ndash;Jun 30)</td><td>Treasurer</td></tr>
<tr><td>Jul 16&ndash;Aug 1</td><td><b>48-hour notice</b> window for contributions &ge; $1,000</td><td>Treasurer</td></tr>
<tr><td>Jul 23, 2026</td><td><b>FEC 12-Day Pre-Primary report due</b> (covers Jul 1&ndash;15)</td><td>Treasurer</td></tr>
<tr><td>Aug 4, 2026</td><td><b>PRIMARY ELECTION DAY</b></td><td>All</td></tr>
</table>
<p class="small">Contribution limits (2025&ndash;2026): individual <b>$3,500/election</b>; multicandidate PAC
<b>$5,000/election</b>. Primary and general are separate elections. Source: FEC.</p>
</div>
"""

# ---- Section 2: Tech stack ----
stack_rows = [
    ("Website / digital HQ", "Next.js on Vercel", "Vercel ★", "$"),
    ("Donations / payments", "ActBlue + Stripe (merch)", "Stripe ★", "% of raise"),
    ("Donor / finance CRM", "Numero / Airtable", "via Drive", "$$"),
    ("Voter file & field CRM", "VAN / PDI + MiniVAN", "vendor", "$$"),
    ("Prospect / donor research", "Apollo.io", "Apollo ★", "$$"),
    ("Mass email (ESP)", "ActBlue Express / Mailchimp", "drafts via Lois247 ★", "$"),
    ("Finance / VIP email (1:1)", "Gmail", "Gmail ★", "$"),
    ("Peer-to-peer SMS", "Scale to Win / Hustle", "vendor", "$$"),
    ("Design / creative", "Canva", "Canva ★", "$"),
    ("Video / YouTube growth", "vidIQ + YouTube", "vidIQ ★", "$"),
    ("Content drafting", "in-house + Lois247", "Lois247 ★", "$"),
    ("Team chat & ops", "Slack", "Slack ★", "$"),
    ("Docs & storage", "Google Drive", "Drive ★", "$"),
    ("Calendar / deadlines", "Google Calendar", "Calendar ★", "$"),
    ("Diagrams / process maps", "Mermaid", "Mermaid ★", "free"),
    ("Website repo", "GitHub", "GitHub ★", "free"),
]
rows_html = "".join(
    f"<tr><td>{a}</td><td>{b}</td><td>{c}</td><td>{d}</td></tr>" for a, b, c, d in stack_rows
)
s2 = f"""
<div class="section">
<h2>2 &middot; The Campaign Tech Stack</h2>
<p>One source of truth per data type. Every channel carries the disclaimer and feeds data back.
Tools marked <span class="tag">&starf; CONNECTED</span> can be wired up directly from your assistant today (see Section&nbsp;7).</p>
<table>
<tr><th>Function</th><th>Recommended tool</th><th>Connected integration</th><th>Cost</th></tr>
{rows_html}
</table>
<div class="callout"><b>Golden data rule.</b> Money data &rarr; Donor CRM &rarr; FEC reports.
People / volunteer / ID data &rarr; VAN &rarr; GOTV flush list. The website and ads only
<i>acquire</i>; the CRMs <i>remember</i>.</div>
</div>
"""

# ---- Section 3: Week-1 sprint ----
sprint = [
    ("Mon", "Domain + Vercel site skeleton (splash &rarr; email capture + ActBlue button); Google Workspace (shared Drive, group inboxes)", "Site live with working donate + sign-up"),
    ("Tue", "ActBlue page + Stripe for merch; donor CRM; import past-donor list via Apollo enrichment", "A test $5 donation flows into the CRM"),
    ("Wed", "Voter file / VAN access; cut Tier-1 turf; MiniVAN canvass app; P2P texting account pending", "A canvasser can pull a turf packet on their phone"),
    ("Thu", "Social accounts claimed + branded; Canva brand kit (logo, colors, fonts); vidIQ + YouTube", "All handles live with matching art + pinned intro"),
    ("Fri", "Slack workspace + channels + ops canvas; Calendar loaded with FEC deadlines + call time + shifts; Gmail finance templates drafted", "Team in Slack; calendar shows Jul 15 / Jul 23 / Aug 4"),
]
sprint_html = "".join(
    f"<tr><td><b>{d}</b></td><td>{b}</td><td>{r}</td></tr>" for d, b, r in sprint
)
s3 = f"""
<div class="section">
<h2>3 &middot; Week-1 Setup Sprint (stand up the whole stack)</h2>
<p>Run this June 17&ndash;22 so every channel is live before the first full canvass weekend (Sat Jun 20).</p>
<table>
<tr><th>Day</th><th>Build</th><th>Done when</th></tr>
{sprint_html}
</table>
<h3>Brand kit (lock Day 4, use everywhere)</h3>
<ul>
<li><b>Colors:</b> deep navy + warm red accent + clean white (suburban, trustworthy).</li>
<li><b>Logo lockup:</b> <b>GRANT</b> wordmark + &ldquo;for Congress &middot; MO-02&rdquo;.</li>
<li><b>Tagline:</b> <i>Lower costs. Stronger schools. Showing up.</i></li>
</ul>
</div>
"""

# ---- Section 4: Channel quick-start cards ----
channels = [
    ("5.1 Website / HQ &mdash; Vercel", "Convert visitors to donors, volunteers, emails.",
     "Next.js template; pages = Home, Issues, About, Volunteer, Donate, Events, Press; forms &rarr; CRM.",
     "Sign-ups/week; donate conversion %"),
    ("5.2 Email &mdash; Gmail + ESP", "1:1 finance via Gmail; small-dollar via ESP.",
     "3&ndash;5 mass/week &rarr; daily final week; peak on Jul 15 &amp; Jul 23 + final 72 hrs.",
     "$/email; open & click; list growth"),
    ("5.3 Peer-to-peer SMS", "GOTV, recruiting, deadline-day asks, ballot chase.",
     "Opt-in numbers only; scripts mirror the field phone script; ramps with the chase.",
     "IDs + ballot returns from texts"),
    ("5.4 Social (organic) + Canva", "Cheap reach, recruiting, momentum, rapid response.",
     "Brand kit + templates; 1&ndash;2 posts/day across FB/IG/X/TikTok/YouTube.",
     "Reach; sign-ups; share rate"),
    ("5.5 Video / YouTube &mdash; vidIQ", "Searchable, persuasive video library.",
     "1 anchor video/week + 2&ndash;3 shorts; launch, 3 issue shorts, testimonials, GOTV.",
     "Retention %; search views; CTR"),
    ("5.6 Paid digital ads", "Cost-efficient persuasion + GOTV (no broadcast TV).",
     "Verify political-advertiser status Week 1; live Jul 16; heavy-up final 10 days.",
     "Cost per ID; cost per donor"),
    ("5.7 Direct mail", "Workhorse persuasion + GOTV ($70K).",
     "4 pieces: intro &rarr; issues &rarr; contrast &rarr; GOTV (in homes by Jul 31).",
     "Cost/piece; GOTV lift"),
    ("5.8 Earned media / PR", "Free credibility &mdash; local TV, Post-Dispatch, radio.",
     "Press list + media kit; release at each milestone; op-ed mid-campaign.",
     "Placements/week; share of voice"),
    ("5.9 Field / canvassing", "The engine: 35&ndash;40K IDs, turn out the 1s &amp; 2s.",
     "VAN + MiniVAN; canvass Thu/Sat/Sun &rarr; daily final 10 days; chase from early July.",
     "IDs/day; contacts/shift; returns"),
    ("5.10 Fundraising &mdash; ActBlue", "Frictionless legal giving, reconciled for FEC.",
     "Primary-designated page; limit checks wired in; surge on deadlines + final 72 hrs.",
     "$/day; avg gift; COH for Jul 23"),
    ("5.11 Prospecting &mdash; Apollo", "Build/enrich call-time + host-committee lists.",
     "Import universe; enrich + segment by capacity; daily call sheets to candidate.",
     "Qualified prospects/week"),
    ("5.12 Ops &mdash; Slack/Drive/Calendar", "One nervous system for staff + volunteers.",
     "Channels + ops canvas; Drive mirrors the playbook; 8:30 standup; deadline reminders.",
     "Standup adherence; deadline hit-rate"),
]
cards = "".join(
    f'<div class="card"><h4>{t}</h4><p><b>Goal:</b> {g}</p><p><b>Setup/cadence:</b> {s}</p>'
    f'<p class="small"><b>KPI:</b> {k}</p></div>'
    for t, g, s, k in channels
)
s4 = f"""
<div class="section">
<h2>4 &middot; Channel Playbooks (quick-start cards)</h2>
<p>Every paid or public item carries <b>&ldquo;Paid for by Matt Grant for Congress.&rdquo;</b>
Full detail per channel is in <span class="small">08-channel-implementation-playbook.md</span>.</p>
<div class="cardgrid">{cards}</div>
</div>
"""

# ---- Section 5: Rhythm + KPIs ----
s5 = f"""
<div class="section">
<h2>5 &middot; The Weekly Operating Rhythm</h2>
{flow("<b>MON</b>Standup &middot; week goals &middot; finance push",
      "<b>TUE</b>Content batch &middot; call time",
      "<b>WED</b>Media pitch &middot; phones",
      "<b>THU</b>Canvass eve &middot; email")}
{flow("<b>FRI</b>Reconcile $ &middot; compliance check",
      "<b>SAT</b>BIG canvass &middot; social from trail",
      "<b>SUN</b>Metrics &middot; plan next week")}
<ul>
<li><b>Daily:</b> candidate call time (2&ndash;3 hrs) + a voter-contact shift + 1&ndash;2 social posts.</li>
<li><b>Weekly:</b> one earned-media hit, one email, one anchor video, one finance event, Sunday metrics.</li>
<li><b>Deadline weeks (Jul 15, Jul 23):</b> compliance + finance override everything else.</li>
</ul>

<h2>KPI Dashboard (post in Slack every Sunday)</h2>
<table>
<tr><th>Metric</th><th>Target by Aug 4</th><th>Source</th></tr>
<tr><td>Raised (cumulative)</td><td><b>$350,000</b></td><td>Donor CRM / ActBlue</td></tr>
<tr><td>Cash on hand at Jul 23 report</td><td><b>$60,000+</b></td><td>Donor CRM</td></tr>
<tr><td>Voter IDs</td><td>35,000&ndash;40,000</td><td>VAN</td></tr>
<tr><td>Confirmed 1&ndash;2 supporters</td><td>&ge; 20,000</td><td>VAN</td></tr>
<tr><td>Active volunteers</td><td>150&ndash;250</td><td>VAN / Slack</td></tr>
<tr><td>FEC deadlines hit</td><td><b>100%</b></td><td>Compliance</td></tr>
</table>
</div>
"""

# ---- Section 6: Compliance ----
s6 = f"""
<div class="section">
<h2>6 &middot; Compliance Overlay (wired into every tool)</h2>
<ul>
<li><b>Disclaimer</b> auto-included in site footer, email templates, ad accounts, mail proofs, paid-social presets, lit templates.</li>
<li><b>Limit checks</b> in the ActBlue/CRM intake flag anyone nearing <b>$3,500</b> (primary).</li>
<li><b>48-hour-notice trigger:</b> a Slack alert + treasurer task fires on any <b>$1,000+</b> gift during <b>Jul 16&ndash;Aug 1</b>.</li>
<li><b>Calendar reminders</b> for <b>Jul 15</b> and <b>Jul 23</b> set 5 days early.</li>
<li><b>Data privacy:</b> donor PII access-restricted; no SSNs / bank / card numbers stored.</li>
<li><b>Firewall:</b> zero coordination with Super PACs.</li>
<li><b>Never accept:</b> corporate/union treasury funds, foreign nationals, federal contractors, straw donors, cash over $100.</li>
</ul>
<div class="callout"><b>This is educational information, not legal advice.</b> Consult a campaign finance
attorney or the FEC for guidance specific to your situation. Compliance facts verified 2026-06-17.</div>
</div>
"""

# ---- Section 7: What I can execute ----
exec_rows = [
    ("1", "Load FEC deadlines, call-time blocks &amp; canvass shifts into your calendar", "Google Calendar", "Yes &mdash; changes your calendar"),
    ("2", "Draft the finance, endorsement &amp; 6-email fundraising sequence as Gmail drafts", "Gmail", "No &mdash; drafts only"),
    ("3", "Design the brand kit, palm card, yard sign &amp; a week of social graphics", "Canva", "No &mdash; creates designs"),
    ("4", "Generate YouTube titles, descriptions &amp; thumbnails (launch + 3 issue shorts)", "vidIQ", "No &mdash; creates assets"),
    ("5", "Build the Slack ops canvas + channel structure + weekly metrics template", "Slack", "Yes &mdash; posts to workspace"),
    ("6", "Stand up the website skeleton &amp; deploy a splash page", "Vercel", "Yes &mdash; public deploy"),
    ("7", "Build the call-time prospect list with enriched contacts", "Apollo", "No &mdash; internal list"),
    ("8", "Draft press releases &amp; op-ed via the content engine", "Lois247", "No &mdash; drafts"),
    ("9", "Create the shared Drive folder structure mirroring this playbook", "Google Drive", "Yes &mdash; creates files"),
]
exec_html = "".join(
    f"<tr><td>{n}</td><td>{a}</td><td>{i}</td><td>{o}</td></tr>" for n, a, i, o in exec_rows
)
s7 = f"""
<div class="section">
<h2>7 &middot; What Your Assistant Can Execute Now</h2>
<p>These are live integrations connected to this workspace. Pick any to start &mdash; I confirm before
anything sends or publishes externally.</p>
<table>
<tr><th>#</th><th>Action</th><th>Integration</th><th>Outward-facing?</th></tr>
{exec_html}
</table>
<div class="callout"><b>Recommended first moves (lowest risk, highest leverage):</b>
&#35;2 Gmail drafts, &#35;3 Canva creative, &#35;1 Calendar deadlines, &#35;5 Slack ops canvas.</div>
<p class="small">Full strategy package: 01 Campaign Plan &middot; 02 Compliance &amp; Filing &middot;
03 Fundraising &middot; 04 Messaging &middot; 05 Field &amp; GOTV &middot; 06 Execution Calendar &middot;
07 Sample Artifacts &middot; 08 Channel Implementation Playbook.</p>
</div>
"""

html = f"<html><head><meta charset='utf-8'><style>{CSS}</style></head><body>{cover}{s1}{s2}{s3}{s4}{s5}{s6}{s7}</body></html>"

HTML(string=html).write_pdf(OUT)
print("Wrote", OUT, "(", os.path.getsize(OUT), "bytes )")
