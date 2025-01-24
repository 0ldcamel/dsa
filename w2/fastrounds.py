def count_rounds(numbers):
    num_dict = {}
    n = len(numbers)
    for i in range(n):
        num_dict[numbers[i]] = i

    count = 1
    for j in range(1, n):
        if num_dict[j] > num_dict[j + 1]: 
            count += 1
    return count


if __name__ == "__main__":
    print(count_rounds([1, 2, 3, 4])) # 1
    print(count_rounds([1, 3, 2, 4])) # 2
    print(count_rounds([4, 3, 2, 1])) # 4
    print(count_rounds([1])) # 1
    print(count_rounds([2, 1, 4, 7, 5, 3, 6, 8])) # 4

    n = 10**5
    numbers = list(reversed(range(1, n+1)))
    print(count_rounds(numbers)) # 100000