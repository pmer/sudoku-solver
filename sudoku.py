#!/usr/bin/env python3

import sys


class Grid:
    def __init__(self, w, h, zero):
        self.w = w
        self.h = h
        self.objects = [zero for _ in range(w * h)]

    def get(self, x, y):
        return self.objects[y * self.w + x]

    def set(self, x, y, value):
        self.objects[y * self.w + x] = value

    def get_row(self, y):
        return [self.get(x, y) for x in range(self.w)]

    def get_col(self, x):
        return [self.get(x, y) for y in range(self.h)]

    def get_sub(self, xoff, yoff, w, h):
        return [self.get(xoff+x, yoff+y) for x in range(w) for y in range(h)]

    def get_3x3(self, x, y):
        return self.get_sub(x // 3 * 3, y // 3 * 3, 3, 3)

    def __str__(self):
        lines = []
        for y in range(self.h):
            s = ''
            for x in range(self.w):
                digit = self.get(x, y)
                s += ' ' if digit == '0' else str(digit)
            lines.append(s)
        return '\n'.join(lines)


class Possibilities:
    def __init__(self, w, h):
        self.digits = Grid(w, h, [])

    def fill(self, grid, solver):
        for y in range(self.digits.h):
            for x in range(self.digits.w):
                digit_possibilities = solver.find_digit_possibilities(grid, x, y)
                self.digits.set(x, y, digit_possibilities)

    def make_obvious_moves(self, grid):
        found_move = False
        for y in range(self.digits.h):
            for x in range(self.digits.w):
                if grid.get(x, y) > 0:
                    continue
                digit_possibilities = self.digits.get(x, y)
                if len(digit_possibilities) == 1:
                    digit_choice = digit_possibilities[0]
                    grid.set(x, y, digit_choice)
                    found_move = True
        return found_move


class SudokuRules:
    @staticmethod
    def grid_size():
        return 9, 9

    @staticmethod
    def find_digit_possibilities(grid, x, y):
        col = grid.get_col(x)
        row = grid.get_row(y)
        sub = grid.get_3x3(x, y)

        def absent(n):
            return (n not in col) and (n not in row) and (n not in sub)

        return [n for n in range(1, 10) if absent(n)]


class Puzzle:
    def __init__(self, rules, initial_grid_objects):
        w, h = rules.grid_size()
        self.grid = Grid(w, h, 0)
        self.grid.objects = initial_grid_objects
        self.poss = Possibilities(w, h)
        self.rules = rules

    def solve(self):
        found_move = True

        while found_move:
            self.poss.fill(self.grid, self.rules)
            found_move = self.poss.make_obvious_moves(self.grid)

    def print(self):
        print(self.grid)


def load_grid(path):
    data = open(path).read().replace('\n', '')
    return list(map(lambda c: 0 if c == ' ' else int(c), data))


if __name__ == '__main__':
    file = sys.argv[1]
    puzz = Puzzle(SudokuRules(), load_grid(file))
    puzz.solve()
    puzz.print()
