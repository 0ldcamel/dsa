def find_order(n):
    table = list(range(1, n + 1))
    output = []
    round = 0
    while len(table) > 1:
        if round == 0:
            odd = len(table) % 2
            output += table[1::2]
            table = table[::2]
            round += 1

        else:
            if odd == 0:
                odd = len(table) % 2
                output += table[1::2]
                table = table[0::2]
                
            else: 
                odd = len(table) % 2
                output += table[::2]
                table = table[1::2]
                
        
    output += table
    return output

        
    return output, table
if __name__ == "__main__":
    # print(find_order(1)) # [1]
    # print(find_order(2)) # [2, 1]
    # print(find_order(3)) # [2, 1, 3]
    print(find_order(7)) # [2, 4, 6, 1, 5, 3, 7]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
    # print(find_order(8)) # [2, 4, 6, 8, 3, 7, 5, 1]
    # print(find_order(12)) # [2, 4, 6, 8, 10, 12, 3, 7, 11, 5, 1, 9]


    # order = find_order(10**5)
    # print(order[-5:]) # [52545, 85313, 36161, 3393, 68929]