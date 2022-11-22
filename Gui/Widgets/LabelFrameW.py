from tkinter import LabelFrame
from tkinter.constants import SUNKEN

from Gui.Widgets.Widget import Widget


class LabelFrameW(Widget):
    def __init__(self, root, text=None, bg='#888888', width=400, height=300, font='Times 16'):
        super().__init__()
        self.widget = LabelFrame(root, text=text, bg=bg, width=width, height=height, font=font, fg='#800000',
                                 relief=SUNKEN)
