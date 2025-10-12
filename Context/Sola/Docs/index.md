# Sola Product Documentation - Index

**Source**: Sola Docs.pdf (33MB)
**Extracted**: sola-docs-cleaned.txt (522 lines, cleaned from raw 14K+ lines)
**Status**: Text extracted with some formatting issues, but searchable
**Last Updated**: 2025-10-12

---

## ⚠️ Note on Text Quality

The text was extracted from PDF using macOS Preview. Some words are fragmented or run together (e.g., "secturiy" instead of "security", "butild" instead of "build"). Despite formatting issues, the content is searchable and the main concepts are readable.

---

## Document Structure

### 1. Getting Started (Lines 1-20)
- Welcome and overview
- "From security questions to solutions in minutes"
- How Sola AI works
- Quick navigation to key features

### 2. Quickstart Guide (Lines 21-50)
**Step-by-step guide to getting started:**
1. Connect your data sources
2. Build your app with Sola AI
3. Explore triggered alerts and canvases
4. Review and investigate issues

### 3. Core Concepts (Lines 51-110)

#### How Sola Works (Lines 31-42)
- Creating custom security solutions
- 4 building blocks:
  1. **Queries** - Data inquiry for security questions
  2. **Canvases** - Data visualization (dashboards, reports)
  3. **Alerts** - Monitoring and alert rules
  4. **Workflows** - Automation and remediation

#### Sola AI (Lines 43-60)
- Built-in security expert
- Generates insights and builds custom apps
- AI copilot for investigation
- Graph-enhanced research mode

#### Graph Research (Lines 61-108)
- Advanced reasoning mode
- Maps relationships between resources, controls, and risks
- Provides complete, grounded answers
- Visual evidence and contextual analysis

### 4. Prompt Guide (Lines 109-162)
**Best practices for building with Sola AI:**
1. **Start** - Begin with broad prompts
2. **Provide** - Give Sola AI what it needs
3. **Expand** - Grow beyond the basics
- Tips for effective prompting
- How to ask clarification questions
- Iterating on AI responses

### 5. Release Notes & What's New (Lines 163-264)

#### September 17, 2025
- **Vibe canvases** - Fully customizable interactive interfaces
- **Agentic workflows** - AI-native orchestration for investigations/remediation

#### September 10, 2025
- Send CSV to Slack integration
- New apps in App Gallery

#### July 23, 2025
- **Graph-enhanced research** in Sola AI
- Slack Sola Agent
- Export query results to CSV
- Filter canvas widgets

### 6. Apps - Creating Custom Security Solutions (Lines 265-304)

**What's a Sola App?**
- Custom security tool tailored to specific needs
- Autonomous, supports own use case
- Can connect to one or more data sources
- Different workspace members as creators/consumers

**App Components:**
1. Queries - Expose underlying data
2. Canvases - Code data into interactive interfaces
3. Alerts - Monitor data with rules
4. Workflows - Automate actions with AI flows

### 7. Queries (Lines 305-362)
- Querying security data for insights
- Analyzing security risks
- Exploring security posture
- Publishing queries for use in canvases/alerts/workflows

### 8. Canvases (Lines 363-390)
**Use cases:**
- Asset inventory boards (with filters/drill-down)
- Threat intelligence trackers with prioritized IOCs
- Patch tracking dashboards
- Access review boards (Okta/Azure AD risky accounts)

**Supported visuals:**
- Dynamic charts (bar, line, pie, stacked)
- Interactive tables
- Scorecards and counters for KPIs
- Text blocks, images, layouts
- Can build narrative-driven dashboards, security guides, executive reports

### 9. Alerts (Lines 391-446)
- Track security risks, misconfigurations, policy violations
- Notify when records meet specific conditions
- Proactively monitor security events
- Respond quickly when risks arise

### 10. Workflows (Lines 447-564)
**Agentic Workflows:**
- AI-native orchestration
- Step-by-step automation
- Each block is like an AI agent
- Grounded in Sola's domain expertise
- Reasons over identity, access, risk severity, posture impact

**Key features:**
- Created with Sola AI (describe workflow, AI generates blocks)
- Security intelligence built-in
- Intelligent responses, not just task execution

### 11. Data Sources & Integrations (Lines 565-750)

#### Cloud Providers
- **Amazon Web Services (AWS)** (Lines 575-578)
  - Cross-account role (recommended for production)
  - Read-only access to AWS services

- **Google Cloud Platform (GCP)** (Lines 579-590)
  - Service account (recommended for production)
  - Read-only access to GCP services

- **Microsoft Azure** (Lines 591-600)
  - Read-only access to Azure services

#### Identity & Access
- **Google Workspace** (Lines 601-636)
  - Full workspace data integration

- **Okta** (Lines 677-690)
  - Identity and access monitoring
  - Security posture analysis

#### Development & Collaboration
- **GitHub** (Lines 637-676)
  - Custom GitHub App setup
  - Repository and organization permissions
  - Sync behavior and limitations

- **Zoom** (Lines 757-790)
  - Server-to-server OAuth app
  - Meetings, users, roles, settings monitoring

#### Security Tools
- **Wiz** (Lines 719-720)
  - Service account integration
  - Read-only access to findings, issues, configurations

- **MongoDB Atlas** (Lines 691-718)
  - User roles, access permissions, authentication
  - Network exposure and cluster security

#### Web & External
- **WordPress** (Lines 721-732)
  - Vulnerability scanning
  - Email domain matching for automatic verification

- **Sola Web Checker** (Lines 733-750)
  - External domains, websites, internet-facing infrastructure
  - Common vulnerabilities and misconfigurations

- **Cloudflare** (Lines 791-800)
  - Cloudflare data integration

#### Other Integrations
- **CSV File Upload** (Lines 751-756)
  - Custom datasets for analysis
  - Bring your own data

### 12. Connectors (Action Integrations) (Lines 801-921)

**What are connectors?**
- Enable actions during conversations
- Send information FROM Sola to external systems

#### Available Connectors

**Slack** (Lines 867-906)
- Slack App (recommended for production)
- Bot permissions and scopes
- Send messages, notifications from Sola AI

**Jira** (Lines 907-954)
- Create issues directly from chat conversations
- API token authentication
- Expedite remediation workflow

#### Connector Permissions (Lines 837-851)
- **Workspace level** - Configure when adding connector
- **App level** - Control which apps can use connector

### 13. System Management & Settings (Lines 955-988)

#### Account Settings (Lines 959-960)
- Personal Sola account
- Name, email, password
- AI assistant activation settings

#### Workspace Settings (Lines 961-968)
- Workspace name
- Members management

#### Roles and Permissions (Lines 969-978)
- Workspace permissions
- App permissions

#### Privacy & Security (Lines 979-988)
- Account session activity
- Single Sign-On (SSO)

### 14. Resources (Lines 989-1043)

#### Glossary (Line 1004)
- Security terminology
- Jargon decoded

#### FAQs (Lines 1003-1042)
**Common questions:**
- How to structure apps?
  - By security domain (Identity & Access, Cloud Security)
  - By vendor (AWS Security, GitHub)
  - By team (SOC Team Monitoring, CISO)

- **Data security:**
  - Encrypted at rest and in transit
  - Strict authentication and authorization
  - Sola AI follows standard security policies

---

## How to Search This Documentation

### Option 1: Search the Cleaned Text File
```bash
# Search for specific terms
grep -i "canvas" Context/Sola/Docs/sola-docs-cleaned.txt

# Search with context (5 lines before/after)
grep -i -C 5 "workflow" Context/Sola/Docs/sola-docs-cleaned.txt

# Search for multiple terms
grep -i "alert\|notification" Context/Sola/Docs/sola-docs-cleaned.txt
```

### Option 2: Use Claude to Search
Since I can read the cleaned text file, just ask me:
- "What does Sola documentation say about canvases?"
- "How do I set up AWS integration according to the docs?"
- "What are agentic workflows in Sola?"

### Option 3: Reference by Line Numbers
Use the line numbers from this index to jump to specific sections:
```bash
# View lines 31-42 (How Sola Works)
sed -n '31,42p' Context/Sola/Docs/sola-docs-cleaned.txt

# View lines 575-578 (AWS integration)
sed -n '575,578p' Context/Sola/Docs/sola-docs-cleaned.txt
```

---

## Quick Reference - Key Concepts

### The 4 Building Blocks
1. **Queries** → Ask questions, get data
2. **Canvases** → Visualize data (dashboards)
3. **Alerts** → Monitor and notify
4. **Workflows** → Automate actions

### Sola AI Capabilities
- Build apps from prompts
- Graph-enhanced research
- AI copilot for investigation
- Generate queries, alerts, canvases

### Integration Categories
- **Cloud**: AWS, GCP, Azure
- **Identity**: Okta, Google Workspace, Zoom
- **Dev Tools**: GitHub
- **Security**: Wiz, WordPress Scanner, Web Checker
- **Data**: MongoDB Atlas, CSV Upload
- **Actions**: Slack, Jira

---

## Known Issues with Extracted Text

Common OCR/extraction errors you'll see:
- "secturiy" → security
- "butild" → build
- "wih" → with
- "yo" / "yot" / "yotu" → you / your
- "utto" / "tto" → to
- Fragmented words like "sec t uri y" → security

**Tip**: When searching, try multiple variations:
```bash
grep -i "securit\|secturiy" Context/Sola/Docs/sola-docs-cleaned.txt
```

---

## Files in This Directory

- `Sola Docs.pdf` - Original 33MB PDF documentation
- `docstext.rtfd/` - RTF output from Preview (intermediate)
- `sola-docs-raw.txt` - Raw text extraction (14,437 lines, very fragmented)
- `sola-docs-cleaned.txt` - Cleaned text (522 lines, still has some issues but readable)
- `index.md` - This file (navigation guide)

---

## Next Steps for Better Documentation

If you need cleaner text:
1. **When in office**: Install `pdfplumber` or `PyPDF2` Python libraries
2. **Run proper extraction**: Use tools designed for PDF text extraction
3. **Alternative**: Some sections could be manually retyped if frequently referenced

For now, this is searchable and usable despite formatting quirks.

---

**Last Updated**: 2025-10-12
