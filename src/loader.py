import math
from typing import Dict, List, Tuple

def read_solomon(filename: str) -> List[Dict]:
    """Đọc dữ liệu bài toán từ file định dạng Solomon (.txt)"""
    customers = []
    reading = False

    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            if "CUST NO" in line.upper():
                reading = True
                continue

            if not reading:
                continue

            parts = line.split()
            if len(parts) < 7:
                continue

            try:
                cid, x, y, demand, ready, due, service = map(float, parts[:7])
                customers.append({
                    "id": int(cid),
                    "x": x,
                    "y": y,
                    "demand": demand,
                    "ready": ready,
                    "due": due,
                    "service": service
                })
            except ValueError:
                continue

    return customers

def calculate_distance_matrix(customers: List[Dict]) -> List[List[float]]:
    """Tính trước ma trận khoảng cách Euclid giữa tất cả các điểm"""
    n = len(customers)
    matrix = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                dx = customers[i]["x"] - customers[j]["x"]
                dy = customers[i]["y"] - customers[j]["y"]
                matrix[i][j] = math.hypot(dx, dy)
    return matrix