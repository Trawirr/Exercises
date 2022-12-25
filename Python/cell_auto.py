import matplotlib.pyplot as plt
import numpy as np
import random
import time

class CellAuto:
    def __init__(self) -> None:
        self._cells = []
        self._history = []
        
    def run(self, n=10):
        for i in range(n):
            self.get_next_stage()
            if len(self._cells) == 0:
                break
            if self.check_for_oscillator():
                print(f"{self.sort_cells(self._history[0])} is an oscillator")
                break
            if self.check_for_still():
                print(f"{self.sort_cells(self._history[0])} becomes still")
                break

    def load_random_cells(self, width, height, n):
        all_cells = [(x, y) for x in range(width) for y in range(height)]
        cells = random.sample(all_cells, min(len(all_cells), n))
        self._cells = cells

    def check_for_oscillator(self):
        cells_h_ns = self.sort_cells(self.normalize_cells(self._history[0]))
        cells_ns = self.sort_cells(self.normalize_cells(self._cells))
        return cells_h_ns == cells_ns

    def check_for_still(self):
        for cells_h in self._history[1:]:
            cells_h_ns = self.sort_cells(self.normalize_cells(cells_h))
            cells_ns = self.sort_cells(self.normalize_cells(self._cells))
            if cells_ns == cells_h_ns:
                return True
        return False

    def load_cells(self, cells):
        self._cells = cells

    def normalize_cells(self, cells):
        xs = [c[0] for c in cells]
        ys = [c[1] for c in cells]

        x_min = min(xs)
        y_min = min(ys)

        normalized_cells = [(x-x_min, y-y_min) for x, y in cells]
        return normalized_cells

    def sort_cells(self, cells):
        cells.sort(key=lambda xy: f"{xy[0]}_{xy[1]}")
        return cells

    def get_next_stage(self):
        adjacent_table = {}
        for x, y in self._cells:
            adjacent_cells = [(x+dx, y+dy) for dx in [-1, 0, 1] for dy in [-1, 0, 1] if (x+dx, y+dy) != (x, y)]
            for cell in adjacent_cells:
                adjacent_table[cell] = adjacent_table[cell] + 1 if cell in adjacent_table.keys() else 1
        new_cells = []
        for cell in adjacent_table.keys():
            if cell in self._cells and adjacent_table[cell] in [2,3]:
                new_cells.append(cell)
            elif cell not in self._cells and adjacent_table[cell] == 3:
                new_cells.append(cell)
                
        self._history.append(self._cells)
        self._cells = new_cells

    def get_cells(self):
        xs = [c[0] for c in self._cells]
        ys = [c[1] for c in self._cells]

        x_min, x_max = min(xs), max(xs)
        y_min, y_max = min(ys), max(ys)

        cells = []
        for x in range(x_min, x_max+1):
            row = []
            for y in range(y_min, y_max+1):
                if (x, y) in self._cells:
                    row.append(1)
                else:
                    row.append(0)
            cells.append(row)
        return cells

    def draw_cells(self, cells=None):
        if not cells:
            plt.imshow(self.get_cells())
            plt.show()
        else:
            plt.imshow(cells)
            plt.show()

# Looking for oscillators not larger than 6x6
for i in range(10000):
    ca = CellAuto()
    ca.load_random_cells(6, 6, random.randint(3, 35))
    ca.run(50)