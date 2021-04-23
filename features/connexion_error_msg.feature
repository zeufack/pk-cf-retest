Feature: Connexion Error
    In to connecting from outside of France 
    As a user
    I clear error message

    Scenario: log into account
        Given navigate to carrefour web site
        When try to connet 
        Then the error message shoul be clear
    
