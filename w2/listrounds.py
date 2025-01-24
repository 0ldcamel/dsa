def find_rounds(numbers):
    num_dict = {}
    n = len(numbers)
    output = []
    for i in range(n):
        num_dict[numbers[i]] = i
    j = 1
    
    round = []
    if n == 1:
        return [[n]]
    while j < n:
        round = [j]
        while num_dict[j] < num_dict[j + 1]:
            round += [j + 1]
            j += 1
            if j == n:
                # round += [n]
                output.append(round)
                break
        else:
            output.append(round)
            round = []
            j += 1
            if j == n:
                output.append([n])
    return output

if __name__ == "__main__":
    print(find_rounds([1, 2, 3, 4]))
    # # [[1, 2, 3, 4]]

    print(find_rounds([1, 3, 2, 4]))
    # # [[1, 2], [3, 4]]    

    print(find_rounds([4, 3, 2, 1]))
    # # [[1], [2], [3], [4]]
    
    print(find_rounds([1]))
    # # [[1]]

    print(find_rounds([2, 1, 4, 7, 5, 3, 6, 8]))
    # [[1], [2, 3], [4, 5, 6], [7, 8]]

    