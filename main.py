from mercadolivre import obter_produto
from whatsapp import enviar_mensagem
from config import LINK_AFILIADO
from config import CONVERSA_WHATSAPP

produto = obter_produto(
    "https://meli.la/1D6Asbi"
)

mensagem = f"""
OFERTA ENCONTRADA

PRODUTO:
{produto['titulo']}

PRECO:
{produto['preco']}

LINK:
{produto['link']}
"""

print("\nMensagem gerada:\n")
print(mensagem)

enviar_mensagem(
    CONVERSA_WHATSAPP,
    mensagem
)