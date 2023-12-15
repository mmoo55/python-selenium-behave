#@fixture.setup.testbase
Feature: Prueba

  @demo
  Scenario: Login

    Given Im on the webpage
    When I enter valid credentials
    Then I can see the whole page