Feature: Validate Dataset Structure

  As a Data Quality Engineer
  I want to validate dataset structure
  So that malformed datasets are rejected before processing

  Scenario: Valid dataset passes structure validation
    Given a dataset with the expected columns exists
    When the dataset structure is validated
    Then the validation result should pass
    And the required schema should be confirmed

  Scenario: Missing required columns fails validation
    Given a dataset with missing required columns exists
    When the dataset structure is validated
    Then the validation result should fail
    And the missing columns should be reported

  Scenario: Extra columns are identified
    Given a dataset with unexpected additional columns exists
    When the dataset structure is validated
    Then the validation result should flag the extra columns
