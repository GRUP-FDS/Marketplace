from time import sleep

from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By


class MySeleniumTest(LiveServerTestCase):
    
    
    browser = webdriver.Chrome()
    browser.maximize_window()
        # ... continue com as interações e validações na página web
    def test_cadastro(self):
        self.browser.get('http://127.0.0.1:8000/')
        sleep(9)
        
        #LOGAR
        button = self.browser.find_element(By.ID,'logar').click()
        sleep(1)

        input_user = self.browser.find_element(By.ID,'user')
        input_senha = self.browser.find_element(By.ID,'senha')
        input_user.send_keys('lulu')
        input_senha.send_keys('soulinda')
        button = self.browser.find_element(By.ID,'login-registrar').click()
        sleep(3)


        #PESQUISANDO CARRO E VER DETALHES
        input_search = self.browser.find_element(By.ID,'search')
        input_search.send_keys('ka')
        button = self.browser.find_element(By.ID,'confirm-search').click()
        button = self.browser.find_element(By.ID, 'descricao-carro').click()
        sleep(3)

        #CRIANDO ANUNCIO 
        button = self.browser.find_element(By.ID,'home').click()
        #COLOCANDO DADOS DO ANUNCIO 
        self.browser.find_element(By.ID,'criar-anuncios').click()
        input_marca = self.browser.find_element(By.ID,'id_brand')
        input_model = self.browser.find_element(By.ID,'id_car_model')
        input_km = self.browser.find_element(By.ID,'id_mileage')
        input_ano = self.browser.find_element(By.ID,'id_year')
        input_combustivel = self.browser.find_element(By.ID,'id_fuel_type')
        input_estado = self.browser.find_element(By.ID,'id_type')
        input_price = self.browser.find_element(By.ID,'id_price')
        input_color = self.browser.find_element(By.ID,'id_color')
        input_image = self.browser.find_element(By.ID, 'id_image')
        input_descricao = self.browser.find_element(By.ID,'id_description') 
       

        
        #preenchendo campos
        input_marca.send_keys('Produto de Teste')
        input_model.send_keys('Este é um produto de teste')
        input_km.send_keys('10')
        input_ano.send_keys('2023')
        input_combustivel.send_keys('2023')
        input_estado.send_keys('2023')
        input_price.send_keys('2023')
        input_color.send_keys('2023')
        #input_image.send_keys('image.padrao')
        input_descricao.send_keys('jsjshjshsjhjk')
        self.browser.find_element(By.ID,'botao-criar-produto').click()    
        sleep(1)
        
        #ENTRANDO NOS MEUS ANUNCIOS
        self.browser.find_element(By.ID,'botao-meus-anuncios').click()

        #ENTRANDO NA DESCRICAO DOS MEUS ANUNCIOS
        self.browser.find_element(By.ID,'descricao_my_ads').click()
        self.browser.find_element(By.ID,'botao-meus-anuncios').click()
        sleep(1)
        #DEELETANDO ANUNCIO
        self.browser.find_element(By.ID,'delete_my_ads').click()
        self.browser.find_element(By.ID,'cancel_delete').click()
        self.browser.find_element(By.ID,'delete_my_ads').click()
        self.browser.find_element(By.ID,'confirm_delete').click()
        button = self.browser.find_element(By.ID,'home').click()
        sleep(1)

        #BOTÃO SAIR
        self.browser.find_element(By.ID,'sairlogout').click()



        
        




    def tearDown(self):
        self.selenium.quit()
        super().tearDown()


