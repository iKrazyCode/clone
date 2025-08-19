import re
from django.utils.safestring import mark_safe
from urllib.parse import urlparse

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options
import platform
import pickle
from time import sleep 
import os

class MyDriver:
    driver = None

    def __init__(self, not_window=False):
        os_info = platform.system()
        if os_info == 'Windows':
            op = webdriver.ChromeOptions()
            if not_window:
                op.add_argument("--headless")

            #op.add_argument("--incognito") # ESTAVA COMENTADO - deixa em janela anonima
            op.add_argument('--no-sandbox')
            op.add_argument("--start-maximized")
            op.add_argument("--disable-dev-shm-usage")  # Para evitar alguns problemas de memória
            op.add_argument("--disable-blink-features=AutomationControlled")  # Desabilita detecção de automação
            op.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36")
            #op.add_argument('window-size=1990,999')
            op.add_argument("--disable-web-security")
            op.add_argument("--user-data-dir=/tmp/chrome_dev_test")

            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=op)            

            self.driver = driver


        elif os_info == 'Linux':
            op = Options()

            if not_window:
                op.headless = True
            driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=op)
            self.driver = driver

        # Remover a propriedade 'webdriver'
        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

        # Alterar outras propriedades do navegador para evitar detecção
        driver.execute_script("Object.defineProperty(navigator, 'plugins', {get: () => [1, 2, 3, 4, 5]})")
        driver.execute_script("Object.defineProperty(navigator, 'languages', {get: () => ['en-US', 'en']})")

def auto_get_page(url):
    """
    Responsável por pegar a página, mesmo após um préload, usando SELENIUM
    url: Página que vai ser baixada
    """ 
    mydriver = MyDriver(not_window=True)
    driver = mydriver.driver
    page = driver.get(url)
    #driver.implicitly_wait(30)
    sleep(15) # Aguardar os scripts da página carregar completamente
    resp = driver.page_source
    #driver.close()
    return resp


# apagar acima creio eu





def form_injection(text_html, url_base):
    """
    PASSAR O url PELA VIEW, USANDO O CONTEXT
    Template é a instancia do TemplateCopy
    """
    texto = text_html

    #action = "{% url 'home:renderizator' url=URL %}"
    action = ''
 
    parsed = urlparse(url_base)
    template_copy_url_trated = f"{parsed.scheme}://{parsed.netloc}/"
    print(template_copy_url_trated)

    # Remove os action e method dos forms, para em seguida adicionar novos action e method ao form
    texto = re.sub(
        r'(action[ ]*=[ ]*[\'"])(.*?)([\'"][ ]*)',
        r'',
        texto,
        flags=re.IGNORECASE | re.DOTALL
    )

    texto = re.sub(
        r'(method[ ]*=[ ]*[\'"])(.*?)([\'"][ ]*)',
        r'',
        texto,
        flags=re.IGNORECASE | re.DOTALL
    )

    texto = re.sub(
        r'(<form)(.*?)(>)',
        r'\1 action="{}" method="POST" \2\3{}'.format(action, "{% csrf_token %}"),
        texto,
        flags=re.IGNORECASE | re.DOTALL
    )

    # script: remove todas tags script -DESATIVADO POR ENQUANTO
    texto = re.sub(
        r'(<script.*?>)(.*?)(</script>)',
        r'',
        texto,
        flags=re.IGNORECASE | re.DOTALL
    )

    # /ajax/
    texto = re.sub(
        r'\\/ajax\\/',
        str(template_copy_url_trated.replace('/', '\/')) + r'\\/ajax\\/',
        texto,
        flags=re.IGNORECASE | re.DOTALL 
    )

    # input disabled: remove todos atributos de disabled dos input
    texto = re.sub(
        r'(<input.*?)(disabled)(.*?>)',
        r'\1\3',
        texto,
        flags=re.IGNORECASE | re.DOTALL
    )

    # base: remove todas tags base
    texto = re.sub(
        r'(<base.*?>)(.*?)',
        r'',
        texto,
        flags=re.IGNORECASE | re.DOTALL
    )

    # remover ../../: remove todas tags script
    texto = re.sub(
        r'(\.\./)+',
        r'/',
        texto,
        flags=re.IGNORECASE | re.DOTALL
    )
    
    # src: adicionar o dominio do site no começo 

    texto = re.sub(
        r'(src[ ]*=[ ]*[\'"]?)\.?\/(.*?)([\'"][ ]*?)',
        r'\1{}\2\3'.format(template_copy_url_trated),
        texto,
        flags=re.IGNORECASE | re.DOTALL
    )

    # href: adicionar o dominio do site no começo 
    texto = re.sub(
        r'(href[ ]*=[ ]*[\'"]?)\.?\/(.*?)([\'"][ ]*?)',
        r'\1{}\2\3'.format(template_copy_url_trated),
        texto,
        flags=re.IGNORECASE | re.DOTALL
    )

    # Para src que não contem / no inicio
    texto = re.sub(
        r'(src\s*=\s*[\'"])(?!(https?://|data:))(/?[^\'"]+)([\'"])',
        r'\1{}\2\3'.format(template_copy_url_trated),
        texto,
        flags=re.IGNORECASE | re.DOTALL
    )

    # para href que não contem / no inicio 
    texto = re.sub(
        r'(href\s*=\s*[\'"])(?!(https?://|data:))(/?[^\'"]+)([\'"])',
        r'\1{}\2\3'.format(template_copy_url_trated),
        texto,
        flags=re.IGNORECASE | re.DOTALL
    )



    return mark_safe(texto)




