# Desafio b2bflow

Projeto desenvolvido em Python para leitura de contatos armazenados no Supabase e envio de mensagens personalizadas via Z-API.

## Funcionalidades

* Busca contatos cadastrados no Supabase.

* Envia a mensagem:

  ```
  Olá, <nome_contato> tudo bem com você?
  ```

* Processa até 3 contatos por execução.

* Após o envio, atualiza o campo `enviado` para `true`.

## Tecnologias utilizadas

* Python
* Supabase
* Z-API
* Requests
* Python Dotenv

## Estrutura da tabela

Tabela: `contatos`

| Campo        | Tipo |
| ------------ | ---- |
| id           | int8 |
| nome_contato | text |
| telefone     | text |
| enviado      | bool |

## Variáveis de ambiente

Criar um arquivo `.env` na raiz do projeto:

```env
SUPABASE_URL=
SUPABASE_KEY=

ZAPI_INSTANCE_ID=
ZAPI_INSTANCE_TOKEN=
```

## Instalação

Criar e ativar o ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate
```

Instalar as dependências:

```bash
pip install -r requirements.txt
```

## Execução

```bash
python main.py
```

## Exemplo de registro

| nome_contato | telefone      | enviado |
| ------------ | ------------- | ------- |
| Kevin Guedes | 5592994441097 | false   |
