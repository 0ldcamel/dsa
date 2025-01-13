def count(s):
    zeros = s.count("0")
    ones = s.count("1")
    return min(zeros, ones)

if __name__ == "__main__":
    print(count("01101")) # 2
    print(count("1111")) # 0
    print(count("101111")) # 1
    print(count("00001111")) # 4