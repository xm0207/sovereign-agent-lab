"""
Exercise 3 — Answers
====================
Fill this in after completing the three Rasa conversations.

CALM vs Old Rasa — what changed
---------------------------------
The old open-source Rasa approach used:
  - nlu.yml: intent training examples
  - rules.yml: explicit dialogue rules
  - FormValidationAction: Python class to parse slot values

Rasa Pro CALM uses:
  - flows.yml: natural language descriptions of what each flow does
  - from_llm slots: the LLM extracts values from conversation
  - ONE custom action: ActionValidateBooking for the business rules

The conversation is the same from the manager's perspective.
The machinery underneath is completely different.

CONVERSATION SCRIPTS
---------------------
Conversation 1 (happy path):
  You:    calling to confirm a booking
  Agent:  [asks guest count]
  You:    160 guests
  Agent:  [asks vegan count]
  You:    about 50 need vegan
  Agent:  [asks deposit]
  You:    £200 deposit
  Agent:  [confirms or escalates?]

Conversation 2 (deposit too high):
  Same as above but use a deposit above £300 (e.g. "£500 deposit").

Conversation 3 (out of scope):
  Start normally, then when asked for vegan count say something like
  "can you arrange parking for the speakers?" and observe what happens.
  Does CALM handle this differently than the old rules approach?
"""

# ── Conversation 1: Happy path ─────────────────────────────────────────────

CONVERSATION_1_TRACE = """
You: I want to confirm a booking.
Agent: How many guests are you confirming for tonight's event?

You: 200, 50 of them are vegan
Agent: What deposit amount in GBP are you proposing to secure the booking?

You: oh, its 160 people, 50 of them are vegan.I can pay a 200 pound deposit
Agent: Ok, I am updating guest_count, vegan_count to 160, 50 respectively.
Thank you – booking confirmed. 160 guests, 50 requiring vegan meals, £200 deposit accepted. I'll send written confirmation to the organiser shortly.
Is there anything else I can help you with?
"""

CONVERSATION_1_OUTCOME = "confirmed"

# ── Conversation 2: Deposit too high ───────────────────────────────────────

CONVERSATION_2_TRACE = """
You: I want to confirm a booking.
Agent: How many guests are you confirming for tonight's event?

You: 160 guests, 50 of them are vegan.
Agent: What deposit amount in GBP are you proposing to secure the booking?

You: I can pay a £500 deposit.
Agent: I need to check one thing with the organiser before I can confirm. The issue is that a deposit of £500 exceeds the organiser's authorised limit of £300. Can I come back to you within 15 minutes?
Is there anything else I can help you with?
"""

CONVERSATION_2_OUTCOME = "escalated"
CONVERSATION_2_REASON  = "The proposed deposit of £500 exceeded the organiser's authorised limit of £300."

# ── Conversation 3: Out of scope ───────────────────────────────────────────

CONVERSATION_3_TRACE = """
You: Do you have parking?
Agent: I'm sorry, I'm not trained to help with that.
I can only help with confirming tonight's venue booking. For anything else, please contact the event organiser directly.
Is there anything else I can help you with?
"""

# Describe what CALM did after the out-of-scope message. Min 20 words.
CONVERSATION_3_WHAT_HAPPENED = """
CALM did not hallucinate an answer about parking. It explicitly said that this request was outside its training scope, restated that it only handles tonight's booking confirmation, and redirected the user to the organiser.
"""

# Compare Rasa CALM's handling of the out-of-scope request to what
# LangGraph did in Exercise 2 Scenario 3. Min 40 words.
OUT_OF_SCOPE_COMPARISON = """
Rasa CALM and the LangGraph agent both handled the out-of-scope request conservatively and did not fabricate an answer. The difference is that CALM sounded more flow-bounded and role-specific, while the LangGraph agent framed the limitation in terms of missing tools and functional capability. CALM behaved like a tightly scoped service workflow, whereas LangGraph behaved like a general agent that knew its current tool boundary.
"""

# ── Task B: Cutoff guard ───────────────────────────────────────────────────

TASK_B_DONE = True

# List every file you changed.
TASK_B_FILES_CHANGED = [
    "exercise3_rasa/actions/actions.py",
    "week1/answers/ex3_answers.py",
]

# How did you test that it works? Min 20 words.
TASK_B_HOW_YOU_TESTED = """
I retrained the Rasa model, started the action server and chat server in separate terminals, then ran a normal booking conversation and a high-deposit conversation. The £200 deposit path confirmed successfully, while the £500 deposit path escalated instead of confirming.
"""

# ── CALM vs Old Rasa ───────────────────────────────────────────────────────

# In the old open-source Rasa (3.6.x), you needed:
#   ValidateBookingConfirmationForm with regex to parse "about 160" → 160.0
#   nlu.yml intent examples to classify "I'm calling to confirm"
#   rules.yml to define every dialogue path
#
# In Rasa Pro CALM, you need:
#   flow descriptions so the LLM knows when to trigger confirm_booking
#   from_llm slot mappings so the LLM extracts values from natural speech
#   ONE action class (ActionValidateBooking) for the business rules
#
# What does this simplification cost? What does it gain?
# Min 30 words.

CALM_VS_OLD_RASA = """
CALM moves more language understanding work from handwritten Python and explicit intent/rule files into the LLM layer. That greatly reduces boilerplate for slot extraction and conversational phrasing, and it makes natural user corrections easier to handle. Python still remains the right place for hard business rules, such as deposit cutoffs, because those rules must be deterministic and auditable. The trade-off is that old Rasa felt more rigid but also more predictable, while CALM is simpler and more flexible but introduces more hidden model behaviour and dependency on LLM reliability.
"""

# ── The setup cost ─────────────────────────────────────────────────────────

# CALM still required: config.yml, domain.yml, flows.yml, endpoints.yml,
# rasa train, two terminals, and a Rasa Pro licence.
# The old Rasa ALSO needed nlu.yml, rules.yml, and a FormValidationAction.
#
# CALM is simpler. But it's still significantly more setup than LangGraph.
# That setup bought you something specific.
# Min 40 words.

SETUP_COST_VALUE = """
The extra setup buys a controlled, production-style workflow with explicit boundaries, reproducible dialogue structure, and clearer separation between LLM language handling and deterministic business validation. Compared with LangGraph, CALM cannot improvise arbitrary tool use or dynamically expand into new tasks unless those behaviours are represented in flows and supporting actions. For the confirmation use case, that limitation is partly a feature: it reduces drift, keeps the assistant narrowly scoped, and makes escalation logic easier to trust in an operational setting.
"""
