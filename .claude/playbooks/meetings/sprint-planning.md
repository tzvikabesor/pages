# Sprint Planning - Preparation Playbook

**Meeting Type**: R&D Commitment & Sprint Kickoff
**Frequency**: Bi-weekly, Sundays 17:00
**Duration**: [TBD]
**Follows**: Backlog Refinement (5 days prior)
**Outcome**: Locked sprint backlog, sprint starts Monday

---

## Pre-Meeting Preparation (2-3 hours, day before or morning of)

### Step 0: Check Your Jira Reality (15 min)
**Quick reality check on your work**

```bash
# What's in flight?
python3 scripts/analyze_jira.py --active

# What have you delivered recently?
python3 scripts/analyze_jira.py --recent
```

**Why this matters**:
- Shows R&D what you've been delivering (builds credibility)
- Identifies any tickets that should be done but aren't (potential blockers)
- Grounds negotiation in actual work patterns, not abstract promises

---

### Step 1: Review Refinement Output (30 min)
- [ ] Re-read finalized candidate list from Wednesday
- [ ] Refresh on business rationale for each story
- [ ] Note any changes since refinement
- [ ] Check if any new information affects priorities

### Step 2: Anticipate R&D/CTO Challenges (45 min)

**For each story, ask:**
- What technical concerns might Dor/Leon raise?
- What dependencies could be problematic?
- Where might they push back on scope?
- What's negotiable vs. non-negotiable?

**Prepare responses:**
- Business value justification
- User impact data/stories
- Strategic importance
- Alternative approaches if they reject scope

### Step 3: Know Your Walk-Away Points (15 min)
- [ ] Which stories are **must-haves** this sprint?
- [ ] Which are **nice-to-haves** (can defer)?
- [ ] Where can you compromise on scope but keep value?
- [ ] What would make this sprint a failure?

### Step 4: Sync with Shlomi (Optional, 15 min)
If there's been any shift since refinement:
- [ ] Brief Shlomi on your thinking
- [ ] Align on negotiation strategy
- [ ] Clarify his priorities vs. yours
- [ ] Ensure you're representing product perspective well

---

## Meeting Materials Checklist

Have ready:
- [ ] Prioritized candidate list (from refinement)
- [ ] Story details (Jira links, acceptance criteria)
- [ ] Business value justifications
- [ ] Design assets/mockups
- [ ] Dependency maps
- [ ] Alternative scopes (if needed)

---

## During Meeting

### Your Mindset: "Harsh Water"
- Push hard for what matters
- Listen to technical reality
- Find alternative paths when blocked
- Systemic progression > tactical perfection

### Meeting Flow

#### Opening (5-10 min)
**Product presents context:**
- Sprint goals (aligned with quarterly OKRs)
- Business drivers for priorities
- Any urgency factors

#### Story Review (Main portion)
**For each candidate story:**

**You present:**
- What it is, why it matters now
- Expected business/user impact
- Design/scope overview

**R&D/CTO challenges:**
- Technical feasibility concerns
- Dependency issues
- Scope questions
- Timeline challenges

**Negotiation:**
- Defend where critical
- Adapt where possible
- Find compromise that preserves value
- Document what's changing and why

#### Commitment
- R&D commits to sprint backlog
- Priorities locked
- Sprint starts Monday

---

## Negotiation Strategies

### When Dor/Leon Push Back:

**Strategy 1: Clarify the WHY**
- Don't just defend the WHAT
- Explain business impact, user pain, strategic value
- Sometimes they didn't understand importance

**Strategy 2: Explore Alternatives**
- "If full scope is too much, what IS doable?"
- "Can we split this into must-have + nice-to-have?"
- "What would make this more feasible?"

**Strategy 3: Trade, Don't Fight**
- "If we deprioritize X, can we do Y?"
- "What if we defer this to next sprint?"
- Show flexibility on timing, not on overall goals

**Strategy 4: Escalate to Principles**
- When stuck, go to higher-level goals
- "Our OKR is X, this story directly serves that"
- Let strategic clarity guide tactical decisions

### When to Stand Firm
- User-facing quality/safety issues
- Commitments to customers/partners
- Strategic bets that can't wait
- Shlomi's explicit priorities

### When to Compromise
- Nice-to-haves vs. must-haves
- Timing (this sprint vs. next)
- Scope (full version vs. MVP)
- Order (later in sprint vs. earlier)

---

## Red Flags During Meeting

**Warning signs of misalignment:**
- ❌ R&D surprised by stories (should've been previewed)
- ❌ Design incomplete (should've been done at refinement)
- ❌ Dependencies not mapped (prep failure)
- ❌ Can't articulate business value (prep failure)
- ❌ Everything is "must-have" (lack of real priorities)

**If these happen:**
- Acknowledge the gap
- Take stories back for more work if needed
- Don't force through unready work
- Better to delay than commit to failure

---

## Post-Meeting Actions

### Immediate (Within 1 hour):
- [ ] Update sprint backlog in Jira/tool
- [ ] Document any scope changes from original plan
- [ ] Note rationale for compromises
- [ ] Communicate sprint plan to stakeholders (if needed)

### Before Sprint Starts (Monday morning):
- [ ] Ensure R&D has everything they need
- [ ] Clear any remaining blockers
- [ ] Set up tracking/status checks
- [ ] Prep for any kickoff activities

### Track During Sprint:
- [ ] Stories getting pushed back? Why?
- [ ] Your estimates vs. reality
- [ ] What you negotiated working out?
- [ ] Learnings for next planning

---

## Success Criteria

**You know it went well when:**
- ✅ Sprint has clear, achievable scope
- ✅ R&D confident in commitments
- ✅ Product priorities preserved where critical
- ✅ Compromises feel reasonable, not defeats
- ✅ Both sides feel heard and respected
- ✅ You can explain trade-offs if asked

**Warning signs it didn't:**
- ❌ Scope feels random or disconnected from goals
- ❌ R&D skeptical they can deliver
- ❌ You feel steamrolled or ignored
- ❌ Critical items got cut without good reason
- ❌ Tension in the room, not collaboration

---

## Relationship Dynamics to Monitor

### With Dor (VP R&D):
- How does he challenge? (Technical? Capacity? Strategic?)
- What earns his respect/trust?
- When does he defer to product?
- [Document patterns as you learn]

### With Leon (CTO):
- What's his decision-making style?
- When does he intervene?
- How to best work with him?
- [Document patterns as you learn]

### With Shlomi:
- Does he back you up?
- When does he override you?
- How to stay aligned?
- [Document patterns as you learn]

---

## Continuous Improvement

### After Each Sprint Planning:
1. What went better than last time?
2. Where did I lose negotiations I should've won?
3. Where did I dig in when I should've compromised?
4. What prep would've helped?
5. How's my relationship with Dor/Leon evolving?

### Track Over Time:
- Win rate on priorities
- Quality of compromises
- Trust building with R&D
- Shlomi's confidence in you

---

## Connection to Your Growth Edges

**This meeting tests:**
- **"Harsh water" approach** - Push hard but adapt
- **Authority dynamics** - Dor/Leon have power, stay grounded
- **Advocacy** - Stand up for product, don't let things go too easily
- **Translation not performance** - Be authentic, not impressive
- **Systemic progression** - Find paths forward even when blocked

**Watch for:**
- "People feel stupid" signal - Are you out of sync?
- Over-compliance - Are you folding too easily?
- Rebellion - Are you digging in on ego vs. principle?

---

---

## Jira Integration Quick Reference

**Before planning**:
- `python3 scripts/analyze_jira.py --active` - Current work reality
- `python3 scripts/analyze_jira.py --recent` - Recent delivery (credibility)
- Check `.claude/sola-reference-index.md` for full integration guide

**After planning**:
- Update Jira with sprint commitments
- Flag any tickets affected by scope negotiations
- Track what got deferred and why

---

**Last Updated**: 2025-10-12
**Next Sprint Planning**: Sunday, Oct 12, 2025 at 17:00
