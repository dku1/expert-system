from Gui.Interfaces.Message import Message
from Gui.Interfaces.Answers import Answers
from Gui.Communication.Client.Question.Question import Question


class TypeSelection(Question):
    def __init__(self, root, answers: list, guiEvent, userAnswers, settingMessage, radioButtonSetting):
        super().__init__(root, guiEvent, userAnswers, settingMessage, radioButtonSetting)
        self.question = Message(self.root, "Выберите тип заболеваний", settingMessage)
        self.answers = Answers(self.question.getFrame(), answers, self.responseProcessing, self.radioButtonSetting)

    def responseProcessing(self):
        typeDisease = self.getResponse()
        self.userAnswers.setTypeDisease(typeDisease)
        self.guiEvent()

    def getResponse(self):
        return self.answers.getAnswerUser()

    def destroy(self):
        super().destroy()

    def draw(self):
        super().draw()
