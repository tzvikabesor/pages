# Work System Project - Working Notes

This file captures decisions, insights, and context as the project evolves.

---

## 2024-10-10 - Project Initiation

### Why This Needs to Be a Project

Started with ad-hoc file creation (ABOUT.md, ROADMAP.md, etc.) but realized this won't reach v1 without structured approach.

Key insight: **This system needs to integrate with actual work tools and provide automated value, not just be better-organized markdown files.**

### Core Requirements Identified

1. **Calendar Integration** - Time-blocking needs to connect to Google Calendar
2. **Slack/Jira Integration** - Work context should surface without opening multiple tools
3. **Interfaces** - Need dashboards/views that make right information visible at right time
4. **Automation** - Routines and workflows that maintain the system
5. **Agents** - Still figuring out what this means and what value it provides

### Critical Success Factor

**Must reduce cognitive load, not add to it.** If the system requires constant manual maintenance, it will fail. ADHD brain needs external structure that works automatically.

### Next Steps

1. Return from Rome (2024-10-19)
2. Schedule dedicated time for discovery phase
3. Document current tool landscape
4. Make key integration decisions
5. Start building

---

## Questions to Answer

- What does "v1 complete" actually mean in practice? What would I be doing differently?
- Which integration is most valuable to tackle first?
- What's the minimum viable dashboard that would actually change behavior?
- How do we validate that something is working vs. just built?

---

## Ideas & Explorations

_Capture interesting ideas here as they emerge_

---

## Technical Notes

### 2024-10-10 - Slack MCP Integration Setup

**Decision**: Use user-level token approach (no workspace admin approval needed)

**Approach**:
- Using `korotovsky/slack-mcp-server` (supports xoxp user tokens)
- User token gives access to channels/DMs I'm already in
- Start with read-only to see value before expanding

**Completed**:
1. ✅ Created Slack app in Solla workspace
2. ✅ Got user OAuth token (xoxp) and refresh token
3. ✅ Created `.env` file with tokens (added to .gitignore)
4. ✅ Configured MCP server in `.mcp.json`

**Configuration**:
- MCP server: `slack-mcp-server@latest` via npx
- Transport: stdio
- Auth: xoxp user token from environment variable
- Files created:
  - `.mcp.json` - MCP server configuration
  - `.env` - Secure token storage
  - `.gitignore` - Prevents committing secrets

**Security note**:
- Token is stored directly in `.mcp.json` (not as environment variable reference)
- Added `.mcp.json` to `.gitignore` to prevent committing token
- This is the secure approach for project-scoped MCP servers

**Status**:
- ✅ MCP server configured in `.mcp.json`
- ⏳ Waiting to verify server loads and tools are available
- Need to test Slack integration works

**Next steps**:
1. Verify Slack MCP tools are available (check for `mcp__slack__*` tools)
2. Test listing channels in Solla workspace
3. Test reading messages from a channel
4. Document available tools and their usage
5. Update roadmap with working Slack integration

---

**Last Updated**: 2024-10-10
