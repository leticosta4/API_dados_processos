import pytest
from app.utils.crawling import driver_setup, dictionaries, initial_search, simple_data_collection, proceeding_parts_collection

temp_driver = driver_setup()
url1 = 'https://www2.tjal.jus.br/cpopg/show.do?processo.codigo=01000O7550000&processo.foro=1&processo.numero=0710802-55.2018.8.02.0001'
url2 = 'https://www2.tjal.jus.br/cposg5/show.do?processo.codigo=P00006BXP0000'

@pytest.mark.parametrize("test_sec, test_driver, expected_dict", [
    (True, temp_driver, {'class': '#classeProcesso > span:nth-child(1)', 'matter': '#assuntoProcesso > span:nth-child(1)', 'judge': '.div-conteudo > table:nth-child(13) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(4)'}),
    (False, temp_driver, {'class': '#classeProcesso', 'matter': '#assuntoProcesso', 'judge': '#juizProcesso'})
])
def test_dictionaries(test_sec, test_driver, expected_dict):
    assert dictionaries(test_sec, test_driver) == expected_dict

@pytest.mark.parametrize("temp_driver, test_n1, test_n2, expected_bool", [
    (temp_driver, '0710802552018', '0001', True),
    (temp_driver, '1111111111111', '0001', False)
])
def test_initial_search(temp_driver, test_n1, test_n2, expected_bool):
    temp_driver.get('https://www2.tjal.jus.br/cpopg/open.do')
    assert initial_search(temp_driver, test_n1, test_n2) == expected_bool
    #talvez fechar o driver aqui 

@pytest.mark.parametrize("test_url, temp_driver, test_grau2, expeted_list", [
    (url1, temp_driver, False, ["Procedimento Comum Cível", "Cível", "Dano Material", "02/05/2018", "José Cícero Alves da Silva", "R$ 281.178,42"]),
    (url2, temp_driver, True, ["Apelação Cível", "Cível", "Obrigações", "Não encontrada na página", "José Cícero Alves da Silva", "281.178,42"])])
def test_simple_data_collection(test_url, temp_driver, test_grau2, expeted_list):
    temp_driver.get(test_url)
    assert simple_data_collection(temp_driver, test_grau2) == expeted_list

@pytest.mark.parametrize("test_url, temp_driver, expected_dict_keys", [
    (url1, temp_driver, ['Autor', 'Autora', 'Ré', 'Réu']),
    (url2, temp_driver, ['Apelante:', 'Apelado:', 'Apelada:'])
])
def test_proceeding_parts_collection(test_url, temp_driver, expected_dict_keys):
    temp_driver.get(test_url)
    assert sorted(proceeding_parts_collection(temp_driver).keys()) == sorted(expected_dict_keys)

#faltam ainda testes p 2 funcoes do crawling, mas n sei se faço ainda ou n