def find_rounds(numbers):
    n = len(numbers)

    result = []
    current = 1

    while current <= n:
        round = []
        for number in numbers:
            if number == current:
                round.append(number)
                current += 1
        result.append(round)

    return result