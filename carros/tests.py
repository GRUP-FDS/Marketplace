from time import sleep

from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


class MySeleniumTest(LiveServerTestCase):
    
    chrome_options = Options()
    chrome_options.add_argument("--remote-debugging-port=8000") 
    browser = webdriver.Chrome(options=chrome_options)
    browser.maximize_window()
        # ... continue com as interações e validações na página web
    def test_cadastro(self):
        self.browser.get('http://127.0.0.1:8000/')
        sleep(9)
        
        #LOGAR
        button = self.browser.find_element(By.ID,'logar').click()
        sleep(9)

        input_user = self.browser.find_element(By.ID,'user')
        input_senha = self.browser.find_element(By.ID,'senha')
        input_user.send_keys('lulu')
        input_senha.send_keys('soulinda')
        button = self.browser.find_element(By.ID,'login-registrar').click()
        sleep(3)

        #PESQUISANDO
        input_search = self.browser.find_element(By.ID,'search')
        input_search.send_keys('ka')
        button = self.browser.find_element(By.ID,'confirm-search').click()
        sleep(3)

        #button = self.browser.find_element(By.ID,'carcar').click()
        button = self.browser.find_element(By.ID,'home').click()
        
        #TESTE PARA DELETAR ANÚNCIO
        button = self.browser.find_element(By.ID,'logar')
        button.click()
        sleep(1)
        button = self.browser.find_element(By.ID,'registrar')
        button.click()
        sleep(1)
        input_username = self.browser.find_element(By.ID,'input-username')
        input_password = self.browser.find_element(By.ID,'input-password')
        input_repassword = self.browser.find_element(By.ID,'input-repassword')
        input_username.send_keys('luluzinha2')
        input_password.send_keys('soulindalinda2')
        input_repassword.send_keys('soulindalinda2')
        sleep(1)
        self.browser.find_element(By.ID,'cadastro').click()
        self.browser.find_element(By.ID,'criar-anuncios').click()
        sleep(1)

        input_title = self.browser.find_element(By.ID,'id_title')
        input_description = self.browser.find_element(By.ID,'id_description')
        input_price = self.browser.find_element(By.ID,'id_price')
        input_image = self.browser.find_element(By.ID,'id_image')
        input_title.send_keys('Produto de Teste')
        input_description.send_keys('Este é um produto de teste')
        input_price.send_keys('10.99')
        input_image.send_keys('C:\caminho\para\imagem.jpg')
        sleep(1)
        
        self.browser.find_element(By.ID,'botao-criar-produto').click()
        sleep(1)
        
        #BOTÃO SAIR
        self.browser.find_element(By.ID,'sairlogout').click()

    def tearDown(self):
        self.selenium.quit()
        super().tearDown()


