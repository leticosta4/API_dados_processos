from app import app
from flask import render_template, request, jsonify
from app.backend.data_handling import proceeding_num_validation, prepare_search_info, search_setup

@app.route("/index") 
@app.route("/") 
def index(): 
     return render_template('index.html') 

@app.route("/dados_processo", methods=['POST'])
def enviar_dados_processo():
    data = request.get_json() #recebendo o json como input do front
    proceeding_number = data.get('proceeding_number') 

    if not proceeding_number:
        return jsonify({'error': 'Número do processo é obrigatório'}), 400

    if not proceeding_num_validation(proceeding_number):
        return jsonify({'error': 'Número do processo inválido'}), 400
    
    nums, url_center = prepare_search_info(proceeding_number)
    collected_data = search_setup(nums[0], nums[1], url_center) #dicionario que vai ser mandado p o front como json

    return jsonify(collected_data), 200
