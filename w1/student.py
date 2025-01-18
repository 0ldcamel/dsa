def check_number(number):
    if len(number) != 9 or number[0] != "0":
        return False
    factors = [3,7,1,3,7,1,3,7]
    numbers = [int(number[i]) for i in range(8)]
    check_sum = [factors[i] * numbers[i] for i in range(8)]
    return (0 if sum(check_sum) % 10 == 0 else 10 - sum(check_sum) % 10) == int(number[8])
    # TODO

if __name__ == "__main__":
    print(check_number("012749138")) # False
    print(check_number("012749139")) # True
    print(check_number("013333337")) # True
    print(check_number("012345678")) # False
    print(check_number("012344550")) # True
    print(check_number("1337")) # False
    print(check_number("0127491390")) # False