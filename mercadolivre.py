from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


def obter_produto(link):

    service = Service(
        ChromeDriverManager().install()
    )

    driver = webdriver.Chrome(
        service=service
    )

    try:

        driver.get(link)

        time.sleep(8)

        titulo = driver.find_element(
            By.CLASS_NAME,
            "ui-pdp-title"
        )

        preco_inteiro = driver.find_element(
            By.CLASS_NAME,
            "andes-money-amount__fraction"
        )

        centavos = driver.find_element(
            By.CLASS_NAME,
            "andes-money-amount__cents"
        )

        preco = f"R$ {preco_inteiro.text},{centavos.text}"

        produto = {
            "titulo": titulo.text,
            "preco": preco,
            "link": driver.current_url
        }

        return produto

    finally:

        driver.quit()