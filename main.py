import time
from src.loader import read_solomon
from src.greedy import greedy_tsp
from src.lns import lns_optimize

def main():
    # 1. Đọc dữ liệu
    data_path = "data/C101.txt"
    customers = read_solomon(data_path)
    print(f"-> Đã tải {len(customers)} khách hàng từ {data_path}")

    # 2. Chạy Greedy ban đầu
    start_time = time.time()
    initial_solution, initial_cost = greedy_tsp(customers)
    greedy_time = time.time() - start_time
    print(f"[Greedy] Cost: {initial_cost:.2f} | Time: {greedy_time:.4f}s")

    # 3. Tối ưu bằng LNS
    start_time = time.time()
    best_solution, best_cost = lns_optimize(initial_solution, customers, iterations=1000)
    lns_time = time.time() - start_time
    print(f"[LNS]    Cost: {best_cost:.2f} | Time: {lns_time:.4f}s")

    # 4. Tính % cải thiện
    improvement = ((initial_cost - best_cost) / initial_cost) * 100
    print(f"-> LNS giúp tối ưu thêm: {improvement:.2f}%")

if __name__ == "__main__":
    main()