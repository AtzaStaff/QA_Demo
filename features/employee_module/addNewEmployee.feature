Feature: Employees Module
  Background:
    Given Open StaffWizard
    Then  Login

  Scenario: Adding a new employee
    Given   Navigate across the panel until Add new employee forms
    Then    Validate that the Unique ID field is not empty
    Then    Entering the First name
    # Then    Entering the Middle name
    Then    Entering the Last name
    Then    Select the country
    Then    Entering the address
    Then    Entering the PO Box
    Then    Entering the second address
    Then    Validate that the State is the one enetered in Address field
    Then    Validate that the City is the one enetered in Address field
    Then    Validate that the Zip Code is the one enetered in Address field
    Then    Entering the Mobile Phone
    Then    Entering the Personal Email
    Then    Entering the Date of Birth
    Then    Selecting the Race and Ethnicity
    Then    Entering the Social Secutiry Number
    Then    Selecting the Region
    Then    Selecting the Branch
    Then    Selecting the Pay Type
    Then    Selecting the Employee Status
    Then    Entering the Hire Date
    Then    Entering the Join Date
    Then    Click on the "Add Employee" button
    Then    Validate the successful addition
