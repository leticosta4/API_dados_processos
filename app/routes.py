from app import app
from flask import request, jsonify#,render_template
from app.backend.data_handling import proceeding_num_validation, prepare_search_info, search_setup

# @app.route("/index") 
# @app.route("/") 
# def index(): 
#      return render_template('index.html') 

@app.route("/dados_processo", methods=['POST'])
def proceeding_data():
    data = request.get_json() #recebendo o json como input do front
    proceeding_number = data.get('proceeding_number') 

    if not proceeding_number:
        return jsonify({'error': 'Número do processo é obrigatório'}), 400

    if not proceeding_num_validation(proceeding_number):
        return jsonify({'error': 'Número do processo inválido'}), 400
    
    nums, url_center = prepare_search_info(proceeding_number)
    collected_data = search_setup(nums[0], nums[1], url_center) #dicionario que vai ser mandado p o front como json

    if isinstance(collected_data, dict):
        return jsonify(collected_data), 200
    else:
        return f"Erro na obtençao no dicionario com os dados", 400
    
