Feature: Load Valid Records To SQLite

  As a Data Quality Engineer
  I want valid records to be loaded into SQLite
  So that downstream analytics and reporting can consume trusted data

  Scenario: Only valid records are inserted
    Given a dataset with valid and invalid records exists
    When the SQLite load operation runs
    Then the valid records should be inserted into the orders table
    And the invalid records should be rejected

  Scenario: Load statistics are recorded
    Given a dataset is ready for load
    When the load completes
    Then the inserted row count should be reported
    And the rejected row count should be reported

  Scenario: Load execution is logged
    Given the SQLite load runs
    When the execution completes
    Then the log should record the start and completion in English
