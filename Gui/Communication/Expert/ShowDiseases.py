from Gui.Interfaces.Button import Button
from Gui.Interfaces.Answers import Answers
from Gui.Interfaces.Message import Message


class ShowDiseases:
    def __init__(self, root, typeDiseases, diseases, buttonBackEvent, buttonAddEvent, messageSetting, buttonSetting,
                 radioButtonSetting, eventShow):
        self.message = Message(root, typeDiseases, messageSetting)
        self.answers = Answers(self.message.getFrame(), list(diseases), lambda: eventShow(self.answers.getAnswerUser()),
                               radioButtonSetting)
        self.buttonAdd = Button(self.message.getFrame(), buttonAddEvent, "Добавить", buttonSetting)
        self.buttonBack = Button(root, buttonBackEvent, "Назад", buttonSetting)

    def draw(self):
        self.message.draw()
        self.answers.draw()
        self.buttonAdd.draw()
        self.buttonBack.draw()

    def destroy(self):
        self.message.destroy()
        self.buttonBack.destroy()
