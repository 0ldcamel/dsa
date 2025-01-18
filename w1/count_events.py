import time, random

def count_even_1(numbers):
    result = 0
    for x in numbers:
        if x % 2 == 0:
            result += 1
    return result

def count_even_2(numbers):
    return sum(x % 2 == 0 for x in numbers)


if __name__ == "__main__":
    numbers = [random.randint(1, 100) for i in range(10**7)]
    start_time = time.time()
    count_even_1(numbers)
    end_time = time.time()
    print("Implementation 1 running time:", end_time - start_time)

    start_time = time.time()
    count_even_2(numbers)
    end_time = time.time()
    print("Implementation 2 running time:", end_time - start_time)