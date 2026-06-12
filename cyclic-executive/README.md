# Executivo Cíclico

Projeto em Python para simular um executivo cíclico de escalonamento de tarefas em tempo real.

## Descrição

Este algoritmo organiza tarefas em um cronograma periódico de frames. Cada frame contém um conjunto de tarefas cujo tempo total de execução cabe no tamanho de frame definido. O programa calcula o hiperperíodo e executa a simulação do executivo cíclico mostrando a sequência de tarefas e tempo ocioso.

## Estrutura do código

- `main.py` - define tarefas com período e tempo de execução, calcula o hiperperíodo, define o cronograma estático e simula o executivo cíclico.

## Como usar

1. Instale as dependências:

```bash
pip install python
```

2. Execute o script:

```bash
python cyclic-executive/main.py
```

3. O script mostrará no terminal a execução de cada tarefa por frame, incluindo o tempo ocioso restante no final de cada frame.

## Parâmetros principais

- `tasks`: dicionário com tarefas, cada uma com `T` (período) e `C` (tempo de computação).
- `FRAME_SIZE`: tamanho do frame em unidades de tempo.
- `hyperperiod`: mínimo múltiplo comum dos períodos, que define o ciclo maior após o qual o padrão se repete.
- `schedule`: cronograma estático das tarefas para cada frame.

## Personalização

- Altere `tasks` para testar outros conjuntos de tarefas.
- Ajuste `FRAME_SIZE` e `schedule` para aprender como o executivo cíclico pode acomodar diferentes tarefas e frames.

## Requisitos

- Python 3.8+

## Observações

- `time.sleep` é usado apenas para acelerar a visualização da simulação e não representa tempo real do sistema.
