# Real-Time Algorithms

Repositório com duas implementações educativas de escalonamento de tarefas em tempo real:

- `rate-monotonic/` - simulação do algoritmo Rate Monotonic (RM) com gráfico de Gantt.
- `cyclic-executive/` - simulação de um executivo cíclico com frames e cronograma estático.

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

## Estrutura do repositório

- `rate-monotonic/main.py` - escalonador RM e geração de gráfico de Gantt.
- `cyclic-executive/main.py` - executivo cíclico com simulação de frames.
- `rate-monotonic/README.md` - documentação específica do algoritmo Rate Monotonic.
- `cyclic-executive/README.md` - documentação específica do executivo cíclico.

## Requisitos

- Python 3.8+
- `numpy` e `matplotlib` para o subprojeto `rate-monotonic`

## Observação

Os READMEs dentro de cada pasta explicam melhor os detalhes de cada algoritmo e como personalizar os conjuntos de tarefas.
