from time import sleep

from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def setUp():
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--icognito') 
        browser = webdriver.Chrome(options=chrome_options)
        browser.maximize_window()
        return browser   
#teste

class MySeleniumTest(LiveServerTestCase):
        # ... continue com as interações e validações na página web
    def test_cadastrar(self):

        browser = setUp()
        browser.get('http://127.0.0.1:8000/')
        browser.find_element(By.ID,'logar').click()
        browser.find_element(By.ID,'registrar').click()
        input_username = browser.find_element(By.ID,'input-username')
        input_password = browser.find_element(By.ID,'input-password')
        input_repassword = browser.find_element(By.ID,'input-repassword')
        input_username.send_keys('brunaamademais')
        input_password.send_keys('blackthigas')
        input_repassword.send_keys('blackthigas')
        sleep(3)
        browser.find_element(By.ID,'cadastro').click()

        botao_sair = browser.find_element(By.ID,'sairlogout')
        assert botao_sair.text == "Sair"

        #------------------------------------------------------------------------------------------------------------#
    def test_logar(self):
        sleep(3)
        browser = setUp()
        browser.get('http://127.0.0.1:8000/')
        browser.find_element(By.ID,'logar').click()
        input_user = browser.find_element(By.ID,'user')
        input_senha = browser.find_element(By.ID,'senha')
        input_user.send_keys('BrunaCarvalho')
        sleep(3)
        input_senha.send_keys('bruna123')
        browser.find_element(By.ID,'login-registrar').click()
        sleep(3)

        botao_sair = browser.find_element(By.ID,'sairlogout')
        assert botao_sair.text == "Sair"
        #------------------------------------------------------------------------------------------------------------#
    def test_criar_anuncio(self):
        
        browser = setUp()
        browser.get('http://127.0.0.1:8000/')
        sleep(3)
        browser.find_element(By.ID,'logar').click()
        input_user = browser.find_element(By.ID,'user')
        input_senha = browser.find_element(By.ID,'senha')
        input_user.send_keys('BruncaCarvalho')
        input_senha.send_keys('bruna123')
        browser.find_element(By.ID,'login-registrar').click()
        sleep(3)

        
        browser.find_element(By.ID,'criar-anuncios').click()
        sleep(3)
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
        sleep(3)
        
        #ENTRANDO NOS MEUS ANUNCIOS
        browser.find_element(By.ID,'botao-meus-anuncios').click()
        sleep(3)

        meus_anuncios_exemplo = browser.find_element(By.ID,'anuncio_exemplo')
        print(meus_anuncios_exemplo)
        assert meus_anuncios_exemplo.text == "Este é um produto de teste"
        #------------------------------------------------------------------------------------------------------------#


    def test_pesquisar_anuncio(self):
        sleep(3)
        browser = setUp()
        browser.get('http://127.0.0.1:8000/')
        browser.find_element(By.ID,'filtros').click()
        input_filter_brand = browser.find_element(By.ID,'filter_brand')
        input_filter_brand.send_keys('ford')
        input_filter_model = browser.find_element(By.ID,'filter-model')
        input_filter_model.send_keys('ka')
        browser.find_element(By.ID,'botao_filtrar').click()
        sleep(3)

        carro_exemplo = browser.find_element(By.ID,'nome_carro')
        assert carro_exemplo.text == "FORD KA"
 
        #------------------------------------------------------------------------------------------------------------#
    def test_visualizar_anuncio(self):
        sleep(3)
        browser = setUp()
        browser.get('http://127.0.0.1:8000/')
        browser.find_element(By.ID,'logar').click()
        input_user = browser.find_element(By.ID,'user')
        input_senha = browser.find_element(By.ID,'senha')
        input_user.send_keys('BrunaCarvalho')
        input_senha.send_keys('bruna123')
        browser.find_element(By.ID,'login-registrar').click()
        browser.find_element(By.ID,'botao-meus-anuncios').click()
        sleep(3)

        meus_anuncios = browser.find_element(By.ID,'confirmar_anuncio')
        assert meus_anuncios.text == "Meus anúncios"
        #------------------------------------------------------------------------------------------------------------#

    def test_chat_online(self):

        browser = setUp()
        browser.get('http://127.0.0.1:8000/')
        sleep(3)
        browser.find_element(By.ID,'logar').click()
        input_user = browser.find_element(By.ID,'user')
        input_senha = browser.find_element(By.ID,'senha')
        input_user.send_keys('BrunaCarvalho')
        input_senha.send_keys('bruna123')
        browser.find_element(By.ID,'login-registrar').click()
        browser.find_element(By.ID,'home').click()
        sleep(3)

        input_search = browser.find_element(By.ID,'search')
        input_search.send_keys('ka')
        sleep(3)
        browser.find_element(By.ID,'confirm-search').click()
        browser.find_element(By.ID,'descricao-carro').click()
        browser.find_element(By.ID,'botao_entrar_contato').click()
        sleep(3)
        input_masseges = browser.find_element(By.ID,'chat-message-input')
        input_masseges.send_keys('Olá, estou interessado no seu carro')
        sleep(2)
        browser.find_element(By.ID,'chat-message-submit').click()
        sleep(3)

        mensagem = browser.find_element(By.ID,'mensagem_exemplo')
        assert mensagem.text == "Olá, estou interessado no seu carro"
        #------------------------------------------------------------------------------------------------------------#

    
    def test_deleter_anuncio(self):
        
        browser = setUp() 
        browser.get('http://127.0.0.1:8000/')
        browser.find_element(By.ID,'logar').click()
        input_user = browser.find_element(By.ID,'user')
        input_senha = browser.find_element(By.ID,'senha')
        input_user.send_keys('BrunaCarvalho')
        input_senha.send_keys('bruna123')
        browser.find_element(By.ID,'login-registrar').click()
        sleep(3)
        
        browser.find_element(By.ID,'criar-anuncios').click()
        sleep(3)
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
        sleep(3)

        browser.find_element(By.ID,'botao-meus-anuncios').click()
        sleep(2)

        browser.find_element(By.ID,'delete_my_ads').click()
        sleep(2)
        browser.find_element(By.ID,'confirm_delete').click()
        sleep(2)


        mensagem_sem_anuncio = browser.find_element(By.ID,'mensagem_sem_anuncio')
        assert mensagem_sem_anuncio.text == "Você ainda não tem nenhum anúncio. Crie um agora."

    #     #------------------------------------------------------------------------------------------------------------#
    def test_anuncio_vendido(self):

         browser = setUp()
         browser.get('http://127.0.0.1:8000/')
         sleep(3)
         browser.find_element(By.ID,'logar').click()
         input_user = browser.find_element(By.ID,'user')
         input_senha = browser.find_element(By.ID,'senha')
         input_user.send_keys('antoniosilva')
         input_senha.send_keys('mochimochi')
         browser.find_element(By.ID,'login-registrar').click()
         sleep(3)

        
         browser.find_element(By.ID,'criar-anuncios').click()
         sleep(3)
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
         sleep(2) 
      
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
         sleep(3)
       
         #ENTRANDO NOS MEUS ANUNCIOS
         browser.find_element(By.ID,'botao-meus-anuncios').click()
         sleep(3)
         browser.find_element(By.ID,'descricao_my_ads').click()
         browser.find_element(By.ID,'marcar_vendido').click()
         sleep(2)

         mensagem_anuncio_vendido = browser.find_element(By.ID,'vendido')
         assert mensagem_anuncio_vendido.text == 'Vendido'


    #     #------------------------------------------------------------------------------------------------------------#
    def test_atualizar_produto(self): 
         browser = setUp()
         browser.get('http://127.0.0.1:8000/')
         browser.find_element(By.ID,'logar').click()
         input_user = browser.find_element(By.ID,'user')
         input_senha = browser.find_element(By.ID,'senha')
         input_user.send_keys('brunaamamuito')
         input_senha.send_keys('thiagopreto')
         browser.find_element(By.ID,'login-registrar').click()
         sleep(3)
        
         browser.find_element(By.ID,'botao-meus-anuncios').click()
         browser.find_element(By.ID,'atualizar_my_ads').click() #id do botao "atualizar"

         #atualizando os campos do anuncio
         input_descricao = browser.find_element(By.ID,'id_description')
         input_descricao.clear()
         input_descricao.send_keys('Atualização do campo de descrição')
         browser.find_element(By.ID,'botao-criar-produto').click() #id do botao de "atualizar produto"
         sleep(3)

         descricao_descricao = browser.find_element(By.ID,'descricao_descricao')
         assert descricao_descricao.text == 'Atualização do campo de descrição'
        #------------------------------------------------------------------------------------------------------------#

    def test_minhas_conversas(self):
        browser = setUp()
        browser.get('http://127.0.0.1:8000/')
        browser.find_element(By.ID,'logar').click()
        input_user = browser.find_element(By.ID,'user')
        input_senha = browser.find_element(By.ID,'senha')
        input_user.send_keys('BrunaCarvalho')
        input_senha.send_keys('bruna123')
        browser.find_element(By.ID,'login-registrar').click()
        sleep(3)

        browser.find_element(By.ID,'minhas-conversas').click()
        sleep(2)
        # browser.find_element(By.ID,'oi').click()
        # sleep(2)

        # input_mensagem = browser.find_element(By.ID,'chat-message-input')
        # sleep(1)
        # input_mensagem.send_keys('oioioi')
        # sleep(2)

        mensagem_exemplo = browser.find_element(By.ID,'tela_conversas')
        assert mensagem_exemplo.text == 'Minhas conversas'


        

    #def tearDown(self):
        #browser = setUp()
        #selenium.quit()
        #super().tearDown()
