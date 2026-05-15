# Naming Conventions Skill

### 4.1 Variable Naming Conventions

|Element|Convention|Example|
|---|---|---|
|Variables|`snake_case`|`user_input`, `coin_result`|
|Functions|`snake_case`|`find_upper()`, `calculate_area()`|
|Classes|`PascalCase`|`CoinGame`, `AreaCalculator`|
|Constants|`UPPER_CASE`|`MAX_ATTEMPTS`, `COIN_SIDES`|

Improve unclear variable names when intent is obvious. If intent is unclear, **do not rename** and instead mention it in the explanation section.

For more information on intent refer to the guardrails defined in the guardrails.policies.md file. Abide by the strict rules outlined there to ensure that no changes are made that could alter the behavior of the code.

File path: `agent-test/.github/policies/guardrails.policies.md`

