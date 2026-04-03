# Get Elected

A Claude AI Skill that helps any person in the United States run a legally compliant, strategically sound campaign for public office — from school board to Congress.

## What This Skill Does

Get Elected is a comprehensive campaign assistant that provides guidance across every phase of running for office:

- **Campaign Finance Compliance** — Federal FEC rules and state-specific filing requirements, contribution limits, disclosure deadlines, and reporting obligations.
- **Campaign Strategy** — Race analysis, voter targeting, timeline planning, staffing structures, and budget frameworks tailored to the office you are seeking.
- **Messaging and Communications** — Platform development, stump speeches, debate preparation, press releases, op-eds, and issue framing.
- **GOTV (Get Out The Vote)** — Canvassing plans, phone bank scripts, poll watcher coordination, Election Day logistics, and early/absentee vote strategies.
- **Voter Engagement Tools** — 15 interactive tools for town halls, petition drives, voter registration events, community listening sessions, and more.

### Skill Core Loop

Every session follows the same five-step routing process to deliver the right guidance for the right person at the right time.

```mermaid
flowchart TD
    A["User Question"] --> B["1. JURISDICTION\nIdentify office level and location"]
    B --> C["2. ROLE\nWho is the user?"]
    C --> D["3. PHASE\nWhere in the campaign lifecycle?"]
    D --> E["4. MODULE\nRoute to the correct reference file"]
    E --> F["5. OUTPUT\nGenerate artifact with guardrails applied"]

    style A fill:#4a90d9,color:#fff
    style B fill:#50c878,color:#fff
    style C fill:#50c878,color:#fff
    style D fill:#50c878,color:#fff
    style E fill:#50c878,color:#fff
    style F fill:#f5a623,color:#fff
```

### Campaign Lifecycle

A campaign moves through seven distinct phases, each with its own priorities, tasks, and compliance requirements.

```mermaid
flowchart LR
    E["Exploring"] --> FI["Filing"]
    FI --> BU["Building"]
    BU --> FR["Fundraising"]
    FR --> RU["Running"]
    RU --> RE["Reporting"]
    RE --> PO["Post-Election"]

    E -.- E1["Viability assessment\nShould I run?"]
    FI -.- FI1["Ballot access\nCommittee setup"]
    BU -.- BU1["Team recruitment\nInfrastructure"]
    FR -.- FR1["Donor strategy\nCompliance"]
    RU -.- RU1["Messaging\nGOTV\nEvents"]
    RE -.- RE1["Compliance filings\nAudits"]
    PO -.- PO1["Transition\nWind-down\nDebt"]

    style E fill:#4a90d9,color:#fff
    style FI fill:#4a90d9,color:#fff
    style BU fill:#4a90d9,color:#fff
    style FR fill:#4a90d9,color:#fff
    style RU fill:#4a90d9,color:#fff
    style RE fill:#4a90d9,color:#fff
    style PO fill:#4a90d9,color:#fff
```

## How to Use It

Get Elected is a Claude AI skill. It triggers automatically when you ask campaign-related questions. You can also invoke any of its 80+ slash commands directly for instant artifact generation — everything from a fundraising plan to a compliance checklist to a volunteer onboarding packet.

Examples:

- "I want to run for city council in Phoenix. Where do I start?"
- "What are the campaign finance rules for a state senate race in Missouri?"
- "Help me write a stump speech about infrastructure and education."
- `/campaign-plan` — Generate a full campaign plan framework
- `/fundraising-strategy` — Build a fundraising strategy with timelines and targets
- `/compliance-checklist` — Produce a filing and compliance checklist for your race

### Jurisdiction Routing

Campaign rules are layered. Federal rules govern federal races, state rules govern state and local races, and some localities add additional requirements on top.

```mermaid
flowchart TD
    Q["What office are you running for?"] --> FED["Federal Office\nPresident / Senate / House"]
    Q --> ST["State Office\nGovernor / Legislature / AG"]
    Q --> CO["County Office\nExecutive / Commissioner / Sheriff"]
    Q --> MU["Municipal Office\nMayor / City Council / Judge"]
    Q --> SB["School Board /\nSpecial District"]

    FED --> FEC["FEC Rules Apply"]
    FEC --> SBAL["State Ballot Access Rules"]

    ST --> SEA["State Election Agency"]

    CO --> SEA2["State Election Agency"]
    CO --> CLR["County Rules Layer"]

    MU --> SEA3["State Election Agency"]
    MU --> MLB["Local Election Board"]

    SB --> SEA4["State Election Agency"]
    SB --> DLB["District / Local Board"]

    style Q fill:#4a90d9,color:#fff
    style FEC fill:#d94a4a,color:#fff
    style SEA fill:#50c878,color:#fff
    style SEA2 fill:#50c878,color:#fff
    style SEA3 fill:#50c878,color:#fff
    style SEA4 fill:#50c878,color:#fff
    style CLR fill:#f5a623,color:#fff
    style MLB fill:#f5a623,color:#fff
    style DLB fill:#f5a623,color:#fff
```

### User Roles

The skill adapts its guidance based on who you are. Each role is routed to the modules most relevant to their responsibilities.

```mermaid
flowchart TD
    U["Who are you?"] --> CA["Candidate"]
    U --> TR["Treasurer"]
    U --> CM["Campaign Manager"]
    U --> VO["Volunteer"]
    U --> AD["Advisor / Consultant"]

    CA --> CA1["Strategy\nMessaging\nFundraising\nCompliance\nGOTV"]
    TR --> TR1["Compliance\nContribution Tracking\nExpenditure Tracking\nFiling Reports"]
    CM --> CM1["Workflows\nMessaging\nField Operations\nVolunteer Mgmt\nScheduling"]
    VO --> VO1["GOTV Scripts\nCanvassing\nVolunteer Rules\nDonation Questions"]
    AD --> AD1["Full Access\nProfessional Language\nAll Modules"]

    style U fill:#4a90d9,color:#fff
    style CA fill:#50c878,color:#fff
    style TR fill:#f5a623,color:#fff
    style CM fill:#7b68ee,color:#fff
    style VO fill:#e06666,color:#fff
    style AD fill:#999,color:#fff
```

## Directory Structure

The following diagram shows how the major module groups connect and feed into each other.

```mermaid
flowchart TD
    subgraph CORE["Core Reference Layer"]
        REF["references/\nLifecycle, Roles, Glossary\nEthics, Agency Directory"]
        FED["federal/\nFEC Rules, Limits\nDisclosure, Compliance"]
        STA["states/\n11 States Covered\nMO Full Model"]
    end

    subgraph PLAN["Planning Layer"]
        WRK["workflows/\nFirst 30 Days, Filing\nTreasurer Setup, GOTV Plan"]
        TOO["tools/\nContribution Tracker\nExpenditure Tracker\nDisclaimer Generator"]
    end

    subgraph EXEC["Execution Layer"]
        MSG["messaging/\nSpeeches, Debate Prep\nPress, Social, Email, Ads"]
        TAC["tactics/\nField Strategy, Crisis Mgmt\nBallot Chase, Scheduling"]
        OUT["outreach/\nStakeholder Letters\nEndorsement Playbook"]
    end

    subgraph GEN["Generation Layer"]
        ART["artifacts/\nDocument Templates\nGenerated Plans"]
        CMD["commands/\n80+ Slash Commands"]
    end

    REF --> WRK
    FED --> TOO
    STA --> TOO
    WRK --> MSG
    WRK --> TAC
    TOO --> TAC
    MSG --> ART
    TAC --> ART
    OUT --> ART
    CMD --> ART

    style CORE fill:#e8f0fe,stroke:#4a90d9
    style PLAN fill:#e8fee8,stroke:#50c878
    style EXEC fill:#fef3e8,stroke:#f5a623
    style GEN fill:#f0e8fe,stroke:#7b68ee
```

```
get-elected/
├── references/          # Core reference materials and legal foundations
├── federal/             # Federal election law, FEC rules, and compliance guides
├── states/              # State-specific election law and filing requirements
│   ├── AZ/
│   ├── CA/
│   ├── FL/
│   ├── GA/
│   ├── IL/
│   ├── MI/
│   ├── MO/              # Full coverage — complete state model
│   ├── NY/
│   ├── OH/
│   ├── PA/
│   └── TX/
├── workflows/           # Step-by-step campaign workflow guides
├── tools/               # Calculators, generators, and planning utilities
├── messaging/           # Speech templates, talking points, and comms frameworks
├── outreach/            # Voter contact, canvassing, and coalition-building
├── tactics/             # Field strategy, digital tactics, and GOTV operations
├── artifacts/           # Templates and generated document frameworks
├── commands.md          # Full catalog of 80+ slash commands
└── voter-engagement-tools.md  # 15 interactive voter engagement tools
```

## Coverage

Get Elected currently covers **11 states** with state-specific election law, filing requirements, and compliance guidance:

| State | Abbreviation | Coverage Level |
|-------|--------------|----------------|
| Arizona | AZ | Core coverage |
| California | CA | Core coverage |
| Florida | FL | Core coverage |
| Georgia | GA | Core coverage |
| Illinois | IL | Core coverage |
| Michigan | MI | Core coverage |
| Missouri | MO | **Full coverage** |
| New York | NY | Core coverage |
| Ohio | OH | Core coverage |
| Pennsylvania | PA | Core coverage |
| Texas | TX | Core coverage |

Missouri serves as the complete state model with exhaustive coverage of every office level, filing deadline, contribution limit, and compliance requirement. Other states include core coverage sufficient to guide candidates through the major requirements of running for office.

### State Coverage Model

Missouri provides the template for full state coverage. Each state begins with an overview file and expands to the full five-file structure as coverage deepens.

```mermaid
flowchart TD
    STATE["New State Added"] --> OV["overview.md\nAgency structure\nCommittee types\nKey differences"]

    OV -->|"Coverage expands"| FULL["Full 5-File Structure"]

    subgraph FULL["Full Coverage - Missouri Model"]
        F1["overview.md\nAgency, committee types"]
        F2["contribution-limits.md\nLimits by office level"]
        F3["disclosure-requirements.md\nReporting schedules, filing"]
        F4["ballot-access.md\nHow to get on the ballot"]
        F5["local-rules.md\nCounty, city, school board"]
    end

    OV2["Other 10 States\nCore Coverage"] -.- OV
    MO["Missouri\nFull Coverage"] -.- FULL

    style STATE fill:#4a90d9,color:#fff
    style OV fill:#f5a623,color:#fff
    style MO fill:#50c878,color:#fff
    style OV2 fill:#e06666,color:#fff
```

Federal election law and FEC compliance guidance apply to all 50 states.

## Key Workflows

### Should I Run? Decision Tree

The skill walks prospective candidates through a structured viability assessment before they commit to a campaign.

```mermaid
flowchart TD
    START["Considering Running\nfor Office"] --> PR["Personal Readiness\nTime, family, finances,\npublic scrutiny tolerance"]
    PR -->|"Ready"| PL["Political Landscape\nIncumbent strength, district lean,\nrecent election results"]
    PR -->|"Not Ready"| WAIT["Consider Waiting\nor Supporting Others"]

    PL -->|"Viable Path"| RES["Resources Assessment\nCan you raise enough?\nDo you have a team?"]
    PL -->|"Unwinnable"| ALT["Consider a\nDifferent Office"]

    RES -->|"Sufficient"| ISS["Issue Fit\nDo your priorities match\ndistrict concerns?"]
    RES -->|"Insufficient"| BUILD["Build Resources\nFirst, Then Reassess"]

    ISS -->|"Strong Fit"| RUN["Run for Office"]
    ISS -->|"Weak Fit"| REFRAME["Reframe Platform\nor Choose Different Race"]

    RUN --> FILE["Begin Filing Process"]

    style START fill:#4a90d9,color:#fff
    style RUN fill:#50c878,color:#fff
    style WAIT fill:#e06666,color:#fff
    style ALT fill:#f5a623,color:#fff
    style BUILD fill:#f5a623,color:#fff
    style REFRAME fill:#f5a623,color:#fff
```

### Donation Processing Flow

Every contribution must pass through a compliance pipeline before it can be deposited and reported.

```mermaid
flowchart LR
    REC["Receive\nDonation"] --> VER["Verify\nEligibility"]
    VER -->|"Eligible"| CHK["Check\nContribution\nLimits"]
    VER -->|"Ineligible"| REJ["Reject and\nReturn Funds"]

    CHK -->|"Within Limits"| RCD["Record in\nContribution\nTracker"]
    CHK -->|"Over Limit"| PAR["Return Excess\nKeep Allowed\nAmount"]

    PAR --> RCD
    RCD --> DEP["Deposit to\nCampaign\nAccount"]
    DEP --> RPT["Include in\nCompliance\nReport"]

    VER -.- VN["Check: US citizen or\ngreen card holder?\nNot a corporation?\nNot a foreign national?"]
    CHK -.- CN["Check: Under individual\nlimit for this office?\nAggregate limits?"]

    style REC fill:#4a90d9,color:#fff
    style REJ fill:#e06666,color:#fff
    style RPT fill:#50c878,color:#fff
```

### Compliance Reporting Cycle

Campaign finance compliance is not a one-time task. It is an ongoing cycle that runs throughout the life of the campaign.

```mermaid
flowchart TD
    TRK["Track\nEvery contribution\nand expenditure\nas it occurs"] --> REC["Reconcile\nBank statements\nvs. internal records\nmonthly"]
    REC --> REV["Review\nItemization thresholds\nDisclosure requirements\nDeadline calendar"]
    REV --> FILE["File\nSubmit reports to\nFEC or state agency\non schedule"]
    FILE --> MON["Monitor\nAgency confirmations\nAmendment requests\nAudit notices"]
    MON --> TRK

    style TRK fill:#4a90d9,color:#fff
    style REC fill:#50c878,color:#fff
    style REV fill:#f5a623,color:#fff
    style FILE fill:#7b68ee,color:#fff
    style MON fill:#e06666,color:#fff
```

## Slash Commands

Over **80 slash commands** provide instant artifact generation for every aspect of a campaign. Commands span categories including:

- Campaign planning and launch
- Finance and fundraising
- Legal compliance and filing
- Messaging and communications
- Field operations and GOTV
- Digital strategy and social media
- Volunteer management
- Opposition research frameworks

Run any command by name to generate a ready-to-use document, checklist, or plan.

## Messaging and Communications

### Messaging Channels

A campaign's core message must be adapted consistently across every communication channel. The skill generates tailored content for each.

```mermaid
flowchart TD
    CORE["Core Message\nWho you are\nWhat you stand for\nWhy it matters now"] --> SP["Stump Speeches\nRally remarks\nTown hall remarks"]
    CORE --> SOC["Social Media\nPlatform-specific posts\nVideo scripts"]
    CORE --> PR["Press Relations\nPress releases\nOp-eds\nMedia advisories"]
    CORE --> EM["Email Fundraising\nDonor appeals\nNewsletter updates"]
    CORE --> DEB["Debate Prep\nOpening statements\nRebuttal frameworks\nClosing arguments"]
    CORE --> ADS["Paid Media\nTV/radio scripts\nDigital ad copy\nMail pieces"]
    CORE --> POD["Podcast Campaign\nInterview talking points\nGuest pitches"]

    style CORE fill:#4a90d9,color:#fff
    style SP fill:#50c878,color:#fff
    style SOC fill:#50c878,color:#fff
    style PR fill:#50c878,color:#fff
    style EM fill:#50c878,color:#fff
    style DEB fill:#50c878,color:#fff
    style ADS fill:#50c878,color:#fff
    style POD fill:#50c878,color:#fff
```

### Issue Response Engine

When an issue or attack surfaces, the skill generates a complete response package across all required formats from a single input.

```mermaid
flowchart TD
    ISS["Issue or Attack\nSurfaces"] --> ANALYZE["Analyze\nContext, severity,\naudience impact"]
    ANALYZE --> GEN["Generate Response Package"]

    GEN --> R1["Official Statement\nFormal position"]
    GEN --> R2["Social Media Posts\nPlatform-tailored"]
    GEN --> R3["Talking Points\nFor surrogates"]
    GEN --> R4["Press Response\nFor media inquiries"]
    GEN --> R5["Email to Supporters\nRally the base"]
    GEN --> R6["Town Hall Answer\nIn-person framing"]
    GEN --> R7["Debate Rebuttal\nTimed response"]
    GEN --> R8["Internal Briefing\nFor campaign staff"]

    style ISS fill:#e06666,color:#fff
    style ANALYZE fill:#f5a623,color:#fff
    style GEN fill:#4a90d9,color:#fff
```

## Field Operations

### Voter Contact Pipeline

The voter contact operation follows a progressive engagement funnel from raw voter data to Election Day turnout.

```mermaid
flowchart LR
    VF["Voter File\nAcquire registered\nvoter data"] --> TGT["Target\nScore and segment\nby persuadability"]
    TGT --> ID["Identify\nDoor knocks and\ncalls to ID support"]
    ID --> PER["Persuade\nTailored messaging\nto undecided voters"]
    PER --> MOB["Mobilize\nLock in supporters\nVolunteer recruitment"]
    MOB --> GOTV["GOTV\nEarly vote chase\nElection Day turnout"]
    GOTV --> VOTE["Vote\nPoll monitoring\nBallot cure"]

    style VF fill:#4a90d9,color:#fff
    style TGT fill:#50c878,color:#fff
    style ID fill:#50c878,color:#fff
    style PER fill:#f5a623,color:#fff
    style MOB fill:#f5a623,color:#fff
    style GOTV fill:#e06666,color:#fff
    style VOTE fill:#7b68ee,color:#fff
```

### GOTV Operations Timeline

The final two weeks of a campaign follow a structured escalation from early vote operations through Election Day.

```mermaid
flowchart LR
    D14["Day -14\nEarly Vote\nLaunch"] --> D10["Day -10\nAbsentee Ballot\nChase Begins"]
    D10 --> D7["Day -7\nVolunteer\nSurge Training"]
    D7 --> D5["Day -5\nPoll Location\nLogistics Final"]
    D5 --> D3["Day -3\nFinal Voter\nContact Push"]
    D3 --> D1["Day -1\nStaging and\nSupply Distribution"]
    D1 --> ED["Election Day\nPoll Watching\nRide to Polls\nBallot Cure\nTurnout Tracking"]

    style D14 fill:#4a90d9,color:#fff
    style D10 fill:#4a90d9,color:#fff
    style D7 fill:#50c878,color:#fff
    style D5 fill:#50c878,color:#fff
    style D3 fill:#f5a623,color:#fff
    style D1 fill:#f5a623,color:#fff
    style ED fill:#e06666,color:#fff
```

### Crisis Management: The RESPOND Framework

When a crisis hits, the skill guides users through a structured seven-step response protocol.

```mermaid
flowchart TD
    R["R - Recognize\nIdentify the crisis\nAssess severity"] --> E["E - Evaluate\nWho is affected?\nWhat are the facts?"]
    E --> S["S - Strategize\nChoose response posture\nDefend, pivot, or own"]
    S --> P["P - Prepare\nDraft statements\nBrief surrogates"]
    P --> O["O - Operationalize\nDeploy response\nacross all channels"]
    O --> N["N - Neutralize\nCounter misinformation\nProvide evidence"]
    N --> D["D - Document\nRecord lessons learned\nUpdate crisis playbook"]

    style R fill:#e06666,color:#fff
    style E fill:#e06666,color:#fff
    style S fill:#f5a623,color:#fff
    style P fill:#f5a623,color:#fff
    style O fill:#4a90d9,color:#fff
    style N fill:#4a90d9,color:#fff
    style D fill:#50c878,color:#fff
```

## Voter Engagement Tools

**15 interactive tools** help candidates build genuine connections with voters:

- Town hall planning and facilitation guides
- Voter registration drive toolkits
- Community listening session frameworks
- Petition and ballot initiative support
- Neighborhood canvassing systems
- Phone and text banking scripts
- Coalition-building workshops
- And more

## Guardrails

Get Elected operates under strict guardrails to ensure responsible use:

- **Nonpartisan** — This skill serves candidates of any party or no party. It does not advocate for any political ideology, party, or candidate.
- **No Invented Law** — All legal and compliance information is grounded in referenced source material. The skill will never fabricate statutes, regulations, or filing requirements.
- **Educational Only** — This skill provides educational information to help citizens participate in democracy. It is not a substitute for professional legal, financial, or strategic counsel.
- **No Dark Arts** — This skill will not assist with voter suppression, disinformation, illegal coordination, or any other unethical campaign practice.

## Contributing

Contributions are welcome. Areas where help is especially valuable:

- Adding or expanding state-specific coverage beyond the current 11 states
- Updating legal references to reflect new legislation or rule changes
- Improving templates and artifact quality
- Adding new slash commands for underserved campaign needs
- Testing workflows against real-world campaign scenarios

Please open an issue or submit a pull request. All contributions must maintain the nonpartisan, educational character of the project.

## Disclaimer

Get Elected provides **educational information only** and does **not** constitute legal advice. Campaign finance law, election law, and filing requirements vary by jurisdiction and change frequently. Always consult a qualified attorney, your state or local election authority, or the Federal Election Commission for authoritative guidance specific to your race and jurisdiction. Use of this skill does not create an attorney-client relationship or any other professional advisory relationship.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
