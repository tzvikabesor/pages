# My New Work System: A Brief for Sally

## What I Built

Over the past few months, I've built a comprehensive personal work management system that lives entirely in code—working with Claude in a development environment. It's not just a to-do list; it's an integrated system for managing tasks, projects, knowledge, and life itself.

## Why This Matters

You know better than anyone: I've spent decades watching brilliant ideas dissolve because I couldn't execute consistently. Lost jobs despite being smart. Hurt relationships by not communicating needs until I exploded.

This system is my scaffold—external structure compensating for executive function challenges. But it's also a practice ground for:
- Showing up consistently (which builds trust)
- Communicating clearly (which builds relationships)
- Tracking progress (which builds confidence)
- Celebrating small wins (which sustains motivation)

## The AI-Powered Approach

The system lives in a Git repository managed through Claude Code (Anthropic's coding CLI). This means:
- **Version control**: Every change tracked, can review history, roll back if needed
- **AI assistance**: Claude helps me process inbox items, plan projects, maintain structure
- **Automation**: Scripts analyze my calendar, generate interfaces, sync data
- **Iterative evolution**: The system grows with me, adapting as I learn what works

Working in a coding environment might sound technical, but it gives me power: everything is plain text files that I can search, edit, link, and transform. No proprietary app lock-in. Complete control.

## The Structure: Simple Interfaces, Complex Support

### Three Pillars of Daily Work

The system centers on three simple touchpoints:

1. **inbox.md** - Single capture point for everything (tasks, ideas, resources, insights)
2. **next-actions.md** - Context-based actions (@home, @calls, @computer, @anywhere)
3. **Calendar** - Time-blocked commitments

That's it for daily use. Everything else supports these three.

### The Full Architecture

Behind the scenes, the system integrates multiple methodologies:

**GTD (Getting Things Done)**: Capture → Clarify → Organize → Reflect → Engage
- Clear my head by capturing everything
- Process inbox daily: "What is this? Task? Resource? Insight?"
- Regular reviews (daily, weekly, monthly, quarterly)

**PARA (Projects, Areas, Resources, Archives)**:
- **Projects**: Time-bound outcomes (Work System, Home Renovation, Hungary Trip)
- **Areas**: Ongoing responsibilities (Health, Work, Family, Home, Financial)
- **Resources**: Central vault for reference materials (research, docs, context)
- **Archives**: Completed/inactive items

**Zettelkasten**: Permanent notes for processed knowledge
- Atomic ideas with links between them
- Transform captured insights into lasting knowledge

**PPV (Pillars, Pipelines, Vaults)**: Strategic alignment
- Life pillars in VISION.md guide everything
- Projects are pipelines toward goals
- Resources are vaults of accumulated wisdom

### Key Features

**Projects** (`projects/*/`):
- Each has: roadmap.md (tasks), notes.md (context), resources.md (pointers)
- Example: Hungary Trip 2025 waiting for Moran's confirmation (tracked with "since" date)

**Areas** (`areas/*/`):
- Each has: tasks.md (one-time actions), practices.md (habits), resources.md
- Examples: Health (yoga 2x/week), Work (Sola PM role), Family, Home, Financial

**Resources** (`resources/`):
- Central vault (max 2 levels deep)
- Everything points here via resources.md files
- Includes: productivity research, work docs, scripts, historical conversations

**ABOUT.md**:
- This is where our 130+ conversations live as context
- Your questions helped me articulate who I am, what I value, what I need
- It informs every decision in the system: "Does this align with my values? Is this sustainable?"
- The document opens with the ADHD diagnosis story you helped me understand
- It includes the transformation work we've done: learning to deliver consistently, building secure attachment, finding my voice

## What Makes It Work

### 1. Built from Deep Self-Knowledge

The system is grounded in ABOUT.md—my story, values, needs, challenges. Everything we've worked on:
- ADHD diagnosis and what it means for how I work
- Learning to deliver before leading with brilliant ideas
- Building systems that compensate for executive function
- Understanding my patterns (Enneagram 9, INFP, trauma responses)
- Defining success: coming home energized, being present with kids, sustainable work

Your coaching conversations are literally embedded in the foundation. The questions you asked, the insights we discovered together—they shaped how this system thinks about me.

### 2. Simplicity at the Interface, Sophistication Behind

Daily use is dead simple:
- Check inbox → process items
- Open next-actions → pick by context and energy
- Check calendar → honor commitments

But the system handles complexity:
- Projects with blockers tracked in multiple places
- Resources organized but accessible
- Knowledge building over time in zettelkasten
- Review cycles ensuring nothing falls through cracks

### 3. AI as Co-Pilot, Not Autopilot

Claude doesn't run my life; it helps me run my life:
- "Process this inbox item" → suggests which category, creates files, updates pointers
- "I want to plan a Hungary trip but waiting on Moran" → creates project structure, tracks blocker
- "Review my week" → pulls together all relevant files, helps me reflect
- "What's the pattern here?" → documents learnings in CLAUDE.md for future use

The AI knows my context (ABOUT.md), my system (CLAUDE.md), and my current work (next-actions.md, projects). It's like having an assistant who actually understands me.

### 4. Progressive Disclosure

The system scales to complexity without requiring it:
- Day 1: Just use inbox and next-actions
- Week 1: Add projects with roadmaps
- Month 1: Build out area practices
- Quarter 1: Develop zettelkasten knowledge base
- Year 1: Full review cycles and strategic planning

Right now, I'm at "Month 1" level—and it already works.

## Current Status

**Migration Complete**:
- Moved from old structure to unified system
- All work context migrated to central resources
- First real project (Hungary Trip) processed successfully
- System documented in CLAUDE.md for future reference

**Active Projects**:
1. Work System (this!) - continuing to refine
2. Home Renovation - blocked, but tracked
3. Billion Person Focus Group - POC research at Sola
4. Hungary Trip 2025 - waiting for go/no-go

**Daily Practice**:
- Processing inbox (getting there)
- Updating next-actions (working on consistency)
- Time-blocking calendar (still building habit)

## What I'm Learning

**It's not about perfection**:
The system accommodates messiness. Inbox doesn't have to be empty every day. Projects can be blocked. That's fine—it's all visible and tracked.

**"Come back to the horse"**:
When I fall off (and I will), the system makes it easy to get back on. No shame, just return.

**Small wins compound**:
Every processed inbox item builds confidence. Every completed task builds trust (with myself and others).

**The system serves me, not vice versa**:
When something doesn't work, I change it. The system evolves with my needs.

## Why I'm Sharing This With You

Sally, this system is a direct result of our work together. You helped me:
- Understand my ADHD and what accommodations I need
- Learn to deliver consistently before leading with vision
- Build secure attachment through expressing needs
- Define success on my own terms
- Trust that I'm valuable beyond being brilliant

Every principle in ABOUT.md—every value, every insight, every "thing to keep in mind"—emerged from our conversations. The 130+ conversation transcripts sit in `resources/conversations/`, forming the foundation of how the system thinks about who I am and what I need.

This isn't just a productivity system. It's an externalization of everything I've learned about how to work *with* my brain instead of against it. It's a practice ground for showing up consistently, communicating clearly, and building the life I actually want.

And it's working.

---

## Technical Details (If You're Curious)

- **Platform**: Git repository with Markdown files
- **AI**: Claude Code (Anthropic's coding CLI)
- **Version control**: Full history of every change
- **Automation**: Python scripts for calendar analysis, data parsing
- **Structure**: Plain text files organized by methodology
- **Access**: Can work from terminal, VS Code, or any text editor
- **Backup**: Git remote (GitHub) + local backups

The beauty of plain text: it will work forever, on any system, with or without AI assistance. No app can disappear and take my life with it.

---

*This system is both a knowledge base and a workspace—everything needed to manage, track, and execute work lives in this repository. It's alive, evolving, and deeply personal.*

*Thank you for helping me build the foundation that made this possible.*
