# Line Management Skill

Python code blocks should be cleanly divided indo easily understood chunks for clarity. This skill outlines the Line management conventions to be upheld by the agent. Wherever needed, the agent will modify code such that the following practices are followed.

### Spacing & Layout

Spacing should be: Clean, Compact, Intentional

Guidelines:

- Group related logic together
- Use intentional spacing: one blank line for minor divisions, two blank lines for major structural boundaries (functions, sections).
- Avoid excessive empty lines
- Maintain consistent indentation (4 spaces)
- Remove trailing whitespace

The visual style should resemble clean, well-maintained production Python code.

Example:

```python

# =========================
# Standard Library Imports
# =========================

import math
import random


# =========
# Constants
# =========

COIN_SIDES = ("heads", "tails")


# =========================
# Input Helper Functions
# =========================

# Input: Accept a positive integer entered by the user
# Processing: Validate that the input is numeric and greater than zero
# Output: Return the validated integer

def get_positive_integer() -> int:
    while True:
        user_input = input("Enter a positive integer: ").strip()
        if user_input.isdigit() and int(user_input) > 0:
            return int(user_input)
        print("Invalid input. Please enter a positive integer.")
```

---

### 4.4 Line Length Management

- Respect common Python line length conventions (~79–88 characters)
- Break long lines sensibly
- Avoid excessive line wrapping that harms readability