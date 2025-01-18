class WordFinder:
    def set_grid(self, grid):
        self.grid = grid
        return self.grid


    def count(self, word):
        self.cau = self.set_grid(grid)
        count = 0
        for item in self.cau:
            if word in item:
                count += 1
            if word[::-1] in item:
                count += 1
        return count

if __name__ == "__main__":
    grid = ["TIRATIRA",
            "IRATIRAT",
            "RATIRATI",
            "ATIRATIR"]

    finder = WordFinder()
    finder.set_grid(grid)

    print(finder.count("TIRA")) # 7 
    print(finder.count("TA")) # 13
    print(finder.count("RITARI")) # 3
    print(finder.count("A")) # 8
    print(finder.count("AA")) # 6
    print(finder.count("RAITA")) # 0     