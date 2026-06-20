import os
import logging
import requests
from dotenv import load_dotenv
from supabase import create_client


load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
ZAPI_INSTANCE_ID = os.getenv("ZAPI_INSTANCE_ID")
ZAPI_INSTANCE_TOKEN = os.getenv("ZAPI_INSTANCE_TOKEN")


def buscar_contatos(supabase):
    resposta = (
        supabase
        .table("contatos")
        .select("id, nome_contato, telefone, enviado")
        .eq("enviado", False)
        .limit(3)
        .execute()
    )

    return resposta.data


def enviar_mensagem(telefone, nome_contato):
    url = (
        f"https://api.z-api.io/instances/{ZAPI_INSTANCE_ID}"
        f"/token/{ZAPI_INSTANCE_TOKEN}/send-text"
    )

    mensagem = f"Olá, {nome_contato} tudo bem com você?"

    payload = {
        "phone": telefone,
        "message": mensagem
    }

    resposta = requests.post(url, json=payload, timeout=30)

    if resposta.status_code != 200:
        raise Exception(f"Erro Z-API: {resposta.status_code} - {resposta.text}")

    return resposta.json()


def marcar_como_enviado(supabase, contato_id):
    supabase.table("contatos").update(
        {"enviado": True}
    ).eq("id", contato_id).execute()


def main():
    supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

    contatos = buscar_contatos(supabase)

    if not contatos:
        logging.info("Nenhum contato pendente encontrado.")
        return

    for contato in contatos:
        try:
            contato_id = contato["id"]
            nome_contato = contato["nome_contato"]
            telefone = contato["telefone"]

            logging.info(f"Enviando mensagem para {nome_contato}")

            resposta = enviar_mensagem(telefone, nome_contato)

            marcar_como_enviado(supabase, contato_id)

            logging.info(f"Mensagem enviada com sucesso: {resposta}")

        except Exception as erro:
            logging.error(f"Erro ao processar contato: {erro}")


if __name__ == "__main__":
    main()