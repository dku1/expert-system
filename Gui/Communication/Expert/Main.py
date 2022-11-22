from Gui.Interfaces.Message import Message
from Gui.Interfaces.ExpertMain import ExpertMain
from Gui.Communication.Communication import Communication


class Main(Communication):
    def __init__(self, root, guiEvents, settingMessage, radioButtonSetting):
        super().__init__(root, guiEvents)
        self.message = Message(self.root, "Что вас интересует?", settingMessage)
        self.answers = ExpertMain(self.message.getFrame(), self.getActions(), radioButtonSetting)

    def getActions(self):
        return {"Виды заболеваний": self.guiEvent[0], "Заболевания": self.guiEvent[1], "Правила": self.guiEvent[2]}

    def destroy(self):
        self.message.destroy()

    def draw(self):
        self.message.draw()
        self.answers.draw()
