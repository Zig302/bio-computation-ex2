import itertools
import networkx as nx

def generate_subgraphs_ex1(n):
    # Create our vertices and edges of the full graph
    vertices = range(1, n + 1)
    all_edges = list(itertools.permutations(vertices, 2))
    all_graphs = []

    # We iterate on all possible amounts of edges possible, bcs its weakly connected we need at least n-1 edges
    for x in range(n-1, len(all_edges)+1):
        temp_graphs = []
        # We create all possible graphs with 'x' amount of edges
        for graph_edges in itertools.combinations(all_edges, x):
            # Create our new graph
            graph = nx.DiGraph()
            graph.add_nodes_from(vertices)
            graph.add_edges_from(graph_edges)

            # Check if its weakly connected
            if nx.is_weakly_connected(graph):
                # Now we check if we have any isomorphic graphs like the one we created
                if not any(nx.is_isomorphic(graph, G) for G in temp_graphs):
                    temp_graphs.append(graph)
                    all_graphs.append(graph)

    # Output to file
    with open('subgraphs_part1.txt', 'w') as f:
        f.write(f"n={n}\n")
        f.write(f"count={len(all_graphs)}\n")
        for k, G in enumerate(all_graphs, 1):
            f.write(f"#{k}\n")
            for edge in sorted(G.edges()):
                f.write(f"{edge[0]} {edge[1]}\n")

    return all_graphs

def generate_motifs_ex2(n, input_file):
    # Read input graph from txt file
    input_graph = nx.DiGraph()
    vertices = set()
    with open(input_file, 'r') as f:
        for line in f:
            u, v = map(int, line.strip().split())
            input_graph.add_edge(u, v)
            vertices.add(u)
            vertices.add(v)

    # Ensure there are enough vertices
    if len(vertices) < n:
        raise ValueError(f"Input graph has {len(vertices)} vertices, need at least {n}")

    # Generate all motifs from part 1
    motifs = generate_subgraphs_ex1(n)

    # Count occurrences of each motif
    motif_counts = [0] * len(motifs)
    vertex_list = sorted(vertices)
    for subset in itertools.combinations(vertex_list, n):
        # Create induced subgraph
        induced = input_graph.subgraph(subset).copy()
        if nx.is_weakly_connected(induced):
            for i, motif in enumerate(motifs):
                if nx.is_isomorphic(induced, motif):
                    motif_counts[i] += 1
                    break  # Each induced subgraph matches at most one motif, so we stop after we found

    # Output to file
    with open('subgraphs_part2.txt', 'w') as f:
        f.write(f"n={n}\n")
        f.write(f"count={len(motifs)}\n")
        for k, (G, count) in enumerate(zip(motifs, motif_counts), 1):
            f.write(f"#{k}\n")
            f.write(f"count={count}\n")
            for edge in sorted(G.edges()):
                f.write(f"{edge[0]} {edge[1]}\n")


if __name__ == '__main__':
    # Answer both parts of the exercise via part2
    generate_motifs_ex2(2, 'input.txt')