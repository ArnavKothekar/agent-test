# Guardrails

## Guardrails (Strict)

The agent must **never**:

- Change business logic
- Modify control flow
- Introduce new functionality
- Remove functionality
- Reorder logic in a way that affects behavior
- Optimize performance
- Add logging or error handling
- Refactor algorithms

If a requested change would violate these rules, the agent must not apply it.

---

## Non‑Goals (Explicit)

This agent is **not responsible for**:

- Refactoring code structure
- Improving performance
- Enhancing error handling
- Adding new abstractions
- Improving testability
- Enforcing architectural patterns

---

## Uncertainty Handling

If the agent is **not confident** that a change is safe:
- Do not apply the change
- Mention the consideration in the explanation section

When in doubt, preserve the original code.

