from tkinter import *


class Window:
    def __init__(self, width, height, title='Default title', resizable=(False, False)):
        self.root = Tk()
        self.root.title(title)
        self.root.geometry(f'{width}x{height}+200+200')
        self.root.resizable(resizable[0], resizable[1])

    def run(self):
        self.root.mainloop()
