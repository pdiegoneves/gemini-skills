---
name: universal-planner
description: "Use sempre que precisar realizar qualquer tarefa relacionada a código."
category: planning
risk: unknown
source: my
date_added: "2026-04-08"
---

# Universal Planner

## Purpose
This skill enforces a mandatory, standardized planning protocol for **every request involving code modifications or new implementations**. It ensures technical integrity by requiring a deep understanding of context and a structured breakdown of tasks before any files are modified.

## Mandatory Usage
**CRITICAL:** This skill MUST be activated and its workflow followed for ANY request that involves:
- Implementing new features
- Fixing bugs or resolving errors
- Refactoring existing code
- Modifying configuration files
- Writing tests

## Planning Workflow

Before touching any code, the agent MUST follow these four steps:

### 1. Context Understanding
- Analyze the existing codebase related to the request.
- Identify dependencies, affected modules, and potential side effects.
- Verify assumptions by reading relevant files or running discovery commands.

### 2. Specification
- Clearly define WHAT will be performed.
- List the expected outcomes and technical requirements.
- Identify the criteria for a "successful" implementation.

### 3. Complete Planning
- Design the architectural approach.
- Select necessary tools and libraries (verifying their availability).
- Define the testing strategy to be used for validation.

### 4. Atomic Task Execution
- Break down the plan into small, independent, and verifiable tasks.
- Use the following status markers to track progress in every response:
  - `[ ]` **Pending Task**: Not yet started.
  - `[/]` **In Progress**: Task currently being executed. Mark this when starting.
  - `[X]` **Completed**: Task finished and verified. Mark this immediately after completion.
  - `[-]` **Error/Failed**: Task resulted in an error. **Action:** Stop current execution, initiate a new planning phase focused on correcting the error, then resume the original tasks once resolved.

## Examples

### Trigger: "Fix the login error"
1. **Context**: I found that the `AuthService` is throwing a 401 due to a missing header.
2. **Spec**: Add the `X-API-KEY` header to all outgoing requests in `apps/common/services`.
3. **Plan**: Modify `api_client.py`, update tests, and run integration suite.
4. **Tasks**:
   - [X] Read `apps/common/services/api_client.py` to identify header insertion point.
   - [/] Update `headers` dictionary in `ApiClient.request`.
   - [ ] Add unit test in `tests/test_api_client.py`.
   - [ ] Run `pytest tests/test_api_client.py`.

## Rules
- Never skip the planning phase.
- Never modify files until Step 4 (Atomic Task Execution).
- Tasks must be small enough to be completed in 1-2 turns.
- Always update the task list status in every message during the Execution phase.
