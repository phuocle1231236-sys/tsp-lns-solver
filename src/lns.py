import random
from typing import List, Tuple
from src.loader import calculate_distance_matrix

def calculate_tour_cost(tour: List[int], dist_matrix: List[List[float]]) -> float:
    """Tính tổng khoảng cách của một chu trình (tour)"""
    cost = 0.0
    for i in range(len(tour) - 1):
        cost += dist_matrix[tour[i]][tour[i+1]]
    return cost

def destroy_random(tour: List[int], remove_count: int) -> Tuple[List[int], List[int]]:
    """Hàm phá hủy (Destroy): Xóa ngẫu nhiên 'remove_count' điểm khỏi tour"""
    # Không xóa điểm đầu và điểm cuối (Depot 0)
    customer_nodes = tour[1:-1]
    removed_nodes = random.sample(customer_nodes, min(remove_count, len(customer_nodes)))
    
    partial_tour = [node for node in tour if node not in removed_nodes]
    return partial_tour, removed_nodes

def repair_greedy(partial_tour: List[int], removed_nodes: List[int], dist_matrix: List[List[float]]) -> List[int]:
    """Hàm tái thiết (Repair): Chèn lại các điểm bị xóa vào vị trí tối ưu nhất"""
    current_tour = list(partial_tour)
    
    for node in removed_nodes:
        best_cost_increase = float('inf')
        best_index = 1
        
        # Thử chèn node vào từng vị trí có thể
        for i in range(1, len(current_tour)):
            prev_node = current_tour[i - 1]
            next_node = current_tour[i]
            
            # Chi phí tăng thêm = (A->node + node->B) - (A->B)
            cost_increase = (dist_matrix[prev_node][node] + 
                             dist_matrix[node][next_node] - 
                             dist_matrix[prev_node][next_node])
            
            if cost_increase < best_cost_increase:
                best_cost_increase = cost_increase
                best_index = i
                
        current_tour.insert(best_index, node)
        
    return current_tour

def lns_optimize(initial_tour: List[int], customers: List[dict], iterations: int = 1000, destroy_ratio: float = 0.2) -> Tuple[List[int], float]:
    """
    Tối ưu hóa tour ban đầu bằng Large Neighborhood Search (LNS)
    """
    dist_matrix = calculate_distance_matrix(customers)
    current_tour = list(initial_tour)
    current_cost = calculate_tour_cost(current_tour, dist_matrix)
    
    best_tour = list(current_tour)
    best_cost = current_cost
    
    remove_count = int((len(customers) - 1) * destroy_ratio)
    
    for _ in range(iterations):
        # 1. Phá hủy (Destroy)
        partial_tour, removed_nodes = destroy_random(current_tour, remove_count)
        
        # 2. Tái thiết (Repair)
        new_tour = repair_greedy(partial_tour, removed_nodes, dist_matrix)
        new_cost = calculate_tour_cost(new_tour, dist_matrix)
        
        # 3. Chấp nhận nghiệm tốt hơn
        if new_cost < current_cost:
            current_tour = new_tour
            current_cost = new_cost
            
            if current_cost < best_cost:
                best_tour = list(current_tour)
                best_cost = current_cost
                
    return best_tour, best_cost