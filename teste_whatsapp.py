from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

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
    "Faça login e pressione ENTER"
)

print("WhatsApp conectado!")

input(
    "Pressione ENTER para fechar"
)

driver.quit()