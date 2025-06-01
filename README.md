# Biological Computation - Ex2
Generate, list, and identify isomorphic connected subgraphs from directed graphs.

# Motif Finder – Biological Computation Exercise 2

This repository contains a Python implementation of Exercise 2 from the *Biological Computation* course. The task involves generating all **weakly connected directed subgraphs (motifs)** of a given size `n`, and counting their occurrences in an input directed graph.

---

## 📁 Project Structure

.
├── main.py # Main program for both parts
├── input.txt # Input graph (user-provided)
├── subgraphs_part1.txt # Output of all unique motifs of size n
├── subgraphs_part2.txt # Occurrence counts of each motif in input graph
└── .venv/ # (Optional) Python virtual environment

---

## ⚙️ Requirements

- Python 3.6+
- [networkx](https://networkx.org/)

Install dependencies using pip:

```bash
pip install networkx

