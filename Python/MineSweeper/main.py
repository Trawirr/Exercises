from tkinter import *
from settings import *
from utils import *
from cell import Cell

root = Tk()
# settings
root.configure(bg="black")
root.geometry(f"{WIDTH}x{HEIGHT}")
root.title("MineSweeper")
root.resizable(False, False)

top_frame = Frame(
    root,
    bg='black',
    width=1080,
    height=height_perc(20)
)
top_frame.place(x=0, y=0)

left_frame = Frame(
    root,
    bg='black',
    width=width_perc(25),
    height=height_perc(80)
)
left_frame.place(x=0,y=height_perc(20))

center_frame = Frame(
    root,
    bg='black',
    width=width_perc(75),
    height=height_perc(80)
)

center_frame.place(x=width_perc(25), y=height_perc(20))

game_title = Label(
    top_frame,
    bg='black',
    fg='white',
    text='Minesweeper game',
    font=('Lato', 48)
)

game_title.place(x=width_perc(25), y=0)

for x in range(COLS):
    for y in range(ROWS):
        c = Cell(x, y)
        c.create_button(center_frame)
        c.btn.grid(column=x, row=y)

Cell.randomize_mines()
Cell.create_cell_count_label(left_frame)
Cell.label_counter.place(x=0,y=0)

# run the window
root.mainloop()