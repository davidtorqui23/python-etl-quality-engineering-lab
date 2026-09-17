# How to Execute the AI-Assisted Workflows

This document is the operational guide for using the specialized agents included in the Python ETL Quality Engineering Lab.

It explains:

- Which agent to select
- Which workflow to use
- Which prompt to provide
- Which artifacts should be created
- Which verification steps must be completed

---

# Before Starting

Before executing any workflow:

1. Open the project in Visual Studio Code.
2. Activate the Python virtual environment.
3. Verify the current Git status.
4. Select the appropriate agent.
5. Use the prompt associated with the type of change.
6. Review all generated changes before committing.
7. Execute the regression suite.
8. Generate the pytest HTML report.
9. Create one focused commit for the completed change.

Activate the virtual environment in PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Verify the repository:

```powershell
git status
```

---

# Select the Correct Workflow

Use the following decision guide:

```text
Does the request add new business behavior?
    Yes
    → New User Story
    → Delivery Manager

Does the behavior already exist and only need another scenario?
    Yes
    → Test Case Enhancement
    → Test Automation Engineer

Is the existing behavior incorrect?
    Yes
    → Bug Fix
    → Delivery Manager

Is the behavior correct but the structure needs improvement?
    Yes
    → Technical Refactor
    → Delivery Manager

Are tests missing logs or producing duplicate logs?
    Yes
    → Test Logging Compliance
    → Test Automation Engineer

Does the repository require cleanup or a final review?
    Yes
    → Project Audit
    → Delivery Manager
```

---

# Workflow 1: Implement a New User Story

## Use this workflow when

Use this workflow when implementing a new ETL capability or business rule.

Examples:

- Validate a new data field
- Add a transformation
- Add a load target
- Introduce another ETL stage
- Add new business behavior

## Select this agent

```text
Delivery Manager
```

## Prompt template

```text
Execute Full Lifecycle

Story ID:
US-XXX

Business Requirement:

[Describe the required functionality]

Business Value:

As a [role],

I want [capability]

so that [business outcome].

Lifecycle Mode:
Execute

Follow the Delegation Principle.

The Delivery Manager must coordinate the specialized agents and verify their outputs.

Required lifecycle:

- Story Writer
- Feature Writer
- Test Designer
- ETL Implementer
- Implementation Builder
- Test Automation Engineer
- Step Review Agent
- Code Review Agent
- Data Quality Review Agent

Technical Requirements:

- Use the shared logger from src/common/logger.py
- Keep all log messages in English
- Store complex test inputs under tests/resources/input/
- Store expected results under tests/resources/expected/
- Execute the complete regression suite
- Generate the pytest HTML report

Continue until the story reaches:

- Done
or
- Blocked
```

## Expected lifecycle

```text
Business Requirement
        ↓
User Story
        ↓
Gherkin Feature
        ↓
Test Design
        ↓
Implementation Design
        ↓
Source Code
        ↓
Automated Tests
        ↓
Reviews
        ↓
Regression
        ↓
Done
```

## Expected artifacts

Depending on the scope, the workflow may generate or update:

```text
docs/stories/
features/
docs/test-designs/
docs/steps/
docs/traceability/
docs/implementation-designs/
src/
tests/
docs/review-reports/
docs/history/
```

---

# Workflow 2: Add a Test Case

## Use this workflow when

Use this workflow when functionality already exists and only additional coverage is required.

Examples:

- Add another invalid email format
- Add a boundary value
- Add a null-value scenario
- Add regression coverage for a defect
- Add another input variation

Do not create a complete User Story unless the scenario introduces new business behavior.

## Select this agent

```text
Test Automation Engineer
```

## Prompt template

```text
Test Case Enhancement

Target Module:

[Existing module or validator]

Target Test File:

[Existing test file]

Scenario:

[Describe the new test scenario]

Expected Behavior:

[Describe the expected result]

Required Actions:

1. Review the current implementation and existing tests.

2. Confirm that the scenario is not already covered.

3. Reuse existing fixtures, helpers and test patterns.

4. Store complex input data under:

tests/resources/input/

5. Store expected results under:

tests/resources/expected/

6. Add the automated test to the appropriate existing test file.

7. Use the shared logger from:

src/common/logger.py

8. Preserve centralized test lifecycle logging from:

tests/conftest.py

9. Add meaningful business execution logs only when necessary.

10. Keep all log messages in English.

11. Do not duplicate fixtures, lifecycle messages, assertions or business logic.

12. Preserve existing functionality.

13. Execute the affected test file.

14. Execute the complete regression suite.

15. Generate the pytest HTML report.

Do not create:

- A new User Story
- A new Feature
- A new validation domain
- A new validator unless new behavior is required
- Unnecessary markdown files

This is a test case enhancement only.
```

## Test-data convention

Complex test data must not be hardcoded inside test methods.

Use:

```text
tests/resources/
├── input/
│   └── scenario_input.json
└── expected/
    └── scenario_expected.json
```

Tests should remain focused on:

```text
Arrange
Act
Assert
```

---

# Workflow 3: Fix a Defect

## Use this workflow when

Use this workflow when existing behavior does not match an approved requirement.

Examples:

- Valid data is incorrectly rejected
- Invalid data is accepted
- SQLite receives invalid records
- A transformation produces an incorrect value
- A pipeline stage raises an unexpected exception

## Select this agent

```text
Delivery Manager
```

## Prompt template

```text
Bug Fix

Defect ID:
BUG-XXX

Affected Story:
US-XXX

Affected Module:

[Module name]

Observed Behavior:

[Describe the current behavior]

Expected Behavior:

[Describe the expected behavior]

Reproduction Scenario:

[Describe the data and steps required to reproduce the defect]

Required Actions:

1. Reproduce the defect with an automated failing test.

2. Record the failure in the existing defect resolution log.

3. Identify the root cause.

4. Apply the smallest safe correction.

5. Preserve unrelated functionality.

6. Use the shared logger from src/common/logger.py.

7. Keep all log messages in English.

8. Use WARNING for expected data quality findings.

9. Use ERROR only for unexpected technical failures.

10. Execute the affected test.

11. Execute the complete regression suite.

12. Generate the pytest HTML report.

13. Append the resolution and verification result to the existing defect log.

Do not create unnecessary domains, managers or service layers.

Stop only when:

- The defect is resolved and regression passes
or
- The defect becomes Blocked
```

---

# Workflow 4: Perform a Technical Refactor

## Use this workflow when

Use this workflow when improving project structure or maintainability without changing behavior.

Examples:

- Move a file to the correct package
- Remove duplicate logging modules
- Extract hardcoded test data
- Update imports
- Consolidate utilities
- Simplify a workflow

## Select this agent

```text
Delivery Manager
```

## Prompt template

```text
Project Refactor

Refactor ID:
TR-XXX

Objective:

[Describe the technical improvement]

Current State:

[Describe the current structure or problem]

Target State:

[Describe the desired structure]

Required Actions:

1. Review affected files and dependencies.

2. Apply only the required refactor.

3. Update affected imports.

4. Update tests only when required.

5. Preserve existing behavior.

6. Do not introduce new business functionality.

7. Do not create domains, managers or service layers unless explicitly required.

8. Keep shared infrastructure under:

src/common/

9. Keep business components in their appropriate layers:

- src/extract/
- src/transform/
- src/load/
- src/validation/

10. Execute the complete regression suite.

11. Generate the pytest HTML report.

Verification Required:

- Existing behavior preserved
- Imports valid
- Tests passing
- Logging preserved
- No unnecessary files created

This is a refactor only.
```

---

# Workflow 5: Review Test Logging

## Use this workflow when

Use this workflow when tests are missing logs, lifecycle logs are duplicated or log output is difficult to read.

## Select this agent

```text
Test Automation Engineer
```

## Prompt template

```text
Test Logging Compliance Review

Target:

tests/

Objective:

Ensure consistent and readable test logging without duplicated lifecycle messages.

Required Actions:

1. Review tests/conftest.py.

2. Review all relevant test files.

3. Ensure conftest.py is the single source of truth for:

- START TEST
- TEST PASSED
- TEST FAILED
- END TEST

4. Remove duplicated lifecycle logging from individual tests.

5. Preserve meaningful business execution logs.

6. Ensure tests use the shared logger when business logging is required.

7. Keep all log messages in English.

8. Apply these levels:

- INFO for normal execution
- WARNING for expected data quality findings
- ERROR for unexpected technical failures
- CRITICAL for execution-stopping failures

9. Do not modify assertions or business behavior.

10. Execute the complete regression suite.

11. Verify that logs are readable and not duplicated.

Do not create new tests.

Do not create new functionality.

Modify only what is required for logging compliance.
```

---

# Workflow 6: Audit the Repository

## Use this workflow when

Use this workflow before publishing a release or presenting the portfolio.

## Select this agent

```text
Delivery Manager
```

## Prompt template

```text
Project Final Audit

Objective:

Review the repository for maintainability and portfolio readiness.

Analyze:

- src/
- tests/
- tests/resources/
- docs/
- logs/
- reports/
- .github/
- requirements.txt
- pytest.ini
- README.md
- HOW_EXECUTE.md
- .gitignore

Identify:

- Dead code
- Unused imports
- Duplicate implementations
- Duplicate tests
- Hardcoded complex test data
- Unused markdown files
- Outdated documentation
- Orphan files
- Incorrect package placement
- Logging duplication
- Redundant workflows
- Technical debt

Classify findings as:

- KEEP
- REFACTOR
- ARCHIVE
- REMOVE

For every markdown file, provide its complete path and determine whether it is:

- Required
- Referenced
- Optional
- Obsolete
- Orphaned

Do not modify or delete files.

Generate audit findings only.
```

---

# Running Tests

## Complete regression

```powershell
python -m pytest -v
```

## Complete regression with HTML report

```powershell
python -m pytest -v --html=reports/pytest/report.html --self-contained-html
```

## Specific test file

```powershell
python -m pytest tests/test_validate_email_quality.py -v
```

## Specific test file with report

```powershell
python -m pytest tests/test_validate_email_quality.py -v --html=reports/pytest/email-report.html --self-contained-html
```

## Tests matching a name

```powershell
python -m pytest -k "email" -v
```

---

# Reviewing Results

After execution, review:

```text
Console output
↓
Pytest HTML report
↓
Execution log
↓
Validation log
↓
Generated output
```

Expected locations:

```text
reports/pytest/
logs/
data/processed/
data/output/
```

Generated logs, reports, temporary databases and virtual environments must not be committed.

---

# Committing Changes

Use one focused commit for each completed change.

## User Story

```powershell
git add .
git commit -m "feat(US-XXX): describe implemented functionality"
git push
```

## Test Case Enhancement

```powershell
git add .
git commit -m "test: add coverage for the new scenario"
git push
```

## Bug Fix

```powershell
git add .
git commit -m "fix: correct affected behavior"
git push
```

## Technical Refactor

```powershell
git add .
git commit -m "refactor: describe the structural improvement"
git push
```

---

# Engineering Rules

1. Use a complete lifecycle only for new business behavior.

2. Use Test Case Enhancement for additional coverage.

3. Keep complex input data outside test methods.

4. Keep expected results separate from input data.

5. Use the shared logger from `src/common/logger.py`.

6. Keep lifecycle logging centralized in `tests/conftest.py`.

7. Keep all log messages in English.

8. Use WARNING for expected invalid data.

9. Use ERROR only for unexpected technical failures.

10. Execute regression after every change.

11. Generate the pytest HTML report before completing relevant work.

12. Use one focused Git commit per completed change.

13. Never commit generated logs, reports, temporary databases or virtual environments.