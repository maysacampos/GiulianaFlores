Feature: Criar usuario

  Scenario: Criar usuario
    Given que acesso o site Blaze Demo em Register
    When preencho os campos de name Lavinia e company Teste
    When preencho os campos de login com usuario lavinia_aurora_alves@eton.com.br e senha nCRh8ypPS3bKG@8
    When preencho o campo de confirm password com nCRh8ypPS3bKG@8
    Then clicar em Register
   