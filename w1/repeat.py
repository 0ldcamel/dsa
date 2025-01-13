def find(s):
    for i in range(len(s)):
        if s[: i + 1] * (len(s) // (i + 1)) == s:
            return i + 1

if __name__ == "__main__":
    print(find("aaa")) # 1
    print(find("abcd")) # 4
    print(find("abcabcabcabc")) # 3
    print(find("aybabtuaybabtu")) # 7
    print(find("abcabca")) # 7