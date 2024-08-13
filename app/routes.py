from app import app
from flask import request, jsonify#,render_template
from app.utils.data_handling import proceeding_num_validation, prepare_search_info, search_setup

# @app.route("/index") 
# @app.route("/") 
# def index(): 
#      return render_template('index.html') 

@app.route('/dados_processo', methods=['POST'])
def proceeding_data():
    data = request.get_json()  #recebendo o json como input do front
    proceeding_number = data.get('proceeding_number') 

    if not proceeding_number:
        return jsonify({'erro': 'Número do processo é obrigatório'}), 400

    if not proceeding_num_validation(proceeding_number):
        return jsonify({'erro': 'Número do processo inválido'}), 400

    nums, url_center = prepare_search_info(proceeding_number)
    collected_data, status_code = search_setup(nums[0], nums[1], url_center)  #dicionario a ser levado como json para o front e status code

    if isinstance(collected_data, dict):
        if not collected_data: 
            return jsonify({'erro': 'Dicionário final vazio'}), 404
        return jsonify(collected_data), status_code
    else:
        return jsonify({'erro': 'Erro na obtenção dos dados'}), 500