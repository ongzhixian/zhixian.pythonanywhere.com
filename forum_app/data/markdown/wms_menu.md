# WMS Menu

Feature: WMS Menu

  # Without premises
  Scenario: When WMS administrator logs in
    When "WMS administrator" logs in to application
    Then application menu should have "WMS" menu item

  # With premises
  Scenario: When WMS administrator logs in
    Given user has role "WMS administrator"
    When user open the application menu
    Then user should have "WMS" menu item