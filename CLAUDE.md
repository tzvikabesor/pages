# Claude Instructions

**ALWAYS check ROADMAP.md first** before starting any task or answering questions about work status.

## Work System Overview

This is a personal work management system designed for:
- **Task tracking**: High-level goals and current work status
- **Knowledge capture**: Learnings, insights, and reference material
- **Interface generation**: Creating tools and workflows based on captured knowledge

## File Structure

### Core Files
- `ABOUT.md`: Your background, story, current needs and wants - context for all work
- `ROADMAP.md`: Current priorities, in-progress tasks, and recent completions (CHECK THIS FIRST)
- `PROJECTS.md`: List of all projects (active, on hold, completed)
- `VISION.md`: Future directions and north star - synthesizes ideas into coherent possible futures
- `CLAUDE.md`: This file - instructions for how to use the system

### Documentation
- `.claude/context.md`: Project context and background information
- `.claude/knowledge.md`: Accumulated learnings and insights
- `.claude/commands/`: Custom commands for workflow automation

### Working Directories
- `projects/`: Large, ongoing efforts with their own structure and tracking
- `tasks/`: Detailed task breakdowns for complex work items (can be standalone or part of a project)
- `ideas/`: Project ideas not yet ready for the roadmap - each gets its own file to develop
- `scripts/`: Utility scripts and automation tools
- `interfaces/`: Dashboards, tools, and generated interfaces built from knowledge

## Work Organization

### The Spectrum: Ideas → Projects → Tasks

- **Ideas**: Project concepts not yet ready for active work
  - Each idea gets its own file in `ideas/` to develop
  - Ideas are synthesized into coherent themes in `VISION.md`
  - Represents possible futures and north star directions
- **Projects**: Large, ongoing, open-ended efforts with evolving scope
  - Each project gets its own folder in `projects/`
  - Projects can have their own roadmaps, documentation, and task lists
  - Ideas "graduate" to projects when ready for active work
- **Tasks**: Specific work items with clear endpoints
  - Can be standalone or belong to a project
  - Complex tasks get detailed breakdowns in `tasks/`
  - Simple tasks just live in ROADMAP.md
- **ROADMAP.md**: High-level view showing current priorities across all projects and standalone tasks

## Workflow

1. **Always** check ROADMAP.md to understand current priorities
2. Reference knowledge.md for relevant past learnings
3. For new projects: Create folder in `projects/` with its own structure
4. For complex tasks: Create detailed breakdown in `tasks/`
5. Update ROADMAP.md as work progresses (use [ ], [-], [x] convention)
6. Capture new learnings in knowledge.md using `/work:capture`
7. Create tools and scripts as needed in `scripts/` and `interfaces/`

## Rules

1. **When user says they'll do something**: Add it as a task to ROADMAP.md even if not explicitly asked
2. **When user says "as a rule"**: Document that rule in this section of CLAUDE.md
3. **When user asks about a task**: Check both the main ROADMAP.md AND all active project roadmaps in `projects/*/roadmap.md` - tasks may be tracked at either level
4. **When adding tasks that belong to in-progress projects**: Add cross-references in the main ROADMAP.md pointing to the project's detailed roadmap (e.g., "[-] Project Name → See `projects/project-name/roadmap.md` for detailed tasks")

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