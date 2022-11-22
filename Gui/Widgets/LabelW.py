from tkinter import Label

from Gui.Widgets.Widget import Widget


class LabelW(Widget):
    def __init__(self, root, text, fg=None, bg='#888888'):
        super().__init__()
        self.widget = Label(root, text=text, fg=fg,
                            font='Times 15', bg=bg)
