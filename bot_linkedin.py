from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv
import os
import random
import time

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv('PASSWORD')

# Configuração do navegador
options = Options()
options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')
options.add_argument("--disable-webrtc")

# Usar o WebDriver Manager para gerenciar o ChromeDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    # Acessar a página de login do LinkedIn
    driver.get('https://www.linkedin.com/login')

    # Maximizar a janela do navegador
    driver.maximize_window()

    # Esperar pelo campo de e-mail
    email_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'username'))
    )

    # Simular digitação no campo de e-mail
    for char in EMAIL:
        email_field.send_keys(char)
        time.sleep(random.uniform(0.1, 0.3))

    # Esperar pelo campo de senha
    password_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'password'))
    )

    # Simular digitação no campo de senha
    for char in PASSWORD:
        password_field.send_keys(char)
        time.sleep(random.uniform(0.1, 0.3))

    # Enviar o formulário de login
    time.sleep(random.uniform(2, 4))  # Aguardar antes de enviar
    password_field.send_keys(Keys.RETURN)

    # Verifica se o login foi bem-sucedido
    WebDriverWait(driver, 10).until(
        EC.url_contains("feed")
    )
    print("Login realizado com sucesso!")

except Exception as e:
    print(f"Erro durante o login: {e}")
    driver.save_screenshot("erro_login.png")  # Captura tela para depuração

finally:
    # Aguarde 30 segundos antes de fechar o navegador
    print("Aguardando 30 segundos antes de fechar...")
    time.sleep(30)
    driver.quit()
