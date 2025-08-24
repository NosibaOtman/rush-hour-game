class Board:
    """
    Add a class description here.
    Write briefly about the purpose of the class
    """

    def __init__(self):
        # implement your code and erase the "pass"
        # Note that this function is required in your Board implementation.
        # However, is not part of the API for general board types.
        self.cars = []
        self.board = self.build_board()
        self.goal = None

    def build_board(self):
        lst = []
        for i in range(7):
            lst1 = []
            for j in range(7):
                lst1.append("_")
            lst.append(lst1)
        return lst

    def __str__(self):
        """
        This function is called when a board object is to be printed.
        :return: A string of the current status of the board
        """
        # The game may assume this function returns a reasonable representation
        # of the board for printing, but may not assume details about it.
        str = ""
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                str += self.board[i][j]
            str += '\n'
        return str

    def cell_list(self):
        """ This function returns the coordinates of cells in this board
        :return: list of coordinates
        """
        # In this board, returns a list containing the cells in the square
        # from (0,0) to (6,6) and the target cell (3,7)
        lst = []
        for i in range(7):
            for j in range(7):
                lst.append((i, j))
        lst.append((3, 7))
        return lst

    def possible_moves(self):
        """ This function returns the legal moves of all cars in this board
        :return: list of tuples of the form (name,movekey,description) 
                 representing legal moves
        """
        lst = []
        for car in self.cars:
            d = car.possible_moves()
            for movekey in d:
                c = car.movement_requirements(movekey)[0]
                if c[0] == 3 and c[1] == 7 and not self.goal:
                    lst.append((car.get_name(), movekey, d[movekey]))
                    continue
                if c[0] < 0 or c[0] >= 7 or c[1] < 0 or c[1] >= 7:
                    continue
                if not self.cell_content(c):
                    lst.append((car.get_name(), movekey, d[movekey]))
        return lst

    def target_location(self):
        """
        This function returns the coordinates of the location which is to be filled for victory.
        :return: (row,col) of goal location
        """
        # In this board, returns (3,7)
        return (3, 7)

    def cell_content(self, coordinate):
        """
        Checks if the given coordinates are empty.
        :param coordinate: tuple of (row,col) of the coordinate to check
        :return: The name if the car in coordinate, None if empty
        """
        # # implement your code and erase the "pass"
        # for car in range(len(self.cars)):
        if coordinate[0] == 3 and coordinate[1] == 7:
            return self.goal
        if self.board[coordinate[0]][coordinate[1]] == "_":
            return None
        return self.board[coordinate[0]][coordinate[1]]

    def add_car(self, car):
        """
        Adds a car to the game.
        :param car: car object of car to add
        :return: True upon success. False if failed
        """
        # Remember to consider all the reasons adding a car can fail.
        # You may assume the car is a legal car object following the API.
        # implement your code and erase the "pass"
        for car1 in self.cars:
            if car1.get_name() == car.get_name():
                return False
        for coord in car.car_coordinates():
            x, y = coord
            if x > 6 or y > 6:
                return False
            if x < 0 or y < 0:
                return False
            if self.cell_content(coord):
                return False
        self.cars.append(car)
        for coord in car.car_coordinates():
            x, y = coord
            self.board[x][y] = car.get_name()
        return True

    def move_car(self, name, movekey):
        """
        moves car one step in given direction.
        :param name: name of the car to move
        :param movekey: Key of move in car to activate
        :return: True upon success, False otherwise
        """
        # implement your code and erase the "pass"
        for move in self.possible_moves():
            if move[0] == name and move[1] == movekey:
                for car in self.cars:
                    if car.get_name() == name:
                        car_coords = car.car_coordinates()
                        if car.movement_requirements(movekey)[0] == (3, 7):
                            car.move(movekey)
                            self.goal = car.get_name()
                            return True
                        for coord in car_coords:
                            self.board[coord[0]][coord[1]] = "_"
                        car.move(movekey)
                        car_coords = car.car_coordinates()
                        for coord in car_coords:
                            self.board[coord[0]][coord[1]] = car.get_name()
                        return True
        return False

