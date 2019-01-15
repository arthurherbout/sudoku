import gym
import sys
import numpy as np

from gym import error, spaces, utils
from gym.utils import seeding

import sudoku

class SudokuEnv(gym.Env):
    """
    The Sudoku problem.

    Description:
    We are given a Sudoku grid to fill. When the episode starts, a checked
    grid of 20 digits is given to the agent whose objective is to complete it correctly.

    Observations:
    There are 9^(20 chose 81) starting positions

    Actions:
    There are 9 * 81 = 729 discrete deterministic actions.
    For each cell in the (9,9) grid, we can put a number from 1 to 9.
    Actions will be noted as:
        action_r_c_v: r is the row, c the column and v the value

    Rewards:
        - action reward: +1
        - completion reward: +100

    Rendering:
    Filling in the Sudoku grid.
    - red: original values
    - white: filled values

    """
    metadata = {'render.modes' : ['human']}

    def __init__(self):
        """
        This function initializes the Sudoku env and creates a Sudoku grid.
        Args:
            - self: SudokuEnv, to be created.
        Returns:
            - None
        """
        self.sudoku = sudoku.Sudoku()
        self.state = self.sudoku.grid
        self.episode_over = False
        self.reward = len(self.state[self.state > 0])

    def step(self, action):
        """
        Args:
            - self: Sudoku environment instance
            - action: np.array(729), one-hot encoding of the action to take
        Returns:
            - ob (object):
                an environment-specific object representing your observation
                of the environment.
            - reward (float):
                amount of reward achieved by the previous action. The goal is
                to increase your total reward.
            - episode_over (bool):
                whether it's time to reset the environment again.
            - info (dict):
                diagnostic information useful for debugging.
        """
        self.take_action(action)
        self.check_status()
        self.get_reward()
        return self.state, self.reward, self.episode_over, {}

    def reset(self):
        self.sudoku = sudoku.Sudoku()
        self.state = self.sudoku.grid
        self.episode_over = False
        self.reward = len(self.state[self.state > 0])

    def render(self, mode='human'):
        print(self.state)

    def take_action(self, action):
        """
        This method add the number encoded by "action" at the position
        encoded by "action".
        Args:
            - self: Sudoku env
            - action: np.array(729), one-hot encoding of the action to take.
        Returns:
            - None
        """
        # Getting back the action number
        action = np.argmax(action)

        # Getting back the number to be written
        digit = action % 9 + 1

        # Getting back the cell number
        cell = action // 9

        # Getting back the related row and column numbers
        row = cell // 9
        column = cell % 9

        # Adding the number at its location
        grid = self.state
        if grid[row][column] == 0:
            grid[row][column] = digit
        self.state = grid

    def check_status(self):
        """
        We will use sudoku.is_correct_init() to perform the sanity check.

        """
        flag = self.sudoku.is_correct_init()
        if flag == False:
            return True
        else:
            lenght = len(self.state[state.state > 0])
            if lenght == self.reward:
                return True
            else:
                self.reward = lenght
                return False

    def get_reward(self):
        reward = self.reward
        completed = len(self.state[self.state > 0]) == 81
        if self.episode_over == True and completed == True:
            reward += 100
        self.reward = reward
