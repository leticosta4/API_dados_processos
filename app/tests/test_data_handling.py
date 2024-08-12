from app.backend.data_handling import proceeding_num_validation, break_number_down, prepare_search_info, search_setup
import pytest

@pytest.mark.parametrize("test_input, expected", [('0710802-55.2018.8.02.0001', True),
                                                 ('071080255.2018.8.02.0001', False),
                                                 ('0710802-55.2018202.0001', False),
                                                 ('0710802-5a.2018.8.02.0001', False),
                                                 ('0710802-55.2018.8.02.001', False)])
def test_proceeding_num_validation_returns_proper_bool(test_input, expected):
    assert proceeding_num_validation(test_input) == expected

def test_break_number_down_returns_list_items():
    list_ = break_number_down(num='0710802-55.2018.8.02.0001')
    assert len(list_[0]) == 13 and len(list_[1]) == 4 and len(list_[-1]) == 4
    assert list_[0] == '0710802552018' and list_[1] == '0001' and list_[-1] == '8.02'

@pytest.mark.parametrize("test_input, expected_tribunal",[('0710802-55.2018.8.02.0001', 'www2.tjal'), ('0070337-91.2008.8.06.0001', 'esaj.tjce')])
def test_prepare_search_info_returns_tribunal(test_input, expected_tribunal):
    l, tribunal = prepare_search_info(test_input)
    assert tribunal == expected_tribunal

def test_search_setup_returns_full_dict():
    two_keys = False
    expected_dict, expected_status_code = search_setup('0710802552018', '0001', 'www2.tjal')
    if expected_dict.get('dados_primeiro_grau') and expected_dict.get('dados_segundo_grau'): two_keys = True

    assert two_keys == True and expected_status_code == 200

def test_search_setup_returns_2nd_dict_empty():
    expected_dict, s = search_setup('0706553222022', '0001', 'www2.tjal')
    assert expected_dict['dados_segundo_grau'] == 'Não existente. O processo não possui segundo grau.'

def test_search_setup_returns_error_not_found(): 
    expected_msg, expected_status_code = search_setup('1111111911111', '1111', 'www2.tjal')
    assert expected_msg == {'erro': 'Nenhum processo encontrado para o número fornecido'} and expected_status_code == 404
