from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=service)

try:

    # Seu link de afiliada
    driver.get("https://meli.la/2XaVoXA")

    # Aguarda a página carregar
    time.sleep(10)

    # Captura o título
    titulo = driver.find_element(
        By.CLASS_NAME,
        "ui-pdp-title"
    )

    # Captura o valor inteiro
    preco_inteiro = driver.find_element(
        By.CLASS_NAME,
        "andes-money-amount__fraction"
    )

    # Captura os centavos
    centavos = driver.find_element(
        By.CLASS_NAME,
        "andes-money-amount__cents"
    )

    # Monta o preço completo
    preco = f"R$ {preco_inteiro.text},{centavos.text}"

    # Cria o dicionário
    produto = {
        "titulo": titulo.text,
        "preco": preco,
        "link": driver.current_url
    }

    # Exibe o dicionário
    print("\nDICIONÁRIO:")
    print(produto)

    # Cria a mensagem
    mensagem = f"""
🔥 OFERTA ENCONTRADA

📱 {produto['titulo']}

💰 {produto['preco']}

🔗 {produto['link']}
"""

    print("\nMENSAGEM GERADA:")
    print(mensagem)

except Exception as erro:

    print("ERRO:")
    print(erro)

input("\nPressione ENTER para fechar")

driver.quit()