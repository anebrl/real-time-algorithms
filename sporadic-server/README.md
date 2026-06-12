# Sporadic Server

Projeto em Python para simular um escalonador com Servidor Esporádico para tarefas periódicas e aperiódicas.

## Descrição

O algoritmo usa um servidor esporádico para aceitar e servir tarefas aperiódicas enquanto mantém o escalonamento das tarefas periódicas por prioridade. A simulação gera um Diagrama de Gantt mostrando quando cada tarefa é executada e quando o servidor atende eventos aperiódicos.

## Como usar

1. Instale as dependências:

```bash
pip install matplotlib numpy
```

2. Execute o script:

```bash
python sporadic-server/main.py
```

3. O script exibirá no terminal os eventos de chegada, reabastecimento e conclusão, e depois exibirá um gráfico de Gantt.

## O que o script faz

- Define tarefas periódicas com período, tempo de computação e prioridade.
- Define um servidor esporádico com capacidade inicial (`Cs`), período de reabastecimento (`Ts`) e prioridade.
- Recebe eventos aperiódicos com tempo de chegada e carga de computação.
- Simula a execução passo a passo e desenha um Diagrama de Gantt.

## Estrutura das tarefas

- `periodic_tasks`: lista de tarefas periódicas com `name`, `C`, `T`, `D` e `Prio`.
- `sporadic_server`: dicionário com `Cs`, `Ts` e `Prio`.
- `aperiodic_events`: eventos com `name`, `C`, `original_C` e `arrival_time`.

## Personalização

- Altere `periodic_tasks`, `sporadic_server` e `aperiodic_events` no `main.py` para testar outros cenários.
- Ajuste `SIMULATION_TIME` para mudar a duração da simulação.

## Requisitos

- Python 3.8+
- `numpy`
- `matplotlib`
