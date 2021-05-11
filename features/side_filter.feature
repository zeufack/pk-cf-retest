@chrome
Feature:#573: Side Filter
    In order to to sort product by sidenav check box criteria
    As a user
    I want the page not scroll to top

    Scenario: select side nav filter
        Given navigate to carrefour bio website sidenav
        When select the sidenav filter
        Then the page shoul not scroll to top
    
    