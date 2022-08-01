# WMS Supplier


    
    
Feature: Application Menu
  Only users with WMS-related roles should have WMS menu item in application menu.

  Background:
    Given user has role "WMS supplier"

  Scenario: WMS supplier should have "WMS" application menu item
    When user open the application menu
    Then user should have "WMS" menu item


Feature: WMS Menu
  Only users with "WMS supplier" role should see "Supplier" WMS menu item in WMS menu.

 Background:
    Given user has role "WMS supplier"

  Scenario: WMS supplier should have "Supplier" WMS menu item
    When user open the WMS menu
    Then user should have "Supplier" menu item


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