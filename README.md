# SMTP Python - Gerenciamento de E-mails

Este projeto implementa um servidor SMTP simples em Python usando `aiosmtpd` para receber e-mails e armazená-los em um servidor local. A interface de gerenciamento de mensagens é fornecida por um aplicativo Flask com autenticação básica. As mensagens recebidas são armazenadas em um arquivo JSON e podem ser visualizadas e excluídas pela interface web.

## Funcionalidades

- **Servidor SMTP Local:** Recebe e-mails em um servidor SMTP local na porta 1025.
- **Interface Web:** Gerencie e visualize mensagens de e-mail recebidas através de uma interface web simples com Flask.
- **Autenticação:** Login com e-mail e senha para acessar a interface de mensagens.
- **Visualização de E-mails:** Exibição de informações como remetente, assunto e corpo da mensagem.
- **Exclusão de E-mails:** Exclua mensagens recebidas através da interface.
- **Armazenamento de E-mails:** As mensagens são armazenadas em um arquivo JSON (`emails.json`).

## Como Rodar

### Requisitos

- Python 3.x
- Bibliotecas Python:
  - `aiosmtpd`
  - `Flask`

### Instalando as dependências

1. Clone o repositório:
    ```bash
    git clone https://github.com/DebugDiario/SMTP_Python.git
    cd SMTP_Python
    ```

2. Crie e ative um ambiente virtual (opcional, mas recomendado):
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # Para Linux/Mac
    venv\Scripts\activate  # Para Windows
    ```

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

### Rodando o servidor

1. Execute o servidor SMTP e a aplicação Flask:
    ```bash
    python app.py
    ```

2. O servidor SMTP estará disponível na porta `1025` e a aplicação Flask estará rodando em `http://127.0.0.1:5000`.

3. Acesse a interface web para visualizar e gerenciar as mensagens.

### Acessando a Interface Web

- **Login:** Use o e-mail `admin@gmail.com` e a senha `123456` para fazer login na interface de mensagens.
- **Visualização de E-mails:** Clique em "Ver" para visualizar o conteúdo das mensagens.
- **Exclusão de E-mails:** Clique em "Excluir" para remover uma mensagem da lista.

## Estrutura do Projeto

```plaintext
.
├── app.py                # Código principal da aplicação Flask
├── emails.json           # Arquivo onde as mensagens recebidas são armazenadas
├── templates/             # Contém os templates HTML para a interface
│   ├── index.html        # Tela principal de visualização de mensagens
│   └── login.html        # Tela de login
├── requirements.txt      # Dependências do projeto
└── README.md             # Documentação do projeto
