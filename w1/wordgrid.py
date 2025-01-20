class WordFinder:
    def set_grid(self, grid):
        self.grid = grid
        return self.grid


    def count(self, word):
        cau = self.grid
        count = 0
        word_reversed = word[::-1]
        cols = len(cau[0])
        rows = len(cau)
        word_len = len(word)

        if word_len == 1:
            for row in range(rows):
                for col in range(cols):
                    if cau[row][col] == word:
                        count += 1
            return count

        for row in range(rows):
            for col in range(cols):
                # south west
                south_west = "".join([cau[row + i][col - i] for i in range(word_len) if (row + i < rows and col - i >= 0)])
                if south_west == word or south_west == word_reversed:
                    count += 1
            
                # south:
                south = "".join([cau[row + i][col] for i in range(word_len) if row + i < rows])
                if south == word or south == word_reversed:
                    count += 1

                # south east
                south_east = "".join([cau[row + i][col + i] for i in range(word_len) if (row + i < rows and col + i < cols)])
                if south_east == word or south_east == word_reversed:
                    count += 1

                # east:
                east = "".join([cau[row][col + i] for i in range(word_len) if col + i < cols])
                if east == word or east == word_reversed:
                    count += 1
        return count

if __name__ == "__main__":
    # # test 1
    # print("Test 1")
    # grid = ["TIRATIRA",
    #         "IRATIRAT",
    #         "RATIRATI",
    #         "ATIRATIR"]

    # finder = WordFinder()
    # finder.set_grid(grid)

    # print(finder.count("TIRA")) # 7 
    # print(finder.count("TA")) # 13
    # print(finder.count("RITARI")) # 3
    # print(finder.count("A")) # 8
    # print(finder.count("AA")) # 6
    # print(finder.count("RAITA")) # 0     

    # Test 2
    grid = ["AAAAB",
        "ABBAB",
        "BAABA",
        "AAABB",
        "ABBBB",
        "AAAAB"]

    finder = WordFinder()
    finder.set_grid(grid)

    print(finder.count("A"))
    print(finder.count("BAAB"))
    print(finder.count("ABB"))
    print(finder.count("AB"))
    print(finder.count("BAA"))