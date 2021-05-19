@chrome
Feature: Translation Error

    Scenario: Translate code in carrefour drive section
        Given you are on carrefour landing page
        When you scroll down to drive section
        Then you should have femmes enceintes instead of common.pregnant-women
    
    
    