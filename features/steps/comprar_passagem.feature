Feature: Comprar Passagem

  Scenario: Comprar Passagem
    Given que acesso o site Blaze Demo 
    When que seleciono Boston em Choose your departure city
    When que seleciono Rome em Choose your destination city
    Then clicar em Find Flights
    When que clico na primeira passagem que aparece em Cloose This Flight
    When que preencho os seguintes campos:
      | campo               | valor                    |
      | Name                | Lavinia                  |
      | Adress              | 123 Av. Souza            |
      | City                | Rio de Janeiro           |
      | State               | Rio de Janeiro           |
      | Zip Code            | 35500099                 |
      | Card Type           | Visa                     |
      | Credit Card Number  | 123443211234             |
      | Month               | 12                       |
      | Year                | 2017                     |
      | Name on Card        | Lavinia Aurora           |
    Then clicar em Purchase Flight
