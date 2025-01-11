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

    try:
    # Localizar a barra de pesquisa
        search_bar = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'search-global-typeahead__input'))
        )
        time.sleep(random.uniform(2, 3))  # Pausa antes da pesquisa
        search_keyword = "Desenvolvedor Backend"  # Substitua pela palavra-chave desejada
        print(f"Realizando pesquisa pela palavra-chave: {search_keyword}")

        # Simular digitação na barra de pesquisa
        for char in search_keyword:
            search_bar.send_keys(char)
            time.sleep(random.uniform(0.1, 0.3))
        search_bar.send_keys(Keys.RETURN)
        time.sleep(random.uniform(3, 5))  # Aguardar resultados carregarem

        # Filtrar para resultados de "Pessoas"
        try:
            # Rolando a página para garantir visibilidade do botão
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)

            pessoas_tab = WebDriverWait(driver, 15).until(
                EC.element_to_be_clickable((By.XPATH, "//button[text()='Pessoas']"))
            )
            pessoas_tab.click()
            print("Filtro 'Pessoas' aplicado com sucesso!")
            time.sleep(random.uniform(3, 5))
        except Exception as e:
            # Salvar uma captura de tela para depuração
            driver.save_screenshot("erro_pessoas_filtro.png")
            print(f"Erro ao tentar aplicar o filtro 'Pessoas': {e}")

        # Iterar pelos resultados
        print("Iniciando iteração pelos perfis...")

        # Localizar todos os botões "Conectar" na página
        connect_buttons = WebDriverWait(driver, 15).until(
            EC.presence_of_all_elements_located((By.XPATH, "//button[contains(@aria-label, 'Convidar') and contains(@aria-label, 'para se conectar')]"))
        )
        print(f"Botões 'Conectar' encontrados: {len(connect_buttons)}")

        count = 0
        for index, connect_button in enumerate(connect_buttons):
            if count >= 2:  # Limitar a 2 convites para teste
                print("Limite de 2 convites atingido.")
                break

            try:
                print(f"Enviando convite para o botão {index + 1}...")

                # Clicar no botão "Conectar"
                connect_button.click()
                time.sleep(random.uniform(2, 4))  # Aguardar o modal abrir

                # Clicar no botão "Adicionar Nota"
                try:
                    add_note_button = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, "//button[contains(@aria-label, 'Adicionar nota')]"))
                    )
                    add_note_button.click()
                    print("Botão 'Adicionar Nota' clicado.")
                    time.sleep(random.uniform(1, 2))

                    # Preencher a mensagem personalizada
                    message_box = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, "//textarea[@name='message']"))
                    )
                    message = f"Olá! Estou ampliando minha rede com profissionais voltados para a área da tecnologia em geral. Seria ótimo conectar com você!"
                    for char in message:
                        message_box.send_keys(char)
                        time.sleep(random.uniform(0.05, 0.1))
                    print("Mensagem personalizada adicionada.")

                    # Enviar convite
                    try:
                        send_button = WebDriverWait(driver, 10).until(
                            EC.element_to_be_clickable((By.XPATH, "//button[contains(@aria-label, 'Enviar convite')]"))
                        )
                        send_button.click()
                        print("Convite enviado com sucesso!")
                        count += 1
                    except Exception as e:
                        print(f"Erro ao clicar no botão 'Enviar': {e}")
                        continue

                except Exception as e:
                    print(f"Erro ao adicionar mensagem personalizada: {e}")
                    continue

                # Aguarda um tempo antes de prosseguir
                time.sleep(random.uniform(10, 15))
            except Exception as e:
                print(f"Erro ao processar o botão {index + 1}: {e}")
                continue

    except Exception as e:
        print(f"Erro durante a iteração pelos botões: {e}")
        driver.save_screenshot("erro_iteracao_botoes.png")  # Captura tela para análise


except Exception as e:
    print(f"Erro durante o login: {e}")
    driver.save_screenshot("erro_login.png")  # Captura tela para depuração

finally:
    # Aguarde 15 segundos antes de fechar o navegador
    print("Aguardando 15 segundos antes de fechar...")
    time.sleep(15)
    driver.quit()
