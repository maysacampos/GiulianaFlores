import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestCompra3:
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def teardown_method(self, method):
        self.driver.quit()

    def wait_for_element(self, by, value):
        return WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((by, value)))

    def test_compra3(self):
        # Passo 1: Acessar o site
        self.driver.get("https://www.giulianaflores.com.br/")
        self.driver.set_window_size(1936, 1066)

        # Passo 2: Selecionar um produto
        self.wait_for_element(By.CSS_SELECTOR, ".owl-item:nth-child(2) > a > img").click()

        # Passo 3: Inserir CEP
        self.wait_for_element(By.ID, "inputSearchAddress").send_keys("35500099")
        self.wait_for_element(By.CSS_SELECTOR, ".apply-button").click()

        # Passo 4: Selecionar endereço
        self.wait_for_element(By.CSS_SELECTOR, ".itemAddress").click()
        self.wait_for_element(By.CSS_SELECTOR, ".apply-button").click()

        # Passo 5: Verificar se o produto está correto
        product_title = self.wait_for_element(By.CSS_SELECTOR, ".item:nth-child(1) .title-item").text
        product_price = self.wait_for_element(By.CSS_SELECTOR, ".item:nth-child(1) .actual-price").text
        assert product_title == "Buquê de 12 Rosas Vermelhas"
        assert product_price == "R$ 199,90"

        # Passo 6: Adicionar produto ao carrinho
        self.wait_for_element(By.CSS_SELECTOR, ".item:nth-child(1) .title-item").click()
        self.wait_for_element(By.ID, "ContentSite_lbtBuy").click()

        # Passo 7: Confirmar dados de envio
        confirm_button = self.wait_for_element(By.ID, "btConfirmShippingData")
        assert confirm_button.text == "OK  "
        shipping_cost = self.wait_for_element(By.CSS_SELECTOR, ".vlPriceCalendar").text
        assert shipping_cost == "R$ 29,90"
        confirm_button.click()

        # Passo 8: Verificações finais
        assert self.wait_for_element(By.LINK_TEXT, "Buquê de 12 Rosas Vermelhas").text == "Buquê de 12 Rosas Vermelhas"
        assert self.wait_for_element(By.CSS_SELECTOR, ".precoPor_basket:nth-child(3)").text == "R$ 199,90"

        # Passo 9: Remover produto do carrinho
        self.wait_for_element(By.ID, "ContentSite_Basketcontrol1_rptBasket_rptBasketItems_0_lbtRemoveProduct_0").click()

        print("Teste de compra concluído com sucesso!")


