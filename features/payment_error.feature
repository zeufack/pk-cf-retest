@proxy
Feature: Add payment method
    In order to add a payment method 

    Scenario: There is a payment method input
        Given you are connect on carrefour market and you are log in to your account
        When navigate to payment method
        Then you should have an input for payment method
    
    