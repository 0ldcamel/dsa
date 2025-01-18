from itertools import product

def count_numbers(a, b):
    valids = ["2", "5"]
    valid_products = []
    for i in range(len(str(a)), len(str(b)) + 1):
        valid_products += [int(''.join(p)) for p in product(valids, repeat=i) if (a <=int(''.join(p)) <= b)]
    return len(valid_products)

if __name__ == "__main__":
    print(count_numbers(1, 100)) # 6
    print(count_numbers(60, 70)) # 0
    print(count_numbers(25, 25)) # 1
    print(count_numbers(1, 10**9)) # 1022
    print(count_numbers(123456789, 987654321)) # 512