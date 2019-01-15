from gym.envs.registration import register

register(
    id='sudoku-v0',
    entry_point='gym_sudoku.envs:SudokuEnv',
)

register(
    id='sudoku_extrahard-v0',
    entry_point='gym_sudoku.envs:SudokuExtraHardEnv',
)
