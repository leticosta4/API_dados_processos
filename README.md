# API_dados_processos
API desenvolvida, juntamente com web crawling, para a busca, nos tribunais de Justiça de Alagoas ou do Ceará, de múltiplos dados referentes a processos, a primeiro e segundo grau, dependendo da existência dos mesmos. A busca é feita a partir do número do processo desejado, enviado na entrada em um JSON.

### Dados coletados
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
- [Selenium-webdriver]( https://www.selenium.dev/documentation/webdriver/)
- [Webdriver-manager](https://pypi.org/project/webdriver-manager/)



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

- <b>Recomendação:</b> uso da extensão  `Thunder Client`  no VS Code para testes manuais com input e output (ambos na forma de JSON).

### Rodando testes com pytest
Com o pytest já instalado via [dependências](#execução-do-projeto), rode o comando:

- Todos os testes:

      pytest ./app/tests/

- Teste específico:
   
      pytest ./app/tests/ -k "nome da função do teste"