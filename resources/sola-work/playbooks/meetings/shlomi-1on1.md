# Shlomi 1:1 - Preparation Playbook

**Meeting Type**: Manager 1:1
**Frequency**: Bi-weekly
**Duration**: [TBD]
**Your Manager**: Shlomi Lavi (VP Product)

---

## The Core Challenge

**Current State**: Meeting is very tactical (especially from Shlomi's side). You sometimes bring broader topics, sometimes don't have anything.

**The Problem**: You have product vision for Sola but haven't figured out how to present it, get his feedback, and iterate it together. This makes tactical execution harder because vision isn't clear/shared.

**The Opportunity**: Move from purely tactical 1:1s to strategic alignment that makes tactical pieces flow better.

**Key Insight**: "Vision and execution are interdependent — two horses pulling the same carriage."
- Vision without delivery = speculation
- Delivery without vision = grind
- You need BOTH, aligned with Shlomi

---

## Two-Track Approach

### Track 1: Tactical Execution (Immediate)
Handle the tactical items that come up week-to-week

### Track 2: Strategic Alignment (Build Over Time)
Gradually introduce and iterate on product vision for growth and AI experiences

**Don't try to do everything at once.** Start with Track 1 while preparing Track 2.

---

## Pre-Meeting Preparation

### Step 0: Check Your Jira Progress (10 min)
**Show concrete delivery, not just talk**

```bash
# What have you delivered since last 1:1?
python3 scripts/analyze_jira.py --recent

# What's currently active?
python3 scripts/analyze_jira.py --active

# Any blockers in "To Discuss"?
python3 scripts/analyze_jira.py | grep "To Discuss"
```

**Why this matters**:
- Shlomi values "delivery + communication" over brilliant ideas
- Concrete progress builds trust for strategic conversations
- Identifies blockers you need his help with
- Shows patterns in your work (Canvas 2.0 focus, AI work, etc.)

**Questions to prepare**:
- [ ] What did I complete since last 1:1?
- [ ] What's in flight that he should know about?
- [ ] Any tickets stuck in "To Discuss" needing his input?
- [ ] Do my Jira patterns align with strategic priorities?

---

### Step 1: Review Open Issues (15 min)

Check `.claude/people/sola-people.md` → Shlomi's section:
- [ ] What's on his open issues list for you?
- [ ] What's on your open issues list for him?
- [ ] What got resolved since last time?
- [ ] What new issues emerged?

### Step 2: Tactical Prep (15 min)

**Your Side:**
- [ ] Blockers you need his help with
- [ ] Decisions that need his input/approval
- [ ] Updates he should know about
- [ ] Questions about priorities or direction

**His Side (anticipate):**
- [ ] What tactical issues is he likely to raise?
- [ ] Are there fires he's aware of that you should address?
- [ ] Any sprint/delivery concerns from his view?

### Step 3: Strategic Prep (20 min - when ready)

**Only when you're ready to start Track 2:**
- [ ] Draft 1-page vision doc for growth and AI experiences
- [ ] Identify ONE strategic topic to discuss (don't overload)
- [ ] Frame it as "I'd like your feedback on..." not "Here's the plan"
- [ ] Prepare to listen and iterate, not pitch and defend

---

## Meeting Structure (Flexible)

### Opening (2 min)
Quick check-in: How are things? Any context shifts since last time?

### His Agenda First (10-15 min)
Let Shlomi raise his tactical issues first:
- Listen actively
- Take notes
- Clarify what he needs from you
- Commit to actions

**Why first?**
- Respects his priorities as your manager
- Clears his mental space to engage with your topics
- Models the communication you want him to see from you

### Your Tactical Items (10-15 min)
Go through your list:
- Blockers needing his help
- Decisions needing his input
- Updates he should know
- Priority questions

**Communication Style:**
- Be concise (respect his time)
- Lead with the question/need, then context
- Don't make him work to understand what you need
- "I need X because Y. What do you think?"

### Strategic Topic (5-10 min - occasional, not every meeting)
**Only introduce when:**
- Tactical items are under control
- You have something concrete to show
- You're ready to iterate, not just present
- Timing feels right

**How to Introduce:**
- "I've been thinking about [growth and AI experiences strategy]. I'd love 10 minutes to get your feedback on some ideas I'm developing."
- **Frame as work-in-progress**, not finished vision
- Show, don't just tell (doc, diagram, examples)
- Ask specific questions: "Does this align with where you see us going?" "What am I missing?" "What would you change?"

### Closing (2 min)
- Recap actions (yours and his)
- Schedule next meeting if needed
- Thank him for his time/input

---

## After Meeting

### Immediate (Within 1 hour):
- [ ] Update `.claude/people/sola-people.md` → Shlomi's section
  - Check off resolved open issues
  - Add new open issues from discussion
  - Update "Last Synced" date
- [ ] Document action items in your task system
- [ ] Note any shifts in his thinking or priorities

### Reflection (5 min):
- How did tactical items go? Clear and efficient?
- If you raised strategic topic: How did he respond?
- What did you learn about his priorities/thinking?
- What patterns are emerging in these 1:1s?

---

## Building Strategic Alignment Over Time

### Phase 1: Establish Tactical Excellence (Weeks 1-4)
**Goal**: Prove you're on top of execution before adding strategic layer

**Actions:**
- Come prepared with clear tactical items
- Follow through on all commitments
- Over-communicate progress
- Build his trust in your delivery

**Success Signal**: He stops bringing tactical fire drills because you're ahead of them

---

### Phase 2: Introduce Vision Iteratively (Weeks 5-8)
**Goal**: Start sharing product vision, get feedback, iterate together

**Approach:**
- Start with ONE aspect of vision, not everything
- Frame as "thinking I'm developing" not "plan I'm presenting"
- Make it concrete (doc, diagram, user stories)
- Ask for his feedback explicitly
- Listen more than you talk

**Example Topics to Start With:**
- "Here's how I see growth and AI experiences evolving next 6 months - does this align with your thinking?"
- "I've been mapping user needs for AI experiences - want to share what I'm seeing"
- "Thinking about how we can drive growth through AI capabilities - would love your input"

**Success Signal**: He engages with the vision, adds his perspective, you iterate together

---

### Phase 3: Co-Create Strategic Direction (Weeks 9+)
**Goal**: Vision becomes shared, not just yours

**What This Looks Like:**
- You bring strategic thinking, he adds his perspective
- Decisions flow easier because vision is clear
- Tactical items make more sense in context of strategy
- He references the shared vision in other contexts
- You're aligned on where growth and AI experiences are going

**Success Signal**: He says "As we discussed in our vision..." or "This aligns with where we're heading..."

---

## Communication Patterns to Develop

### What Shlomi Values (Based on Your ABOUT.md):
✅ Delivery + communication over just brilliant ideas
✅ Consistent execution that builds trust
✅ Being ahead of problems, not reactive
✅ Clear communication (especially upward)

### What Doesn't Work:
❌ Running ahead without sharing context ("people feel stupid" signal)
❌ Brilliant ideas without execution track record
❌ Assuming he knows what you're thinking
❌ Waiting until problems are crises

### Your Growth Edge Here:
- Over-communicate upward (doesn't come naturally)
- Lead with delivery, THEN strategic vision
- Trust that "delivery + communication will create space for strategic thinking"
- Balance between not saying enough and overwhelming with information

---

## Red Flags / Warning Signs

**In the meeting:**
- 🚩 You have nothing to say (means you're not tracking open issues)
- 🚩 He's surprised by something (means you didn't communicate enough)
- 🚩 Tactical items are always fires (means you're reactive, not proactive)
- 🚩 You're frustrated he's "too tactical" (but you haven't earned space for strategic yet)
- 🚩 You present vision but he doesn't engage (timing wrong, or approach wrong)

**Between meetings:**
- 🚩 You're avoiding preparing (something's not working)
- 🚩 His open issues list keeps growing (you're not resolving things)
- 🚩 You're dreading the meeting (relationship needs attention)
- 🚩 You're running ahead without him (pattern from your past)

---

## The Long Game

**Your Success at Sola Depends On Two Questions:**
1. Can you trust Tzvika to get things done once he takes responsibility?
2. Does Tzvika know what he's talking about — even beyond his direct product scope?

**This 1:1 is where you build BOTH:**
- Question 1 → Tactical excellence, consistent delivery, follow-through
- Question 2 → Strategic thinking, product vision, informed perspective

**Start with #1, build to #2. Don't skip steps.**

---

## Special Topics / Situational Prep

### When You Need to Advocate for Something:
- Prepare business case (not just opinion)
- Anticipate his questions/concerns
- Have data or examples
- Be ready for "harsh water" - push hard but adapt if needed
- Know what's negotiable vs. non-negotiable

### When You Need Career Conversation:
- Choose a 1:1 where tactical items are light
- Frame as "I'd like to discuss my development"
- Be specific about what you want (senior IC path, principal PM, etc.)
- Ask what he needs to see from you
- Document his feedback clearly

### When There's Conflict or Tension:
- Address it directly but calmly
- "I noticed [pattern], want to make sure we're aligned"
- Listen to his perspective first
- Find the misalignment (usually communication gap)
- Agree on how to improve going forward

---

## Open Questions to Explore

1. How often should strategic topics come up vs. staying tactical?
2. What format does Shlomi prefer for vision discussions? (Doc? Conversation? Diagram?)
3. When is the right time to shift from tactical-only to strategic-tactical balance?
4. How does he want to be involved in vision development? (Review? Co-create? Just informed?)
5. What are HIS strategic priorities that your vision should align with?

---

## Notes & Patterns

**Shlomi's Response Patterns:**
[To be documented as you learn]

**What Topics Engage Him:**
[To be documented]

**What Topics He Dismisses:**
[To be documented]

**Best Timing for Strategic Discussions:**
[To be documented]

---

---

## Jira Integration Quick Reference

**Before every 1:1**:
- `python3 scripts/analyze_jira.py --recent` - Show delivery since last meeting
- `python3 scripts/analyze_jira.py --active` - Current work status
- Check for "To Discuss" tickets needing his input

**During 1:1**:
- Lead with concrete progress (Jira data helps)
- Reference specific tickets when discussing work
- Note any new tickets to create based on discussion

**After 1:1**:
- Update Jira based on decisions/priorities discussed
- Update `.claude/people/sola-people.md` → Shlomi's open issues
- Create any tickets for follow-up actions

**For full integration guide**: See `.claude/sola-reference-index.md`

---

**Last Updated**: 2025-10-12
**Next 1:1**: [Check calendar]
**Current Phase**: Phase 1 - Establishing Tactical Excellence
