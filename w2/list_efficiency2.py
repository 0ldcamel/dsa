import time

def add_numbers():
    numbers = []
    for i in range(10**5):
        numbers.append(i)
    return numbers

def remove_numbers(numbers):
    for i in range(10**5):
        numbers.remove(numbers[0])


start_time = time.time()
numbers = add_numbers()
end_time = time.time()
print("Adding time:", end_time - start_time)

start_time = time.time()
numbers = remove_numbers(numbers)
end_time = time.time()
print("Removing time:", end_time - start_time)