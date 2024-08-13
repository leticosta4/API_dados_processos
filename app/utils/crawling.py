import time
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager

def driver_setup(): #preparando o driver do chrome
    options = ChromeOptions()
    options.add_argument("--headless") 

    service = ChromeService(executable_path=ChromeDriverManager().install())
    d = webdriver.Chrome(service=service, options=options)

    d.implicitly_wait(5) 
    return d

def dictionaries(sec, driver):
    unique_elements = {}
    if sec:
        unique_elements = {
            'class': '#classeProcesso > span:nth-child(1)',
            'matter': '#assuntoProcesso > span:nth-child(1)',
            'judge': '.div-conteudo > table:nth-child(13) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(4)', 
        }

        try: #as vezes essaa verificação é pedida pelo sit, outras vezes não
            driver.find_element(By.CSS_SELECTOR, ".modal__process-choice > input:nth-child(1)").click()
            driver.find_element(By.CSS_SELECTOR, "#botaoEnviarIncidente").click()

        except NoSuchElementException:
            print("Não foi requerida a confirmação com seleção do processo\n")
            pass

    else:
        unique_elements = {
            'class': '#classeProcesso',
            'matter': '#assuntoProcesso',
            'judge': '#juizProcesso', 
        }

    return unique_elements

def proceeding_verification(driver):
    print("Etapa de verificação da existência do processo iniciada")
    try:
        driver.find_element(By.CSS_SELECTOR, "#mensagemRetorno")
        return False  #processo não encontrado   
    except NoSuchElementException: pass

    return True 

def initial_search(driver, n1, n2):
    print("Etapa de busca inicial iniciada")
    driver.find_element(By.CSS_SELECTOR, "#numeroDigitoAnoUnificado").send_keys(n1)
    driver.find_element(By.CSS_SELECTOR, "#foroNumeroUnificado").send_keys(n2)
    try:
        driver.find_element(By.CSS_SELECTOR, "#botaoConsultarProcessos").click()
        if not proceeding_verification(driver): return False  #nenhum processo encontrado em primeiro grau

    except NoSuchElementException:
        print("Segundo grau")
        driver.find_element(By.CSS_SELECTOR, "#pbConsultar").click()
        if not proceeding_verification(driver): return False  #nenhum processo encontrado em segundo grau - colocar uma condição de nao existente

    return True  

def simple_data_collection(driver, second_degree_search):
    print("Etapa de coleta simples de dados iniciada")
    unique_elements = dictionaries(second_degree_search, driver) #etapa de confirmação se for processo de segundo grau - com condicional

    driver.find_element(By.CSS_SELECTOR, ".unj-link-collapse__show").click() #ja garantindo a exibicao de mais informações na pagina com o "mais"
    
    class_ = driver.find_element(By.CSS_SELECTOR, unique_elements['class']).text
    matter = driver.find_element(By.CSS_SELECTOR, unique_elements['matter']).text
    try: 
        judge = driver.find_element(By.CSS_SELECTOR, unique_elements['judge']).text
    except NoSuchElementException:
        print("elemento de juiz não encontrado")
        judge = "Não encontrado(a) na página"
        pass
    
    try: 
        distribuition_date = (driver.find_element(By.CSS_SELECTOR, "#dataHoraDistribuicaoProcesso").text)[:10] 
    except NoSuchElementException:
        print("elemento de data de distribuicao não encontrado")
        distribuition_date = "Não encontrada na página"
        pass

    area = driver.find_element(By.CSS_SELECTOR, "#areaProcesso > span:nth-child(1)").text

    try:
        legal_action_value = driver.find_element(By.CSS_SELECTOR, "#valorAcaoProcesso").text
    except NoSuchElementException:
        print("elemento de valor da ação não encontrado")
        legal_action_value = "Não encontrado na página"
        pass

    return [class_, area, matter, distribuition_date, judge, legal_action_value]

def proceeding_parts_collection(driver):
    proceeding_parts = {}
    
    try: #pode ter mais partes, entao talvez clicar no mais - usando js p clicar diretamente no elemento que ta coberto por outro
        mais_partes = driver.find_element(By.CSS_SELECTOR, "#linkpartes")
        driver.execute_script("arguments[0].scrollIntoView(true);", mais_partes)
        driver.execute_script("arguments[0].click();", mais_partes)

        tbody_proceeding_parts = driver.find_element(By.CSS_SELECTOR, '#tableTodasPartes > tbody:nth-child(1)')

    except NoSuchElementException:
        print("Não existe esse elemento para exibir mais partes do precesso")
        tbody_proceeding_parts = driver.find_element(By.CSS_SELECTOR, '#tablePartesPrincipais > tbody:nth-child(1)')

    except Exception as e:
        print(f"ERRO: {e}")
        print(f"EXCEÇÃO: {type(e).__name__}")

    proceeding_parts_rows = tbody_proceeding_parts.find_elements(By.TAG_NAME, 'tr')

    for row in proceeding_parts_rows:
        proceeding_parts_cells = row.find_elements(By.TAG_NAME, 'td') 

        if len(proceeding_parts_cells) >= 2:
            position = proceeding_parts_cells[0].find_element(By.TAG_NAME, 'span').text.strip() #a primeira célula é a função 
            names = proceeding_parts_cells[1].text.strip().split('\n')
            proceeding_parts[position] = names

    return proceeding_parts

def proceeding_updates_collection(driver):
    proceeding_updates = []
    try: #clicando no mais para acessar a lista de todas as movimentacaoes 
        mais_movimentacoes = driver.find_element(By.CSS_SELECTOR, "#linkmovimentacoes")
        driver.execute_script("arguments[0].scrollIntoView(true);", mais_movimentacoes)
        driver.execute_script("arguments[0].click();", mais_movimentacoes)

    except Exception as e:
        print(f"ERRO: {e}")
        if isinstance(e, NoSuchElementException): print("Não existe esse elemento para exibir mais movimentações do processo")
        else: print(f"EXCEÇÃO: {type(e).__name__}")

    tbody_proceeding_updates = driver.find_element(By.CSS_SELECTOR, '#tabelaTodasMovimentacoes')
    proceeding_updates_rows = tbody_proceeding_updates.find_elements(By.TAG_NAME, 'tr')

    for row in proceeding_updates_rows:
        temp_updates = []
        proceeding_updates_cells = row.find_elements(By.TAG_NAME, 'td')
        
        if len(proceeding_updates_cells) >= 3:
            date = proceeding_updates_cells[0].text.strip()
            move_title = proceeding_updates_cells[-1].text.strip()
            move_description_element = proceeding_updates_cells[-1].find_element(By.TAG_NAME, 'span')
            move_description = move_description_element.text.strip().replace('\n', '; ') if move_description_element.text.strip() else ""

            temp_updates.append(move_title)
            if move_description:
                temp_updates.append(move_description)
            
            proceeding_updates.append({'data': date, 'movimento': temp_updates})

    return proceeding_updates

def proceeding_search(n1, n2, url, second_degree_search):
    driver = driver_setup()
    driver.get(url)

    process_found = initial_search(driver, n1, n2)
    
    if not process_found:
        driver.quit()
        if second_degree_search == False: return {'erro': 'Nenhum processo encontrado para o número fornecido'}
        else: return 'Não existente. O processo não possui segundo grau.'

    basic_info = simple_data_collection(driver, second_degree_search)

    #coleta de partes do processo e movimentações, independentemente do grau
    print("Etapa de coleta complexa de dados iniciada")
    basic_info.append(proceeding_parts_collection(driver))
    basic_info.append(proceeding_updates_collection(driver))

    time.sleep(5)

    keys = ['classe', 'area', 'assunto', 'data_de_distribuicao', 'juiz', 'valor_da_acao', 'partes_do_processo', 'movimentacoes']
    collected_data = dict.fromkeys(keys)
    
    print("Etapa de armazenamento de dados iniciada")
    for key, value in zip(keys, basic_info):
        collected_data[key] = value

    driver.quit()
    return collected_data