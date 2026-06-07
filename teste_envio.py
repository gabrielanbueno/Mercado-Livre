from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(
    ChromeDriverManager().install()
)

driver = webdriver.Chrome(
    service=service
)

driver.get("https://web.whatsapp.com")

input("Faça login e pressione ENTER")

grupo = input("Digite o nome da conversa: ")

try:

    campo_pesquisa = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//input[@aria-label='Pesquisar ou começar uma nova conversa']"
            )
        )
    )

    campo_pesquisa.click()

    campo_pesquisa.send_keys(grupo)

    time.sleep(3)

    campo_pesquisa.send_keys(Keys.ENTER)

    print("Conversa selecionada!")

    input(
        "A conversa abriu? Se sim, pressione ENTER"
    )

except Exception as erro:

    print("ERRO:")
    print(erro)

input("ENTER para fechar")

driver.quit()