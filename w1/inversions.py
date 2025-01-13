import itertools

def count(t):
    inverts = 0
    pairs = list(itertools.combinations(range(len(t)), 2))
    for i, j in pairs:
        if t[i] > t[j]:
            inverts += 1
    return inverts


if __name__ == "__main__":
    print(count([1,3,2])) # 1
    print(count([1])) # 0
    print(count([4,3,2,1])) # 6
    print(count([1,8,2,7,3,6,4,5])) # 12

