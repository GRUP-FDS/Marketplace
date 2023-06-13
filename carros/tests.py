from time import sleep
from django.test import LiveServerTestCase
from selenium import webdriver
#from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
#from urllib3.util.timeout import Timeout


def setUp():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--icognito')
    chrome_options.add_argument('--headless')
    #driver = webdriver.Chrome(options=chrome_options)
    driver = webdriver.Chrome(options=chrome_options, timeout=10)

    driver.maximize_window()

    return driver

class MySeleniumTest(LiveServerTestCase):
        # ... continue com as interações e validações na página web
    def test_cadastrar(self):
        driver = setUp()
        driver.get('http://127.0.0.1:8000/')
        driver.find_element(By.ID,'logar').click()
        driver.find_element(By.ID,'registrar').click()
        input_username = driver.find_element(By.ID,'input-username')
        input_password = driver.find_element(By.ID,'input-password')
        input_repassword = driver.find_element(By.ID,'input-repassword')
        input_username.send_keys('brunaamademais')
        input_password.send_keys('blackthigas')
        input_repassword.send_keys('blackthigas')
        sleep(3)
        driver.find_element(By.ID,'cadastro').click()

        botao_sair = driver.find_element(By.ID,'sairlogout')
        assert botao_sair.text == "Sair"

        #------------------------------------------------------------------------------------------------------------#
    def test_logar(self):
        
        sleep(3)
        driver = setUp()
        driver.get('http://127.0.0.1:8000/')
        driver.find_element(By.ID,'logar').click()
        input_user = driver.find_element(By.ID,'user')
        input_senha = driver.find_element(By.ID,'senha')
        input_user.send_keys('BrunaCarvalho')
        sleep(3)
        input_senha.send_keys('bruna123')
        driver.find_element(By.ID,'login-registrar').click()
        sleep(3)

        botao_sair = driver.find_element(By.ID,'sairlogout')
        assert botao_sair.text == "Sair"
        #------------------------------------------------------------------------------------------------------------#
    def test_criar_anuncio(self):
        
        driver = setUp()
        driver.get('http://127.0.0.1:8000/')
        sleep(3)
        driver.find_element(By.ID,'logar').click()
        input_user = driver.find_element(By.ID,'user')
        input_senha = driver.find_element(By.ID,'senha')
        input_user.send_keys('BruncaCarvalho')
        input_senha.send_keys('bruna123')
        driver.find_element(By.ID,'login-registrar').click()
        sleep(3)

        driver.find_element(By.ID,'criar-anuncios').click()
        sleep(1)
        input_marca = driver.find_element(By.ID,'id_brand')
        sleep(1)
        input_model = driver.find_element(By.ID,'id_car_model')
        sleep(1)
        input_km = driver.find_element(By.ID,'id_mileage')
        sleep(1)
        input_ano = driver.find_element(By.ID,'id_year')
        sleep(1)
        input_combustivel = driver.find_element(By.ID,'id_fuel_type')
        sleep(1)
        input_estado = driver.find_element(By.ID,'id_type')
        sleep(1)
        input_price = driver.find_element(By.ID,'id_price')
        sleep(1)
        input_color = driver.find_element(By.ID,'id_color')
        sleep(1)
        input_image = driver.find_element(By.ID, 'id_image')   
        sleep(1)
        input_descricao = driver.find_element(By.ID,'id_description') 
       
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
        driver.find_element(By.ID,'botao-criar-produto').click()    
        sleep(3)
        
        #ENTRANDO NOS MEUS ANUNCIOS
        driver.find_element(By.ID,'botao-meus-anuncios').click()
        sleep(3)

        meus_anuncios_exemplo = driver.find_element(By.ID,'anuncio_exemplo')
        print(meus_anuncios_exemplo)
        assert meus_anuncios_exemplo.text == "Este é um produto de teste"
        #------------------------------------------------------------------------------------------------------------#


    def test_pesquisar_anuncio(self):
        
        sleep(3)
        driver = setUp()
        driver.get('http://127.0.0.1:8000/')
        driver.find_element(By.ID,'filtros').click()
        input_filter_brand = driver.find_element(By.ID,'filter_brand')
        input_filter_brand.send_keys('ford')
        input_filter_model = driver.find_element(By.ID,'filter-model')
        input_filter_model.send_keys('ka')
        driver.find_element(By.ID,'botao_filtrar').click()
        sleep(3)

        carro_exemplo = driver.find_element(By.ID,'nome_carro')
        assert carro_exemplo.text == "FORD KA"
 
        #------------------------------------------------------------------------------------------------------------#
    def test_visualizar_anuncio(self):
        
        sleep(3)
        driver = setUp()
        driver.get('http://127.0.0.1:8000/')
        driver.find_element(By.ID,'logar').click()
        input_user = driver.find_element(By.ID,'user')
        input_senha = driver.find_element(By.ID,'senha')
        input_user.send_keys('BrunaCarvalho')
        input_senha.send_keys('bruna123')
        driver.find_element(By.ID,'login-registrar').click()
        driver.find_element(By.ID,'botao-meus-anuncios').click()
        sleep(3)

        meus_anuncios = driver.find_element(By.ID,'confirmar_anuncio')
        assert meus_anuncios.text == "Meus anúncios"
        #------------------------------------------------------------------------------------------------------------#

    def test_chat_online(self):
        

        driver = setUp()
        driver.get('http://127.0.0.1:8000/')
        sleep(3)
        driver.find_element(By.ID,'logar').click()
        input_user = driver.find_element(By.ID,'user')
        input_senha = driver.find_element(By.ID,'senha')
        input_user.send_keys('BrunaCarvalho')
        input_senha.send_keys('bruna123')
        driver.find_element(By.ID,'login-registrar').click()
        driver.find_element(By.ID,'home').click()
        sleep(3)

        input_search = driver.find_element(By.ID,'search')
        input_search.send_keys('ka')
        sleep(3)
        driver.find_element(By.ID,'confirm-search').click()
        driver.find_element(By.ID,'descricao-carro').click()
        driver.find_element(By.ID,'botao_entrar_contato').click()
        sleep(3)
        input_masseges = driver.find_element(By.ID,'chat-message-input')
        input_masseges.send_keys('Olá, estou interessado no seu carro')
        sleep(2)
        driver.find_element(By.ID,'chat-message-submit').click()
        sleep(3)

        mensagem = driver.find_element(By.ID,'mensagem_exemplo')
        assert mensagem.text == "Olá, estou interessado no seu carro"
        #------------------------------------------------------------------------------------------------------------#

    
    def test_deleter_anuncio(self):
        
        driver = setUp() 
        driver.get('http://127.0.0.1:8000/')
        driver.find_element(By.ID,'logar').click()
        input_user = driver.find_element(By.ID,'user')
        input_senha = driver.find_element(By.ID,'senha')
        input_user.send_keys('BrunaCarvalho')
        input_senha.send_keys('bruna123')
        driver.find_element(By.ID,'login-registrar').click()
        sleep(3)
        
        driver.find_element(By.ID,'criar-anuncios').click()
        sleep(3)
        input_marca = driver.find_element(By.ID,'id_brand')
        input_model = driver.find_element(By.ID,'id_car_model')
        input_km = driver.find_element(By.ID,'id_mileage')
        input_ano = driver.find_element(By.ID,'id_year')
        input_combustivel = driver.find_element(By.ID,'id_fuel_type')
        input_estado = driver.find_element(By.ID,'id_type')
        input_price = driver.find_element(By.ID,'id_price')
        input_color = driver.find_element(By.ID,'id_color')
        input_image = driver.find_element(By.ID, 'id_image')   
        input_descricao = driver.find_element(By.ID,'id_description') 
       
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
        driver.find_element(By.ID,'botao-criar-produto').click()    
        sleep(3)

        driver.find_element(By.ID,'botao-meus-anuncios').click()
        sleep(2)

        driver.find_element(By.ID,'delete_my_ads').click()
        sleep(2)
        driver.find_element(By.ID,'confirm_delete').click()
        sleep(2)


        mensagem_sem_anuncio = driver.find_element(By.ID,'mensagem_sem_anuncio')
        assert mensagem_sem_anuncio.text == "Você ainda não tem nenhum anúncio. Crie um agora."

        #------------------------------------------------------------------------------------------------------------#
    def test_anuncio_vendido(self):
        

        driver = setUp()
        driver.get('http://127.0.0.1:8000/')
        sleep(3)
        driver.find_element(By.ID,'logar').click()
        input_user = driver.find_element(By.ID,'user')
        input_senha = driver.find_element(By.ID,'senha')
        input_user.send_keys('lulu')
        input_senha.send_keys('px132652')
        driver.find_element(By.ID,'login-registrar').click()
        sleep(3)

        
        driver.find_element(By.ID,'criar-anuncios').click()
        sleep(3)
        input_marca = driver.find_element(By.ID,'id_brand')
        input_model = driver.find_element(By.ID,'id_car_model')
        input_km = driver.find_element(By.ID,'id_mileage')
        input_ano = driver.find_element(By.ID,'id_year')
        input_combustivel = driver.find_element(By.ID,'id_fuel_type')
        input_estado = driver.find_element(By.ID,'id_type')
        input_price = driver.find_element(By.ID,'id_price')
        input_color = driver.find_element(By.ID,'id_color')
        input_image = driver.find_element(By.ID, 'id_image')   
        input_descricao = driver.find_element(By.ID,'id_description')
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
        driver.find_element(By.ID,'botao-criar-produto').click()    
        sleep(3)
        
        #ENTRANDO NOS MEUS ANUNCIOS
        driver.find_element(By.ID,'botao-meus-anuncios').click()
        sleep(3)
        driver.find_element(By.ID,'descricao_my_ads').click()
        driver.find_element(By.ID,'marcar_vendido').click()
        sleep(2)

        mensagem_anuncio_vendido = driver.find_element(By.ID,'vendido')
        assert mensagem_anuncio_vendido.text == 'Vendido'


        #------------------------------------------------------------------------------------------------------------#
    def test_atualizar_produto(self): 
        
        driver = setUp()
        driver.get('http://127.0.0.1:8000/')
        driver.find_element(By.ID,'logar').click()
        input_user = driver.find_element(By.ID,'user')
        input_senha = driver.find_element(By.ID,'senha')
        input_user.send_keys('brunaamamuito')
        input_senha.send_keys('thiagopreto')
        driver.find_element(By.ID,'login-registrar').click()
        sleep(3)
        
        driver.find_element(By.ID,'botao-meus-anuncios').click()
        driver.find_element(By.ID,'atualizar_my_ads').click() #id do botao "atualizar"

        #atualizando os campos do anuncio
        input_descricao = driver.find_element(By.ID,'id_description')
        input_descricao.send_keys('Atualização do campo de descrição')
        driver.find_element(By.ID,'botao-criar-produto').click() #id do botao de "atualizar produto"
        sleep(3)

        descricao_descricao = driver.find_element(By.ID,'descricao_descricao')
        assert descricao_descricao.text == 'Atualização do campo de descrição'
        #------------------------------------------------------------------------------------------------------------#

    def test_minhas_conversas(self):
        
        driver = setUp()
        driver.get('http://127.0.0.1:8000/')
        driver.find_element(By.ID,'logar').click()
        input_user = driver.find_element(By.ID,'user')
        input_senha = driver.find_element(By.ID,'senha')
        input_user.send_keys('BrunaCarvalho')
        input_senha.send_keys('bruna123')
        driver.find_element(By.ID,'login-registrar').click()
        sleep(3)

        driver.find_element(By.ID,'minhas-conversas').click()
        driver.find_element(By.ID,'conversante').click()
        sleep(2)

        input_mensagem = driver.find_element(By.ID,'chat-message-input')
        sleep(1)
        input_mensagem.send_keys('oioioi')
        sleep(2)

        mensagem_exemplo = driver.find_element(By.ID,'mensagem_exemplo')
        assert mensagem_exemplo.text == 'oioioi'


        

    #def tearDown(self):
        #driver = set_Up()
        #selenium.quit()
        #super().tearDown()
