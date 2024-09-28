# 1 - Bibliotecas / Imports
import time
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given(u'que acesso o site Blaze Demo em Register')
def step_impl(context):
    context.driver = webdriver.Chrome()  # Inicializa o driver do Chrome
    context.driver.get("https://blazedemo.com/register")  # Acessa o site
    context.driver.implicitly_wait(10)

@when(u'preencho os campos de name {name} e company {company}')
def step_impl(context, name, company):
    context.driver.find_element(By.ID, "name").send_keys(name)  # Verifique o nome correto do campo
    context.driver.find_element(By.ID, "company").send_keys(company)  # Verifique o nome correto do campo

@when(u'preencho os campos de login com usuario {usuario} e senha {senha}')
def step_impl(context, usuario, senha):
    context.driver.find_element(By.ID, "email").send_keys(usuario)  # Verifique o nome correto do campo
    context.driver.find_element(By.ID, "password").send_keys(senha)  # Verifique o nome correto do campo

@when(u'preencho o campo de confirm password com {senha}')
def step_impl(context, senha):
    context.driver.find_element(By.ID, "password-confirm").send_keys(senha)  # Verifique o nome correto do campo

@then(u'clicar em Register')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()          # clicar no botão Register
    
def after_all(context):
    context.driver.quit()  # Fecha o navegador ao final do teste


