Feature: Validate Registration functionality

Scenario: Navigation to Facebook
Given Navigates to Facebook
When  User enters username
When  User enters password
And   User clicks on Login button
Then  User logged into Facebook

Scenario Outline:  Test End to end registration
Given  User is on login page
When   User enters "<site>"
When   User enters usernama
And    User enters passeord
Examples:
  |site                   |
  |https://www.google.com/|
  |https://www.amazon.com/|

