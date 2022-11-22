from tkinter import Radiobutton
from tkinter.constants import RAISED

from Gui.Widgets.Widget import Widget


class RadiobuttonW(Widget):
    def __init__(self, frame, text, variable, value, command, bg, fg):
        super().__init__()
        self.widget = Radiobutton(frame, text=text, variable=variable, value=value,
                                  command=command,
                                  fg=fg,
                                  relief=RAISED,
                                  width=30,
                                  cursor="hand2",
                                  indicatoron=False,
                                  font='Times 15',
                                  bg=bg,
                                  tristatevalue="x")
