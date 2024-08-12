from app.backend.crawling import proceeding_search

def proceeding_num_validation(num_input):
    if len(num_input) != 25: return False

    if num_input[7] != '-': return False
    
    dots = [num_input[10], num_input[15], num_input[17], num_input[20]]
    if not all(n == '.' for n in dots): return False

    raw_number = num_input.replace('-', '').replace('.', '')
    if not raw_number.isdigit(): return False

    return True

def break_number_down(num):
    pt1 = num[:15].replace("-", "").replace(".", "")
    trib = num[16:20]
    pt2 = num[-4:]

    return [pt1, pt2, trib]

def prepare_search_info(num_processo):
    info = break_number_down(num_processo)
    url_center = 'www2.tjal' if info[-1] == '8.02' else 'esaj.tjce' #se for 8.06 é do ceara
         
    return info, url_center
   
def search_setup(num1, num2, url_center):
    """fazer primeiro com o primeiro grau e depois com o segundo"""
    proceeding_data = {}
    search_url_primeiro_grau = f"https://{url_center}.jus.br/cpopg/open.do"
    search_url_segundo_grau = f"https://{url_center}.jus.br/cposg5/open.do"

    try: 
        primeiro_grau = proceeding_search(num1, num2, search_url_primeiro_grau, False)
        proceeding_data['dados_primeiro_grau'] =  primeiro_grau
        try:
            segundo_grau = proceeding_search(num1, num2, search_url_segundo_grau, True) #rever isso daqui p quando um processo nao tiver o seu segundo grau
            print("\n\nDICIONARIO SEGUNDO GRAU:", segundo_grau)
            proceeding_data['dados_segundo_grau'] = segundo_grau

        except Exception as e:
            print(f"Erro no retorno do dicionário com as informações de segundo grau do processo => {e}")
            print(f"EXCEÇÃO: {type(e).__name__}")
           
    except Exception as e:
            print(f"Erro no retorno do dicionário com as informações de primeiro grau do processo => {e}")
            print(f"EXCEÇÃO: {type(e).__name__}")
    
    return proceeding_data
    