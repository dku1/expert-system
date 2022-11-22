from tkinter import IntVar
from Gui.Widgets.RadiobuttonW import RadiobuttonW


class Answers:
    def __init__(self, root, answers, command, radioButtonSetting):
        self.__root = root
        self.__answers = answers
        self.__command = command
        self.__variable = IntVar(value=len(answers) + 1)
        self.setting = radioButtonSetting

    def getAnswerUser(self):
        return list(self.__answers)[self.__variable.get()]

    def draw(self):
        for index, answer in enumerate(self.__answers):
            RadiobuttonW(self.__root, text=answer, variable=self.__variable, value=index, command=self.__command,
                         bg=self.setting['bg'], fg=self.setting['fg']).draw(padx=30, pady=10)
