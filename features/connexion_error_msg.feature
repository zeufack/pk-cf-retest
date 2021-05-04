@chrome
Feature: Connexion Error
    In to connecting from outside of France 
    As a user
    I should have a clear error message

    Scenario: log into account
        Given navigate to carrefour web site
        When try to connet 
        Then the error message should be clear
    
