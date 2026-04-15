# Universal Planner Skill

A mandatory planning protocol for all code-related requests in Gemini CLI.

## Installation

This skill is automatically loaded from the `.claude/skills/universal-planner` directory.

## Usage

This skill triggers on any code-related request. It forces the agent to stop and plan before making any changes.

### The Protocol
1. **Understand Context**: Research files and dependencies.
2. **Specification**: Define what will be done.
3. **Planning**: Create a roadmap and testing strategy.
4. **Atomic Tasks**: Execute using status markers:
   - `[ ]` Pending
   - `[/]` In Progress
   - `[X]` Completed
   - `[-]` Error (Triggers re-planning)
