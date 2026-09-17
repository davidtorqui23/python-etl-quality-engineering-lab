Feature: Validate Customer ID Quality

  As a Data Quality Engineer
  I want to validate customer IDs
  So that malformed identifiers are rejected before downstream processing

  Scenario: Valid customer IDs pass validation
    Given a dataset with valid customer IDs exists
    When customer ID quality is validated
    Then the validation result should pass

  Scenario: Non-numeric customer IDs fail validation
    Given a dataset with customer IDs containing letters exists
    When customer ID quality is validated
    Then the validation result should fail
    And the invalid customer ID rows should be reported

  Scenario: Empty or missing customer IDs fail validation
    Given a dataset with blank or missing customer IDs exists
    When customer ID quality is validated
    Then the validation result should fail
    And the blank customer ID rows should be reported
