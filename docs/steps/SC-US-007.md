# SC-US-007

## Step Catalog

### Step 1: Dataset is available
- Given a validated dataset exists
- Purpose: confirm the dataset is ready for summary generation
- Expected result: summary logic can evaluate the records

### Step 2: Summary counts are computed
- When the summary generation function runs
- Purpose: calculate total, valid, and invalid rows
- Expected result: counts reflect actual dataset quality

### Step 3: Field-level quality counts are calculated
- Then the invalid email, invalid phone, and invalid customer ID counts are recorded
- Purpose: provide attribute-level defect visibility
- Expected result: each data quality dimension is reported

### Step 4: Summary is reviewed before load
- And the quality summary is shared before the load stage begins
- Purpose: confirm the dataset is acceptable for downstream operations
- Expected result: quality status is explicit and actionable

## Acceptance Criteria Mapping
- Total record count -> Step 2
- Valid and invalid record counts -> Step 2
- Invalid emails -> Step 3
- Invalid phone numbers -> Step 3
- Invalid customer IDs -> Step 3
- Summary available before load -> Step 4
- Logging in English -> project logging standard

## Story
US-007: Generate Data Quality Summary
