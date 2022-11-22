from tkinter import IntVar
from Gui.Widgets.RadiobuttonW import RadiobuttonW


class ExpertMain:
    def __init__(self, root, actions, radioButtonSetting):
        self.__root = root
        self.__actions = actions
        self.__variable = IntVar(value=len(actions) + 1)
        self.setting = radioButtonSetting

    def draw(self):
        for action, command in self.__actions.items():
            RadiobuttonW(self.__root, text=action, variable=self.__variable, value=0, command=command,
                         bg=self.setting['bg'], fg=self.setting['fg']).draw(padx=30, pady=10)
