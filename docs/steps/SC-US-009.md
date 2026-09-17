# SC-US-009

## Step Catalog

### Step 1: Read raw dataset
- Given a raw dataset exists
- Purpose: load the source data into memory for ETL processing
- Expected result: dataset is available for validation and transformation

### Step 2: Validate structure and data quality
- When the schema and data quality validations run
- Purpose: ensure the dataset is structurally sound and values meet business quality rules
- Expected result: invalid rows are identified and can be excluded before transformation

### Step 3: Normalize valid records
- Then the valid rows are transformed into standardized formats
- Purpose: normalize customer data for trusted downstream use
- Expected result: consistent and clean data is prepared for summary and load

### Step 4: Generate data quality summary
- And the summary is produced before final load
- Purpose: confirm dataset quality status for downstream decision-making
- Expected result: quality counts are available and recorded

### Step 5: Load valid records into SQLite
- And the trusted subset is saved to the output database
- Purpose: make the data available for reporting and analytics
- Expected result: orders table contains only valid records

### Step 6: Log and report completion
- Then execution logs and pytest reports are generated
- Purpose: preserve evidence of ETL execution and results
- Expected result: the end-to-end run is fully documented

## Acceptance Criteria Mapping
- Read raw dataset -> Step 1
- Execute schema and quality validations -> Step 2
- Execute normalization -> Step 3
- Generate data quality summary -> Step 4
- Load valid records into SQLite -> Step 5
- Generate logs and reports -> Step 6

## Story
US-009: Execute End-To-End ETL Pipeline
