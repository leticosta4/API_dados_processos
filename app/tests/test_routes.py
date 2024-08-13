from app import app
import json

def test_proceeding_data_accepts_full_json():
    response = app.test_client().post(
        '/dados_processo',
        data = json.dumps({"proceeding_number": "0710802-55.2018.8.02.0001"}),
        content_type='application/json',
    )

    output_data = response.get_json()
    if output_data.get('dados_primeiro_grau') and output_data.get('dados_segundo_grau'):
        ok = True if output_data.get('dados_primeiro_grau').get('area') else False
    else: ok = False

    assert response.status_code == 200 and ok == True

def test_proceeding_data_returns_no_number():
    response = app.test_client().post(
        '/dados_processo',
        data = json.dumps({"proceeding_number": ""}),
        content_type='application/json',
    )

    expected_output_data = {'erro': 'Número do processo é obrigatório'}
    
    assert response.status_code == 400 and response.get_json() == expected_output_data