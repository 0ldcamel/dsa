import random, time

def random_integer_list(length, min_val, max_val):
    return[random.randint(min_val, max_val) for i in range(length)]

def count_even_1(numbers):
    result = 0
    for x in numbers:
        if x % 2 == 0:
            result += 1
    return result

def count_even_2(numbers):
    return sum(x % 2 == 0 for x in numbers)

if __name__ == "__main__":
    numbers = random_integer_list(10000000, 1, 100)
    start_time = time.time()
    count_even_1(numbers)
    end_time = time.time()
    print("Implementation 1:", end_time - start_time)
    cau = end_time - start_time

    start_time = time.time()
    count_even_2(numbers)
    end_time = time.time()
    print("Implementation 2:", end_time - start_time)
    pau = end_time - start_time

    print(pau/cau)