# Real-Time Algorithms

Repositório com três implementações educativas de escalonamento de tarefas em tempo real:

- `rate-monotonic/` - simulação do algoritmo Rate Monotonic (RM) com gráfico de Gantt.
- `cyclic-executive/` - simulação de um executivo cíclico com frames e cronograma estático.
- `sporadic-server/` - simulação de um Servidor Esporádico para tarefas aperiódicas.

## Como executar

Para cada subprojeto, entre na pasta correspondente e execute o script principal:

```bash
cd rate-monotonic
python main.py
```

```bash
cd cyclic-executive
python main.py
```

```bash
cd sporadic-server
python main.py
```

## Estrutura do repositório

- `rate-monotonic/main.py` - escalonador RM e geração de gráfico de Gantt.
- `cyclic-executive/main.py` - executivo cíclico com simulação de frames.
- `sporadic-server/main.py` - servidor esporádico para tarefas aperiódicas e periódicas.
- `rate-monotonic/README.md` - documentação específica do algoritmo Rate Monotonic.
- `cyclic-executive/README.md` - documentação específica do executivo cíclico.
- `sporadic-server/README.md` - documentação específica do Servidor Esporádico.

## Requisitos

- Python 3.8+
- `numpy` e `matplotlib` para os subprojetos `rate-monotonic` e `sporadic-server`

## Observação

Os READMEs dentro de cada pasta explicam melhor os detalhes de cada algoritmo e como personalizar os conjuntos de tarefas.
