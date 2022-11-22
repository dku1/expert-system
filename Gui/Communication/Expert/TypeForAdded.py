from Gui.Interfaces.Button import Button
from Gui.Interfaces.Answers import Answers
from Gui.Interfaces.Message import Message


class TypeForAdded:
    def __init__(self, root, buttonBackEvent, typeDisease, typeEvents, settingMessage, radioButtonSetting,
                 buttonSetting, guiEvent):
        self.typeDisease = typeDisease
        self.message = Message(root, "Виды заболеваний", settingMessage)
        self.answers = Answers(self.message.getFrame(), typeDisease, lambda: typeEvents(self.answers.getAnswerUser()),
                               radioButtonSetting)
        self.buttonAdd = Button(self.message.getFrame(), guiEvent, "Добавить", buttonSetting)
        self.buttonBack = Button(root, buttonBackEvent, "Назад", buttonSetting)

    def destroy(self):
        self.message.destroy()
        self.buttonBack.destroy()

    def draw(self):
        self.message.draw()
        self.answers.draw()
        self.buttonAdd.draw()
        self.buttonBack.draw()
