@chrome
Feature:#581: Type Promotion
    In order to buy a promotional item
    I want the the price must to be in accordance with the reduction 

    Scenario: Apply promotion type
        Given Savigate to carrefour market and login to account
        When Select the article "landons fumés"
        Then the total amount to be paid should be "5.28"
    
    