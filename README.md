# Directed Subgraph Generator and Motif Counter

This repository contains Python scripts for generating all non-isomorphic weakly connected directed graphs (subgraphs) with \( n \) vertices and counting their occurrences as induced subgraphs in a given input graph. The project is designed for a graph theory assignment, solving two related problems:

1. **Exercise 1**: Generate all non-isomorphic weakly connected directed graphs with \( n \) vertices and output them to a file.
2. **Exercise 2**: For a given input graph and integer \( n \), generate the same subgraphs as in Exercise 1 and count how many times each appears as an induced subgraph in the input graph.

The code uses Python 3 and the NetworkX library to handle graph operations and isomorphism checks.

## Prerequisites

To run the code, you need:
- **Python 3.6+**: Ensure Python is installed. [Download Python](https://www.python.org/downloads/).
- **NetworkX**: A Python library for graph operations. Install it using pip:
  ```bash
  pip install networkx


Input File (for Exercise 2): A text file (input.txt) containing the edges of the input graph, with each line formatted as two space-separated integers (e.g., 1 2 for a directed edge from vertex 1 to 2).

Repository Structure

generate_subgraphs_ex1.py: Script for Exercise 1, generating all non-isomorphic weakly connected directed subgraphs.
generate_subgraphs_ex2.py: Script for Exercise 2, counting occurrences of each subgraph in an input graph.
input.txt: Example input file for Exercise 2 with edges:1 2
2 3
1 4


README.md: This file, providing project documentation.

Installation

Clone the repository:git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name


Install the required Python package:pip install networkx


Ensure input.txt exists in the repository directory for Exercise 2 (or create your own input file).

Usage
Running Exercise 1
The script generate_subgraphs_ex1.py generates all non-isomorphic weakly connected directed graphs with ( n ) vertices and writes them to subgraphs_1.txt.
Command:
python generate_subgraphs_ex1.py

Example:

The script is set to run with ( n=3 ). To change ( n ), modify the generate_subgraphs_ex1(3) call in the script to your desired value (e.g., generate_subgraphs_ex1(4)).
Run:python generate_subgraphs_ex1.py


Output file subgraphs_1.txt will contain:n=3
count=13
#1
1 2
2 3
#2
1 2
1 3
...



Running Exercise 2
The script generate_subgraphs_ex2.py takes an integer ( n ) and an input graph from input.txt, counts occurrences of each non-isomorphic weakly connected subgraph as an induced subgraph, and writes results to subgraphs_2.txt.
Command:
python generate_subgraphs_ex2.py

Example:

Ensure input.txt exists with edges, e.g.:1 2
2 3
1 4


The script is set to run with ( n=2 ). Modify the generate_subgraphs_ex2(2, 'input.txt') call in the script to change ( n ) or the input file.
Run:python generate_subgraphs_ex2.py


Output file subgraphs_2.txt will contain:n=2
count=2
#1
count=3
1 2
#2
count=0
1 2
2 1



How It Works
Exercise 1: Generating Non-Isomorphic Subgraphs

Input: A positive integer ( n ).
Process:
Generates all possible directed edges for ( n ) vertices using itertools.permutations.
Iterates over edge counts from ( \max(1, n-1) ) to ( n(n-1) ), creating all possible graphs with ( x ) edges.
Filters graphs to ensure they are weakly connected using nx.is_weakly_connected.
Uses nx.is_isomorphic to check for isomorphism, keeping only one representative per isomorphism class.
Outputs the graphs to subgraphs_1.txt in the format:n=<value>
count=<number of unique graphs>
#1
<edge1>
<edge2>
...
#2
...




Key Feature: Efficiently handles isomorphism by checking within each edge count, reducing unnecessary comparisons.

Exercise 2: Counting Motif Occurrences

Input: An integer ( n ) and a graph specified by edges in input.txt.
Process:
Reuses generate_subgraphs_ex1 to generate all non-isomorphic weakly connected subgraphs (motifs) with ( n ) vertices.
Reads the input graph from input.txt into a NetworkX DiGraph.
Generates all subsets of ( n ) vertices from the input graph.
For each subset, creates the induced subgraph and checks if it’s weakly connected.
Uses nx.is_isomorphic to match each weakly connected induced subgraph to a motif, incrementing its count.
Outputs to subgraphs_2.txt in the format:n=<value>
count=<number of motifs>
#1
count=<occurrences>
<edge1>
<edge2>
...
#2
count=<occurrences>
...




Key Feature: Accurately counts induced subgraph occurrences, handling isomorphism and weak connectivity.

Example Outputs
Exercise 1 (( n=2 ))
Running generate_subgraphs_ex1(2) produces:
n=2
count=2
#1
1 2
#2
1 2
2 1

Exercise 2 (( n=2 ), input graph: ( 1 \to 2 ), ( 2 \to 3 ), ( 1 \to 4 ))
Running generate_subgraphs_ex2(2, 'input.txt') produces:
n=2
count=2
#1
count=3
1 2
#2
count=0
1 2
2 1

Notes

Performance: The code is optimized for small ( n ) (e.g., ( n \leq 5 )) due to the exponential growth of graphs (e.g., 199 for ( n=4 ), 9364 for ( n=5 )). For larger ( n ), consider adding pre-filtering by degree sequences to reduce isomorphism checks.
Input Validation: Ensure input.txt for Exercise 2 has valid edges (two space-separated integers per line) and at least ( n ) vertices.
Customization: Modify the ( n ) value in the scripts’ if __name__ == '__main__': block to test different sizes.

Contributing
Feel free to fork this repository, submit issues, or create pull requests with improvements, such as performance optimizations or additional error handling.
License
This project is licensed under the MIT License. See the LICENSE file for details.
Acknowledgments

Built using Python and NetworkX.
Inspired by graph theory problems for enumerating directed subgraphs and motif counting.



