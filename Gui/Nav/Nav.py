from abc import ABC
from tkinter import Menu
from abc import abstractmethod


class Nav(ABC):
    def __init__(self, gui):
        self.gui = gui
        self.menu = Menu(self.gui.window.root)
        self.navigationMenu = Menu(self.menu, tearoff=0)
        self.initCommands()
        self.menu.add_cascade(label="Навигация", menu=self.navigationMenu)
        self.gui.window.root.configure(menu=self.menu)

    @abstractmethod
    def initCommands(self):
        pass

    def destroy(self):
        self.menu.destroy()
