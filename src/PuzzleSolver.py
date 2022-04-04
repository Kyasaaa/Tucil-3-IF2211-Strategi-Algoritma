import PriorityQueue as PQ
import copy
from time import time, sleep

class PuzzleSolver:
    global moves_units, puzzle_solution, direction
    direction = ["RIGHT", "DOWN", "LEFT", "UP"]     # List of possible moves direction for puzzle in command
    moves_units = [(0,1), (1,0), (0,-1), (-1,0)]    # List of possible moves direction for puzzle in units
    puzzle_solution = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]    # Solution of 15-puzzle 
    
    # Constructor
    def __init__(self):
        self.puzzle = []                        # Initial puzzle state
        self.solution_moves = []                # List of moves to reach solution puzzle
        self.kurang = [0 for i in range(16)]    # Store value of kurang(i)
        self.visited = []                       # List of puzzle that already visited
        self.nodes = 0                          # Number of generated nodes to reach solution
        self.total_moves = 0                    # Total moves to reach solution

    # Calculate kurang value of specific index
    def countKurang(self, rowIdx, colIdx):
        kurang = 0
        currElmt = self.puzzle[rowIdx][colIdx]
        if (currElmt == 0):
            currElmt = 16
        while (rowIdx < 4):
            while (colIdx < 4):
                if (currElmt > self.puzzle[rowIdx][colIdx] and self.puzzle[rowIdx][colIdx] != 0):
                    kurang += 1
                colIdx += 1
            rowIdx += 1
            colIdx = 0
        return kurang
    
    # Calculate sum of kurang(i) + X
    def sigmaKurang(self):
        sumKurang = 0
        for i in range(4):
            for j in range(4):
                sumKurang += self.countKurang(i, j)

                if (self.puzzle[i][j] == 0 and (i+j) % 2 != 0):
                    sumKurang += 1
        return sumKurang

    # Check whether the initial puzzle can reach the solution or not 
    def is_solveable(self, sumKurang):
        return sumKurang % 2 == 0
    
    # Calculate the cost of a puzzle to reach the solution
    def calCost(self, puzzle):
        cost = 0
        for i in range(4):
            for j in range(4):
                if (puzzle_solution[i][j] != puzzle[i][j] and puzzle[i][j] != 0):
                    cost += 1
        return cost

    # Get the position of zero element or empty slot
    def getZeroPosition(self, puzzle):
        for i in range(4):
            for j in range(4):
                if (puzzle[i][j] == 0):
                    return (i,j)
        return (-1,-1)
    
    # Check whether the (x,y) coordinate is valid or not
    def validIndex(self, x, y):
        return (0 <= x < 4 and 0 <= y < 4)

    # Do Branch and Bound algorithm
    def doBnB(self):
        pq = PQ.PriorityQueue()

        start = time()

        pq.enqueue((self.calCost(self.puzzle), 0, self.puzzle, []))
        self.nodes = 1
        while(not pq.is_empty()):
            curCost, level, curPuzzle, curSolution = pq.dequeue()
            self.visited.append(curPuzzle)
            self.total_moves += 1

            if (curCost == 0):
                self.solution_moves = curSolution
                self.total_moves = level

                return time() - start

            x,y = self.getZeroPosition(curPuzzle)
            for dx, dy in moves_units:
                if (self.validIndex(x + dx, y + dy)):
                    newPuzzle = copy.deepcopy(curPuzzle)
                    newSolution = copy.deepcopy(curSolution)

                    newPuzzle[x][y], newPuzzle[x+dx][y+dy] = newPuzzle[x + dx][y + dy], newPuzzle[x][y]
                    newSolution.append((dx, dy))
                    newCost = self.calCost(newPuzzle)

                    if (newPuzzle not in self.visited):
                        pq.enqueue((newCost, level + 1, newPuzzle, newSolution))
                        self.nodes += 1
    
    # Generate every move to reach solution
    def generateMoves(self):
        print("Please wait while we generating every move...\n")
        sleep(2)
        print(f"Total moves: {self.total_moves}\n")
        sleep(1)
        print("Initial Puzzle: \n")
        for i in range(4):
            for j in range(4):
                if (self.puzzle[i][j] < 10):
                    print(f" {self.puzzle[i][j]} ", end="")
                else:
                    print(self.puzzle[i][j], end=" ")
            print()
        print()
        sleep(0.75)

        step = 1
        newPuzzle = self.puzzle
        for dx, dy in self.solution_moves:
            print(f"STEP {step}: ", end="")
            for move in range(len(moves_units)):
                if (moves_units[move] == (dx, dy)):
                    print(direction[move])

            x, y = self.getZeroPosition(self.puzzle)
            newPuzzle[x][y], newPuzzle[x+dx][y+dy] = newPuzzle[x + dx][y + dy], newPuzzle[x][y]
            for i in range(4):
                for j in range(4):
                    if (newPuzzle[i][j] < 10):
                        print(f" {newPuzzle[i][j]} ", end="")
                    else:
                        print(newPuzzle[i][j], end=" ")
                print()
            print()
            sleep(0.75)
            step += 1