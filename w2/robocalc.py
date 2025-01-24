def calculate(input, rules):
    string = "L"+ input + "R"
    string_len = len(string)
    keys_used = []
    index = 0
    state = 1
    rule_dict = create_rule_dict(rules)
    while True:
        if index == string_len:
            return False
        if (string[index], state, index, string) not in keys_used:
            keys_used.append(((string[index], state, index, string)))
        else:
            # print("reusing key", "string:", string, "state:", state, "index:", index, "string:", string)
            return False
        new_values = rule_dict.get((string[index], state))
        if new_values is not None:
            new_char, new_state, move = new_values
            # print("rule:", string[index], state, new_char, new_state, move, end=" ")
        else:
            return False

        string = string[:index] + new_char + string[index + 1:]
        state = new_state
        
        index_shift = get_move(move)
        if index_shift == "REJECT":
            return False
        elif index_shift == "ACCEPT":
            return True
        else:
            index += index_shift
        # print("string:", string, "state:", state, "index:", index)


def create_rule_dict(rules):
    rule_dict = {}
    for rule in rules:
        current_char, current_state, new_char, new_state, move = rule[0], rule[1], rule[2], rule[3], rule[4]
        rule_dict[(current_char, current_state)] = (new_char, new_state, move)
    return rule_dict

def get_move(move):
    if move == "RIGHT":
        return 1
    elif move == "LEFT":
        return -1
    else:
        return move

if __name__ == "__main__":
    rules = []

    rules.append(("L", 1, "L", 2, "RIGHT"))
    rules.append(("L", 3, "L", 2, "RIGHT"))

    rules.append(("0", 2, "X", 4, "RIGHT")) # if "O" is at index 1, cross it, change state to 4
    rules.append(("1", 4, "X", 5, "RIGHT")) 
    rules.append(("1", 2, "X", 6, "RIGHT")) # if "1" is at index 1, cross it, change state to 6
    rules.append(("0", 6, "X", 7, "RIGHT"))

    rules.append(("0", 4, "0", 4, "RIGHT"))
    rules.append(("0", 5, "0", 5, "RIGHT"))
    rules.append(("0", 7, "0", 7, "RIGHT"))
    rules.append(("1", 6, "1", 6, "RIGHT"))
    rules.append(("1", 5, "1", 5, "RIGHT"))
    rules.append(("1", 7, "1", 7, "RIGHT"))

    rules.append(("X", 2, "X", 2, "RIGHT"))
    rules.append(("X", 4, "X", 4, "RIGHT"))
    rules.append(("X", 5, "X", 5, "RIGHT"))
    rules.append(("X", 6, "X", 6, "RIGHT"))
    rules.append(("X", 7, "X", 7, "RIGHT"))

    rules.append(("R", 2, "R", 2, "ACCEPT"))
    rules.append(("R", 4, "R", 4, "REJECT"))
    rules.append(("R", 6, "R", 6, "REJECT"))

    rules.append(("R", 5, "R", 3, "LEFT"))
    rules.append(("R", 7, "R", 3, "LEFT"))
    rules.append(("0", 3, "0", 3, "LEFT"))
    rules.append(("1", 3, "1", 3, "LEFT"))
    rules.append(("X", 3, "X", 3, "LEFT"))

    # print(calculate("0", rules)) # False
    print(calculate("1001", rules)) # False