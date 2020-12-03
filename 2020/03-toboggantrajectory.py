from functools import reduce

class Toboggan:
    def __init__(self, map, slope):
        self.slope = slope
        self.path = [(0, 0)]
        self.trees = 0
        self.map = []

        with open(map, "r") as file:
            for line in file:
                self.map.append(line[:-1])

    def move(self):
        oldPos = self.path[-1]
        newPos = (oldPos[0] + self.slope[0], oldPos[1] + self.slope[1])
        self.path.append(newPos)
        if self.isTree(newPos):
            self.trees += 1

    def canMove(self):
        return self.path[-1][1] < len(self.map) - 1

    def isTree(self, pos):
        return self.map[pos[1]][pos[0] % len(self.map[0])] == "#"

    def predictTrees(self):
        while self.canMove():
            self.move()
        return self.trees

if __name__ == "__main__":
    # --- Part 1 --- How many trees do we encounter with a (3, 1) trajectory and starting from top-left?
    slope = (3, 1)
    toboggan1 = Toboggan("03-input.txt", slope)
    print(f"There are {toboggan1.predictTrees()} trees within the (3, 1) toboggan trajectory.")

    # --- Part 2 --- What do you get if you multiply together the number of trees encountered on each of the listed slopes?
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    trees = []
    for slope in slopes:
        toboggan2 = Toboggan("03-input.txt", slope)
        trees.append(toboggan2.predictTrees())
    print(f"The tree product of all slopes is {reduce(lambda x, y: x * y, trees)}")
