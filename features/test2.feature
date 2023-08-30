Feature:User registration
  Background: Read the data from data driven
    testdata=read("testdata.csv")
  Scenario Outline: Successful user registration
    Given The user is on the registration page
    When they enter '<email>' and'<password>'
    And they click the login button

    Then they should be redirected to the facebook page
    Examples:
        | testdata |