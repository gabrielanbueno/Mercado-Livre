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

driver = webdriver.Chrome(service=service)

try:

    driver.get("https://web.whatsapp.com")

    input(
        "\nFaça login no WhatsApp Web e pressione ENTER..."
    )

    grupo = input(
        "\nDigite o nome EXATO da conversa: "
    )

    pesquisa = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//input[@aria-label='Pesquisar ou começar uma nova conversa']"
            )
        )
    )

    pesquisa.click()

    pesquisa.send_keys(grupo)

    time.sleep(3)

    pesquisa.send_keys(Keys.ENTER)

    print("Conversa aberta!")

    time.sleep(3)

    caixa = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//*[@data-testid='conversation-compose-box-input']"
            )
        )
    )

    caixa.click()

    caixa.send_keys("TESTE AUTOMATICO")

    time.sleep(1)

    caixa.send_keys(Keys.ENTER)

    print("Mensagem enviada!")

except Exception as erro:

    print("ERRO:")
    print(erro)

input("\nPressione ENTER para fechar")

driver.quit()