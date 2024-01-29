from flask import Flask, request, jsonify
import requests

app = Flask(__name__)
@app.route('/receive_data', methods=['POST'])
def receive_data():
    data = request.json

    nome_usuario = data.get('nomeUsuario', '')
    email_usuario = data.get('emailUsuario', '')
    telefone_usuario = data.get('telefoneUsuario', '')
    estabelecimento_usuario = data.get('estabelecimentoUsuario', '')

    # Agora você pode chamar sua função para preencher o formulário ou fazer o que for necessário
    preencher_formulario(nome_usuario, email_usuario, telefone_usuario, estabelecimento_usuario)

    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(debug=True)
