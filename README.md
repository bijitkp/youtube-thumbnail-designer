# Agentic AI YouTube Thumbnail Generator

An autonomous Agentic AI workflow that generates, critiques, refines, and selects high-quality YouTube thumbnails using LangGraph orchestration.

Built using:
- LangGraph
- LangChain concepts
- OpenAI multimodal generation
- Autonomous critic-feedback loop
- Conditional graph routing

---

# Project Overview

This project demonstrates a fully autonomous Agentic AI pipeline where multiple AI agents collaborate to:

1. Research a topic
2. Generate thumbnail prompts
3. Generate thumbnail images
4. Critique outputs
5. Refine prompts iteratively
6. Decide whether to continue or terminate
7. Save the best generated result

The orchestration is handled completely by LangGraph using graph-based state transitions instead of manual procedural loops.

---

# Key Features

## Autonomous Agentic Loop

The system uses:
- conditional routing
- iterative refinement
- stateful orchestration

instead of a manual `while` loop.

---

## Multi-Agent Workflow

The pipeline consists of multiple specialized AI agents:

| Agent | Responsibility |
|---|---|
| Web Search Agent | Topic research |
| Prompt Writer Agent | Thumbnail prompt creation |
| Generator Agent | Image generation |
| Critic Agent | Quality evaluation |
| Router Agent | Autonomous decision making |
| Compiler Agent | Final asset selection |
| Saver Agent | Report + output persistence |

---

## LangGraph Orchestration

Implemented using:
- `StateGraph`
- `START`
- `END`
- `add_node()`
- `add_conditional_edges()`
- `graph.compile()`

---

## Structured Critic Output

The critic uses:
- Pydantic schema validation
- structured OpenAI responses

This guarantees:
- integer-safe ratings
- deterministic orchestration
- reliable routing decisions

---

# Architecture

```text
START
  ↓
web_search
  ↓
prompt_writer
  ↓
generator
  ↓
critic
  ↓
router
   ├── continue → prompt_writer
   └── finish   → compiler
                        ↓
                      saver
                        ↓
                       END