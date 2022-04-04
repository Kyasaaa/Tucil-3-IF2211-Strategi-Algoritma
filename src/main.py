import PuzzleSolver as ps
from time import sleep

print("==================================================")
print("|          WELCOME TO 15-PUZZLE SOLVER           |")
print("+================================================+")
print("| Please choose the following input method:      |")
print("| [1] File input                                 |")
print("| [2] User input                                 |")
print("|                                                |")
print("==================================================")

opt = int(input(">>> Input method: "))
print()

# Print value of kurang(i)
def printKurang():
    print("Value of Kurang(i): ")
    for i in range(1, 17):
        print(f"Kurang({i}): ", end="")
        for j in range(4):
            for k in range(4):
                if (Puzzle.puzzle[j][k] == i or (Puzzle.puzzle[j][k] == 0 and i == 16)):
                    print(Puzzle.countKurang(j, k))
                    k = 3
                    j = 3
    print()

# Check whether there are puzzle elements that do not match the puzzle configuration
def checkConfig():
    exist = [0 for _ in range(16)]
    for i in range(4):
        for j in range(4):
            if (exist[Puzzle.puzzle[i][j]] == 1):
                return False
            else:
                exist[Puzzle.puzzle[i][j]] = 1
    
    for i in range(16):
        if exist[i] == 0:
            return False 
    return True

Puzzle = ps.PuzzleSolver()

if (opt == 1):
    filename = input("Please input the file name: ")
    path = "./test/" + filename
    file = open(path, 'r')
    for line in file.readlines():
        Puzzle.puzzle.append([int (x) for x in line.split()])

else:
    print("Create your initial puzzle state: ")
    for i in range (4):
        x = [int(x) for x in input().split()]
        Puzzle.puzzle.append(x)

print() 

if (not checkConfig()):
    print("There is a format error in the puzzle")
    sleep(1)
    print("Aborting...")
    sleep(1)
    
else:
    printKurang()
    sumKurang = Puzzle.sigmaKurang()
    print(f"Sum of Kurang(i) + X: {sumKurang}")
    if (Puzzle.is_solveable(sumKurang)):
        print("Puzzle is solveable")
        print()

        execTime = Puzzle.doBnB()
        Puzzle.generateMoves()

        print(f"Number of generated nodes: {Puzzle.nodes}")
        print(f"Execution time: {execTime} seconds")
    
    else:
        print("Puzzle is unsolveable")