"""This file defines the class sudoku that creates and checks if the created
sudoku is solvable"""

import numpy as np

class Sudoku():
    def __init__(self, n = 20):
        """
        This method initializes the Sudoku so that it is correct and solvable.
        Args:
            - self: Sudoku instance, to be iniatilized.
            - n: int, number of numbers to set in the grid.
        Returns:
            - None
        """
        self.grid = self.create_sudoku(n)
        count = 1
        self.correct_init = self.is_correct_init()
        while self.correct_init == False:
            count = count + 1
            self.grid = self.create_sudoku(n)
            self.correct_init = self.is_correct_init()
        self.count = count

    def create_sudoku(self, n):
        """
        This method creates a random sudoku grid.
        Args:
            - self: Sudoku instance, to be created
            - n: int, number of numbers to set in the grid
        Returns:
            - grid: numpy array(9,9)
        """
        # Creating an empty grid
        grid = np.zeros((9,9))

        # Randomly chosing the numbers to set and their position
        numbers = np.random.randint(1,9,n)
        indexes = np.arange(81)
        np.random.shuffle(indexes)
        indexes = indexes[:n]

        # Populating the grid accordingly
        for i in range(len(indexes)):
            index = indexes[i]
            number = numbers[i]
            row = index // 9
            col = index % 9
            grid[row][col] = number
        return grid

    def is_correct_init(self):
        """
        This method verifies if the created Sudoku grid can be solved.
        Args:
            - self: Sudoku instance, to be verified
        Returns:
            - boolen_value: whether the grid is correct
        """

        try:
            getattr(self, "grid")
        except AttributeError:
            raise RuntimeError("You must run create_random_sudoku first.")

        flag_col = self.check_row(True)
        flag_row = self.check_row(False)
        flag_block = self.check_block()

        if flag_col and flag_row and flag_block:
            return True
        else:
            return False

    def check_row(self, transpose = False):
        """
        This method checks whether there is a conflict in the grid row.
        Args:
            - self: Sudoku instance, to be checked.
            - transpose: boolean, whether to consider columns or rows
        Returns:
            - flag: boolean, whether the columns show conflicts or not
        """

        try:
            getattr(self, "grid")
        except AttributeError:
            raise RuntimeError("You must run create_random_sudoku first.")

        grid = self.grid
        flag = True
        if transpose == True:
            grid = np.transpose(grid)
        for i in range(len(grid)):
            row = grid[i]
            row = row[row != 0]
            row_set = set()
            for element in row:
                row_set.add(element)
            if len(row_set) != len(row):
                flag = False
                break
        return flag

    def check_block(self):
        """
        This method checks whether there is a conflict in the grid blocks.
        Args:
            - self: Sudoku instance, to be checked.
        Returns:
            - flag: boolean, whether the blocks show conflicts or not.
        """

        try:
            getattr(self, "grid")
        except AttributeError:
            raise RuntimeError("You must run create_sudoku first.")

        grid = self.grid
        flag = True
        for i in range(3):
            row = 3 * i
            block = grid[row:row+3]
            block = np.transpose(block)
            for j in range(3):
                col = 3 * j
                unit = block[col:col+3]
                unit = unit[unit != 0]
                unit_set = set()
                for element in unit:
                    unit_set.add(element)
                if len(unit_set) != len(unit):
                    flag = False
                    break
            if flag == False:
                break
        return flag

    def complete_sudoku(self, method = "backtrack"):
        """
        This method completes the Sudoku given a specific method.
        Args:
            - self: Sudoku instance, to be completed.
            - method: one of "backtrack", "coloring", "IP", "RL".
        Returns:
            - flag: boolean, whether the Sudoku is solvable.
            If True, the completed Sudoku is available through the attribute
            "solution".
        """
        if method == "backtrack":
            flag = self.backtrack_solution()
        return flag

    def backtrack_solution(self):
        """
        This method implements the backtrack method.
        Args:
            - self: Sudoku instance, to be solved using backtracking.
        Returns:
            - flag: boolean, whether the Sudoku is solvable.
            If True, the completed Sudoku is available through the attribute
            "solution".
        """

        # Retrieving the set values
        mask = self.grid > 0


    def put_number(self, row, col, number):
        """
        This function checks if the number number can be added in the column
        col and the row row.
        Args:
            - self: Sudoku instance.
            - row: int(0-8), number of the row to be considered.
            - col: int(0-8), number of the column to be considered.
            - number: int(1-9), number to be added at the (row,col) cell.
        Returns:
            - flag: whether of not the number can be added. If True, the number
            is added.
        """
