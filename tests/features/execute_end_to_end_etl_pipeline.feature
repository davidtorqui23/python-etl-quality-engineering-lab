Feature: Execute End-To-End ETL Pipeline

  As a Data Quality Engineer
  I want to execute the complete ETL process
  So that raw data can be transformed into trusted and loaded data through an automated pipeline

  Scenario: ETL pipeline loads valid records and rejects invalid rows
    Given a raw dataset is available
    When the ETL pipeline runs
    Then the dataset is validated
    And the valid records are normalized
    And the data quality summary is generated
    And the valid records are loaded into SQLite

  Scenario: ETL pipeline logs each stage
    Given the ETL pipeline executes
    When each stage completes
    Then the log should contain the stage information in English

  Scenario: ETL pipeline is regression tested
    Given the project test suite runs
    Then all end-to-end and validation tests should pass
