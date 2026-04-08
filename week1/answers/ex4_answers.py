"""
Exercise 4 — Answers
====================
Fill this in after running exercise4_mcp_client.py.
"""

# ── Basic results ──────────────────────────────────────────────────────────

# Tool names as shown in "Discovered N tools" output.
TOOLS_DISCOVERED = ["search_venues", "get_venue_details"]

QUERY_1_VENUE_NAME    = "not shown in visible trace"
QUERY_1_VENUE_ADDRESS = "not shown in visible trace"
QUERY_2_FINAL_ANSWER  = "not shown in visible trace; only the initial search_venues function call was displayed"

# ── The experiment ─────────────────────────────────────────────────────────
# Required: modify venue_server.py, rerun, revert.

EX4_EXPERIMENT_DONE = True

# What changed, and which files did or didn't need updating? Min 30 words.
EX4_EXPERIMENT_RESULT = """
I changed The Albanach's status from 'available' to 'full' in sovereign_agent/tools/mcp_venue_server.py, reran Exercise 4, and then reverted the change. The visible terminal output did not materially change: the same two MCP tools were discovered and the client still showed the same initial search_venues function call. This suggests the MCP-served data changed underneath, but exercise4_mcp_client.py did not print tool results or final venue selection clearly enough to expose the difference. No client-side tool registration code needed changing.
"""

# ── MCP vs hardcoded ───────────────────────────────────────────────────────

LINES_OF_TOOL_CODE_EX2 = 4
LINES_OF_TOOL_CODE_EX4 = 0

# What does MCP buy you beyond "the tools are in a separate file"? Min 30 words.
MCP_VALUE_PROPOSITION = """
MCP gives dynamic capability discovery and a cleaner separation between the agent client and the tool provider. In Exercise 2, the LangGraph client directly imported and registered concrete Python functions. In Exercise 4, the client discovered tools from the MCP server at runtime. That means the tool surface can evolve independently, be shared across agents, and be exposed through a standard protocol rather than hardcoded imports.
"""

# ── Week 5 architecture ────────────────────────────────────────────────────
# Describe your full sovereign agent at Week 5 scale.
# At least 5 bullet points. Each bullet must be a complete sentence
# naming a component and explaining why that component does that job.

WEEK_5_ARCHITECTURE = """
- A planner agent should decompose large research or booking tasks into substeps because a single model loop becomes harder to control as the task grows in breadth and ambiguity.
- An executor agent should handle concrete tool calls because execution needs predictable schemas, retries, and tighter control over side effects than high-level planning does.
- A shared MCP tool server should expose reusable capabilities such as venue search, detail lookup, file access, and web search because multiple agents should not each hardcode the same tool integration.
- A state and memory layer should store session context, slot values, and selected prior information because multi-step tasks require continuity across turns and sometimes across sessions.
- A policy and validation layer should enforce business rules, safety limits, and escalation thresholds because prompts alone are too soft for hard operational constraints.
- An observability layer should record traces, tool calls, failures, and cost metrics because debugging agent behaviour without structured telemetry quickly becomes impossible.
"""

# ── The guiding question ───────────────────────────────────────────────────
# Which agent for the research? Which for the call? Why does swapping feel wrong?
# Must reference specific things you observed in your runs. Min 60 words.

GUIDING_QUESTION_ANSWER = """
The research task fits the LangGraph-style agent better, while the phone-call confirmation task fits the Rasa CALM agent better. In Exercise 2, the LangGraph agent explored multiple tools, checked venues, calculated catering, checked weather, and generated a flyer in a flexible loop. That behaviour is useful for open-ended research and synthesis. In Exercise 3, the CALM agent behaved like a tightly scoped workflow: it collected guest count, vegan count, and deposit, accepted a £200 deposit, escalated a £500 deposit above the £300 cutoff, and refused the parking question as out of scope. Swapping them feels wrong because the research agent is built to improvise across tools, whereas the call agent is built to stay inside a narrow, auditable service flow.
"""
