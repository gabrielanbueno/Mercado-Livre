from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def enviar_whatsapp(grupo, mensagem):

    service = Service(
        ChromeDriverManager().install()
    )

    driver = webdriver.Chrome(
        service=service
    )

    driver.get(
        "https://web.whatsapp.com"
    )

    input(
        "Faça login no WhatsApp Web e pressione ENTER"
    )

    pesquisa = driver.find_element(
        By.XPATH,
        '//div[@contenteditable="true"]'
    )

    pesquisa.send_keys(grupo)

    time.sleep(3)

    pesquisa.send_keys(Keys.ENTER)

    time.sleep(2)

    campos = driver.find_elements(
        By.XPATH,
        '//div[@contenteditable="true"]'
    )

    caixa = campos[-1]

    caixa.send_keys(mensagem)

    caixa.send_keys(Keys.ENTER)

    input(
        "Mensagem enviada. ENTER para fechar."
    )

    driver.quit()