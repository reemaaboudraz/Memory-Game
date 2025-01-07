import random
import time
import string
import argparse
import os

from grid import BrainBuster


class GameInstructions:
   
    def __init__(self, grid_size):

        
        self.attempts_tried = 0
        self.score = 0
        self.grid_size = grid_size
        self.b = BrainBuster(grid_size)

    

    def option1(self):
        print("Select two positions (e.g., A1, B3):")
        pos1_str, pos2_str = input("Enter two positions: ").split()
        
        pos1 = (int(pos1_str[1]), ord(pos1_str[0].upper()) - ord('A'))
        pos2 = (int(pos2_str[1]), ord(pos2_str[0].upper()) - ord('A'))

        if not (0 <= pos1[0] < self.grid_size and 0 <= pos1[1] < self.grid_size and
                0 <= pos2[0] < self.grid_size and 0 <= pos2[1] < self.grid_size):
            print("Invalid positions. Try again.")
            return
        
        self.b.uncover_cell(pos1[0], pos1[1])
        self.b.uncover_cell(pos2[0], pos2[1])

        time.sleep(3)

        if self.b.grid[pos1[0]][pos1[1]] == self.b.grid[pos2[0]][pos2[1]]:
            print("Bravo! It's a match!")
            self.b.uncovered_cells.add((pos1[0], pos1[1]))
            self.b.uncovered_cells.add((pos2[0], pos2[1]))

            self.score += 10
            self.attempts_tried += 1
        else:
            print("Try again! The numbers do not match.")
            self.b.hidden_grid[pos1[0]][pos1[1]] = "X"
            self.b.hidden_grid[pos2[0]][pos2[1]] = "X"
            self.b.uncovered_cells.discard((pos1[0], pos1[1]))
            self.b.uncovered_cells.discard((pos2[0], pos2[1]))
            self.attempts_tried += 1

        if len(self.b.uncovered_cells) == self.grid_size * self.grid_size:
            print("Congratulations! You've uncovered all the cells.")
            self.display_score()
            return True 

        return False
    
    def option2(self):
        print("Enter the coordinates of the cell you want to uncover (e.g., A1):")
        pos_str = input("Enter position: ")
        row = int(pos_str[1])
        col = ord(pos_str[0].upper()) - ord('A')

        if not (0 <= row < self.grid_size and 0 <= col < self.grid_size):
            print("Invalid position. Try again.")
            return

        self.b.uncover_cell(row, col)
        self.score -= 1  
        print("All cells have been uncovered. Game Over!")
        self.display_score()
        return True 

    def option3(self):

      self.b.reveal_grid()
      print("Better luck next time!")
      print("Would you like to start a new game?")
      user_choice = input("Do you want to start a new game? (y/n): ").strip().lower()
      if user_choice == 'y':
        self.option4()
      elif user_choice == 'n':
        print("Goodbye! Thanks for playing.")
        exit()  
      else:
        print("Invalid input. Please enter 'y' to start a new game or 'n' to exit.")
        self.option3()

    
    
    def option4(self):
        print("Starting a new game...")
        self.__init__(self.grid_size)
        self.b.new_grid_game()

        self.score = 0
        self.attempts_tried = 0
        
        main()


    def calculate_score(self):
        if self.attempts_tried == 0:
            return 0
        return (self.num_pairs / self.attempts_tried) * 100
    
    def display_score(self):
        print(f"Current score: {self.score}")
       

    def option5(self):
     print("Thank you for playing!")
     exit()  



def main():


    parser = argparse.ArgumentParser(description="Welcome to Brain Buster!")
    parser.add_argument('grid_size', type=int, help="The size of the game grid (e.g., 4 for 4x4, 6 for 6x6, etc.)")
    args = parser.parse_args()  
    
    game = GameInstructions(grid_size=args.grid_size)

    while True:
        print("\nChoose an option:")
        print("1. Let me select two elements")
        print("2. Uncover one element for me")
        print("3. I give up - reveal the grid")
        print("4. New Game")
        print("5. Exit ")
        
        game.b.display_grid()
        choice = input("Select: ")
        if choice == '1':
            game.option1()
        elif choice == '2':
            game.option2()
        elif choice == '3':
            game.option3()
            break
        elif choice == '4':
            game.option4()
        elif choice == '5':
            game.option5()
            break
        else:
            print("Invalid option. Please try again.")


main()
