class WordFinder:
    
    def set_grid(self, grid):
        self.grid = grid
        return self.grid

    def count(self, word):
        return self.count_3(word)

    def count_3(self, word):
        cau = self.grid 
        count = 0
        for pau in cau:
            if word in pau:
                count += 1
        return count
    
    # def count_6(self, word):
    #     grid = self.grid 
    #     rows = len(grid)
    #     cols = len(grid[0])
    #     new_grid = ["".join(grid[i][j]) for i in range(rows)]
    #     return new_grid.count_3(word)


def grid_6(grid):
    rows = len(grid)
    cols = len(grid[0])
    new_grid = ["".join(grid[i][j]) for i in range(rows) for j in range(cols)]
    return new_grid

if __name__ == "__main__":
    grid = ["TIRATIRA",
            "IRATIRAT",
            "RATIRATI",
            "ATIRATIR"]

    finder = WordFinder()
    finder.set_grid(grid)
    
    print(grid_6(grid))
    print(finder.count("TIRA")) # 7 
    # print(finder.count("TA")) # 13
    # print(finder.count("RITARI")) # 3
    # print(finder.count("A")) # 8
    # print(finder.count("AA")) # 6
    # print(finder.count("RAITA")) # 0     