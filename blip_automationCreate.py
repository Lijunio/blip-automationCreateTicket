from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/processar_dados', methods=['POST'])
def processar_dados():
    try:
        dados = request.get_json()

        # Extrair os dados do JSON
        nome = dados.get('nomeUsuario')
        email = dados.get('emailUsuario')
        telefone = dados.get('telefoneUsuario')
        estabelecimento = dados.get('estabelecimentoUsuario')

        # Dados a serem enviados para o GLPI
        dados_formulario = {
            'campo_nome': nome,
            'campo_email': email,
            'campo_telefone': telefone,
            'campo_estabelecimento': estabelecimento,
            # Adicione outros campos conforme necessário
        }

        # URL do endpoint do GLPI para o formulário desejado
        url_glpi = 'https://www.telessaude.hc.ufmg.br/glpi/marketplace/formcreator/front/formdisplay.php?id=34'

        # Enviar dados para o GLPI
        response = requests.post(url_glpi, data=dados_formulario)

        return jsonify({'status': 'success'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
