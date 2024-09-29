# 1 - Bibliotecas / Imports
import time
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given(u'que acesso o site Blaze Demo')
def step_impl(context):
    context.driver = webdriver.Chrome()  # Inicializa o driver do Chrome
    context.driver.get("https://blazedemo.com/")  # Acessa o site
    context.driver.implicitly_wait(10)
    
@when(u'que seleciono {city} em Choose your departure city')
def step_impl(context, city):
    context.driver.find_element(By.NAME, "fromPort").click()  
    context.driver.implicitly_wait(10)        

@when(u'que seleciono {city} em Choose your destination city')
def step_impl(context, city):
    context.driver.find_element(By.NAME, "toPort").click() 
    context.driver.implicitly_wait(10)  

@then('clicar em Find Flights')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, 'input[type="submit"].btn.btn-primary').click()
    context.driver.implicitly_wait(10)  

@when('que clico na primeira passagem que aparece em Cloose This Flight')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "input[type='submit'].btn.btn-small").click()
    context.driver.implicitly_wait(15)  

@when(u'que preencho os seguintes campos')
def step_impl(context):
    # Acessa a tabela de dados do cenário
    for row in context.table:
        campo = row['campo']
        valor = row['valor']
        
        # Preenche os campos com base no nome
        if campo == "Name":
            context.driver.find_element(By.ID, "inputName").send_keys(valor)
        elif campo == "Adress":  # Corrigido para "Address" se necessário
            context.driver.find_element(By.ID, "address").send_keys(valor)
        elif campo == "City":
            context.driver.find_element(By.ID, "city").send_keys(valor)
        elif campo == "State":
            context.driver.find_element(By.ID, "state").send_keys(valor)
        elif campo == "Zip Code":
            context.driver.find_element(By.ID, "zipCode").send_keys(valor)
        elif campo == "Card Type":
            context.driver.find_element(By.ID, "cardType").send_keys(valor)
        elif campo == "Credit Card Number":
            context.driver.find_element(By.ID, "creditCardNumber").send_keys(valor)
        elif campo == "Month":
            context.driver.find_element(By.ID, "creditCardMonth").send_keys(valor)
        elif campo == "Year":
            context.driver.find_element(By.ID, "creditCardYear").send_keys(valor)
        elif campo == "Name on Card":
            context.driver.find_element(By.ID, "nameOnCard").send_keys(valor)


@then(u'clicar em Purchase Flight')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()          # clicar no botão 
    
def after_all(context):
    context.driver.quit()  # Fecha o navegador ao final do teste


