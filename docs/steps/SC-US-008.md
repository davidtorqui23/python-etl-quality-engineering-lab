# SC-US-008

## Step Catalog

### Step 1: Database is prepared
- Given the target SQLite database path is available
- Purpose: ensure the data/output location exists before the insert begins
- Expected result: the database can be created and opened safely

### Step 2: Valid rows are identified
- When the dataset is checked against business rules
- Purpose: exclude invalid customer IDs, invalid emails, and invalid phone numbers
- Expected result: only valid rows remain for insertion

### Step 3: Database load is executed
- Then the valid records are inserted into the orders table
- Purpose: load trusted data into SQLite for downstream consumption
- Expected result: inserted row count reflects the valid dataset records

### Step 4: Rejected and reported records are captured
- And the rejected record count is returned with execution statistics
- Purpose: provide measurable data quality information for downstream operations
- Expected result: summary statistics show both inserted and rejected counts

## Acceptance Criteria Mapping
- Create SQLite database -> Step 1
- Create orders table -> Step 1
- Load only valid records -> Step 2 and Step 3
- Reject invalid records -> Step 2 and Step 4
- Validate inserted row count -> Step 3
- Generate load statistics -> Step 4
- Log execution -> project logging standard

## Story
US-008: Load Valid Records To SQLite
