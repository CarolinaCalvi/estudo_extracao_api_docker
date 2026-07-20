# Estudo de Extracao de API

Este projeto e um estudo simples de consumo de API com Python usando a biblioteca `requests` e Docker.

O objetivo do codigo e consultar vagas na API da Gupy, buscando por um termo especifico e tratando a paginacao automaticamente para reunir todos os resultados.

## O que o codigo faz

1. Importa as bibliotecas `requests`, `json` e `math`.
2. Faz uma requisição para a API:
   `https://employability-portal.gupy.io/api/v1/jobs`
3. Busca os dados em formato JSON.
4. Exibe no terminal o conteúdo retornado na primeira requisição.
5. Lê as informações de paginação presentes em `pagination`, como:
   `total`, `limit` e `offset`.
6. Calcula a quantidade de posições paginadas com base em `total / limit`.
7. Usa `math.ceil()` para arredondar esse valor para cima.
8. Percorre os valores de `offset` de `0` até `total_offset`.
9. Faz uma nova requisição para cada `offset`.
10. Armazena cada resposta retornada em uma lista chamada `resultados_offsets`.
11. Salva essa lista no arquivo `resultado_api_docker.json`.

## Como a logica funciona

* `total`: quantidade total de vagas encontradas.
* `limit`: quantidade de registros retornados pela API em cada resposta.
* `offset`: valor utilizado para navegar entre os resultados paginados.

No código atual, o valor de `total / limit` é usado para estimar quantas posições paginadas precisam ser consultadas. Em seguida, `math.ceil()` garante que, mesmo quando a divisão não for exata, a última parte dos resultados também seja considerada.

Exemplo:

* `total = 644`
* `limit = 10`
* `total / limit = 64.4`
* `math.ceil(64.4) = 65`


Com isso, o programa descobre quantas paginas existem e faz novas requisicoes ate trazer todos os dados da busca.

## Estrutura do arquivo gerado

O arquivo `resultado_api_docker.json` será salvo com uma lista de respostas da API, contendo os dados retornados em cada requisição feita para cada `offset` consultado.

## Requisitos

Este projeto foi executado em **Windows**, utilizando **Python 3.14.5**.

### 1. Instalar o Python

Baixe e instale o Python:

https://www.python.org/downloads/

Durante a instalação, marque a opção para adicionar o Python ao PATH.


## Execução com Docker


### Build da imagem

```bash
docker build -t estudo-extracao-api-docker .
```

### Executar o container

```bash
docker run --rm -v "${PWD}:/app" estudo-extracao-api-docker
```

Esse comando permite que o arquivo `resultado_api_docker.json` seja salvo diretamente na máquina.


## Observação

Este projeto tem foco em estudo da lógica de paginação e consumo de APIs. Dependendo do comportamento da API, pode ser necessário ajustar a forma de avanço do `offset`, o tratamento de erros e o intervalo entre as requisições.
