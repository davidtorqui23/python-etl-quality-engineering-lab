# SC-US-002

## Step Catalog

### Step 1: Dataset is available
- Given a dataset with the expected columns exists
- Purpose: confirm the source file exists and is readable
- Expected result: source is available for validation

### Step 2: Structure is validated
- When the dataset structure is validated
- Purpose: compare dataset columns to approved schema
- Expected result: dataset schema is checked against required fields

### Step 3: Validation passes or fails
- Then the validation result should pass
- Or: Then the validation result should fail
- Purpose: return a clear pass/fail outcome
- Expected result: validation result reflects actual structure status

### Step 4: Missing columns reported
- And the missing columns should be reported
- Purpose: produce actionable defect details for malformed datasets
- Expected result: list of missing columns returned

### Step 5: Extra columns flagged
- Then the validation result should flag the extra columns
- Purpose: detect unexpected schema drift
- Expected result: extra columns are listed in the result

## Acceptance Criteria Mapping
- Required columns are present -> Steps 1 and 2
- Missing columns are detected -> Step 4
- Extra columns are identified -> Step 5
- Empty or malformed datasets are rejected -> Step 3
- Validation result is returned -> Step 3

## Story
US-002: Validate Dataset Structure
