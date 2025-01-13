def count(a, b, c):
    if a > b:
        a, b = b, a
    count_a = c // a
    count_b = (c - count_a * a) // b
    return count_a + count_b

if __name__ == "__main__":
    print(count(3, 4, 11))
    print(count(5, 1, 100))
    print(count(2, 3, 1))
    print(count(2, 3, 9))