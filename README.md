# API_dados_processos
API desenvolvida, juntamente com web crawling, para a busca, nos tribunais de Justiça de Alagoas ou do Ceará, de múltiplos dados referentes a processos, a primeiro e segundo grau, dependendo da existência dos mesmos. A busca é feita a partir do número do processo desejado, enviado na entrada em um JSON. 

## Informações Gerais

### Possíveis URLs de busca
**Alagoas:**
- Busca em 1º grau: https://www2.tjal.jus.br/cpopg/open.do
- Busca em 2º grau: https://www2.tjal.jus.br/cposg5/open.do

**Ceará:**
- Busca em 1º grau: https://esaj.tjce.jus.br/cpopg/open.do
- Busca em 2º grau: https://esaj.tjce.jus.br/cposg5/open.do


### Formatos dos números de processo
- TJAL: `NNNNNNN-DD.AAAA.8.02.OOOO`
- TJCE: `NNNNNNN-DD.AAAA.8.06.OOOO`


### Dados que podem ser coletados nessa API
- Classe
- Área
- Assunto
- Data de Distribuição
- Juiz
- Valor da Ação
- Partes do Processo
- Listas das Movimentações (com data e movimento)


### Principais ferramentas utilizadas
- Framework Web: [Flask](https://flask.palletsprojects.com/en/3.0.x/)
- Para automação/web scraping:
  - [Selenium-webdriver]( https://www.selenium.dev/documentation/webdriver/)
  - [Webdriver-manager](https://pypi.org/project/webdriver-manager/)
- Para realização de testes: [pytest](https://docs.pytest.org/en/stable/)
- Navegador usado pelo webdriver_manager: [Chrome](https://www.google.com/chrome/browser-tools/)
- Entre outras

## Tutorial

### Criação de um ambiente virtual
 - Dentro da pasta do projeto, rodar no terminal:
   
         python3 -m venv "nome do ambiente virtual"

 - Para ativar o ambiente virtual:
   - Linux:
   
         source "nome do ambiente virtual"/bin/activate
   - Windows:
         
         "nome do ambiente virtual"\Scripts\activate.bat


### Instalação das dependências 
Dentro da pasta do projeto, rodar no terminal:
         
      pip install -r requirements.txt

### Execução do projeto
Na IDE de sua escolha, rode o arquivo `run.py` para inicilização da API.

- **Recomendação:** uso da extensão  `Thunder Client`  no VS Code para testes manuais com input e output (ambos na forma de JSON).

- **Formato do json:**

  ```
  {
      "proceeding_number": "<numero-do-processo>"
  }
  ```

### Rodando testes com pytest
Com o pytest já instalado via [dependências](#execução-do-projeto), rode o comando:

- Todos os testes:

      pytest ./app/tests/

- Teste específico:
   
      pytest ./app/tests/ -k "nome da função do teste"

- Detalhamento nos testes de um certo arquivo :

      pytest -v app/tests/"nome do arquivo de teste"
