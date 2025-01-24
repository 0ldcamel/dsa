def calculate(input, rules):
    # voit lisätä tämän funktion edellisestä tehtävästä testaamista varten
    string = "L" + input + "R"
    string_len = len(string)
    index = 0
    state = 1
    keys_used = []

    while True:
        if index == string_len:
            break
        new_values = rules.get((string[index], state))
        keys_used.append((string[index], state))
        new_char, new_state, move = new_values
        string = string[:index] + new_char + string[index + 1:]
        state = new_state
        print(string, string[index], state, new_values, index)
        index += 1
    return keys_used

def create_rules():
    rules = {}
    # initiate at left most, index 0
    rules[("L", 1)] = ("L", 2, "RIGHT") # keep left most char as L, rise state to 2 in order to check char at index 1

    # check char at index 1
    rules[("0", 2)] = ("X", 3, "RIGHT") # if char is "0", then mark it with X and rise state to 3
    rules[("1", 2)] = ("X", 3, "RIGHT") # if char is "1", then mark it with X and rise state to 3

    # check char at index 2
    rules[("0", 3)] = ("X", 4, "RIGHT")
    rules[("1", 3)] = ("X", 4, "RIGHT")
    rules[("R", 3)] = ("R", 4, "REJECT") # meaning the input len = 2

    # check char at index 3
    rules[("0", 4)] = ("X", 5, "RIGHT")
    rules[("1", 4)] = ("X", 5, "RIGHT")
    rules[("R", 4)] = ("R", 5, "REJECT") # meaning the input len = 3

    # check char at index 4
    rules[("0", 5)] = ("X", 6, "RIGHT")
    rules[("1", 5)] = ("X", 6, "RIGHT")
    rules[("R", 5)] = ("R", 6, "REJECT") # meaning the input len = 4

    # check char at index 5
    rules[("0", 6)] = ("X", 7, "RIGHT")
    rules[("1", 6)] = ("X", 7, "RIGHT")
    rules[("R", 6)] = ("R", 7, "REJECT") # meaning the input len = 5

    # check char at index 6
    rules[("0", 7)] = ("X", 8, "RIGHT")
    rules[("1", 7)] = ("X", 8, "RIGHT")
    rules[("R", 7)] = ("R", 8, "REJECT") # meaning the input len = 6

    # check char at index 7
    rules[("0", 8)] = ("X", 9, "RIGHT")
    rules[("1", 8)] = ("X", 9, "RIGHT")
    rules[("R", 8)] = ("R", 9, "REJECT") # meaning the input len = 7

    # check char at index 8
    rules[("0", 9)] = ("X", 10, "RIGHT")
    rules[("1", 9)] = ("X", 10, "RIGHT")
    rules[("R", 9)] = ("R", 10, "REJECT") # meaning the input len = 8

    # check char at index 9
    rules[("0", 10)] = ("X", 11, "RIGHT")
    rules[("1", 10)] = ("X", 11, "RIGHT")
    rules[("R", 10)] = ("R", 11, "REJECT") # meaning the input len = 9

    # check char at index 10
    rules[("0", 11)] = ("X", 12, "RIGHT")
    rules[("1", 11)] = ("X", 12, "RIGHT")
    rules[("R", 11)] = ("R", 12, "REJECT") # meaning the input len = 10

    # check char at index 11
    rules[("0", 12)] = ("X", 13, "RIGHT")
    rules[("1", 12)] = ("X", 13, "RIGHT")
    rules[("R", 12)] = ("R", 13, "REJECT") # meaning the input len = 10

    return rules

if __name__ == "__main__":
    rules = create_rules()

    # print(calculate("00", rules)) # True
    # print(calculate("001001", rules)) # True
    # print(calculate("10111011", rules)) # True
    # print(calculate("01", rules)) # False
    # print(calculate("00100", rules)) # False
    # print(calculate("10111101", rules)) # False
    print(calculate("1011110111", rules)) # False