# Bellman_Ford-Enhanced-SCBF-SPFA-Comparison
Approach

Our approach in this investigation is anchored on the construction and execution of Python functions, each of which symbolize the three distinct algorithms: Bellman Ford, Short-Circuiting Bellman Ford (SCBF), and Shortest Path Faster Algorithm (SPFA). These algorithms are evaluated and juxtaposed based on two performance indicators: runtime and memory consumption.

Embodiment of Algorithms: Three separate functions embody each of the algorithms - bellman_ford(), scbf(), and spfa(). These functions are built to find the minimum distance from a root node to every other node within a certain graph.

The bellman_ford() function is designed to relax the graph's edges |V| - 1 times, with |V| symbolizing the quantity of nodes within the graph. It also incorporates a check to detect negative weight cycles.

The scbf() function, akin to the Bellman Ford, relaxes the edges but integrates a short-circuiting technique. This additional step ends the loop if no modifications were made during the last cycle, potentially mitigating redundant iterations.

The spfa() function shares similarities with the bellman_ford() function. However, it introduces a queue methodology to regulate the sequence of node processing, which could offer improved performance in certain circumstances.

Performance Evaluation: The function analyze_performance() is crafted to assess the time taken and memory consumed by each algorithm. It records the time and memory usage prior to and after the execution of the algorithm. The differences between these values give us the total time and memory that the algorithm consumes.

Generation and Illustration of Graphs: The generate_graph() function is used to formulate a random directed graph with a defined number of nodes. The draw_graphs() function then illustrates this formulated graph.

Profiling and Contrastive Evaluation: The profile() function encapsulates each of the algorithmic functions, capturing their runtime and memory consumption. It employs the time.time() function for runtime measurement and the memory_usage function from the memory_profiler library for memory profiling. After each algorithm is profiled, the findings are illustrated using bar graphs and line plots, offering a visual contrast of the runtime and memory consumption of the three algorithms.

In essence, this approach offers a comprehensive and contrastive evaluation of the Bellman Ford, SCBF, and SPFA algorithms, considering both runtime and memory consumption. This method underlines the pros and cons of each algorithm, aiding in the selection of the optimal algorithm based on specific requirements.





