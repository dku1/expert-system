from tkinter import Text
from tkinter.constants import WORD, INSERT, SUNKEN

from Gui.Widgets.Widget import Widget


class TextW(Widget):
    def __init__(self, root, text, textSetting):
        super().__init__()
        self.widget = Text(root, width=45, height=textSetting['height'], cursor="hand2",
                           background=textSetting['background'], relief=SUNKEN, borderwidth=4,
                           font='Times 14', wrap=WORD)
        self.widget.insert(INSERT, text)
        self.widget.configure(state=textSetting['state'])
