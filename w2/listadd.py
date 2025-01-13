def create(t, x):
    output = t[:]
    return [number + x for number in output]

if __name__ == "__main__":
    print(create([1,2,3],1)) # [2,3,4]
    print(create([1,1,1,1,1],4)) # [5,5,5,5,5]
    print(create([0],10**9)) # [1000000000]