import sys
from helper import *
from board import *
from car import *

car_color = ["Y", "B", "O", "G", "W", "R"]
move_key = ["u", "d", "r", "l"]


class Game:
    """
    Add class description here
    """

    def __init__(self, board):
        """
        Initialize a new Game object.
        :param board: An object of type board
        """
        # You may assume board follows the API
        # implement your code here (and then delete the next line - 'pass')
        self.__board = board

    def __single_turn(self):
        """
        Note - this function is here to guide you and it is *not mandatory*
        to implement it. 

        The function runs one round of the game :
            1. Get user's input of: what color car to move, and what 
                direction to move it.
            2. Check if the input is valid.
            3. Try moving car according to user's input.

        Before and after every stage of a turn, you may print additional 
        information for the user, e.g., printing the board. In particular,
        you may support additional features, (e.g., hints) as long as they
        don't interfere with the API.
        """
        # implement your code here (and then delete the next line - 'pass')
        user_choice = input()
        if user_choice == "!":
            return False
        if len(user_choice) != 3:
            print("try to choice again1")
            return True
        if user_choice[0] not in car_color:
            print("try to choice again2")
            return True
        if user_choice[2] not in move_key:
            print("try to choice again3")
            return True
        board.move_car(user_choice[0], user_choice[2])
        return True

    def play(self):
        """
        The main driver of the Game. Manages the game until completion.
        :return: None
        """
        # implement your code here (and then delete the next line - 'pass')
        while not board.cell_content((3, 7)):
            print(board)
            x = self.__single_turn()
            if not x:
                break


if __name__ == "__main__":
    # Your code here
    # All access to files, non API constructors, and such must be in this
    # section, or in functions called from this section.
    if len(sys.argv) == 2:
        dic = load_json(sys.argv[1])
        board = Board()
        for key in dic:
            if key in car_color:
                d = dic[key]
                if 2 <= int(d[0]) <= 4 and (int(d[2]) == 0 or int(d[2]) == 1):
                    car = Car(key, int(d[0]), d[1], int(d[2]))
                    board.add_car(car)
        game = Game(board)
        game.play()
