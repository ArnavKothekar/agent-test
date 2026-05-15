# Commenting Conventions Skill

Python code blocks should follow a standard set of commenting practices for clarity. This skill outlines the commenting conventions to be upheld by the agent. Wherever needed, the agent will modify or add comments such that the following practices are followed.

### Commenting Style

The agent should introduce comments using the following style:

- Use a **concise single-line comment** describing: Input, Procedure, Output
- If a single line comment is too lengthy, use 3 single line comments, one for each section
- Do not repeat what the code already clearly states
- Do not comment every line
- Do not add comments for trivial operations
- Prefer clarity over density

### Commenting Cases

- Definition of a function
- Definition of a class
- Import of libraries
- Procedure 

### Example

```python
# Input: user integer | Processing: validate positivity | Output: validated integer
def get_positive_integer() -> int:

# Input: user inputs and program state
# Processing: coin flip and conditional area calculation
# Output: formatted result printed to stdout
def main() -> None:
	...
```