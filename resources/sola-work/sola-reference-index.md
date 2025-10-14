# Sola Reference Index

**Purpose**: Central guide to all Sola-related context, documentation, and resources in the work system

**Last Updated**: 2025-10-12

---

## Quick Links

**For Meeting Prep**:
- `.claude/meeting-context.md` - All recurring meetings
- `.claude/people/sola-people.md` - People context and open issues
- `.claude/playbooks/meetings/` - Meeting preparation guides

**For Project Context**:
- `Context/Sola/data/Jira.csv` - Your Jira tickets (use `scripts/analyze_jira.py`)
- `Context/Sola/Docs/Sola Docs.pdf` - Product documentation (needs conversion to markdown)

**Your Role**: Product Manager leading growth and AI experiences at Sola

---

## 1. People Reference

**File**: `.claude/people/sola-people.md`

**What it contains**:
- All key people you work with at Sola
- Their roles, relationships to you, and working styles
- **Open Issues / Topics to Discuss** checklists for each person
- Last synced dates

**How to use**:
- **Before any meeting**: Check the person's section for open issues
- **After any meeting**: Update their open issues (check off resolved, add new ones)
- **When learning patterns**: Add to "Working Style / Notes" section

**Key people documented**:
- **Shlomi Lavi** (VP Product, your manager) - Bi-weekly 1:1s
- **Dor Swissa** (VP R&D) - Challenges priorities at Sprint Planning
- **Leon** (CTO) - Technical reality check at Sprint Planning
- **Lior Eli** (UX Designer) - Design partner, must align before Backlog Refinement
- **Nadav Levy** (Senior PM) - Peer, also presents at Backlog Refinement
- **Adi Atzmoni** (Principal Technical Writer) - Strategic product input
- **Ami Yamin** (Head of Design) - Design review and approval

Plus leadership (Guy Fletcher, Ron Peled, Minnie Ketzenberg, Mor Siman Tov)

---

## 2. Meeting Context & Playbooks

### Meeting Context File
**File**: `.claude/meeting-context.md`

**What it contains**: Complete list of all recurring and important meetings with:
- Frequency and timing
- Attendees
- Purpose
- Link to preparation playbook (if exists)

### Meeting Playbooks
**Location**: `.claude/playbooks/meetings/`

**Available playbooks**:

#### Sola Weekly (`sola-weekly.md`)
- **Type**: Company all-hands
- **Frequency**: Weekly
- **Purpose**: Company updates, strategic context, celebration
- **Prep**: Just listen, take notes on anything relevant to your work

#### Backlog Refinement (`backlog-refinement.md`)
- **Type**: Product team story review
- **Frequency**: Bi-weekly, Wednesdays
- **Critical**: "This meeting lives or dies on your prep"
- **Timeline**: Start prep 3-5 days before
- **Outcome**: Production-ready stories for Sprint Planning
- **Prep checklist**:
  - Day 1-2: Gather candidate stories
  - Day 2-4: Make stories production-ready
  - Day 4-5: Prioritize & sequence
  - Day 5: Pre-sync with Lior (design) and Shlomi

#### Sprint Planning (`sprint-planning.md`)
- **Type**: R&D commitment meeting
- **Frequency**: Bi-weekly, Sundays 17:00
- **Key players**: Dor (VP R&D), Leon (CTO), Shlomi
- **Mindset**: "Harsh water" - push hard, listen to reality, find paths forward
- **Prep**: 2-3 hours day before or morning of
- **Negotiation strategies**:
  - Clarify the WHY (business impact)
  - Explore alternatives (what IS doable?)
  - Trade, don't fight (deprioritize X for Y)
  - Escalate to principles (tie to OKRs)

#### Shlomi 1:1 (`shlomi-1on1.md`)
- **Type**: Manager 1:1
- **Frequency**: Bi-weekly
- **Current challenge**: Very tactical, need to add strategic vision layer
- **Three-phase approach**:
  - Phase 1 (Weeks 1-4): Establish tactical excellence
  - Phase 2 (Weeks 5-8): Introduce vision iteratively
  - Phase 3 (Weeks 9+): Co-create strategic direction
- **Prep steps**:
  1. Review open issues (15 min)
  2. Tactical prep (15 min)
  3. Strategic prep when ready (20 min)

#### Agile Cycle Overview (`agile-cycle-overview.md`)
- Explains how Backlog Refinement → Sprint Planning connect
- Bi-weekly cycle timing
- Key relationships and dependencies

---

## 3. Jira Tickets Reference

### Source Data
**File**: `Context/Sola/data/Jira.csv`
- 194 tickets you've created
- Last updated: [Check file timestamp]
- Projects: RND (157), CTO (19), DESIGN (14), SQUAD (3), REVR (1)

### Analysis Tool
**Script**: `scripts/analyze_jira.py`

**Usage**:
```bash
# Summary statistics
python3 scripts/analyze_jira.py --summary

# Active tickets only (To Do, In Progress, To Discuss, Validation)
python3 scripts/analyze_jira.py --active

# Recently completed (last 30 days)
python3 scripts/analyze_jira.py --recent

# Filter by project
python3 scripts/analyze_jira.py --project RND --active

# All tickets grouped by status (default)
python3 scripts/analyze_jira.py
```

### Current Status (as of last analysis)
- **123 Done** (63.4%) - Solid delivery track record
- **39 To Do** (20.1%) - Active backlog
- **29 Won't Do** (14.9%) - Deprioritized/rejected
- **2 To Discuss** (1.0%) - Needs clarification
- **1 Validation** (0.5%) - Ready for review

### Key Focus Areas (from ticket patterns)
- Canvas 2.0 features and migration
- AI app builder enhancements
- Copilot improvements
- Onboarding optimization
- Data source integrations

### When to Use Jira Analysis
- **Before Backlog Refinement**: Review your To Do tickets, see what's ready
- **Before Sprint Planning**: Check what's in flight, recently completed
- **Before Shlomi 1:1**: Show progress (recently completed), discuss blockers (To Discuss)
- **Weekly review**: Friday afternoons, assess progress and plan ahead

---

## 4. Product Documentation

### Current State
**Files**:
- `Context/Sola/Docs/Sola Docs.pdf` - Original 33MB documentation
- `Context/Sola/Docs/sola-docs-cleaned.txt` - Extracted text (522 lines)
- `Context/Sola/Docs/index.md` - **Navigation guide and index**

**Status**: ✅ Converted and searchable (with some formatting quirks)

**How to use**:
1. **Read the index**: `Context/Sola/Docs/index.md` - Complete navigation guide with line numbers
2. **Search the text**: `grep -i "term" Context/Sola/Docs/sola-docs-cleaned.txt`
3. **Ask Claude**: I can search the documentation for you

**Note**: Text has some OCR errors (e.g., "secturiy" instead of "security") but is fully searchable

**Key sections documented**:
- Getting Started & Quickstart (Lines 1-50)
- Core Concepts: Queries, Canvases, Alerts, Workflows (Lines 51-564)
- 15+ Data Source Integrations (Lines 565-750)
- Connectors: Slack, Jira (Lines 801-921)
- System Management & Settings (Lines 955-988)
- FAQs & Resources (Lines 989-1043)

---

## 5. Integration Strategy

### Phase 1: Basic Integration
**Status**: ✅ COMPLETE

**What's done**:
- ✅ Jira analysis tool (`scripts/analyze_jira.py`)
- ✅ Central reference index (this document)
- ✅ Meeting playbooks updated with Jira integration
- ✅ Phase 2-3 plans documented
- ✅ PDF documentation converted to searchable text with index

### Phase 2: Active Integration (PLANNED)
**Goal**: Make Jira data part of regular workflow

**Planned actions**:
- Weekly Jira review routine (Fridays before end of week)
- Regular Jira CSV updates (export fresh data weekly)
- Pattern tracking in ticket completion (velocity, focus areas)
- Integration with meeting prep (auto-check Jira before key meetings)

**Where documented**: See "Phase 2-3 Integration Plans" section below

### Phase 3: Strategic PM Integration (FUTURE)
**Goal**: Connect tactical execution to strategic vision

**Planned actions**:
- Create `projects/growth-and-ai/` folder for strategic initiatives
- Map strategic initiatives to Jira tickets
- Build progress dashboard (initiatives → tickets → outcomes)
- Connect Jira data to OKRs/quarterly goals
- Track how tactical delivery serves strategic vision

**Where documented**: See "Phase 2-3 Integration Plans" section below

---

## 6. Phase 2-3 Integration Plans

### Phase 2: Weekly Jira Review Routine

**When**: Every Friday, 30 minutes before end of work week

**Process**:
1. Export fresh Jira CSV (replace `Context/Sola/data/Jira.csv`)
2. Run: `python3 scripts/analyze_jira.py --summary`
3. Run: `python3 scripts/analyze_jira.py --recent`
4. Review patterns:
   - What got completed this week?
   - What's still in To Do that should be Done?
   - Any blockers in "To Discuss"?
   - Where's the focus? (Canvas 2.0, AI, Onboarding, etc.)
5. Update `.claude/people/sola-people.md` with any new open issues
6. Prepare for next week:
   - What needs to be prioritized?
   - Any prep needed for upcoming meetings?

**Success metrics**:
- Track velocity: How many tickets completed per week?
- Track focus: Are tickets aligned with strategic priorities?
- Track blockers: Are "To Discuss" tickets resolved quickly?

### Phase 3: Strategic Initiative Mapping

**Setup**:
Create `projects/growth-and-ai/` with:
- `roadmap.md` - Strategic initiatives and milestones
- `initiatives/` folder - One file per major initiative
- `metrics.md` - Success metrics and progress tracking

**Initiative structure**:
```markdown
# [Initiative Name]

## Vision
What we're building and why

## Success Metrics
How we'll know it's working

## Milestones
High-level phases

## Jira Tickets
Link to related tickets:
- [RND-XXXX] Description (Status)
- [RND-YYYY] Description (Status)

## Progress
Track completion, learnings, pivots
```

**Integration with existing system**:
- Sprint Planning → Reference initiatives when prioritizing
- Backlog Refinement → Tag stories with initiatives
- Shlomi 1:1 → Discuss initiative progress (strategic layer)
- Weekly Jira review → Roll up ticket progress to initiatives

**When to implement**: After Phase 2 routine is established (4-6 weeks)

---

## 7. How to Use This System

### Daily Use
- **Morning**: Check calendar (`scripts/parse_calendar.py` or sync'd calendar)
- **Before meetings**: Check `.claude/people/sola-people.md` for person's open issues
- **After meetings**: Update person's open issues in `sola-people.md`

### Weekly Routine
- **Wednesday prep**: Backlog Refinement preparation (3-5 days before)
- **Friday review**: Weekly Jira analysis (Phase 2)
- **Sunday prep**: Sprint Planning preparation (day before or morning of)

### Bi-weekly Routine
- **Wednesday**: Backlog Refinement meeting
- **Sunday**: Sprint Planning meeting
- **Every 2 weeks**: Shlomi 1:1 (check his section for open issues first)

### As Needed
- **New meeting**: Document in `.claude/meeting-context.md`, create playbook if recurring
- **New person**: Add section to `.claude/people/sola-people.md`
- **Learning patterns**: Update person's "Working Style / Notes"
- **Strategic thinking**: Update Shlomi 1:1 prep with vision topics (Phase 2-3)

---

## 8. Connection to Your Growth Edges

(From `ABOUT.md`)

**This system helps with**:

1. **Over-communicate upward** (doesn't come naturally)
   - Meeting playbooks force preparation
   - Open issues checklists ensure topics aren't forgotten
   - Jira analysis provides concrete progress data

2. **"People feel stupid" early warning signal**
   - Running ahead without sharing context
   - Meeting prep ensures you bring people along
   - Shlomi 1:1 structure balances tactical and strategic

3. **Vision and execution interdependence**
   - Phase 1: Prove tactical excellence
   - Phase 2-3: Build strategic alignment
   - "Two horses pulling the same carriage"

4. **Harsh water approach**
   - Sprint Planning playbook has negotiation strategies
   - Push hard but find alternative paths
   - Systemic progression > tactical perfection

5. **Advocating for needs**
   - Open issues checklists make it harder to "let things go"
   - Structured 1:1 prep creates space for raising concerns
   - Tracking prevents silence = cumulative cost

---

## 9. Maintenance

**Weekly**:
- Update Jira CSV (export fresh data)
- Run Jira analysis
- Update people's "Last Synced" dates after 1:1s

**Bi-weekly**:
- Review meeting playbooks, update based on learnings
- Check Phase 2-3 plans, adjust as needed

**Monthly**:
- Review this index, add new resources
- Archive outdated information
- Reflect on what's working, what's not

**As needed**:
- Add new meetings to context
- Add new people
- Create new playbooks
- Update documentation structure

---

**Phase 1 Complete** ✅

**Next Steps**:
1. 🎯 **Start using the system** - Tonight's Sprint Planning is perfect timing!
2. 🔄 **Iterate based on what works** - Adjust playbooks as you learn
3. ⏭️ **Phase 2 when ready** - Weekly Jira review routine (4-6 weeks from now)
4. ⏭️ **Phase 3 later** - Strategic initiative mapping

**Last Updated**: 2025-10-12
