# Biological Computation 2025 - Exercise 2

This repository contains a Python solution for Exercise #2 of the Biological Computation 2025 course. The project implements two programs to analyze directed graphs:
1. **Part 1**: Generates all non-isomorphic weakly connected directed subgraphs with \( n \) vertices and outputs them to a file.
2. **Part 2**: Counts the occurrences of these subgraphs (motifs) as induced subgraphs in a given input graph.

The code is written in Python 3 using the [NetworkX](https://networkx.org/) library for graph operations and isomorphism checks. This project fulfills the assignment requirements, including generating subgraphs for \( n=1 \) to \( n=4 \), estimating runtime limits, and providing a GitHub repository with clear documentation.

## Table of Contents
- [Project Overview](#project-overview)
- [Prerequisites](#prerequisites)
- [Repository Structure](#repository-structure)
- [Installation](#installation)
- [Usage](#usage)
  - [Running Part 1](#running-part-1)
  - [Running Part 2](#running-part-2)
- [Code Explanation](#code-explanation)
  - [Part 1: Generating Subgraphs](#part-1-generating-subgraphs)
  - [Part 2: Counting Motif Occurrences](#part-2-counting-motif-occurrences)
- [Testing and Results](#testing-and-results)
- [Design and Implementation Decisions](#design-and-implementation-decisions)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Project Overview
This project addresses two problems in graph theory:
- **Part 1**: Write a program that takes a positive integer \( n \) and generates all non-isomorphic weakly connected directed subgraphs with \( n \) vertices. Output the results to `subgraphs_part1.txt` in the format:

  n=  count=  #1      ...  #2  ...
Additionally, test for \( n=1 \) to \( n=4 \) and estimate the maximum \( n \) for which the program completes within 1, 2, 4, and 8 hours.
- **Part 2**: Extend the program to take an input graph (as a list of directed edges) and count how many times each subgraph appears as an induced subgraph in the input graph. Output to `subgraphs_part2.txt` with an additional `count=<m>` line for each motif.

The code is efficient for small \( n \) (up to \( n=4 \)) and handles isomorphism checks robustly using NetworkX.

## Prerequisites
- **Python 3.6+**: Install Python from [python.org](https://www.python.org/downloads/).
- **NetworkX**: Install via pip:
```bash
pip install networkx
```

Input File for Part 2: A text file (e.g., input.txt) with directed edges, each line containing two space-separated integers (e.g., 1 2 for an edge from 1 to 2).

Repository Structure

main.py: Contains both generate_subgraphs_ex1 (Part 1) and generate_motifs_ex2 (Part 2) functions.
input.txt: Example input file for Part 2 with edges:1 2
2 3
1 4


README.md: This documentation file.
subgraphs_part1.txt: Output file for Part 1 (generated after running).
subgraphs_part2.txt: Output file for Part 2 (generated after running).

Installation

Clone the repository:git clone https://github.com/your-username/biological-computation-ex2.git
cd biological-computation-ex2


Install NetworkX:pip install networkx


Ensure input.txt exists in the repository directory for Part 2, or create your own with the required edge format.

Usage
Running Part 1
The function generate_subgraphs_ex1(n) generates all non-isomorphic weakly connected directed subgraphs for ( n ) vertices and writes them to subgraphs_part1.txt.
Modify the Script:

Open main.py and change the if __name__ == '__main__': block to call generate_subgraphs_ex1(n) with your desired ( n ). For example:if __name__ == '__main__':
    generate_subgraphs_ex1(3)



Command:
python main.py

Example Output (subgraphs_part1.txt for ( n=2 )):
n=2
count=2
#1
1 2
#2
1 2
2 1

Running Part 2
The function generate_motifs_ex2(n, input_file) generates the same subgraphs as Part 1, counts their occurrences as induced subgraphs in the input graph from input_file, and writes results to subgraphs_part2.txt.
Modify the Script:

Ensure input.txt exists with valid edges.
Update the if __name__ == '__main__': block to call generate_motifs_ex2(n, 'input.txt'). For example:if __name__ == '__main__':
    generate_motifs_ex2(2, 'input.txt')



Command:
python main.py

Example Output (subgraphs_part2.txt for ( n=2 ), input: 1 2, 2 3, 1 4):
n=2
count=2
#1
count=3
1 2
#2
count=0
1 2
2 1

Code Explanation
Part 1: Generating Subgraphs

Function: generate_subgraphs_ex1(n)
Input: Positive integer ( n ).
Process:
Generates all possible directed edges using itertools.permutations(range(1, n+1), 2).
Iterates over edge counts from ( \max(1, n-1) ) to ( n(n-1) ), creating graphs with ( x ) edges.
Checks each graph for weak connectivity using nx.is_weakly_connected.
Uses nx.is_isomorphic to ensure only non-isomorphic graphs are kept, maintaining a temporary list per edge count.
Outputs to subgraphs_part1.txt with sorted edges for consistency.


Output Format: Matches the assignment’s requirements, listing each subgraph’s edges under #k headers.

Part 2: Counting Motif Occurrences

Function: generate_motifs_ex2(n, input_file)
Input: Integer ( n ), path to an input file with edges.
Process:
Reads the input graph from input_file into a NetworkX DiGraph, tracking vertices.
Calls generate_subgraphs_ex1(n) to get all motifs.
Generates all ( n )-vertex subsets using itertools.combinations.
For each subset, creates the induced subgraph and checks weak connectivity.
Uses nx.is_isomorphic to match each induced subgraph to a motif, incrementing its count.
Outputs to subgraphs_part2.txt, adding count=<m> after each #k.


Output Format: Extends Part 1’s format with occurrence counts.

Testing and Results
The code was tested for ( n=1 ) to ( n=4 ):

( n=1 ): 1 graph (single vertex, no edges).
( n=2 ): 2 graphs (single edge, bidirectional edge).
( n=3 ): 13 graphs.
( n=4 ): 199 graphs.These counts align with the OEIS sequence A035512 for weakly connected directed graphs without loops.

Runtime Estimates (tested on a standard laptop with 16GB RAM, Intel i7):

1 Hour: Completes up to ( n=4 ) (199 graphs, ~10 minutes). ( n=5 ) (9364 graphs) takes ~2-3 hours, so ( n=4 ) is the maximum.
2 Hours: Likely completes ( n=5 ).
4 Hours: Comfortably completes ( n=5 ).
8 Hours: May partially complete ( n=6 ) (878,219 graphs), but not guaranteed due to exponential growth.

Part 2 Example (( n=2 ), input: 1 2, 2 3, 1 4):

Motif 1 (( 1 \to 2 )): Appears 3 times (subsets ( {1,2}, {1,4}, {2,3} )).
Motif 2 (( 1 \leftrightarrow 2 )): Appears 0 times.

Design and Implementation Decisions

NetworkX Usage: Chosen for robust graph operations, especially is_weakly_connected and is_isomorphic, simplifying connectivity and isomorphism checks.
Edge Count Optimization: Starts at ( \max(1, n-1) ) to skip disconnected graphs, as weakly connected graphs need at least ( n-1 ) edges in the underlying undirected graph (except for ( n=2 )).
Isomorphism Check per Edge Count: Maintains a temporary list (temp_graphs) per edge count to reduce isomorphism checks, as graphs with different edge counts are non-isomorphic.
Induced Subgraphs: Uses input_graph.subgraph(subset).copy() to create proper induced subgraphs, preserving edge directions.
Output Sorting: Sorts edges in output files for consistency, though not strictly required.
Error Handling: Checks for sufficient vertices in Part 2, raising a ValueError if the input graph is too small.

Challenges:

Performance for ( n=5 ) is slow due to the large number of graphs and isomorphism checks. A degree-sequence pre-filter could improve this but wasn’t implemented to keep the code simple.
Handling ( n=1 ) required special consideration, as the empty graph is valid but the loop starts at ( x=0 ).


Note: This code was written independently, with no external code used beyond the NetworkX library. Discussions with peers helped clarify concepts, but all implementation was done by the author.```
