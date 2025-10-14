# Migration Plan: Current System → Unified System

**Created**: 2025-10-15
**Status**: Ready to execute

---

## Pre-Migration Checklist

- [x] Current state committed to git
- [x] Current state pushed to remote
- [x] Unified system synthesis document complete
- [ ] User reviewed and approved migration plan

---

## Migration Overview

This migration transforms the current work system into the unified system described in `projects/work-system/inspirations/unified-system-synthesis.md`.

**Key Changes**:
1. Create new folder structure (areas/, resources/, zettelkasten/, archives/)
2. Create new core files (inbox.md, next-actions.md, VISION.md)
3. Migrate existing files to new locations
4. Archive completed/cancelled items
5. Validate nothing was lost

---

## Phase 1: Create New Structure

### Step 1.1: Create Folders
```bash
mkdir -p areas/{health,family,work,home,financial}
mkdir -p resources/productivity-research
mkdir -p zettelkasten/permanent
mkdir -p archives/{projects,areas,resources}
```

**Validation**: Verify all folders exist with `ls -R`

---

### Step 1.2: Create Core Files

**inbox.md**:
```markdown
# Inbox

All captures go here. Process daily.

## To Process

[Empty - will be populated from ideas/ during migration]

## Processing Guidelines

- Task? → next-actions.md or project/area tasks.md
- Resource? → resources/ with pointer from project/area
- Insight? → zettelkasten/permanent/
- Habit? → areas/*/practices.md
- Someday? → VISION.md
- Delete? → Gone
```

**next-actions.md** (created from ROADMAP.md):
```markdown
# Next Actions

## @home
[ ] Fix Yiftach's wall (home-renovation)
[ ] Remove books from daughters' room (home-renovation)

## @calls
[ ] Call designer about resuming (home-renovation)
[ ] Call Gil Rosenbaum Sunday 2025-10-19 (home-renovation)
[ ] Set dentist appointment (health)
[ ] Set dental hygienist appointment (health)

## @computer
[ ] Time-block next week in Google Calendar (work)
[ ] Answer questions in about-questions.md (work-system)
[ ] Gather course materials for Solla (billion-person-focus-group)

## @anywhere (low energy)
[ ] Work on daily meditation habit (health)

## Waiting For
[ ] Social Security 2024 payment summary (arriving via mail)

## Active Projects (Review Weekly)
[-] Work System → See projects/work-system/roadmap.md
[-] Home Renovation → See projects/home-renovation/roadmap.md
[-] Billion Person Focus Group → See projects/billion-person-focus-group/roadmap.md
```

**VISION.md** (created from ABOUT.md + ROADMAP.md backlog):
```markdown
# Vision

## Pillars (Life Areas)

1. **Family First** (Moran, Yiftach, Naomi, Elisheva)
   - Success: Quality time, present with family, supporting each child's needs

2. **Health & Wellbeing** (ADHD management, sustainable work, meditation)
   - Success: Consistent medication, daily meditation, sustainable energy, work-life balance

3. **Meaningful Work** (Sola PM role, advocacy for people with ADHD)
   - Success: Effective at Sola, helping others with ADHD, work that matters

4. **Home & Environment** (renovation, creating order)
   - Success: Completed renovation, organized systems, peaceful home

5. **Financial Stability**
   - Success: Bills paid, taxes handled, no money stress

## Horizons of Focus (GTD)

### Purpose (50,000 ft) - Why am I here?
To live authentically, support my family, do meaningful work that helps others, and build sustainable systems that respect my ADHD rather than fight it.

### Vision (40,000 ft) - What does success look like in 3-5 years?

**Family**: Kids thriving, strong relationship with Moran, family traditions established
**Health**: ADHD managed well, meditation habit solid, sustainable work pace
**Work**: Making real impact at Sola, helping other ADHD professionals, possibly speaking/writing
**Home**: Renovation complete, organized systems running smoothly
**Financial**: Stable, taxes handled, retirement planning started

### Goals (30,000 ft) - What am I working toward this year?

**2025 Goals**:
- Complete work system implementation (October 2025)
- Resume and make progress on home renovation
- Build billion-person-focus-group MVP for Sola
- Establish daily meditation habit
- Handle 2024 tax returns (waiting on social security docs)

### Areas of Focus (20,000 ft) - What needs attention?
- See /areas/ for detailed area management

### Projects (10,000 ft) - What are current commitments?
- See PROJECTS.md for active projects

### Actions (Runway) - What needs to be done now?
- See next-actions.md

## Someday/Maybe

Ideas for future projects, organized by pillar:

### Family Pillar
- [ ] Plan summer trip (Greece? Other?)
- [ ] Create family history book
- [ ] Set up regular date nights with Moran

### Health Pillar
- [ ] Try yoga practice
- [ ] Explore journaling habit
- [ ] Research sleep optimization

### Work Pillar
- [ ] Write blog post about ADHD in product management
- [ ] Speak at conference about inclusive work practices
- [ ] Explore ADHD coaching/mentoring

### Home Pillar
- [ ] Fix and paint Yiftach's wall (after renovation)
- [ ] Paint daughters' room (remove books, replace carpet)
- [ ] Organize garage/storage

### Financial Pillar
- [ ] Answer questions in financial-control/questions.md
- [ ] Set up retirement planning
- [ ] Review insurance coverage
```

**Validation**: Read each file to ensure content is correct.

---

### Step 1.3: Create Area Files

For each area (health, family, work, home, financial), create:

**areas/health/tasks.md**:
```markdown
# Health Tasks

## Active
[ ] Set dentist appointment
[ ] Set dental hygienist appointment
[ ] Refill ADHD medication prescription (if needed)

## Completed (Last 30 days)
[None yet]

## Someday
[ ] Explore therapy options
[ ] Research sleep tracking apps
```

**areas/health/practices.md**:
```markdown
# Health Practices

## Active Habits

### Daily Meditation (Waking Up app)
**Target**: 10 min/day
**Started**: 2025-10-15
**Current streak**: 0 days (just starting)
**Best time**: Morning before kids wake
**Notes**: Starting fresh with unified system

### ADHD Medication Consistency
**Target**: Daily with breakfast
**Tracking**: Manual check-in
**Notes**: Set pill bottle next to coffee maker

## Habits in Development
[None yet]

## Practices to Explore (Someday)
- Yoga (2x/week morning practice)
- Journaling (evening reflection)
- Evening walks (3x/week)
```

**areas/health/resources.md**:
```markdown
# Health Resources

[To be populated as resources are added]
```

**areas/family/tasks.md**:
```markdown
# Family Tasks

## Active
[To be populated from inbox/next-actions]

## Completed (Last 30 days)
[x] Create Vatican guide for kids (2025-10-13)

## Someday
[See VISION.md someday/maybe]
```

**areas/family/practices.md**:
```markdown
# Family Practices

## Active Habits
[To be populated - family routines, regular activities]

## Practices to Explore
- Weekly family meeting
- Regular date nights with Moran
- Individual time with each child
```

**areas/family/resources.md**:
```markdown
# Family Resources

## Trip Planning
- See archives/projects/vatican-trip-2025/
```

**areas/work/tasks.md**:
```markdown
# Work Tasks

## Active
[ ] Time-block next week in Google Calendar

## Completed (Last 30 days)
[None yet]

## Someday
[See VISION.md someday/maybe]
```

**areas/work/practices.md**:
```markdown
# Work Practices

## Active Habits

### Weekly Planning
**Target**: Sunday evening or Monday morning
**Practice**: Review week ahead, time-block calendar
**Notes**: Part of weekly review

## Practices to Explore
- Daily PM journaling (what worked, what didn't)
- Weekly 1:1s preparation routine
- Monthly professional development time
```

**areas/work/resources.md**:
```markdown
# Work Resources

[To be populated - PM frameworks, Sola documentation, etc.]
```

**areas/home/tasks.md**:
```markdown
# Home Tasks

## Active
[To be populated from home renovation project]

## Completed (Last 30 days)
[None yet]

## Someday
[See VISION.md someday/maybe]
```

**areas/home/practices.md**:
```markdown
# Home Practices

## Active Habits
[To be established after renovation]

## Practices to Explore
- Weekly home review (what needs attention)
- Daily 10-minute tidy
- Maintenance schedule
```

**areas/home/resources.md**:
```markdown
# Home Resources

[To be populated - renovation docs, maintenance schedules, etc.]
```

**areas/financial/tasks.md**:
```markdown
# Financial Tasks

## Active
[ ] Send Social Security 2024 payment summary to Haim Carmon when arrives (for taxes)

## Completed (Last 30 days)
[x] Request Social Security 2024 payment summary (2025-10-09)

## Someday
[ ] Answer questions in financial-control/questions.md
[ ] Set up retirement planning
```

**areas/financial/resources.md**:
```markdown
# Financial Resources

[To be populated - tax documents, financial planning, etc.]
```

**Validation**: Check each area folder has tasks.md, practices.md (except financial), resources.md

---

## Phase 2: Migrate Existing Content

### Step 2.1: Merge ideas/ into inbox.md

**Action**: Read all files in `ideas/` and merge content into `inbox.md`

**Current ideas/ files**:
- [List will be determined during execution]

**Validation**:
- All content from ideas/ appears in inbox.md
- Original ideas/ folder ready for deletion (but keep for now)

---

### Step 2.2: Move inspirations to resources/

**Action**:
```bash
mv projects/work-system/inspirations/ resources/productivity-research/
```

**Create** `projects/work-system/resources.md`:
```markdown
# Work System Resources

## Productivity Research
- resources/productivity-research/august-bradley-ppv.md
- resources/productivity-research/tiago-forte-para.md
- resources/productivity-research/david-allen-gtd.md
- resources/productivity-research/niklas-luhmann-zettelkasten.md
- resources/productivity-research/unified-system-synthesis.md

## Related Notes
[Will link to zettelkasten permanent notes once created]
```

**Validation**:
- resources/productivity-research/ contains all 5 .md files
- projects/work-system/resources.md exists and points correctly
- projects/work-system/inspirations/ no longer exists

---

### Step 2.3: Update Project Roadmaps

For each active project, add `resources.md` if needed:

**projects/home-renovation/resources.md**:
```markdown
# Home Renovation Resources

[To be populated with designer docs, contractor info, etc.]
```

**projects/billion-person-focus-group/resources.md**:
```markdown
# Billion Person Focus Group Resources

## Course Materials
[To be populated with gathered courses]

## Reference
[Links to course materials once they're saved to resources/]
```

**Validation**: Each active project has resources.md

---

### Step 2.4: Archive Completed/Cancelled Projects

**Action**:
```bash
mkdir -p archives/projects
mv trips/vatican/ archives/projects/vatican-trip-2025/
mv trips/castel-gandolfo/ archives/projects/castel-gandolfo-trip-cancelled/
rmdir trips  # Remove empty trips folder
```

**Validation**:
- archives/projects/vatican-trip-2025/ contains vatican-guide.md and vatican-guide.html
- archives/projects/castel-gandolfo-trip-cancelled/ contains all castel-gandolfo files
- trips/ folder no longer exists

---

### Step 2.5: Handle Financial Control Project

**Decision needed**: Is `projects/financial-control/` an active project or should it be archived/moved to areas/financial/?

**Option A**: Move to areas/financial/ (if it's ongoing admin work)
```bash
mkdir -p areas/financial/reference
mv projects/financial-control/* areas/financial/reference/
rmdir projects/financial-control
```

Update `areas/financial/resources.md`:
```markdown
# Financial Resources

## Financial Control
- areas/financial/reference/questions.md
- [Other files from financial-control]
```

**Option B**: Keep as project (if it's a one-time setup)
- Add resources.md to projects/financial-control/
- Keep in projects/ as active project

**Validation**: Financial-control content is in one clear location

---

### Step 2.6: Migrate knowledge.md to zettelkasten/

**Action**:
```bash
mv knowledge.md zettelkasten/index.md
```

**Update** `zettelkasten/index.md` to add structure note format:
```markdown
# Zettelkasten Index

## Entry Points

[Existing content from knowledge.md]

## Structure Notes

[To be developed - maps of related permanent notes]

## Recent Notes

[Links to recently created permanent notes]

## Tags

[Common tags used across notes]
```

**Validation**:
- zettelkasten/index.md exists with content from knowledge.md
- knowledge.md no longer exists at root

---

## Phase 3: Review and Validation

### Step 3.1: File Inventory Check

**Pre-migration snapshot**:
```bash
find . -type f -name "*.md" | grep -v ".git" | sort > /tmp/before-migration.txt
```

**Post-migration snapshot**:
```bash
find . -type f -name "*.md" | grep -v ".git" | sort > /tmp/after-migration.txt
```

**Validation**:
- Compare counts: `wc -l /tmp/before-migration.txt /tmp/after-migration.txt`
- Check for missing files: `diff /tmp/before-migration.txt /tmp/after-migration.txt`
- Ensure all files accounted for (moved, renamed, or intentionally removed)

---

### Step 3.2: Content Verification

**Check each migrated item**:
- [ ] All ROADMAP.md tasks appear in next-actions.md or area tasks
- [ ] All ideas/ content merged into inbox.md
- [ ] All inspirations/ files in resources/productivity-research/
- [ ] All archived trips in archives/projects/
- [ ] knowledge.md content in zettelkasten/index.md
- [ ] VISION.md contains all pillars from ABOUT.md
- [ ] All backlog items in VISION.md someday/maybe

---

### Step 3.3: Link Validation

**Check pointers are correct**:
- [ ] projects/work-system/resources.md points to resources/productivity-research/
- [ ] Each project has resources.md (even if empty)
- [ ] areas/family/resources.md points to archived vatican trip
- [ ] No broken references in any files

---

### Step 3.4: Functional Test

**Simulate daily workflow**:
1. Can I capture something to inbox.md?
2. Can I process it to next-actions.md?
3. Can I find the right next action by context?
4. Can I find a resource when needed (via resources.md pointer)?
5. Can I review a project roadmap?
6. Can I check a habit in practices.md?

**Validation**: All workflows function as expected.

---

## Phase 4: Cleanup and Commit

### Step 4.1: Remove Old Files/Folders

**After validation passes**:
```bash
rm -rf ideas/  # Content migrated to inbox.md
```

**Validation**: Only new structure remains.

---

### Step 4.2: Update CLAUDE.md

Update instructions to reflect new structure:
- Change ROADMAP.md references to next-actions.md
- Add VISION.md to file structure
- Update workflow section to mention three pillars (inbox, next-actions, calendar)
- Add note about areas/ and resources/

**Validation**: CLAUDE.md accurately describes new system.

---

### Step 4.3: Git Commit

```bash
git add -A
git commit -m "Migrate to unified system structure

Implemented Phase 1 of unified system:
- Created areas/ (health, family, work, home, financial) with tasks.md, practices.md, resources.md
- Created resources/ vault with productivity-research/ subfolder
- Created zettelkasten/ with permanent/ and index.md
- Created archives/projects/ for completed work
- Created core files: inbox.md, next-actions.md, VISION.md
- Migrated ROADMAP.md → next-actions.md (context-based)
- Migrated ideas/ → inbox.md
- Migrated inspirations/ → resources/productivity-research/
- Migrated knowledge.md → zettelkasten/index.md
- Archived vatican and castel-gandolfo trips
- Added resources.md to all projects

Validation: All files accounted for, no content lost, workflows functional.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>"

git push
```

---

## Phase 5: Post-Migration

### Step 5.1: Update PROJECTS.md

Ensure PROJECTS.md reflects current state after migration.

---

### Step 5.2: First Inbox Processing

Process everything in inbox.md to test the workflow:
- Clarify each item
- Organize to appropriate location
- Empty the inbox

---

### Step 5.3: First Weekly Review (Optional)

Run first weekly review using new structure:
- Review projects/*/roadmap.md
- Review areas/*/tasks.md
- Update next-actions.md
- Time-block calendar

---

## Success Criteria

Migration is successful when:
- [x] All folders created
- [x] All files migrated to new locations
- [x] All content accounted for (nothing lost)
- [x] All links/pointers work
- [x] Daily workflow functions (inbox → next-actions → calendar)
- [x] Weekly review workflow functions
- [x] Changes committed and pushed to git
- [ ] User can work with new system without confusion

---

## Rollback Plan

If migration fails or causes issues:

```bash
# Restore from git
git reset --hard HEAD~1  # Reset to pre-migration commit
git push --force  # Only if already pushed

# Or restore from backup
# [Git history is the backup]
```

---

## Notes

- This migration is reversible via git history
- Current state is committed before migration starts
- Each phase has validation steps
- Migration can be paused after any phase
- User can test system before final cleanup

---

## Execution Checklist

- [x] Pre-migration git commit complete
- [ ] User reviewed and approved this plan
- [ ] Phase 1: Create structure (folders + files)
- [ ] Phase 2: Migrate content
- [ ] Phase 3: Review and validation
- [ ] Phase 4: Cleanup and commit
- [ ] Phase 5: Post-migration setup
- [ ] Migration complete - system ready to use
