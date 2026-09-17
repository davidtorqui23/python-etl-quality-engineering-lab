# SC-US-005

## Step Catalog

### Step 1: Dataset is available
- Given a dataset with phone values exists
- Purpose: confirm the phone field is present for validation
- Expected result: phone values can be assessed

### Step 2: Phone field is validated
- When phone number quality is validated
- Purpose: check for column presence, blanks, and format compliance
- Expected result: each phone number is assessed for quality

### Step 3: Validation passes or fails
- Then the validation result should pass
- Or: Then the validation result should fail
- Purpose: return a clear pass/fail outcome
- Expected result: validation reflects actual phone quality status

### Step 4: Invalid rows are reported
- And the invalid phone rows should be reported
- Purpose: provide row-level defect context
- Expected result: invalid row indexes and reasons are returned

## Acceptance Criteria Mapping
- Phone column exists -> Steps 1 and 2
- Phone values are not null or blank -> Step 2
- Phone values follow an expected format -> Step 2
- Invalid phone numbers are reported with row context -> Step 4
- Validation result is returned -> Step 3

## Story
US-005: Validate Phone Number Quality
