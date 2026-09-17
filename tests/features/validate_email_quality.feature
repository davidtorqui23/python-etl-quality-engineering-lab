Feature: Validate Email Quality

  As a Data Quality Engineer
  I want to validate email addresses
  So that malformed email values are rejected before downstream processing

  Scenario: Valid emails pass validation
    Given a dataset with valid email addresses exists
    When email quality is validated
    Then the validation result should pass

  Scenario: Invalid email format fails validation
    Given a dataset with malformed email addresses exists
    When email quality is validated
    Then the validation result should fail
    And the invalid email rows should be reported

  Scenario: Blank email values fail validation
    Given a dataset with blank email values exists
    When email quality is validated
    Then the validation result should fail
    And the blank email rows should be reported
