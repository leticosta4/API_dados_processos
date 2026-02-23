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

Build inicial, preparando o ambiente com as dependências necessárias:
         
      docker compose build

Execução da API:

      docker compose up 

> (ou adicione a flag `-d` no final para rodar em background sem logs)


Desligamento dos container

      docker compose down

> (ou adicione `--volumes` para fazer a limpeza)


### Simulando requisição do projeto
Na ambiente de sua escolha, depois de executar os comandos docker necessários para inicialização do projeto:

- **Recomendação:** uso da extensão  `Thunder Client`  no VS Code, ou do Postman, para testes manuais com input e output (ambos na forma de JSON).

- **Formato do json:**

  ```
  {
      "proceeding_number": "<numero-do-processo>"
  }
  ```

### Testes (pytest)

- Todos os testes

      docker compose run api pytest

Com o pytest já instalado via [dependências](#execução-do-projeto), rode o comando:

- Teste específico:
   
      docker compose run api pytest tests/ -k <nome-da-funcao-do-teste>

ou 

      docker compose run api pytest <caminho-do-test> <nome-da-funcao-do-teste>

> e pode colocar a flag `-vv` para melhor detalhamento de logs

- Detalhamento nos testes de um certo arquivo :

      docker compose run api pytest -v app/tests/"nome do arquivo de teste"
