# SC-US-006

## Step Catalog

### Step 1: Source dataset is loaded
- Given a raw orders dataset exists
- Purpose: prepare the source data for customer normalization
- Expected result: normalized transformation can operate on the dataset

### Step 2: Field normalization is applied
- When the customer data normalization logic runs
- Purpose: trim strings, lowercase emails, standardize countries, and strip phone formatting
- Expected result: all required fields are normalized consistently

### Step 3: Validation checks confirm output quality
- Then the normalized data should preserve business values
- Purpose: confirm the transformation is accurate and consistent
- Expected result: normalized output is valid and ready for downstream ETL use

### Step 4: Processed file is produced
- And the output dataset is written to data/processed/orders_normalized.csv
- Purpose: persist the normalized artifact for downstream consumers
- Expected result: output file is generated successfully

## Acceptance Criteria Mapping
- Trim string values -> Step 2
- Convert email addresses to lowercase -> Step 2
- Standardize country values -> Step 2
- Remove spaces and special formatting from phone numbers -> Step 2
- Preserve original data integrity -> Step 3
- Generate normalized dataset -> Step 4

## Story
US-006: Normalize Customer Data
