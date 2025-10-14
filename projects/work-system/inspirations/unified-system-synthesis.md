# Unified Personal Work System

**Created**: 2025-10-15
**Last Updated**: 2025-10-15

A productivity and knowledge management system combining the best of PPV, PARA, GTD, and Zettelkasten, tailored for ADHD, family-first values, and sustainable work.

---

## Part 1: The System

### Overview

This system has three complementary domains:

1. **Strategic Direction** - Where you're going (vision, pillars, goals)
2. **Knowledge Development** - What you're learning (insights, permanent notes)
3. **Action Management** - What you're doing (projects, areas, tasks)

Each domain operates independently but feeds into the others through regular review cycles.

---

### File Structure

```
/
├── inbox.md                    # Daily capture - EVERYTHING goes here first
├── next-actions.md             # Daily working file - context-based next actions
├── PROJECTS.md                 # Active projects index
├── ABOUT.md                    # Your story and context (past)
├── VISION.md                   # Pillars, horizons, goals, someday/maybe (future)
│
├── /projects/                  # Time-bound outcomes with clear endpoints
│   └── /[project-name]/
│       ├── roadmap.md          # Complete task inventory for this project
│       └── resources.md        # Pointers to resources/ relevant to this project
│
├── /areas/                     # Ongoing responsibilities, no end date
│   └── /[area-name]/
│       ├── tasks.md            # Ongoing tasks for this area
│       ├── practices.md        # Habits and routines
│       └── resources.md        # Pointers to resources/ relevant to this area
│
├── /resources/                 # Centralized information vault
│   ├── /[topic-folder]/        # Max one level deep (optional)
│   │   └── files...
│   └── scattered-files...      # Files at root are fine
│
├── /zettelkasten/              # Processed knowledge (wisdom, not information)
│   ├── /permanent/             # Atomic evergreen notes
│   └── index.md                # Entry points and structure notes
│
└── /archives/                  # Completed/inactive items
    ├── /projects/
    ├── /areas/
    └── /resources/
```

---

### Core Files Explained

#### inbox.md - Single Capture Point
**Purpose**: Capture EVERYTHING without thinking about where it goes.

**What goes here**:
- Tasks ("Call dentist")
- Ideas ("Meditation tracker app?")
- Notes from reading ("PPV: alignment over ad-hoc")
- Meeting notes ("Solla wants X by Friday")
- Random thoughts ("Why is Yiftach obsessed with dinosaurs?")

**Processing**: Daily (5-10 min), weekly full clear during review.

**Destinations after processing**:
- Task → `next-actions.md` or project/area `tasks.md`
- Resource → `resources/` with pointer from project/area
- Insight → `zettelkasten/permanent/` (process into atomic note)
- Habit → `areas/*/practices.md`
- Someday/Maybe → `VISION.md`
- Delete → Gone

---

#### next-actions.md - Daily Working File
**Purpose**: Context-based next actions you can do RIGHT NOW.

**Structure**:
```markdown
# Next Actions

## @home
[ ] Fix Yiftach's wall (home-renovation)
[ ] Remove books from daughters' room (home-renovation)

## @calls
[ ] Call designer about resuming (home-renovation)
[ ] Call Gil Rosenbaum Sunday 2025-10-19 (home-renovation)
[ ] Set dentist appointment (health)

## @computer
[ ] Time-block next week in Google Calendar (work)
[ ] Process course materials into knowledge base (billion-person-focus-group)
[ ] Create VISION.md with pillars (work-system)

## @anywhere (low energy)
[ ] Review zettelkasten index (work-system)

## Waiting For
[ ] Social Security 2024 payment summary (arriving via mail)
[ ] Designer callback (home-renovation)

## Active Projects (Review Weekly)
[-] Work System → See projects/work-system/roadmap.md
[-] Home Renovation → See projects/home-renovation/roadmap.md
[-] Billion Person Focus Group → See projects/billion-person-focus-group/roadmap.md
```

**Rules**:
- ONLY next actions (can be done now or very soon)
- Organized by context (where/when/with what can I do this?)
- Kept SHORT (if it's long, you're not doing weekly reviews)
- Project/area name in parentheses for reference

**Daily usage**: Open this file, look at your current context, pick something, do it, check it off.

---

#### VISION.md - Strategic Direction
**Purpose**: Your north star - where you're going and why.

**Structure**:
```markdown
# Vision

## Pillars (Life Areas)
1. Family First (Moran, Yiftach, Naomi, Elisheva)
2. Health & Wellbeing (ADHD management, sustainable work, meditation)
3. Meaningful Work (Sola PM role, advocacy for people with ADHD)
4. Home & Environment (renovation, creating order)
5. Financial Stability

## Horizons of Focus (GTD)
### Purpose (50,000 ft) - Why am I here?
[Your life purpose statement]

### Vision (40,000 ft) - What does success look like in 3-5 years?
[Your vision for each pillar]

### Goals (30,000 ft) - What am I working toward this year?
- [Specific goals for 2025]

### Areas of Focus (20,000 ft) - What needs attention?
- Health, Family, Work, Home, Financial (links to /areas/)

### Projects (10,000 ft) - What are current commitments?
- See PROJECTS.md for active projects

### Actions (Runway) - What needs to be done now?
- See next-actions.md

## Someday/Maybe
Ideas for future projects, organized by pillar:

### Family Pillar
- [ ] Plan summer trip to Greece
- [ ] Create family history book

### Health Pillar
- [ ] Try yoga practice
- [ ] Explore journaling

### Work Pillar
- [ ] Write blog post about ADHD in product management
- [ ] Speak at conference about inclusive work practices

[etc.]
```

**Review Cycle**: Quarterly (January, April, July, October).

---

#### PROJECTS.md - Active Projects Index
**Purpose**: List of all time-bound commitments.

**Structure**:
```markdown
# Active Projects

## Work System
**Goal**: Build unified productivity system
**Target**: End of October 2025
**Status**: In progress
**Details**: See projects/work-system/roadmap.md

## Home Renovation
**Goal**: Complete renovation with designer
**Target**: TBD (resuming now)
**Status**: Restarting
**Details**: See projects/home-renovation/roadmap.md

## Billion Person Focus Group MVP
**Goal**: Build MVP for Sola
**Target**: Q4 2025
**Status**: Gathering materials
**Details**: See projects/billion-person-focus-group/roadmap.md

# On Hold
[Projects paused but may resume]

# Completed
[See archives/projects/ for completed projects]
```

**Review Cycle**: Weekly (quick check), Monthly (deeper review).

---

### Projects Structure

Each project lives in `/projects/[project-name]/` with:

#### roadmap.md - Complete Task Inventory
**Purpose**: ALL tasks for this project (not just next actions).

**Example** (`projects/work-system/roadmap.md`):
```markdown
# Work System Project - Task Inventory

## Phase 1: Research (Completed 2025-10-13)
[x] Research PPV
[x] Research PARA
[x] Research GTD
[x] Research Zettelkasten
[x] Write synthesis document

## Phase 2: Foundation (In Progress)
[x] Rewrite synthesis (structure-first approach)
[ ] Create VISION.md with pillars and horizons
[ ] Create folder structure (areas, resources, zettelkasten)
[ ] Move inspirations to resources/productivity-research/
[ ] Create resources.md for work-system project
[ ] Rename ROADMAP.md → next-actions.md

## Phase 3: Workflow Setup
[ ] Set up inbox processing routine
[ ] Set up weekly review template
[ ] Process inbox.md into system
[ ] Convert inspiration docs to permanent notes

## Phase 4: Establish Rhythms
[ ] Run first weekly review
[ ] Run first monthly area reviews
[ ] Run first quarterly vision review
[ ] Adjust based on what works

## Notes
- Target completion: End of October 2025
- Success criteria: Using system daily without friction
```

**Review Cycle**: Weekly (identify next actions to pull into next-actions.md).

---

#### resources.md - Resource Pointers
**Purpose**: Point to relevant resources in the central vault.

**Example** (`projects/work-system/resources.md`):
```markdown
# Work System Resources

## Productivity Research
- resources/productivity-research/ppv.md
- resources/productivity-research/para.md
- resources/productivity-research/gtd.md
- resources/productivity-research/zettelkasten.md
- resources/productivity-research/unified-system-synthesis.md

## Reference
- zettelkasten/permanent/gtd-weekly-review.md (permanent note)
- zettelkasten/permanent/para-actionability-principle.md (permanent note)

## Related Projects
- N/A
```

**When to update**: When adding new resources, when processing resources into notes.

---

### Areas Structure

Each area lives in `/areas/[area-name]/` with:

#### tasks.md - Ongoing Tasks
**Purpose**: One-time tasks for this ongoing responsibility.

**Example** (`areas/health/tasks.md`):
```markdown
# Health Tasks

## Active
[ ] Set dentist appointment
[ ] Set dental hygienist appointment
[ ] Refill ADHD medication prescription
[ ] Schedule annual physical

## Completed (Last 30 days)
[x] Start daily meditation habit (2025-10-15)

## Someday
[ ] Explore therapy options
[ ] Research sleep tracking apps
```

**Review Cycle**: Weekly (pull next actions to next-actions.md), Monthly (deeper review).

---

#### practices.md - Habits and Routines
**Purpose**: Ongoing practices that don't have an "end" - they're continuous.

**Example** (`areas/health/practices.md`):
```markdown
# Health Practices

## Active Habits

### Daily Meditation (Waking Up app)
**Target**: 10 min/day
**Started**: 2025-10-15
**Current streak**: 3 days
**Best time**: Morning before kids wake
**Notes**:
- Missing days when oversleeping - maybe use alarm?
- Noticing better focus on meditation days

### ADHD Medication Consistency
**Target**: Daily with breakfast
**Started**: [whenever you started]
**Tracking**: [however you track]
**Notes**: Setting pill bottle next to coffee maker helps

## Habits in Development

### Evening Walk
**Target**: 3x/week, 20 minutes
**Status**: Not started yet
**Plan**: After dinner, before kids' bedtime

## Practices to Explore (Someday)
- Yoga (2x/week morning practice)
- Journaling (evening reflection)
- Cold showers (morning energizer)
```

**Review Cycle**: Daily (check-in during morning/evening routine), Weekly (assess progress).

---

#### resources.md - Resource Pointers
Same concept as project resources.md - points to central vault.

**Example** (`areas/health/resources.md`):
```markdown
# Health Resources

## ADHD
- resources/health/adhd-management-strategies.md
- zettelkasten/permanent/adhd-external-structures.md

## Meditation
- resources/health/waking-up-app-guide.md

## Medical
- resources/health/doctors-list.md
- resources/health/medication-history.md
```

---

### Resources Structure

Central vault at `/resources/` follows these rules:

**Organization**:
- **Maximum one level deep**: `resources/[topic-folder]/files` OR `resources/files`
- **Flat is fine**: Having scattered files at root is acceptable
- **No over-organizing**: Wait until project completes to organize further

**Example**:
```
/resources/
├── /productivity-research/       # One level deep
│   ├── ppv.md
│   ├── para.md
│   ├── gtd.md
│   ├── zettelkasten.md
│   └── unified-system-synthesis.md
│
├── /health/                      # One level deep
│   ├── adhd-management-strategies.md
│   ├── waking-up-app-guide.md
│   └── doctors-list.md
│
└── random-article.pdf            # Scattered files at root - OK!
```

**Resource Lifecycle**:
1. **Captured** → Goes to inbox.md
2. **Clarified** → Is this for a project/area? Save to resources/, add pointer in project/area resources.md
3. **Reviewed** → Weekly/Monthly - still needed? Extract insights to zettelkasten?
4. **Archived** → When project completes, decide: keep in resources/ (if reusable) or archive with project
5. **Processed** → Valuable insights extracted to zettelkasten/permanent/, original resource archived

**Key Principle**: Resources are **raw information** (documents, PDFs, research). Zettelkasten is **processed wisdom** (insights, atomic notes). Flow is: consume resource → extract insight → create permanent note → optionally keep resource if still needed.

---

### Zettelkasten Structure

**Purpose**: Build permanent knowledge base through atomic linked notes.

**Structure**:
```
/zettelkasten/
├── /permanent/              # Processed atomic notes
│   ├── gtd-weekly-review.md
│   ├── para-actionability-principle.md
│   ├── zettelkasten-atomic-notes.md
│   └── [date-time]-[title].md
└── index.md                 # Entry points, structure notes, maps of content
```

**What goes here**:
- Insights from reading (processed from resources)
- Ideas developed from inbox items
- Connections between concepts
- Learnings from project work

**What does NOT go here**:
- Raw captures (those go to inbox.md)
- Unprocessed articles (those go to resources/)
- Task lists (those go to next-actions.md or project/area tasks)
- Project documentation (that stays in projects/)

**Permanent Note Format**:
```markdown
# Atomic Notes Principle (Zettelkasten)

**Created**: 2025-10-13
**Tags**: #zettelkasten #knowledge-management #notes

## The Idea

Each note should contain exactly one idea, expressed completely. Like an atom - can't be broken down further without losing its meaning.

## Why This Matters

- Easy to link (one idea → one target)
- Easy to reuse (grab exactly what you need)
- Easy to understand (single concept, clear)
- Forces clarity of thinking

## Connection to Projects

This principle is used in:
- projects/work-system/ (building atomic task breakdowns)
- areas/work/ (creating clear documentation at Sola)

## Related Notes

- [[zettelkasten-linking-principle]]
- [[para-actionability-principle]]
- [[gtd-next-action-clarity]]

## Sources

- resources/productivity-research/zettelkasten.md (original research)
- Niklas Luhmann's original Zettelkasten method
```

**Review Cycle**: Weekly (process new insights from inbox/resources), Monthly (explore connections).

---

### The Three Pillars of Daily Work

Your daily routine centers on:

1. **inbox.md** - Capture everything
2. **next-actions.md** - Do from context lists
3. **Calendar** - Time-blocked commitments

**Morning Routine** (10-15 min):
1. Check **calendar** - what's time-blocked today?
2. Quick **inbox.md** processing - anything urgent from yesterday?
3. Review **next-actions.md** - what contexts will I be in today?
4. Check **areas/health/practices.md** - meditation done?

**Throughout Day**:
- **Capture to inbox.md** - every task, idea, meeting note
- **Do from next-actions.md** - pick by current context
- **Follow calendar** - attend time-blocks

**End of Day** (5-10 min):
- **Quick inbox processing** - don't let it pile up
- **Update next-actions.md** - check off completed items
- **Tomorrow prep** - what contexts will I be in? Anything urgent?

---

### Review Cycles

#### Daily Review (5-10 min)
**When**: End of day
**What**:
- Process inbox.md (at least partially)
- Update next-actions.md (check off done items)
- Check calendar for tomorrow
- Quick practices.md check-in

---

#### Weekly Review (60 min)
**When**: Sunday evening (or your preferred time)
**What**:

1. **Empty inbox.md** (15 min)
   - Process every item
   - Clarify: task? resource? insight? habit? delete?
   - Organize to appropriate location

2. **Review projects** (20 min)
   - Open each `projects/*/roadmap.md`
   - What's done? Check it off
   - What's next? Pull next action to next-actions.md
   - Any blockers? Add to waiting-for

3. **Review areas** (15 min)
   - Open each `areas/*/tasks.md`
   - What's done? Check it off
   - What's next? Pull next action to next-actions.md
   - Check `areas/*/practices.md` - how are habits going?

4. **Update next-actions.md** (5 min)
   - Remove completed items
   - Add next actions from projects/areas
   - Organize by context
   - Should be SHORT list of clear next actions

5. **Review calendar** (5 min)
   - Time-block next week
   - Add commitments from projects/areas
   - Block family time, meditation time, weekly review time

6. **Zettelkasten processing** (optional, 10 min)
   - Any insights from the week to capture?
   - Process one resource into permanent notes
   - Explore one connection between notes

---

#### Monthly Review (90 min)
**When**: Last Sunday of month
**What**:

1. **Run weekly review** (60 min) - Do full weekly review first

2. **Review areas deeply** (30 min)
   - Open each `areas/*/`
   - Is this area getting enough attention?
   - Are practices working? Need changes?
   - Any tasks that should become projects?
   - Any new resources needed?
   - Update `areas/*/tasks.md` and `areas/*/practices.md`

3. **Review PROJECTS.md** (15 min)
   - Any projects to complete/archive?
   - Any projects to start from someday/maybe?
   - Any projects to put on hold?

4. **Quick VISION.md check** (15 min)
   - Are projects/areas aligned with pillars?
   - Anything missing?
   - Any goals to adjust?

---

#### Quarterly Review (2-3 hours)
**When**: January, April, July, October
**What**:

1. **Run monthly review** (90 min) - Do full monthly review first

2. **Review VISION.md deeply** (60+ min)
   - **Pillars**: Are these still my core values? Any changes?
   - **Purpose**: Does this still resonate?
   - **Vision**: What does success look like in each pillar?
   - **Goals**: Review this year's goals - progress? Adjust? Add/remove?
   - **Someday/Maybe**: Review list - anything ready to become a project?

3. **Review Zettelkasten** (30 min)
   - What insights emerged this quarter?
   - What connections surprised you?
   - What permanent notes are most valuable?
   - Are you processing enough? Too much?

4. **System adjustments** (30 min)
   - What's working? Do more of that
   - What's not working? Stop or adjust
   - Any friction points? Fix them
   - Any new needs? Add minimally

---

## Part 2: The Rationale

### What We Took From Each System

#### From PPV (Pillars, Pipelines, Vaults)
**Took**:
- **Pillars**: Life areas based on values (in VISION.md)
- **Purpose-driven thinking**: Quarterly alignment reviews
- **Vaults concept**: Centralized resources/ storage

**Didn't take**:
- Deep hierarchies (Tier 1 → Tier 2 → Tier 3 → Tier 4)
- Complex planning cycles
- Elaborate goal cascading

**Why**: PPV's strategic clarity is valuable, but hierarchies create overhead. We use pillars for direction but keep action management flat.

---

#### From PARA (Projects, Areas, Resources, Archives)
**Took**:
- **Four categories**: Projects, Areas, Resources, Archives
- **Actionability principle**: Organize by "is this active?"
- **Just-in-time organization**: Don't over-organize upfront

**Didn't take**:
- Top-level Resources folder for everything
- Mixing tasks and reference in same structure

**Why**: PARA's simplicity is perfect, but we adapted Resources to be centralized (pointed to by projects/areas) and separated tasks clearly from reference material.

---

#### From GTD (Getting Things Done)
**Took**:
- **Capture → Clarify → Organize → Reflect → Engage** workflow
- **Context-based next actions**: @home, @calls, @computer
- **Weekly review**: Core rhythm
- **Horizons of Focus**: 6 levels from actions to purpose
- **Trusted system principle**: External brain, not mental load

**Didn't take**:
- Complex contexts (we kept it simple)
- Separate waiting-for list (integrated into next-actions.md)

**Why**: GTD's workflow is the engine of the system. Context-based actions eliminate "what should I do now?" paralysis. Weekly review keeps everything current.

---

#### From Zettelkasten
**Took**:
- **Atomic notes principle**: One idea per note
- **Bidirectional linking**: Notes reference each other
- **Bottom-up emergence**: Insights arise organically
- **Permanent notes concept**: Processed wisdom, not raw info

**Didn't take**:
- Fleeting notes folder (merged into inbox.md)
- Literature notes folder (merged into inbox.md processing)
- Complex numbering systems

**Why**: Zettelkasten's knowledge development is powerful, but we simplified capture (single inbox) while keeping the insight extraction process.

---

### Tensions We Identified

1. **Top-Down vs Bottom-Up**
   - **Tension**: PPV wants goal-driven alignment; Zettelkasten wants organic emergence
   - **Resolution**: Separate domains - VISION.md is top-down; zettelkasten/ is bottom-up; they inform each other through reviews

2. **Hierarchical vs Flat**
   - **Tension**: PPV uses deep hierarchies; PARA/GTD prefer flat structures
   - **Resolution**: Flat action management (next-actions.md, projects/areas) + maximum 2-level resources/ + no hierarchy in zettelkasten

3. **Planning vs Action**
   - **Tension**: PPV emphasizes planning; GTD emphasizes doing
   - **Resolution**: Minimal planning (quarterly VISION review, weekly project review) + maximum action (daily next-actions.md usage)

4. **Categorization vs Links**
   - **Tension**: PARA/PPV use folders; Zettelkasten uses links
   - **Resolution**: Folders for action management (findability); links for knowledge (serendipity); both coexist in different domains

5. **Completeness vs Minimalism**
   - **Tension**: PPV is comprehensive; GTD/PARA are focused
   - **Resolution**: Complete in scope (covers purpose, knowledge, action) but minimal in implementation (simple files, clear rules)

6. **Multiple Inboxes vs Single Capture**
   - **Tension**: Zettelkasten wants separate fleeting/literature notes; GTD wants single inbox
   - **Resolution**: Single inbox.md for ALL capture; processing determines destination

7. **Tasks vs Habits**
   - **Tension**: GTD's next actions are one-time; areas have ongoing practices
   - **Resolution**: Separate tasks.md (one-time actions) from practices.md (ongoing habits) in areas/

8. **Resources in Projects vs Central Vault**
   - **Tension**: PARA puts resources in projects; PPV uses central vault
   - **Resolution**: Central resources/ vault (single source of truth) + resources.md pointers in each project/area (distributed access)

---

### How We Resolved Overlaps

**Project Definition**:
- Use PARA's definition: Time-bound outcome with clear endpoint
- Reject PPV's 4-tier hierarchy
- Adopt GTD's "multi-step outcome" simplicity

**Reference Material**:
- Use central resources/ vault (PPV's Vaults concept)
- Projects/areas point to resources via resources.md files
- Zettelkasten is separate (processed knowledge, not raw info)
- Archives include both completed projects AND inactive resources

**Organization Philosophy**:
- Strategic: Top-down (VISION.md pillars)
- Knowledge: Bottom-up (zettelkasten/ emergence)
- Action: Flat (next-actions.md contexts, simple project/area folders)

**Knowledge vs Information**:
- **Information** (raw): resources/ - documents, PDFs, articles
- **Knowledge** (processed): zettelkasten/permanent/ - insights, atomic notes
- **Flow**: Consume resource → extract insight → create permanent note → optionally archive resource

---

## Part 3: Implementation

### Mapping Current State to New Structure

| Current File/Folder | New Location | Action Required |
|-------------------|--------------|-----------------|
| `ROADMAP.md` | `next-actions.md` | Rename + restructure by context |
| `PROJECTS.md` | `PROJECTS.md` | Keep, minor cleanup |
| `ABOUT.md` | `ABOUT.md` | Keep as-is |
| N/A | `VISION.md` | **Create** - pillars, horizons, someday/maybe |
| `ideas/` | `inbox.md` | Merge into single inbox file |
| `knowledge.md` | `zettelkasten/index.md` | Move + evolve into structure notes |
| `projects/work-system/` | `projects/work-system/` | Keep, add `resources.md` |
| `projects/home-renovation/` | `projects/home-renovation/` | Keep, add `resources.md` |
| `projects/billion-person-focus-group/` | `projects/billion-person-focus-group/` | Keep, add `resources.md` |
| `projects/financial-control/` | `areas/financial/` or `archives/` | **Decide**: active area or archive? |
| `projects/*/inspirations/` | `resources/productivity-research/` | Move to central vault |
| `trips/vatican/` | `archives/projects/vatican-trip-2025/` | Archive (completed) |
| `trips/castel-gandolfo/` | `archives/` | Archive (cancelled) |
| N/A | `areas/health/` | **Create** - tasks.md, practices.md, resources.md |
| N/A | `areas/family/` | **Create** - tasks.md, practices.md, resources.md |
| N/A | `areas/work/` | **Create** - tasks.md, practices.md, resources.md |
| N/A | `areas/home/` | **Create** - tasks.md, practices.md, resources.md |
| N/A | `areas/financial/` | **Create** - tasks.md, resources.md |
| N/A | `resources/` | **Create** central vault |
| N/A | `zettelkasten/permanent/` | **Create** for processed notes |

---

### Migration Steps

#### Phase 1: Foundation (This Week)

1. **Create VISION.md**
   - Extract pillars from ABOUT.md
   - Add horizons of focus
   - Move ROADMAP.md backlog items to someday/maybe section
   - Define success criteria for each pillar

2. **Create folder structure**
   ```bash
   mkdir -p areas/{health,family,work,home,financial}
   mkdir -p resources/productivity-research
   mkdir -p zettelkasten/permanent
   mkdir -p archives/{projects,areas,resources}
   ```

3. **Create area files**
   - `areas/health/{tasks.md, practices.md, resources.md}`
   - `areas/family/{tasks.md, practices.md, resources.md}`
   - `areas/work/{tasks.md, practices.md, resources.md}`
   - `areas/home/{tasks.md, practices.md, resources.md}`
   - `areas/financial/{tasks.md, resources.md}`

4. **Create inbox.md**
   - Merge `ideas/` content into single inbox file
   - Process everything in inbox (clarify + organize)

5. **Restructure ROADMAP.md → next-actions.md**
   - Rename file
   - Organize tasks by context (@home, @calls, @computer, @anywhere)
   - Move project references to "Active Projects" section
   - Keep waiting-for section
   - Remove backlog (moved to VISION.md someday/maybe)

6. **Move resources to central vault**
   - `projects/work-system/inspirations/` → `resources/productivity-research/`
   - Create `projects/work-system/resources.md` pointing to new location
   - Repeat for other projects as needed

7. **Archive completed projects**
   - `trips/vatican/` → `archives/projects/vatican-trip-2025/`
   - `trips/castel-gandolfo/` → `archives/projects/castel-gandolfo-trip-cancelled/`

---

#### Phase 2: Workflow Integration (Next Week)

1. **Set up daily routine**
   - Morning: Check calendar → quick inbox process → review next-actions.md
   - Throughout day: Capture to inbox.md
   - Evening: Process inbox → update next-actions.md

2. **Set up weekly review**
   - Pick time (Sunday evening suggested)
   - Create weekly review checklist
   - Run first weekly review using new structure
   - Adjust based on what worked/didn't work

3. **Populate area files**
   - Move current tasks from next-actions.md to appropriate area tasks.md
   - Create practices.md for health area (meditation habit)
   - Add resource pointers as needed

4. **Process one inspiration doc to zettelkasten**
   - Pick one (e.g., GTD research)
   - Extract 2-3 key insights
   - Create atomic permanent notes
   - Link them together
   - Update zettelkasten/index.md
   - See how it feels

---

#### Phase 3: Rhythm Establishment (Rest of October)

1. **Daily rhythm**
   - Practice inbox → next-actions → calendar workflow
   - Build muscle memory
   - Adjust as needed

2. **Weekly reviews**
   - Run 2-3 weekly reviews
   - Refine process
   - Keep inbox empty
   - Keep next-actions.md short and current

3. **Monthly area review**
   - End of October: First monthly review
   - Deep dive on each area
   - Assess practices (is meditation habit sticking?)
   - Adjust system based on friction points

---

#### Phase 4: First Quarterly Review (January 2026)

1. **Full VISION.md review**
   - Pillars still accurate?
   - Purpose still resonates?
   - Goals for 2026?
   - Someday/maybe → projects?

2. **Zettelkasten review**
   - What insights emerged?
   - What connections formed?
   - Are you processing enough resources?

3. **System refinement**
   - What worked well?
   - What created friction?
   - What to add/remove/adjust?

---

### Current Tasks Mapped to New System

From current ROADMAP.md:

**High Priority** → Where they go:
- "Call designer (home renovation)" → `next-actions.md` @calls (from project: home-renovation)
- "Time-block next week" → `next-actions.md` @computer (from area: work)
- "Call Gil Rosenbaum Sunday" → `next-actions.md` @calls (from project: home-renovation)
- "Set dentist appointment" → `areas/health/tasks.md` → pull to `next-actions.md` @calls
- "Set dental hygienist appointment" → `areas/health/tasks.md` → pull to `next-actions.md` @calls
- "Daily meditation habit" → `areas/health/practices.md` (NOT a task, it's a practice)

**In Progress** → Where they go:
- "Answer about-questions.md" → `projects/work-system/roadmap.md` (pillar clarification work)
- "Gather course materials" → `projects/billion-person-focus-group/roadmap.md`
- "Work System project" → `PROJECTS.md` + `projects/work-system/roadmap.md`
- "Home Renovation project" → `PROJECTS.md` + `projects/home-renovation/roadmap.md`
- "Billion Person Focus Group project" → `PROJECTS.md` + `projects/billion-person-focus-group/roadmap.md`

**Waiting For** → Where they go:
- "Social Security payment" → `next-actions.md` waiting-for section (from area: financial)

**Backlog** → Where they go:
- "Fix Yiftach's wall" → `projects/home-renovation/roadmap.md` (future phase)
- "Paint daughters' room" → `projects/home-renovation/roadmap.md` (future phase)
- "Financial control questions" → `areas/financial/tasks.md` or `VISION.md` someday/maybe

---

## Part 4: Why This Works for You

### ADHD Considerations

1. **Single capture point** (inbox.md) - No decision fatigue about where to put things
2. **External structure** - System provides scaffolding (daily/weekly/monthly/quarterly cycles)
3. **Clear next actions** - Always know what you can do right now (context-based)
4. **Regular processing** - Daily/weekly rhythms prevent pile-up and overwhelm
5. **Simple categories** - Only 4 (Projects, Areas, Resources, Archives)
6. **No mental load** - Everything lives outside your head in trusted system

### Family-First Values

1. **Family is Pillar #1** in VISION.md - System explicitly prioritizes family
2. **Time-blocking in calendar** - Protect family time from work creep
3. **Sustainable pace** - No elaborate planning cycles stealing family time
4. **Areas include family** - Ongoing attention to family needs (not just projects)
5. **Trip planning support** - Resources/ and project structure supports family experiences

### Meaningful Work at Sola

1. **Project structure** - Billion-person-focus-group has clear home
2. **Knowledge capture** - Zettelkasten captures PM insights and learnings
3. **Work area** - Ongoing PM responsibilities (not just projects)
4. **Advocacy pillar** - ADHD advocacy work fits in vision and can spawn projects
5. **Professional development** - Resources/ and zettelkasten/ support continuous learning

### Sustainable Systems

1. **Markdown + folders** - No complex tools, no vendor lock-in
2. **Iterative** - Start simple, add only what's needed
3. **Flexible** - PARA allows moving projects → areas → archives as life changes
4. **Low overhead** - Weekly review is ~60 min, daily is ~10 min
5. **No over-organizing** - Maximum 2 levels deep, flat structures, simple rules

---

## Conclusion

This unified system combines:
- **PPV's purpose-driven clarity** → VISION.md pillars and quarterly reviews
- **PARA's organizational simplicity** → Projects, Areas, Resources, Archives
- **GTD's stress-free action management** → Context-based next actions and weekly reviews
- **Zettelkasten's knowledge emergence** → Atomic permanent notes and organic linking

**Key innovations**:
- Single inbox.md for all capture (solves multiple-inboxes problem)
- Central resources/ vault with distributed access via resources.md pointers
- Separation of tasks.md (one-time) from practices.md (ongoing habits) in areas
- Context-based next-actions.md as daily working file
- VISION.md combining pillars, horizons, and someday/maybe

**For you specifically**:
- Respects ADHD (external structure, clear actions, simple categories)
- Honors family-first values (explicit pillar, time-blocking, sustainable pace)
- Supports meaningful work (project/area structure, knowledge capture)
- Creates space for deep thinking (zettelkasten) while keeping life moving (GTD workflow)

**Most importantly**: Simple enough to actually use, flexible enough to evolve, comprehensive enough to not need another system.

---

## Next Actions

1. Review this document - does it make sense?
2. Decide: implement all at once or gradual?
3. Start with Phase 1 (foundation setup)
4. Run first weekly review
5. Adjust based on what works

**Ready when you are.**
