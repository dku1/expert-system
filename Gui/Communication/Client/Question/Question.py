from Gui.Communication.Communication import Communication
from abc import abstractmethod


class Question(Communication):
    def __init__(self, root, guiEvent, userAnswers, settingMessage, radioButtonSetting):
        super().__init__(root, guiEvent)
        self.radioButtonSetting = radioButtonSetting
        self.settingMessage = settingMessage
        self.userAnswers = userAnswers
        self.question = None
        self.answers = None

    @abstractmethod
    def getResponse(self):
        pass

    @abstractmethod
    def responseProcessing(self):
        pass

    def destroy(self):
        self.question.destroy()

    def draw(self):
        self.question.draw()
        self.answers.draw()
