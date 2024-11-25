import asyncio
from aiosmtpd.controller import Controller
from email.parser import BytesParser
from flask import Flask, render_template, jsonify, request, redirect, url_for, session
import threading
import json
import uuid

# Flask app initialization
app = Flask(__name__)
app.secret_key = "s3cr3t_k3y"  # Chave secreta para sessões

# Dados de exemplo para autenticação
USER_EMAIL = "admin@gmail.com"
USER_PASSWORD = "123456"

# Lista para armazenar mensagens recebidas
received_messages = []

# Caminho para o arquivo JSON que armazenará os e-mails
EMAILS_JSON_FILE = "emails.json"


def save_messages_to_json():
    """
    Função para salvar as mensagens no arquivo emails.json.
    """
    try:
        with open(EMAILS_JSON_FILE, "w") as f:
            json.dump(received_messages, f, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"Erro ao salvar as mensagens no arquivo JSON: {e}")


class MyHandler:
    """
    Classe para tratar as mensagens recebidas pelo servidor SMTP.
    """
    async def handle_DATA(self, server, session, envelope):
        try:
            print(f"Nova mensagem recebida de {envelope.mail_from} para {envelope.rcpt_tos}")

            # Parseando o conteúdo do e-mail
            msg = BytesParser().parsebytes(envelope.content)

            subject = msg['subject'] if msg['subject'] else '[Sem Assunto]'
            body = msg.get_payload(decode=True).decode('utf-8', errors='replace') if not msg.is_multipart() else ''.join(
                part.get_payload(decode=True).decode('utf-8', errors='replace')
                for part in msg.walk() if part.get_content_type() == 'text/plain'
            )

            # Gerando um ID único para a mensagem
            message_id = str(uuid.uuid4())

            # Armazenando a mensagem
            message = {
                'id': message_id,
                'from': envelope.mail_from,
                'to': envelope.rcpt_tos,
                'subject': subject,
                'body': body
            }

            received_messages.append(message)
            save_messages_to_json()

            return '250 Message accepted for delivery'
        except Exception as e:
            print(f"Erro ao processar a mensagem: {e}")
            return '550 Internal error'


# Função para iniciar o servidor SMTP
def start_smtp_server():
    try:
        controller = Controller(MyHandler(), hostname='localhost', port=1025)
        controller.start()
        print("Servidor SMTP local rodando na porta 1025...")
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_forever()
    except Exception as e:
        print(f"Erro ao iniciar o servidor SMTP: {e}")


# Rotas do Flask

@app.route('/')
def index():
    if 'logged_in' not in session:
        return redirect(url_for('login'))
    return render_template('index.html', messages=received_messages)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        if email == USER_EMAIL and password == USER_PASSWORD:
            session['logged_in'] = True
            return redirect(url_for('index'))
        return render_template('login.html', error='Credenciais inválidas')
    return render_template('login.html')


@app.route('/api/delete', methods=['POST'])
def delete_message():
    if 'logged_in' not in session:
        return jsonify({'error': 'Unauthorized'}), 401

    message_id = request.json.get('id')
    global received_messages
    received_messages = [msg for msg in received_messages if msg['id'] != message_id]
    save_messages_to_json()
    return jsonify({'message': 'Mensagem excluída com sucesso'}), 200


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))


if __name__ == "__main__":
    smtp_thread = threading.Thread(target=start_smtp_server)
    smtp_thread.daemon = True
    smtp_thread.start()

    app.run(debug=True, use_reloader=False)
