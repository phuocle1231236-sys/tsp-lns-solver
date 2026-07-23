# 🚚 Traveling Salesman Problem (TSP) Solver using Greedy & LNS

> An efficient algorithm solver for Large-Scale Traveling Salesman Problem (TSP) using **Greedy Nearest Neighbor Heuristic** for initial construction and **Large Neighborhood Search (LNS)** for local search optimization. Tested on standard **Solomon Benchmark Datasets**.

---

## 🌟 Features

* **Solomon Data Loader:** Parses standard Solomon VRPTW/TSP benchmark text files (`.txt`).
* **Greedy Heuristic Construction:** Quickly generates an initial feasible tour based on nearest-neighbor strategy.
* **Large Neighborhood Search (LNS):** Uses a Destroy (random removal) and Repair (greedy insertion) framework to escape local optima.

---

## 🏗️ Project Architecture

```text
tsp-lns-solver/
│
├── data/                  # Solomon Benchmark dataset (.txt)
├── src/
│   ├── __init__.py        # Module package initializer
│   ├── loader.py          # Data parser & distance matrix computation
│   ├── greedy.py          # Greedy Nearest Neighbor algorithm
│   └── lns.py             # Large Neighborhood Search algorithm
│
├── main.py                # Main script execution
├── requirements.txt       # Project dependencies
└── README.md              # Project documentation
---

### 📝 Phần 2: Cài đặt & Kết quả Benchmark

```markdown
## 🚀 Quick Start

### 1. Clone the repository
```bash
git clone [https://github.com/phuocle1231236-sys/tsp-lns-solver.git](https://github.com/phuocle1231236-sys/tsp-lns-solver.git)
cd tsp-lns-solver
2. Install dependencies
Bash
pip install -r requirements.txt
3. Run the Solver
Bash
python main.py
🛠️ Tech Stack
Language: Python 3.10+

Libraries: Standard Math & Random Modules, NumPy