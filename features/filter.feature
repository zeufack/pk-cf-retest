Feature: Top Filter
    In order to sort product 
    As a ascending order by price
    I want ascending order by price

    Scenario: sort product by clicking on filter button
        Given i navigate to carrefour bio website
        When i select Prix(croissant)filter
        Then the product list shoul be sorted
    
    