import argparse


from .board import Grid
from .solver import Solver

DEFAULT_GRID = """
[3] [?] [2] [?]
[?] [?] [ ] [?]
"""


class CLI:

    def __init__(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("--timeout", type=int, default=100)
        parser.add_argument("--grid", type=str, default=DEFAULT_GRID)
        self.args = parser.parse_args()
        self.grid = Grid.from_string(self.args.grid)
        self.solver_instance = Solver(grid=self.grid)
        self.solver_instance.run(timeout=self.args.timeout)
        if self.solver_instance.finished():
            self.solver_instance.final_state.show()
