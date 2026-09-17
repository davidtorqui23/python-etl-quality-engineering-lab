# SC-US-004

## Step Catalog

### Step 1: Dataset is available
- Given a dataset with email values exists
- Purpose: confirm the email field is present for validation
- Expected result: email values can be assessed

### Step 2: Email field is validated
- When email quality is validated
- Purpose: check for column presence, blanks, and format compliance
- Expected result: each email is assessed for quality

### Step 3: Validation passes or fails
- Then the validation result should pass
- Or: Then the validation result should fail
- Purpose: return a clear pass/fail outcome
- Expected result: validation reflects actual email quality status

### Step 4: Invalid rows are reported
- And the invalid email rows should be reported
- Purpose: provide row-level defect context
- Expected result: invalid row indexes are returned

## Acceptance Criteria Mapping
- Email column exists -> Steps 1 and 2
- Email values are not null or blank -> Step 2
- Email values match the expected email pattern -> Step 2
- Invalid emails are reported with row context -> Step 4
- Validation result is returned -> Step 3

## Story
US-004: Validate Email Quality
