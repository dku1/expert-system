from Gui.Interfaces.Button import Button
from Gui.Interfaces.Message import Message
from Gui.Interfaces.Answers import Answers


class InterfacesInterview:
    def __init__(self, interview):
        self.interview = interview

    def getMessage(self):
        return Message(self.interview.root, self.interview.questionsInterview.getTextQuestion(),
                       self.interview.settingMessage)

    def getAnswers(self):
        return Answers(self.interview.question.getFrame(), self.interview.questionsInterview.getAnswers(),
                       self.interview.responseProcessing, self.interview.radioButtonSetting)

    def getButton(self):
        return Button(self.interview.root, self.__getButtonEvent(), "Назад", self.interview.settingButton)

    def updatedInterfaces(self):
        self.interview.destroy()

        self.interview.question = self.getMessage()
        self.interview.answers = self.getAnswers()
        self.interview.button = self.getButton()

        self.interview.draw()

    def __getButtonEvent(self):
        if self.interview.iteration == 0:
            return self.interview.guiEvent
        return self.interview.questionsInterview.goToPreviousQuestion
