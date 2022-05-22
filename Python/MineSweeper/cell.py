from tkinter import Button, Label
from settings import *
import random
import ctypes

class Cell:
    all = []
    label_counter = None
    def __init__(self, x, y):
        Cell.all.append(self)
        self.x, self.y = x, y
        self.is_mine = False
        self.is_clicked = False

    def create_button(self, location):
        btn = Button(
            location,
            width=12,
            height=4
        )
        btn.bind('<Button-1>', self.left_click)
        btn.bind('<Button-3>', self.right_click)

        self.btn = btn

    def left_click(self, event):
        print(event)
        print(f'{(self.x, self.y)} - {self.is_mine}!')
        if self.is_mine:
            self.show_mine()
        else:
            self.show_cell()
            if self.number_of_adjacent_mines == 0:
                for cell in self.adjacent_cells:
                    cell.show_cell()
            self.update_label_counter()
            if self.cell_count - MINES_COUNT == 0:
                ctypes.windll.user32.MessageBoxW(0, 'You won the game', 'Game won', 0)

    def right_click(self, event):
        print(event)
        print(f'{(self.x, self.y)} - right clicked!')
        self.mark_cell()

    def show_mine(self):
        for cell in Cell.all:
            if cell.is_mine:
                cell.btn.configure(bg='red')
        print('Show mine log')
        ctypes.windll.user32.MessageBoxW(0, 'You clicked on a mine', 'Game over', 0)

    def show_cell(self):
        self.btn.configure(text=self.number_of_adjacent_mines)
        self.is_clicked = True
        self.btn.configure(bg='SystemButtonFace')
        # Unbind actions for a clicked button
        self.btn.unbind('<Button-1>')
        self.btn.unbind('<Button-3>')

    def mark_cell(self):
        if self.btn['background'] == 'SystemButtonFace':
            self.btn.configure(bg='orange')
        else:
            self.btn.configure(bg='SystemButtonFace')

    @property
    def adjacent_cells(self):
        cells = [cell for cell in Cell.all
                                    if abs(cell.x - self.x) <= 1
                                    and abs(cell.y - self.y) <= 1]
        return cells

    @property
    def number_of_adjacent_mines(self):
        return len([cell for cell in self.adjacent_cells if cell.is_mine])

    @property
    def cell_count(self):
        return len([cell for cell in Cell.all if not cell.is_clicked])

    def update_label_counter(self):
        Cell.label_counter.configure(text=f"Cells left: {self.cell_count - MINES_COUNT}")

    @staticmethod
    def create_cell_count_label(location):
        lbl = Label(
            location,
            bg='black',
            fg='white',
            text=f"Cells left: {CELLS_COUNT}",
            width=12,
            height=4,
            font=('Lato', 30)
        )
        Cell.label_counter = lbl

    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(Cell.all, MINES_COUNT)
        for cell in picked_cells:
            cell.is_mine = True

    def __repr__(self):
        return f"Cell{(self.x, self.y)}"
