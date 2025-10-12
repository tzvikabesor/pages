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

## System Identity

This work system has multiple interconnected identities:

- **ABOUT.md**: The story thus far - where you've been, current needs and wants
- **Tasks & Projects (ROADMAP.md, PROJECTS.md)**: What you're actively working on now
- **Ideas & Vision (ideas/, VISION.md)**: Where you might be going - north star directions

Together, these create a complete picture: past context informing present work while orienting toward possible futures.

## Purpose

This system is both a knowledge base and a workspace - everything needed to manage, track, and execute work lives in this repository.