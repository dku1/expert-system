from tkinter import Button
from tkinter.constants import RIDGE

from Gui.Widgets.Widget import Widget


class ButtonW(Widget):
    def __init__(self, root, command, text='Ответить', font='Times 13', width=18, cursor="hand2"):
        super().__init__()
        self.widget = Button(root,
                             command=command,
                             text=text,
                             font=font,
                             width=width,
                             cursor=cursor,
                             relief=RIDGE)
