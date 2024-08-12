from app.backend.data_handling import proceeding_num_validation, break_number_down, prepare_search_info, search_setup

def test_proceeding_num_validation_returns_true():
    actual_bool = proceeding_num_validation(num_input='0710802-55.2018.8.02.0001')
    assert actual_bool == True

def test_proceeding_num_validation_missing_hyphen_returns_false():
    actual_bool = proceeding_num_validation(num_input='071080255.2018.8.02.0001')
    assert actual_bool == False

def test_proceeding_num_validation_missing_dot_returns_false():
    actual_bool = proceeding_num_validation(num_input='0710802-55.2018202.0001')
    assert actual_bool == False

def test_proceeding_num_validation_contains_invalid_characters_returns_false():
    actual_bool = proceeding_num_validation(num_input='0710802-5a.2018.8.02.0001')
    assert actual_bool == False

def test_proceeding_num_validation_incorrect_length_returns_false():
    actual_bool = proceeding_num_validation(num_input='0710802-55.2018.8.02.001')
    assert actual_bool == False

def test_break_number_down_returns_list_items():
    list_ = break_number_down(num='0710802-55.2018.8.02.0001')
    assert len(list_[0]) == 13 and len(list_[1]) == 4 and len(list_[-1]) == 4
    assert list_[0] == '0710802552018'
    assert list_[1] == '0001'
    assert list_[-1] == '8.02'

def test_prepare_search_info_returns_tribunal():
    l, tribunal = prepare_search_info(num_processo='07108055.2018.8.02.0001')
    right_trib = True if tribunal == 'www2.tjal' or tribunal == 'esaj.tjce' else False

    assert right_trib == True

def test_search_setup_returns_final_dict():
    """
    checar se o dicionario maior tem pelo menos essa primeira chave 'dados_primeiro_grau'
    e se nao tiver ver se possui a msg de erro
    => provavelmente quebrar em 2 funcoes p testes
    """ 
    pass