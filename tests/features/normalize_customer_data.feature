Feature: Normalize Customer Data

  As a Data Quality Engineer
  I want customer data to be normalized
  So that downstream ETL processes consume standardized and consistent information

  Scenario: Valid customer values are preserved after normalization
    Given a dataset with customer records exists
    When the normalized output is generated
    Then the string values should be trimmed
    And the email addresses should be lowercase
    And the phone values should be digits only

  Scenario: Country aliases are standardized
    Given a dataset with country aliases such as CO and USA exists
    When the dataset is normalized
    Then the country values should be converted to Colombia and United States

  Scenario: Normalized output is saved to the processed directory
    Given a valid raw orders dataset exists
    When the normalization process runs
    Then the processed file should be created at data/processed/orders_normalized.csv
