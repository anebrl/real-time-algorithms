import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

def calculate_hyperperiod(periods):
    """Calcula o hiperperíodo (Mínimo Múltiplo Comum) dos períodos das tarefas."""
    # A função np.lcm.reduce encontra o MMC de uma lista de números
    lcm = np.lcm.reduce(periods)
    return lcm

def rate_monotonic_scheduler(tasks):
    """
    Simula o escalonador Rate Monotonic (RM).

    Args:
        tasks (list): Uma lista de dicionários, onde cada dicionário representa uma tarefa.
                      Cada tarefa deve ter as chaves: 'name', 'C' (computação), 'T' (período).

    Returns:
        tuple: Uma tupla contendo o histórico do escalonamento (gantt_data) e o hiperperíodo.
    """
    # Atribui prioridade baseada no período (menor período, maior prioridade)
    # Ordena a lista de tarefas em ordem crescente de período
    tasks.sort(key=lambda x: x['T'])

    periods = [task['T'] for task in tasks]
    hyperperiod = calculate_hyperperiod(periods)

    # Inicializa variáveis de estado para cada tarefa
    for task in tasks:
        task['remaining_C'] = 0  # Tempo de computação restante para a instância atual
        task['next_arrival'] = 0 # Próximo momento de chegada da tarefa

    gantt_data = [] # Lista para armazenar o nome da tarefa em execução a cada instante de tempo
    
    # Loop de simulação, passo a passo no tempo (de 0 até o hiperperíodo)
    for t in range(hyperperiod):
        # 1. Verifica a chegada de novas instâncias de tarefas no tempo 't'
        for task in tasks:
            if t >= task['next_arrival']:
                # Verifica se a tarefa anterior terminou (deadline miss check - opcional)
                if task['remaining_C'] > 0:
                    print(f"AVISO: Deadline perdida para a tarefa {task['name']} no tempo {t}")
                
                # Reseta o tempo de computação e calcula a próxima chegada
                task['remaining_C'] = task['C']
                task['next_arrival'] += task['T']

        # 2. Seleciona a tarefa de maior prioridade pronta para executar
        # Filtra as tarefas que chegaram e ainda precisam de tempo de CPU
        ready_tasks = [task for task in tasks if task['remaining_C'] > 0]

        current_task = None
        if ready_tasks:
            # Como a lista 'tasks' já foi ordenada por período, a primeira tarefa
            # na lista 'ready_tasks' é a de maior prioridade.
            current_task = ready_tasks[0]

        # 3. "Executa" a tarefa, decrementa seu tempo restante e registra no log do Gantt
        if current_task:
            gantt_data.append(current_task['name'])
            current_task['remaining_C'] -= 1
        else:
            # Se não há tarefas prontas, a CPU fica ociosa ('Idle')
            gantt_data.append('Idle')

    return gantt_data, hyperperiod

def plot_gantt_chart(gantt_data, tasks, hyperperiod):
    """
    Gera um Diagrama de Gantt a partir dos dados do escalonador.
    """
    fig, ax = plt.subplots(figsize=(20, 5))

    task_names = [task['name'] for task in tasks]
    y_pos = {name: i for i, name in enumerate(task_names)}
    y_pos['Idle'] = -1 # Garante que 'Idle' não seja plotado

    # Define uma paleta de cores para as tarefas
    colors = plt.cm.get_cmap('viridis', len(task_names))
    task_colors = {task['name']: colors(i) for i, task in enumerate(tasks)}

    # Agrupa blocos de execução contíguos para desenhar os retângulos
    current_task_name = gantt_data[0]
    start_time = 0

    for t in range(1, hyperperiod):
        if gantt_data[t] != current_task_name:
            if current_task_name != 'Idle':
                # Desenha o bloco da tarefa que acabou de terminar
                ax.add_patch(patches.Rectangle(
                    (start_time, y_pos[current_task_name] - 0.4), # Posição (x, y)
                    t - start_time, # Largura (duração)
                    0.8, # Altura
                    facecolor=task_colors[current_task_name],
                    edgecolor='black'
                ))
            current_task_name = gantt_data[t]
            start_time = t

    # Plota o último bloco de execução
    if current_task_name != 'Idle':
         ax.add_patch(patches.Rectangle(
            (start_time, y_pos[current_task_name] - 0.4),
            hyperperiod - start_time,
            0.8,
            facecolor=task_colors[current_task_name],
            edgecolor='black'
        ))

    # Configurações visuais do gráfico
    ax.set_xlim(0, hyperperiod)
    ax.set_ylim(-0.5, len(task_names) - 0.5)

    ax.set_yticks(range(len(task_names)))
    ax.set_yticklabels([f"{task['name']} (Prioridade {i+1})" for i, task in enumerate(tasks)])
    ax.set_xlabel('Tempo (unidades)')
    ax.set_ylabel('Tarefas')
    ax.set_title('Diagrama de Gantt - Escalonamento Rate Monotonic (RM)')
    ax.grid(True, axis='x', linestyle=':')

    # Adiciona marcadores de chegada (instanciação) e deadline
    for i, task in enumerate(tasks):
        # Marcador de chegada (triângulo vermelho)
        for arrival in range(0, hyperperiod, task['T']):
            plt.plot(arrival, i, 'rv', markersize=8, label='Chegada' if arrival == 0 and i == 0 else "")
        # Marcador de deadline (X preto)
        for deadline in range(task['T'], hyperperiod + 1, task['T']):
            plt.plot(deadline, i, 'kx', markersize=8, label='Deadline' if deadline == task['T'] and i == 0 else "")
    
    # Cria a legenda do gráfico
    legend_patches = [patches.Patch(color=task_colors[t['name']], label=f"Execução {t['name']}") for t in tasks]
    handles, labels = plt.gca().get_legend_handles_labels()
    by_label = dict(zip(labels, handles)) # Remove legendas duplicadas
    plt.legend(handles=legend_patches + list(by_label.values()), bbox_to_anchor=(1.01, 1), loc='upper left')
    
    plt.tight_layout(rect=[0, 0, 0.85, 1])
    plt.show()


# --- Ponto de Entrada Principal ---
if __name__ == "__main__":
    # Definição do conjunto de tarefas da Tabela 1
    task_set = [
        {'name': 'Tarefa A', 'C': 3, 'T': 7},
        {'name': 'Tarefa B', 'C': 2, 'T': 12},
        {'name': 'Tarefa C', 'C': 2, 'T': 20},
    ]

    # Executa o escalonador para obter a sequência de execução
    schedule, simulation_time = rate_monotonic_scheduler(list(task_set)) # Passa uma cópia

    # Gera e exibe o Diagrama de Gantt
    # Reordena a lista original por prioridade para o gráfico
    task_set.sort(key=lambda x: x['T'])
    plot_gantt_chart(schedule, task_set, simulation_time)