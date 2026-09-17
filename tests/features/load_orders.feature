Feature: Load Orders Dataset

  As a Data Quality Engineer
  I want to load orders data
  So that I can validate incoming records

  Scenario: Load valid dataset

    Given an orders dataset exists

    When the dataset is loaded

    Then a dataframe should be returned

    And the dataframe should contain 50 rows

    And the dataframe should contain 10 columns