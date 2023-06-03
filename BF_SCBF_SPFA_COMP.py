from collections import deque
import time
from memory_profiler import memory_usage
import matplotlib.pyplot as plt
import random
from memory_profiler import memory_usage

# Implementation of Normal Bellman Ford Algorith
def bellman_ford(graph, source):
    distance = {}
    for node in graph:
        distance[node] = float('Inf')  # Initially all nodes are at infinite distance
    distance[source] = 0

    for _ in range(len(graph) - 1):  # Relax edges |V| - 1 times
        for node in graph:
            for neighbour in graph[node]:
                # If the distance to the neighbour is lower by going through the current node
                if distance[node] != float('Inf') and distance[node] + graph[node][neighbour] < distance[neighbour]:
                    distance[neighbour] = distance[node] + graph[node][neighbour]

    # Check for negative weight cycles
    for node in graph:
        for neighbour in graph[node]:
            if distance[node] != float('Inf') and distance[node] + graph[node][neighbour] < distance[neighbour]:
                raise ValueError('Graph contains a negative-weight cycle')

    return distance

#Implementation of Enhnaced SCBF
def scbf(graph, source):
    # Step 1: Prepare the distance for every node
    distance = {node: float('infinity') for node in graph}
    distance[source] = 0

    # Step 2: Relax edges
    for _ in range(len(graph) - 1):
        updated = False
        for node in graph:
            for neighbour in graph[node]:
                # If the distance between the node and the neighbour is lower than the one I have now
                if distance[neighbour] > distance[node] + graph[node][neighbour]:
                    distance[neighbour] = distance[node] + graph[node][neighbour]
                    updated = True

        # Short-circuit if no updates were made
        if not updated:
            break

    # Step 3: Check for negative weight cycles
    for node in graph:
        for neighbour in graph[node]:
            assert distance[neighbour] <= distance[node] + graph[node][neighbour]

    return distance


#Implementation of Enhanced SPFA
def spfa(graph, source):
    # Step 1: Prepare the distance for every node
    distance = {node: float('infinity') for node in graph}
    distance[source] = 0

    # Create a queue for the nodes to visit, and a set of visited nodes
    queue = deque([source])
    in_queue = {node: False for node in graph}
    in_queue[source] = True

    # Step 2: Relax edges
    while queue:
        node = queue.popleft()
        in_queue[node] = False

        for neighbour in graph[node]:
            # If the distance between the node and the neighbour is lower than the one I have now
            if distance[neighbour] > distance[node] + graph[node][neighbour]:
                distance[neighbour] = distance[node] + graph[node][neighbour]

                # If the neighbour node is not in the queue, add it
                if not in_queue[neighbour]:
                    queue.append(neighbour)
                    in_queue[neighbour] = True

    # Step 3: Check for negative weight cycles
    for node in graph:
        for neighbour in graph[node]:
            assert distance[neighbour] <= distance[node] + graph[node][neighbour]

    return distance



#Performance Analysis Function
def analyze_performance(algorithm, graph, source):
    
    # Record the start time
    start_time = time.time()

    # Record the initial memory usage
    start_memory = memory_usage()[0]

    # Run the algorithm
    algorithm(graph, source)

    # Record the final time
    end_time = time.time()

    # Record the final memory usage
    end_memory = memory_usage()[0]

    # Calculate the time and memory used
    time_used = end_time - start_time
    memory_used = end_memory - start_memory

    print(f"Time used by {algorithm.__name__}: {time_used} seconds")
    print(f"Memory used by {algorithm.__name__}: {memory_used} MiB")


# Your graph generating function
def generate_graph(n):
    graph = {}
    for i in range(n):
        graph[i] = {j: random.randint(1, 100) for j in range(i+1, n)}
    return graph


# Function to draw the denerated graph
def draw_graphs(graph):
    G = nx.DiGraph()
    for node, edges in graph.items():
        for edge, weight in edges.items():
            G.add_edge(node, edge, weight=weight)

    # shell_layout instead of spring_layout
    pos = nx.shell_layout(G)

    nx.draw(G, pos, with_labels=True, connectionstyle='arc3, rad = 0.1')
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, label_pos=0.3, font_size=7)
    plt.show()
    
# Time and memory profiling
def profile(func, graph, start_node):
    start_time = time.time()
    mem_usage = memory_usage((func, (graph, start_node)), interval=0.01)
    end_time = time.time()
    run_time = end_time - start_time
    return run_time, mem_usage

#Driver Code to actualty use the above functions
# Generate a graph
graph = generate_graph(10)
draw_graphs(graph)

#Run the algorithms on the graph for comparison
run_time_bf, mem_usage_bf = profile(bellman_ford, graph, 0)
run_time_scbf, mem_usage_scbf = profile(scbf, graph, 0)
run_time_spfa, mem_usage_spfa = profile(spfa, graph, 0)

# Plot time usage
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.bar(['Bellman Ford', 'SCBF', 'SPFA'], [run_time_bf, run_time_scbf, run_time_spfa])
plt.ylabel('Time (seconds)')

# Plot memory usage
plt.subplot(1, 2, 2)
plt.plot(mem_usage_bf, label='Bellman Ford')
plt.plot(mem_usage_scbf, label='SCBF')
plt.plot(mem_usage_spfa, label='SPFA')
plt.xlabel('Time (in milliseconds)')
plt.ylabel('Memory usage (in MiB)')
plt.legend()
plt.tight_layout()
plt.show()
