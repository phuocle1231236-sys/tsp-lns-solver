from typing import List, Tuple
from src.loader import calculate_distance_matrix

def greedy_tsp(customers: List[dict]) -> Tuple[List[int], float]:
    """
    Thuật toán Tham ăn (Greedy / Nearest Neighbor):
    Luôn chọn điểm chưa thăm gần nhất với điểm hiện tại.
    """
    n = len(customers)
    if n == 0:
        return [], 0.0

    dist_matrix = calculate_distance_matrix(customers)
    
    unvisited = set(range(1, n)) # Depot là 0
    current_node = 0
    tour = [current_node]
    total_cost = 0.0

    while unvisited:
        # Tìm node chưa thăm gần nhất
        next_node = min(unvisited, key=lambda node: dist_matrix[current_node][node])
        total_cost += dist_matrix[current_node][next_node]
        current_node = next_node
        tour.append(current_node)
        unvisited.remove(current_node)

    # Quay về depot (node 0)
    total_cost += dist_matrix[current_node][0]
    tour.append(0)

    return tour, total_cost