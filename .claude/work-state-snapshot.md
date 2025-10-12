# Work State Snapshot - Tzvika at Sola

**Generated**: 2025-10-12
**Purpose**: Claude's understanding of your current work situation. Edit this to correct gaps, then share back for updates.
remarks by Tzvika have this format - tzr: [remark]
---

## Where You're At (Current State)

**Role & Context:**
- Product Manager leading **growth and AI experiences** at Sola (cybersecurity platform) tzr: [Senior product manager]
- Started in 2024, building trust and reputation
- Established as "whatever Tzvika does, he does well"
- Working on major initiatives: Canvas 2.0, AI app builder, Copilot improvements, onboarding optimization - tzr: [AI app builder is actually a project I'm trying to kill, as I want the Customer Success agent - AKA CS agent, to handle all building within the app. there is a story about that]
tzr: [since a year has passed, I am thinking about the next preformance/compansation/status review. this is another topic we should put as something I need to figure out - what do I want, what do I ask for, how do I get what I want]

**Your Work Pattern Shift:**
- **Before**: Brilliant ideas → poor execution → frustration → conflict
- **Now**: Consistent delivery → earned trust → space for strategic thinking
tzr: [and what's next - improving communication with steakholders, to harness them to my vision in "live stream", gain more trust, be able to affect more]
- Critical insight: "Vision and execution are interdependent — two horses pulling the same carriage"

**Your Jira Reality** (194 tickets):
- 123 Done (63.4%) - **Strong delivery track record**
- 42 Active tickets (To Do + In Progress + To Discuss + Validation)
- Focus areas: Canvas 2.0, AI features, Copilot, onboarding, data integrations
- Projects: RND (157), CTO (19), DESIGN (14)

---

## What's Urgent (Next 48 Hours)

### 1. **TODAY - Sprint Planning (Tonight, 17:00)** ⚠️ URGENT
**This is your highest priority right now.**

**The Setup:**
- Bi-weekly agile cycle: Backlog Refinement (Wednesday) → Sprint Planning (Sunday, tonight)
- You're negotiating with Dor (VP R&D) and Leon (CTO) for sprint commitment
- They challenge priorities with technical reality ("harsh water" dynamic)

**What you need to do before 17:00:**
```bash
# Run these NOW to prep
python3 scripts/analyze_jira.py --active
python3 scripts/analyze_jira.py --recent
python3 scripts/analyze_jira.py --summary
```

**Your prep (2-3 hours before meeting):**
1. Check Jira reality (15 min) - see what you've delivered, what's in flight
2. Review Wednesday's Backlog Refinement output (30 min)
3. Anticipate R&D challenges (45 min) - for each story, what will Dor/Leon push back on?
4. Know your walk-away points (15 min) - what's must-have vs. nice-to-have?

**Your strategy:**
- **"Harsh water"** - Push hard initially, listen to technical reality, find alternative paths
- Lead with concrete delivery (your Jira shows 123 Done - this is your credibility)
- Defend business value, but be flexible on scope/timing
- Focus on systemic progression, not tactical perfection

**Playbook**: `.claude/playbooks/meetings/sprint-planning.md`

### 2. **This Week - Follow Through on Sprint Commitments**
Whatever gets locked in tonight needs to get done. This is where you build trust.

---

## What's Important (Strategic Layer)

### The Shlomi Challenge (Your Manager)
**Current state**: Bi-weekly 1:1s are very tactical from his side

**The problem**: You have product vision for growth and AI experiences but haven't figured out how to present it, get his feedback, and iterate together.

**Why this matters**:
- Success at Sola depends on two questions:
  1. Can you trust Tzvika to get things done? (Tactical delivery)
  2. Does Tzvika know what he's talking about beyond his scope? (Strategic thinking)
- You're building #1 (delivery track record is strong)
- You need to build #2 (strategic voice) but haven't found the right approach yet

**Your open issues with Shlomi** (from `.claude/people/sola-people.md`):
- [ ] **STRATEGIC**: Present growth and AI experiences product vision - get feedback, iterate together
- [ ] **TACTICAL**: Q4 priorities for growth and AI - clarify trade-offs
- [ ] **CAREER**: Senior IC path progression - when to formalize conversation?
- [ ] **PROJECT**: Canvas2 resource allocation and timeline
- [ ] **PROCESS**: How to balance tactical execution with strategic vision in our 1:1s?

**The strategy** (from shlomi-1on1.md playbook):
- **Phase 1 (Weeks 1-4)**: Establish tactical excellence - PROVE delivery before adding strategic layer
- **Phase 2 (Weeks 5-8)**: Introduce vision iteratively - start with ONE aspect, frame as "thinking I'm developing"
- **Phase 3 (Weeks 9+)**: Co-create strategic direction - vision becomes shared

**Don't skip from Phase 1 to Phase 3.** You're still building Phase 1 foundation.

### Your Growth Edges
**What you're working on:**
1. **Over-communicate upward** (doesn't come naturally) - especially with Shlomi
2. **"People feel stupid" early warning** - You running ahead without sharing context
3. **Advocating for needs** - Tend to let things go too easily, silence has cumulative cost
4. **Authority dynamics** - Still activates old patterns with Dor/Leon/Shlomi

**What's working:**
- Physical wellbeing (yoga 2x/week) - non-negotiable, directly impacts everything - tzr:[this has been compromized lately. need to get back on track. as hole, we need to discuss habits]
- ADHD management (Concerta 36mg daily) - critical for executive function - tzr: [54mg]
- Family first - secure base of love with Moran and kids

---

## Where You're Going

### Immediate (Next 2-4 Weeks)
- **Execute the sprint** that gets locked tonight
- **Next Backlog Refinement** (in ~5 days) - Wednesday prep cycle starts again
- **Next Shlomi 1:1** (bi-weekly) - check `.claude/people/sola-people.md` for his open issues before meeting
- Continue building tactical excellence track record

### Near-Term (Next 2-3 Months)
- **Build Phase 1 foundation with Shlomi** - consistent delivery, over-communicate progress
- **Canvas 2.0 completion** - major initiative in your Jira
- **AI app builder maturity** - core to your growth/AI experiences mandate
- **Clarify Q4 priorities** - need alignment with Shlomi on trade-offs

### Medium-Term (Next 6-12 Months)
- **Senior IC career path** - Building toward principal/staff PM whose opinion carries strategic weight through trust and clarity, not title
- **AI product expertise** - Becoming known for **"keeping AI human"** — blending intellectual rigor (what AI does) with emotional rigor (how humans experience it)
- **Strategic voice** - Moving from Phase 1 (tactical delivery) → Phase 2 (introducing vision) → Phase 3 (co-creating strategy with Shlomi) - tzr: [with shlomi and leadership - guy, ron, leon]

---

## Key Relationships & Dynamics

**Your Manager - Shlomi (VP Product)**
- Values delivery + communication over brilliant ideas
- Currently very tactical in 1:1s
- If he's skeptical in Backlog Refinement → will be worse in Sprint Planning
- Need his buy-in before presenting to Dor/Leon

**The "Harsh Water" - Dor (VP R&D) & Leon (CTO)**
- Challenge product priorities at Sprint Planning (tonight!) - tzr: [I'm vacating right now, until the 19th, so I won't attend any meetings and need not deliver anything until that day]
- Technical reality check on your ambitions
- Must respect their concerns while advocating for product
- They respect delivery track record - use your 123 Done tickets

**Design Partners - Lior (UX) & Ami (Head of Design)**
- Must align with Lior BEFORE Backlog Refinement
- Design readiness gates story progression
- Ami provides design review/approval - tzr: [Amy is still finding his way as a manager. Currently there is no approval flow, only inconsistant review]

**Product Peer - Nadav (Senior PM)**
- Also presents at Backlog Refinement
- May have competing priorities for sprint capacity
tzr: [A very imprtant track is the track with Adi Atzmoni, the pricipal technical writer. she writes the documentation, but lately we have beed working together to branch her work also to conversation design for the AI. she's becoming the CS agent's prompt engineer, to give it a voice and structure]

---

## What to Focus On Right Now

### Today's Priority Order:
1. ⚠️ **Prep for Sprint Planning (17:00)** - 2-3 hours before meeting
2. Execute the playbook in `.claude/playbooks/meetings/sprint-planning.md`
3. Use Jira data to show credibility (123 tickets done)
4. Know your must-haves vs. nice-to-haves

### This Week:
1. Execute sprint commitments - tzr: [what are the sprint commitments? when will I review them?]
2. Update `.claude/people/sola-people.md` after any 1:1s or key meetings
3. Start tracking what's working in the new system

### Don't Lose Sight Of:
- **The long game**: Building both tactical delivery AND strategic voice
- **Your health**: Sleep, yoga 2x/week, Concerta - these are medicine, not optional - tzr: [I would add here hydration and Body By Science training. Again, we need to work on habits. what's the best way to drink more? as for the BBS, perhaps having an md that talks about the priciples of the system will help you track my progress. I've stopped working out at the gym about 6 weeks ago, agter about 10 weeks of working out. I need to find my way back]
- **Family first**: Work is "day job" - meaningful but not primary identity
- **The shift**: "Delivery + communication will create space for strategic thinking" - trust this
tzr: [we've also dicussed time-blocking my way into having a work-free day (8-10 hours) in the calendar, so I can eventually offer Sola a 4-days-workweek sort of deal. It's a long game, but we need to be on top of it when we plan work time]

---

## Bottom Line

You're in a good place. Strong delivery track record (123 done tickets), building trust, established reputation. The urgent thing is tonight's Sprint Planning where you defend your priorities with Dor/Leon. The important thing is continuing to build tactical excellence while figuring out how to add the strategic layer with Shlomi. Don't skip steps - earn Phase 2 by nailing Phase 1.

---

## Instructions for Editing

**Edit this file to:**
- Correct any misunderstandings
- Fill in gaps in Claude's knowledge
- Add context that's missing
- Update priorities or urgency levels
- Clarify relationships or dynamics

**Then share it back so I can:**
- Update relevant files (ABOUT.md, sola-people.md, playbooks, etc.)
- Adjust my understanding for better support
- Keep the work system accurate and useful

**Last Updated**: 2025-10-12
