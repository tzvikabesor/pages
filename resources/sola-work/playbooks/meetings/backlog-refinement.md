# Backlog Refinement - Preparation Playbook

**Meeting Type**: Product Team Story Review & Prioritization
**Frequency**: Bi-weekly, Wednesdays
**Duration**: [TBD]
**Next Meeting**: [Check calendar]
**Leads To**: Sprint Planning (5 days later, Sunday)

---

## Pre-Meeting Preparation (Critical - This Meeting Lives or Dies on Your Prep)

### Timeline: Start 3-5 Days Before

#### Step 0: Review Your Jira Tickets (30 min)
**Run before starting story gathering**

```bash
# See what's currently in your backlog
python3 scripts/analyze_jira.py --active

# Check what you recently completed (shows velocity/progress)
python3 scripts/analyze_jira.py --recent

# Get overall picture
python3 scripts/analyze_jira.py --summary
```

**Questions to answer:**
- [ ] Which "To Do" tickets are ready for this sprint?
- [ ] Any tickets in "To Discuss" that need resolution first?
- [ ] What recently completed tickets inform current priorities?
- [ ] Are there ticket patterns suggesting focus areas (Canvas 2.0, AI, Onboarding)?

**Why this matters**: Your Jira tickets are your work reality. Starting here grounds your planning in actual backlog, not abstract ideation.

---

#### Step 1: Gather Candidate Stories (Day 1-2)
- [ ] Review backlog for next sprint candidates
- [ ] Check with stakeholders on priority shifts
- [ ] Verify design readiness with Lior/Ami
- [ ] Identify dependencies or blockers
- [ ] Rough prioritization based on current goals

#### Step 2: Make Stories Production-Ready (Day 2-4)
For each story:
- [ ] **User story** is clear (As a [role], I want [action], so that [benefit])
- [ ] **Acceptance criteria** defined (what "done" looks like)
- [ ] **Business value** articulated (why this matters now)
- [ ] **Design assets** available (if visual work)
- [ ] **Dependencies** documented
- [ ] **Open questions** resolved or flagged
- [ ] **Estimated** (if your team sizes stories)

#### Step 3: Prioritize & Sequence (Day 4-5)
- [ ] Rank stories by business value + urgency
- [ ] Consider dependencies (what must come first)
- [ ] Align with OKRs/quarterly goals
- [ ] Prepare rationale for each priority decision
- [ ] Identify what you'd cut if capacity is lower than expected

#### Step 4: Pre-Sync with Key People (Day 5)

**With Lior (UX):**
- [ ] Confirm design is ready for top priorities
- [ ] Surface any design concerns early
- [ ] Align on user experience priorities

**With Shlomi (optional but recommended):**
- [ ] Quick preview of top stories
- [ ] Get early feedback on priorities
- [ ] Understand any strategic shifts
- [ ] Avoid surprises in the meeting

---

## Meeting Materials Checklist

Bring to meeting:
- [ ] Prioritized list of candidate stories
- [ ] Story details (links to Jira/whatever tool)
- [ ] Design assets/mockups
- [ ] Business rationale for priorities
- [ ] Dependencies map
- [ ] Questions for team

---

## During Meeting

### Your Role: Present, Defend, Listen, Adapt

#### Opening (5 min)
- Context: What's driving priorities this sprint?
- Changes: Any shifts since last refinement?

#### Story by Story Review
For each story:
1. **Present**: What it is, why it matters
2. **Show**: Design (if visual), acceptance criteria
3. **Listen**: Team feedback, especially Shlomi's
4. **Clarify**: Answer questions, resolve ambiguities
5. **Adapt**: Adjust based on feedback

#### Priority Discussion
- Defend your prioritization logic
- Be open to re-sequencing based on team input
- Note where Shlomi pushes back (matters for Sprint Planning)

#### Finalize
- [ ] Agreed prioritized list
- [ ] All stories production-ready
- [ ] No blockers for Sprint Planning
- [ ] Clear on what R&D will see Sunday

---

## Red Flags During Meeting

**Warning signs you're not ready:**
- Stories aren't clear → scrambling to explain
- Design missing → delays, frustration
- Shlomi skeptical → won't improve at Sprint Planning
- Team finds gaps in acceptance criteria → quality concerns
- Can't defend priorities → lack of strategic clarity

**If these happen:**
- Acknowledge the gap honestly
- Commit to fix before Sprint Planning
- Don't try to push through unready stories

---

## Post-Meeting Actions

### Immediate (Within 1 hour):
- [ ] Update Jira/tool with decisions
- [ ] Document finalized priority list
- [ ] Note any changes from original plan
- [ ] Share summary with team (if expected)

### Before Sprint Planning (Next 5 days):
- [ ] Resolve any open items flagged
- [ ] Prep for R&D/CTO questions
- [ ] Refresh on business rationale
- [ ] Anticipate technical challenges

---

## Success Criteria

**You know it went well when:**
- ✅ Shlomi is confident in the list
- ✅ Design team aligned
- ✅ No gaps or ambiguities remain
- ✅ Priorities are clear and defensible
- ✅ You feel ready to face Dor/Leon on Sunday

**Warning signs it didn't:**
- ❌ Shlomi skeptical or pushing back hard
- ❌ Design concerns unresolved
- ❌ Stories still have gaps
- ❌ Priorities feel shaky
- ❌ You're dreading Sprint Planning

---

## Continuous Improvement

### After Each Refinement, Reflect:
1. What prep step did I skip that hurt me?
2. Where did I waste time (over-prepared)?
3. What feedback pattern is Shlomi showing?
4. How can I get design aligned earlier?
5. What made a story "production-ready" vs. not?

---

## Notes & Patterns

**Shlomi's Review Style:**
[To be documented as you learn his patterns]

**Common Gaps in Stories:**
[Track what keeps coming up]

**Design Alignment Best Practices:**
[What works with Lior/Ami]

**Time Management:**
- How long does prep realistically take?
- When do you need to start?
- What can be delegated/streamlined?

---

---

## Jira Integration Quick Reference

**Before refinement**:
- `python3 scripts/analyze_jira.py --active` - See your To Do tickets
- Check `.claude/sola-reference-index.md` for full Jira usage guide

**After refinement**:
- Update Jira tickets with decisions
- Mark completed tickets as Done
- Add newly created tickets to Jira

---

**Last Updated**: 2025-10-12
**Next Refinement**: [Check calendar]
