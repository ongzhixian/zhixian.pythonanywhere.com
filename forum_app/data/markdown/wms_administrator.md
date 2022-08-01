# WMS Aministrator

Feature: Application Menu

 Background:
    Given user has role "WMS administrator"

  Scenario: WMS administrator should have "WMS" application menu item
    When user open the application menu
    Then user should have "WMS" menu item

Feature: WMS Menu

 Background:
    Given user has role "WMS administrator"

  Scenario: WMS administrator should have "Supplier" WMS menu item
    When user open the WMS menu
    Then user should have "Supplier" menu item

  Scenario: WMS administrator should have "Customer" WMS menu item
    When user open the WMS menu
    Then user should have "Customer" menu item

  Scenario: WMS administrator should have "Location" WMS menu item
    When user open the WMS menu
    Then user should have "Logion" menu item


Feature: WMS Supplier List
  Only users with "WMS supplier" role should be able to manage supplier list

  Background:
    Given user has role "WMS supplier"

  Scenario: WMS supplier should be able to see supplier list
    When user click on "Supplier" menu item on WMS menu
    Then user should see supplier list

  Scenario: WMS administrator should be able to add supplier
    When user click on "Supplier" menu item on WMS menu
    Then user should see supplier list

  Scenario: WMS administrator should be able to update supplier information
    When user click on "Supplier" menu item on WMS menu
    Then user should see supplier list