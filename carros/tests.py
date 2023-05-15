from time import sleep

from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By


def set_Up():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--icognito') 
    browser = webdriver.Chrome(options=chrome_options)
    browser.maximize_window()
        
    return browser

class MySeleniumTest(LiveServerTestCase):
        # ... continue com as interações e validações na página web
    def cadastrar(self):

        browser = set_Up()
        browser.get('http://127.0.0.1:8000/')
        browser.find_element(By.ID,'registrar').click()
        input_username = browser.find_element(By.ID,'input-username')
        input_password = browser.find_element(By.ID,'input-password')
        input_repassword = browser.find_element(By.ID,'input-repassword')
        input_username.send_keys('lelezinha')
        input_password.send_keys('soumaravilhosa')
        input_repassword.send_keys('soumaravilhosa')
        sleep(1)
        browser.find_element(By.ID,'cadastro').click()

        #------------------------------------------------------------------------------------------------------------#
    def logar(self):

        browser = set_Up()
        browser.get('http://127.0.0.1:8000/')
        button = browser.find_element(By.ID,'logar').click()
        input_user = browser.find_element(By.ID,'user')
        input_senha = browser.find_element(By.ID,'senha')
        input_user.send_keys('lulu')
        input_senha.send_keys('soulinda')
        button = browser.find_element(By.ID,'login-registrar').click()
        sleep(1)

        #------------------------------------------------------------------------------------------------------------#
    def pesquisar_anuncio(self):

        browser = set_Up()
        browser.get('http://127.0.0.1:8000/')
        button = browser.find_element(By.ID,'filtros').click()
        input_filter_brand = browser.find_element(By.ID,'filter_brand')
        input_filter_brand.send_keys('ford')
        input_filter_model = browser.find_element(By.ID,'filter_model')
        input_filter_model.send_keys('ka')

        #------------------------------------------------------------------------------------------------------------#
    def visualizar_anuncio(self):

        browser = set_Up()
        button = browser.find_element(By.ID,'logar').click()
        input_user = browser.find_element(By.ID,'user')
        input_senha = browser.find_element(By.ID,'senha')
        input_user.send_keys('lulu')
        input_senha.send_keys('soulinda')
        button = browser.find_element(By.ID,'login-registrar').click()
        sleep(1)
        browser.find_element(By.ID,'botao-meus-anuncios').click()
        sleep(1)
        #------------------------------------------------------------------------------------------------------------#

    def chat_online(self):

        browser = set_Up()
        input_search = browser.find_element(By.ID,'search')
        input_search.send_keys('ka')
        sleep(1)
        button = browser.find_element(By.ID,'confirm-search').click()
        button = browser.find_element(By.ID,'descricao-carro').click()
        button = browser.find_element(By.ID,'botao_entrar_contato').click()
        #------------------------------------------------------------------------------------------------------------#

    def criar_anuncio(self):
        
        browser = set_Up()
        button = browser.find_element(By.ID,'logar').click()
        input_user = browser.find_element(By.ID,'user')
        input_senha = browser.find_element(By.ID,'senha')
        input_user.send_keys('lulu')
        input_senha.send_keys('soulinda')
        button = browser.find_element(By.ID,'login-registrar').click()
        sleep(1)

        browser.get('http://127.0.0.1:8000/')
        browser.find_element(By.ID,'criar-anuncios').click()
        sleep(1)
        input_marca = browser.find_element(By.ID,'id_brand')
        input_model = browser.find_element(By.ID,'id_car_model')
        input_km = browser.find_element(By.ID,'id_mileage')
        input_ano = browser.find_element(By.ID,'id_year')
        input_combustivel = browser.find_element(By.ID,'id_fuel_type')
        input_estado = browser.find_element(By.ID,'id_type')
        input_price = browser.find_element(By.ID,'id_price')
        input_color = browser.find_element(By.ID,'id_color')
        input_image = browser.find_element(By.ID, 'id_image')   
        input_descricao = browser.find_element(By.ID,'id_description') 
       
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
        browser.find_element(By.ID,'botao-criar-produto').click()    
        sleep(1)
        
        #ENTRANDO NOS MEUS ANUNCIOS
        browser.find_element(By.ID,'botao-meus-anuncios').click()
        #------------------------------------------------------------------------------------------------------------#

    def deleter_anuncio(self):

        browser = set_Up()
        button = browser.find_element(By.ID,'logar').click()
        input_user = browser.find_element(By.ID,'user')
        input_senha = browser.find_element(By.ID,'senha')
        input_user.send_keys('lulu')
        input_senha.send_keys('soulinda')
        button = browser.find_element(By.ID,'login-registrar').click()
        sleep(1)
        
        browser.get('http://127.0.0.1:8000/')
        browser.find_element(By.ID,'botao-meus-anuncios').click()
        browser.find_element(By.ID,'delete_my_ads').click()
        browser.find_element(By.ID,'confirm_delete').click()
        #------------------------------------------------------------------------------------------------------------#

    # def tearDown(self):
    #     browser = set_Up()
    #     selenium.quit()
    #     super().tearDown()