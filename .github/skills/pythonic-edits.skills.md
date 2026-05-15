# Pythonic Edits

Python code can be made far mroe readable using features specific to it. These include Type hints, Import management, style only constructs, and more. 
Standard use of these features should be done for clarity. 
This skill outlines the conventions to be upheld by the agent. 
Wherever needed, the agent will modify code such that the following practices are followed.

### Type Hints

- Add type hints wherever reasonably possible
- Prefer correctness over completeness
- Do not force type hints in:
  - Highly dynamic contexts
  - Duck-typed logic
  - External libraries without clear type contracts

If type inference is uncertain, do not add a type hint and explain why.

---

## Imports Management

- Sort imports into:
	  1. Standard library
	  2. Third-party libraries
	  3. Local imports
- Remove unused imports
- Combine duplicate imports
- Preserve import behavior

---

## Pythonic Improvements (Style-Only)

The agent may introduce **Pythonic constructs** only when they:
- Improve readability
- Do not alter logic or behavior

Examples include:
- `enumerate`
- Direct iteration over collections
- Context managers (`with` statements)

Example:

```python
# Before:
for i in range(len(items)):
    print(i, items[i])

# After:
for index, item in enumerate(items):
    print(index, item)
```