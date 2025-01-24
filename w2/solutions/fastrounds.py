def count_rounds(numbers):
    n = len(numbers)
    pos = [0] * (n+1)
    print(pos)
    for i in range(n):
        print(numbers[i])
        pos[numbers[i]] = i
    print(pos)

count_rounds([2, 1, 4, 7, 5, 3, 6, 8])