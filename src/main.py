# main.py
from src.sum import sum_numbers

if __name__ == "__main__":
    print(sum_numbers([1, 2, 3]))      # 6.0
    print(sum_numbers([-2.5, 10, 0.5]))# 8.0
    print(sum_numbers([]))             # 0.0
