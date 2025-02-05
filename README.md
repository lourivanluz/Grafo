# Teste tecnico API graph

Uma API em que o cliente poderá registrar um grafo para consulta futuras, além de funcionalidades como retorno da melhor rota e retorno de todas rotas possíveis

## Funcionalidades

- Registro de um Grafo no banco de dados
- Busca por Grafo no banco de dados
- Retorno de rotas de um determinado grafo
- Retorno da melhor rota em um determinado grafo

## Variáveis de Ambiente

Para rodar esse projeto, você vai precisar adicionar as seguintes variáveis de ambiente no seu .env;

- `DB_URI` URI utilizado para conexão com banco de dados;

# Endpoints base

[https://web-production-7c188.up.railway.app/](https://web-production-7c188.up.railway.app/)

# Como usar os Endpoints

As rotas da aplicação podem ser dividas em três categorias básicas:

- Registro e Busca de grafos salvos
- Retorno das possíveis rotas de um grafo
- Retorno das melhores rotas de um grafo

Logo abaixo seguem exemplos de cada rota aceita pela aplicação, junto com seu
comportamento esperado, os campos necessários para sua utilização e o que será
retornado pelo servidor.

## Rotas

- [Graph](#graph)
- [Routes](#routes)
- [Distance](#distance)

## Graph

### POST/graph

#### Descrição

```
    - Registra um novo grafo
```

_Envio:_

```json
{
  "data": [
    {
      "source": "A",
      "target": "B",
      "distance": 6
    },
    {
      "source": "A",
      "target": "E",
      "distance": 4
    },
    {
      "source": "B",
      "target": "A",
      "distance": 6
    },
    {
      "source": "B",
      "target": "C",
      "distance": 2
    },
    {
      "source": "B",
      "target": "D",
      "distance": 4
    },
    {
      "source": "C",
      "target": "B",
      "distance": 3
    },
    {
      "source": "C",
      "target": "D",
      "distance": 1
    },
    {
      "source": "C",
      "target": "E",
      "distance": 7
    },
    {
      "source": "D",
      "target": "B",
      "distance": 8
    },
    {
      "source": "E",
      "target": "B",
      "distance": 5
    },
    {
      "source": "E",
      "target": "D",
      "distance": 7
    }
  ]
}
```

_Resposta:_

```json
{
  "id": "81c35b6b-7e4d-4543-bb49-d1e61cf05f04",
  "data": [
    {
      "source": "A",
      "target": "B",
      "distance": 6
    },
    {
      "source": "A",
      "target": "E",
      "distance": 4
    },
    {
      "source": "B",
      "target": "A",
      "distance": 6
    },
    {
      "source": "B",
      "target": "C",
      "distance": 2
    },
    {
      "source": "B",
      "target": "D",
      "distance": 4
    },
    {
      "source": "C",
      "target": "B",
      "distance": 3
    },
    {
      "source": "C",
      "target": "D",
      "distance": 1
    },
    {
      "source": "C",
      "target": "E",
      "distance": 7
    },
    {
      "source": "D",
      "target": "B",
      "distance": 8
    },
    {
      "source": "E",
      "target": "B",
      "distance": 5
    },
    {
      "source": "E",
      "target": "D",
      "distance": 7
    }
  ]
}
```

### GET/graph/< graph_id >

#### Descrição

```
    - Busca no banco de dados pelo id enviado na url da requisição
```

_Envio:_

```json
nobody
```

_Resposta:_

#### Caso exista o grafo

```json
{
  "id": "81c35b6b-7e4d-4543-bb49-d1e61cf05f04",
  "data": [
    {
      "source": "A",
      "target": "B",
      "distance": 6
    },
    {
      "source": "A",
      "target": "E",
      "distance": 4
    },
    {
      "source": "B",
      "target": "A",
      "distance": 6
    },
    {
      "source": "B",
      "target": "C",
      "distance": 2
    },
    {
      "source": "B",
      "target": "D",
      "distance": 4
    },
    {
      "source": "C",
      "target": "B",
      "distance": 3
    },
    {
      "source": "C",
      "target": "D",
      "distance": 1
    },
    {
      "source": "C",
      "target": "E",
      "distance": 7
    },
    {
      "source": "D",
      "target": "B",
      "distance": 8
    },
    {
      "source": "E",
      "target": "B",
      "distance": 5
    },
    {
      "source": "E",
      "target": "D",
      "distance": 7
    }
  ]
}
```

#### Caso não exista o grafo

```json
{
  "error": "id not found"
}
```

## Routes

### Post/routes/< graphId >/from/< town1 >/to/< town2 >?maxStops=< maxStops >

#### Descrição

```
  - Retornará as possíveis rotas entre a `town1` e `town2`
  - Retornará uma lista vazia caso não tenha uma rota possível
  - Retornará uma lista vazia caso a cidade de origem ou destino não esteja no grafo
  - Query params opcionais aceito é:
  maxStops:inteiro - quantidade máxima de cidades visitadas por rota.

```

#### Disclaimer

Sabendo que a complexidade do problema de rotas é NP(Tempo polinomial não determinístico) isso significa que a cada nó ou conexão adicionada aumentará o tempo de resposta exponencialmente, por isso o uso da query param **maxStops** é importante para a velocidade da resposta.

_Envio:_

```json
nobody
```

_Resposta:_

#### Caso exista o grafo

```json
{
  "routes": [
    {
      "route": "AEDBC",
      "stops": 4
    },
    {
      "route": "AEBC",
      "stops": 3
    },
    {
      "route": "ABC",
      "stops": 2
    }
  ]
}
```

#### Caso não exista o grafo

```json
{
  "error": "id not found"
}
```

## Distance

### Post/distance/< graphId >/from/< town1 >/to/< town2 >

#### Descrição

```
    - Retornará as melhores rotas entre a `town1` e `town2`

```

_Envio:_

```json
nobody
```

_Resposta:_

#### Caso exista o grafo

```json
{
  "routes": [
    {
      "distance": 8,
      "path": ["A", "B", "C"]
    }
  ]
}
```

#### Caso não exista o grafo

```json
{
  "error": "id not found"
}
```

#### Caso não exista uma rota

```json
{
  "route": [
    {
      "distance": -1,
      "path": ["no have path"]
    }
  ]
}
```

#### Caso destino e origem forem iguais

```json
{
  "route": [
    {
      "distance": 0,
      "path": ["A"]
    }
  ]
}
```
