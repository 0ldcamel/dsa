def create(n):
    players = list(range(1, n + 1))
    flag = False
    leaves = []
    while len(players) > 0:
        round, flag = leave(players, flag)
        leaves.append(round)
        players = [players.remove(leave) for leave in round]
    return leaves

def leave(a_list, flag):
    n = len(a_list)
    if flag:
        indexes = [i for i in range(n) if i % 2 == 0]
    else:
        indexes = [i for i in range(n) if i % 2 != 0]
    leaves = [a_list[i] for i in indexes]
    if n % 2 == 1:
        flag = True
    return leaves, flag


print(create(7))