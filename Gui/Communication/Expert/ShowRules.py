from tkinter import END
from Gui.Widgets.TextW import TextW
from Gui.Interfaces.Button import Button
from Gui.Interfaces.Message import Message


class ShowRules:
    def __init__(self, root, rules, buttonAddEvent, buttonBackEvent, messageSetting, buttonSetting, textSetting):
        self.rules = rules
        self.message = Message(root, 'Правила', messageSetting)
        self.text = TextW(self.message.getFrame(), self.renderText(), textSetting)
        self.text.widget.configure(state='disabled')
        self.button = Button(root, buttonBackEvent, "Назад", buttonSetting)
        self.buttonAdd = Button(self.message.getFrame(), buttonAddEvent, "Добавить", buttonSetting)

    def renderText(self):
        text = ''
        for rule in reversed(self.rules):
            typeDisease = list(self.rules[rule].keys())[0]
            disease = list(self.rules[rule].keys())[1]
            text += f'{typeDisease}\n'
            for question, answer in self.rules[rule][typeDisease].items():
                text += f'{question} : {answer}\n'
            text += f'{disease} : {self.rules[rule][disease]}\n\n'
        return text

    def destroy(self):
        self.message.destroy()
        self.button.destroy()

    def draw(self):
        self.message.draw()
        self.text.draw()
        self.buttonAdd.draw()
        self.button.draw()
