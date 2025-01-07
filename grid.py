import random
import time
import string
from typing import Set, Tuple  

class BrainBuster:
    
    def __init__(self, grid_size):
       
        self.grid_size = grid_size
        self.grid = []
        self.hidden_grid = [["X" for _ in range(self.grid_size)] for _ in range(self.grid_size)]
        self.attempts = 0
        self.pairs_found = 0
        self.uncovered_cells: Set[Tuple[int, int]] = set() 
        self.num_pairs = (self.grid_size ** 2) // 2
        
        self.add_grid()
        
    def add_grid(self):
        numbers = list(range(self.num_pairs)) * 2
        random.shuffle(numbers)

        for i in range(self.grid_size):
            row = []
            for j in range(self.grid_size):
                row.append(numbers.pop())
            self.grid.append(row)


    def display_grid(self): 
        print("----------------------")
        print("|    Brain Buster    |")  
        print("----------------------")

        print("     " + "  ".join([f"[{chr(65 + col)}]" for col in range(self.grid_size)]))
        print()
        for row in range(self.grid_size):
            print(f"[{row}]   " + "    ".join(self.hidden_grid[row]))
        
    def reveal_grid(self):
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                self.hidden_grid[i][j] = str(self.grid[i][j])
        self.display_grid()

    def new_grid_game(self):
        self.hidden_grid = [["X" for _ in range(self.grid_size)] for _ in range(self.grid_size)]
        self.display_grid()

    def reset_grid(self):
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                if (i, j) not in self.uncovered_cells:
                    self.hidden_grid[i][j] = "X"
        self.display_grid()

    def uncover_cell(self, row, col):
        self.hidden_grid[row][col] = str(self.grid[row][col])
        self.uncovered_cells.add((row, col))
        self.display_grid()

