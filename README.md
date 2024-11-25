# SMTP_Python

Este é um projeto simples que implementa um servidor SMTP local e uma interface de administração usando Flask. O servidor SMTP local captura as mensagens recebidas e as armazena em um arquivo JSON. A interface web permite visualizar e excluir mensagens recebidas de forma simples.

## Funcionalidades

- **Servidor SMTP Local**: O servidor SMTP é iniciado localmente na porta 1025 e aceita mensagens.
- **Interface de Administração**: O projeto inclui uma interface de administração usando Flask para visualizar as mensagens recebidas.
- **Autenticação Simples**: A aplicação usa autenticação simples (usuário e senha) para proteger a visualização das mensagens.
- **Exclusão de Mensagens**: Permite excluir mensagens recebidas a partir da interface.
- **Armazenamento de E-mails**: As mensagens são armazenadas em um arquivo JSON (`emails.json`), permitindo persistência entre reinícios do servidor.

## Como Rodar o Projeto

### Requisitos

- Python 3.x
- Bibliotecas:
  - `aiosmtpd`: Para o servidor SMTP assíncrono.
  - `Flask`: Para a criação da interface web.
  - `json`: Para manipulação de arquivos JSON.

### Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/DebugDiario/SMTP_Python.git
   cd SMTP_Python
