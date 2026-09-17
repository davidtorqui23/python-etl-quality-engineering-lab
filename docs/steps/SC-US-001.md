# SC-US-001

## Step Catalog

### Step 1: Source file exists
- Given an orders dataset exists
- Trigger: OrdersExtractor.validate_path()
- Expected result: the dataset path is verified and readable
- Acceptance criterion: File existence is verified

### Step 2: Dataset is loaded
- When the dataset is loaded
- Trigger: OrdersExtractor.extract()
- Expected result: the raw CSV is read into a pandas DataFrame
- Acceptance criterion: Dataset can be loaded

### Step 3: DataFrame is returned
- Then a dataframe should be returned
- Trigger: extract_orders()
- Expected result: a DataFrame object is returned
- Acceptance criterion: DataFrame is returned

### Step 4: Row count validation
- And the dataframe should contain 50 rows
- Trigger: OrdersExtractor.validate_row_count()
- Expected result: exactly 50 rows are present
- Acceptance criterion: Dataset can be loaded

### Step 5: Schema validation
- And the dataframe should contain 10 columns
- Trigger: OrdersExtractor.validate_columns()
- Expected result: all required columns are present in the expected order
- Acceptance criterion: Structure is preserved

## Acceptance Criteria to Step Mapping
- Dataset can be loaded -> Steps 2 and 4
- File existence is verified -> Step 1
- Structure is preserved -> Step 5
- DataFrame is returned -> Step 3

## Story
US-001: Load Orders Dataset