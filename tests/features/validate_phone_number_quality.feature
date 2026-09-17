Feature: Validate Phone Number Quality

  As a Data Quality Engineer
  I want to validate phone numbers
  So that invalid customer contact information is detected before downstream processing

  Scenario: Valid phone numbers pass validation
    Given a dataset with valid phone numbers exists
    When phone number quality is validated
    Then the validation result should pass

  Scenario: Invalid phone formats fail validation
    Given a dataset with malformed phone numbers exists
    When phone number quality is validated
    Then the validation result should fail
    And the invalid phone rows should be reported

  Scenario: Blank phone values fail validation
    Given a dataset with blank phone values exists
    When phone number quality is validated
    Then the validation result should fail
    And the blank phone rows should be reported
