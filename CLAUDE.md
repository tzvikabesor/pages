# Claude Instructions

**ALWAYS check next-actions.md first** for current work. See `VISION.md` for strategic direction and `PROJECTS.md` for active projects.

## Work System Overview

This is a personal work management system designed for:
- **Task tracking**: High-level goals and current work status
- **Knowledge capture**: Learnings, insights, and reference material
- **Interface generation**: Creating tools and workflows based on captured knowledge

## File Structure

### Core Files
- `ABOUT.md`: Your background, story, current needs and wants - context for all work
- `inbox.md`: Single capture point for everything (tasks, ideas, notes, resources)
- `next-actions.md`: Context-based next actions (@home, @calls, @computer, @anywhere) - CHECK THIS FOR DAILY WORK
- `VISION.md`: Strategic direction - pillars, horizons, goals, someday/maybe (quarterly review)
- `PROJECTS.md`: List of all active projects
- `CLAUDE.md`: This file - instructions for how to use the system

### Documentation
- `.claude/context.md`: Project context and background information
- `.claude/knowledge.md`: Accumulated learnings and insights
- `.claude/commands/`: Custom commands for workflow automation

### Working Directories
- `projects/`: Time-bound outcomes with clear endpoints (each has roadmap.md, resources.md)
- `areas/`: Ongoing responsibilities with no end date (health, family, work, home, financial)
  - Each area has: tasks.md, practices.md, resources.md
- `resources/`: Centralized vault for reference materials (max 2 levels deep)
  - Projects/areas point to resources via their resources.md files
- `zettelkasten/`: Processed knowledge - permanent atomic notes with links
  - `permanent/`: Evergreen notes with single ideas
  - `index.md`: Entry points and structure notes
- `archives/`: Completed projects, inactive areas, old resources
- `scripts/`: Utility scripts and automation tools
- `interfaces/`: Dashboards, tools, and generated interfaces built from knowledge

## Work Organization

### The Three Pillars of Daily Work

Your daily routine centers on:
1. **inbox.md** - Capture everything without thinking
2. **next-actions.md** - Do from context lists (@home, @calls, @computer, @anywhere)
3. **Calendar** - Time-blocked commitments

### GTD Workflow (Capture → Clarify → Organize → Reflect → Engage)

**Capture**: Everything goes to `inbox.md`

**Clarify**: Daily processing - what is this?
- Task? → next-actions.md or project/area tasks.md
- Resource? → resources/ with pointer from project/area
- Insight? → zettelkasten/permanent/
- Habit? → areas/*/practices.md
- Someday? → VISION.md someday/maybe
- Delete? → Gone

**Organize**: Put it in the right place

**Reflect**: Weekly review (see Review Cycles below)

**Engage**: Pick from next-actions.md based on context and energy

### Projects vs Areas

- **Projects** (projects/): Time-bound outcomes with clear endpoints
  - Each has: roadmap.md (task inventory), resources.md (pointers to resources/)
  - Examples: Work System, Home Renovation, Billion Person Focus Group MVP

- **Areas** (areas/): Ongoing responsibilities, no end date
  - Each has: tasks.md (one-time actions), practices.md (habits/routines), resources.md
  - Examples: Health, Family, Work, Home, Financial

## Review Cycles

**Daily** (5-10 min):
- Process inbox.md (at least partially)
- Update next-actions.md (check off done items)
- Check calendar for tomorrow
- Quick practices check-in (areas/*/practices.md)

**Weekly** (60 min, Sunday evening):
1. Empty inbox.md completely
2. Review each projects/*/roadmap.md - what's done? What's next?
3. Review each areas/*/tasks.md - what's done? What's next?
4. Update next-actions.md with pulled next actions by context
5. Review calendar - time-block next week
6. Optional: Process one resource into zettelkasten

**Monthly** (90 min, last Sunday):
- Full weekly review first
- Deep review of each area (are practices working?)
- Review PROJECTS.md (complete/start/pause anything?)
- Quick VISION.md check (aligned with pillars?)

**Quarterly** (2-3 hours, Jan/Apr/Jul/Oct):
- Full monthly review first
- Deep VISION.md review (pillars, purpose, vision, goals)
- Review someday/maybe - anything ready for projects?
- Zettelkasten review - what insights emerged?
- System adjustments - what's working? What's not?

## Rules

1. **When user says they'll do something**: Add it as a task to next-actions.md (with context) or appropriate project/area tasks.md
2. **When user says "as a rule"**: Document that rule in this section of CLAUDE.md
3. **When user asks about a task**: Check next-actions.md first, then project roadmaps (projects/*/roadmap.md) and area tasks (areas/*/tasks.md)
4. **When adding tasks**: Determine if it's a next action (goes to next-actions.md), project task (projects/*/roadmap.md), or area task (areas/*/tasks.md)
5. **When potential project emerges with go/no-go blocker**: Create project folder (projects/[name]/), put blocker as waiting-for item in roadmap.md, put all context in notes.md, add to next-actions.md Waiting For section with "since" date and link to project. If go → activate tasks; if no-go → archive to archives/projects/[name]-cancelled/
6. **People context**: Add to resources/sola-work/people/sola-people.md under person's "Topics to Discuss" section. Only create separate person files if context is extensive (multi-page). Default = single people file for single source of truth.
7. **Resources vs. Zettelkasten**: Work-in-progress thinking and context-dependent material goes to resources/. Processed, universal, evergreen insights go to zettelkasten/permanent/ as atomic notes. When insight emerges from resource that transcends current context, add to next-actions.md for timeboxed "process to zettelkasten" work.
8. **When syncs are already scheduled**: Don't create redundant next actions for topics already captured in person's context. The sync agenda lives in their "Topics to Discuss" - that's sufficient.
9. **Website creation**: All website files (source and published HTML) go in resources/websites/. Keep source as `[name]-source.md` and published as `[name].html`. Push to `pages` remote (git@github.com:tzvikabesor/pages.git) for deployment to https://tzvikabesor.github.io/pages/resources/websites/

## Communication Principles: Data Reliability and Uncertainty

**CRITICAL: Always distinguish between what you know vs. what you don't know**

### When Providing Information:

1. **Only state facts you can verify from reliable sources**
   - If you pulled information from web search, documentation, or files you read - that's reliable
   - If you're making reasonable assumptions or generalizations - explicitly say so
   - If you don't have access to real-time/dynamic data - be very clear about that limitation

2. **Be explicit about uncertainty and limitations**
   - Example: "I don't have access to real-time train schedules. The 40-45 minute estimate is based on general information about the route, but YOU MUST verify actual times and connections before going."
   - Example: "Based on typical patterns this could be X, but this needs verification because [reason]"
   - Don't present educated guesses as facts

3. **Emphasize validation requirements - LOUDLY**
   - When critical details depend on external factors (schedules, availability, pricing, etc.), be emphatic about validation
   - Use strong language: "⚠️ CRITICAL: You MUST verify this before proceeding"
   - Repeat warnings multiple times if the stakes are high
   - Don't just mention it once politely - be insistent when something could cause significant inconvenience

4. **Flag gaps in knowledge proactively**
   - At the start: "I should mention upfront - I cannot access [X], so you'll need to verify [Y]"
   - During planning: "This assumes [X], but I don't have reliable data on that"
   - In summaries: Include a "What I couldn't verify" section

### Real Example from Castel Gandolfo Trip:

**What went wrong**: Stated "38-60 minutes (average 40-45 min)" and "~17 trains per day" as if verified, when actually:
- No access to real-time schedules
- Information was from general research, not actual October 13, 2025 data
- Actual reality: 1.5 hours with train changes

**What should have been said**:
```
⚠️ CRITICAL LIMITATION: I do NOT have access to real-time train schedules.

The 40-45 minute estimate is from general route information, but:
- Actual trains on October 13, 2025 may be much less frequent
- May require connections (adding significant time)
- Schedule could be reduced/irregular on that specific date

YOU MUST check trenitalia.com BEFORE making any plans. Do not rely on my time estimates.

I'm serious - please verify this TODAY before committing to the trip.
```

### Why This Matters:

- User's time and plans have real consequences
- Better to under-promise and over-deliver than create false expectations
- Trust is built on reliability - admitting limitations strengthens rather than weakens credibility
- User can make better decisions when they know what's verified vs. what needs checking

## System Identity

This work system has multiple interconnected identities:

- **ABOUT.md**: The story thus far - where you've been, current needs and wants
- **Tasks & Projects (ROADMAP.md, PROJECTS.md)**: What you're actively working on now
- **Ideas & Vision (ideas/, VISION.md)**: Where you might be going - north star directions

Together, these create a complete picture: past context informing present work while orienting toward possible futures.

## Purpose

This system is both a knowledge base and a workspace - everything needed to manage, track, and execute work lives in this repository.