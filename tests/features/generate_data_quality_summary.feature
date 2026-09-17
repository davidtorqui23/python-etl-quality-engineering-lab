Feature: Generate Data Quality Summary

  As a Data Quality Engineer
  I want a quality summary report
  So that I can understand the quality of the processed dataset before load operations

  Scenario: Summary counts valid and invalid records
    Given a validated dataset is available
    When a quality summary is generated
    Then the total records should be reported
    And the valid records should be reported
    And the invalid records should be reported

  Scenario: Summary counts invalid value categories
    Given a dataset contains invalid emails, phone numbers, and customer IDs
    When a quality summary is generated
    Then the invalid email count should be reported
    And the invalid phone number count should be reported
    And the invalid customer ID count should be reported

  Scenario: Summary is generated before load operations
    Given a processed dataset is ready for loading
    When the load process is preparing
    Then the data quality summary should be available
