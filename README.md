# Real-Time Algorithms

Projeto simples em Python para simular o escalonamento de tarefas em tempo real usando o algoritmo Rate Monotonic (RM) e gerar um Diagrama de Gantt da execução.

## Conteúdo

- `main.py` - implementa o escalonador Rate Monotonic, calcula o hiperperíodo e plota um Diagrama de Gantt com `matplotlib`.

## Como usar

1. Instale as dependências:

```bash
pip install matplotlib numpy
```

2. Execute o script:

```bash
python main.py
```

3. O script exibirá um gráfico com o Diagrama de Gantt e os eventos de chegada e deadline das tarefas.

## Como funciona

- O escalonador RM atribui prioridade com base no período da tarefa: tarefas com período menor têm maior prioridade.
- O `hyperperiod` é calculado como o mínimo múltiplo comum dos períodos das tarefas.
- O agendador simula cada unidade de tempo até o hiperperíodo e registra a tarefa em execução.
- O gráfico mostra blocos de execução de cada tarefa e indica os instantes de chegada e deadline.

## Estrutura das tarefas

No `main.py`, cada tarefa é definida como um dicionário com as chaves:

- `name`: nome da tarefa
- `C`: tempo de computação exigido
- `T`: período da tarefa

Exemplo:

```python
{'name': 'Tarefa A', 'C': 3, 'T': 7}
```

## Personalização

Você pode alterar o conjunto de tarefas no final do `main.py` para testar outros cenários.

## Requisitos

- Python 3.8+
- `numpy`
- `matplotlib`
