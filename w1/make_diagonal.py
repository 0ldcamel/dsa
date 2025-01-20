grid = ["TIRATIRA",
        "IRATIRAT",
        "RATIRATI",
        "ATIRATIR"]

string_1 = "".join([grid[0][0], grid[1][1], grid[2][2], grid[3][3]])
string_2 = "".join([grid[0 + i][0 + i] for i in range(4)])

rows = len(grid)
cols = len(grid[0])

# row = 0, all cols
for i in range(cols):
    cau = "".join([grid[0 + k][i + k] for k in range(cols - i) if k + 0 < rows])
    # print(cau)

# string_3 = "".join([grid[1][0], grid[2][1], grid[3][2]])
# print(string_3)
# row = 1 to row, cols = 0 
# for i in range(1, rows):
#     cau = "".join([grid[k][i + k] for k in range(rows - i) if k + i < rows])
#     print(cau)

for line in grid:
    print(line)

grid_reverse = grid[::-1]
print()

for line in grid_reverse:
    print(line)
