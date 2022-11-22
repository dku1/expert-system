from Gui.Interfaces.Button import Button
from Gui.Interfaces.Answers import Answers
from Gui.Interfaces.Message import Message


class TypeForDiseases:
    def __init__(self, root, buttonBackEvent, typeDisease, typeEvents, settingMessage, radioButtonSetting,
                 buttonSetting):
        self.typeDisease = typeDisease
        self.message = Message(root, "Виды заболеваний", settingMessage)
        self.answers = Answers(self.message.getFrame(), typeDisease,
                               lambda: typeEvents(typeDiseases=self.answers.getAnswerUser()),
                               radioButtonSetting)
        self.buttonBack = Button(root, buttonBackEvent, "Назад", buttonSetting)

    def destroy(self):
        self.message.destroy()
        self.buttonBack.destroy()

    def draw(self):
        self.message.draw()
        self.answers.draw()
        self.buttonBack.draw()
