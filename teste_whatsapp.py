from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(
    ChromeDriverManager().install()
)

driver = webdriver.Chrome(service=service)

driver.get("https://web.whatsapp.com")

input("Faça login no WhatsApp Web e pressione ENTER")

print("WhatsApp conectado com sucesso!")

input("Pressione ENTER para fechar")

driver.quit()