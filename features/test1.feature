Feature:User registration
  Scenario Outline: Successful user registration
    Given The user is on the registration page
    When they enter '<email>' and'<password>'
    And they click the login button

    Then they should be redirected to the facebook page
    Examples:
      | email                   |   password |
      | kishorevemula17@gmail.com| Kishore@123 |
