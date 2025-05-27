# Feature declaration for validating login functionality of the Zen Portal
Feature: ZEN PORTAL Login Validation 

  # Scenario 1: Checks successful login with valid credentials and logout
  Scenario: 1 Successful login and logout with valid credentials
    # Step to navigate to the login page
    Given I am on the login page
    # Step to enter valid username and password
    When I enter valid username and password
    # Step to click on the login button
    And I click the login button
    # Step to verify successful redirection to dashboard
    Then I should be redirected to the dashboard
    # Step to log out from the dashboard
    When I logout from the application
    # Step to ensure the user is redirected back to the login page
    Then I should see the login page again

  # Scenario Outline 2: Validates login failure with invalid credentials using example values
  Scenario Outline: 2 Unsuccessful login with invalid credentials
    # Step to open the login page
    Given I am on the login page
    # Step to enter parameterized invalid credentials
    When I enter invalid username "<wronguser>" and password "<wrongpass>"
    # Step to attempt login with the provided invalid credentials
    When I click the login button
    # Step to verify that an error message is displayed
    Then I should see an error message

    # Examples table providing values for the placeholders used in the scenario outline above
    Examples:
      | wronguser             | wrongpass |
      | wronguser@email.com  | wrong123  |

  # Scenario 3: Ensures that login form elements are enabled and ready for user interaction
  Scenario: 3 Username, password fields and login button should be enabled
    # Step to visit the login page
    Given I am on the login page
    # Step to check that the username field is enabled
    Then The username field should be enabled
    # Step to check that the password field is enabled
    And The password field should be enabled
    # Step to ensure the login button is clickable
    And The login button should be clickable

  # Scenario 4: Verifies login button becomes clickable once credentials are entered
  Scenario: 4 Login button should be clickable after entering credentials
    # Step to load the login page
    Given I am on the login page
    # Step to input valid credentials
    When I enter valid username and password
    # Step to ensure that login button becomes clickable after input
    Then The login button should be clickable
