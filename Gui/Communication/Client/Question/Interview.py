from Gui.Communication.Client.Question.Question import Question
from Gui.Communication.Client.Helpers.Interview.QuestionsInterview import QuestionsInterview
from Gui.Communication.Client.Helpers.Interview.InterfacesInterview import InterfacesInterview


class Interview(Question):
    def __init__(self, root, dataQuestions: list, guiEvent,
                 userAnswers, guiEventShowAnswers, settingMessage, settingButton, radioButtonSetting,
                 iteration: int = 0):
        super().__init__(root, guiEvent, userAnswers, settingMessage, radioButtonSetting)
        self.settingButton = settingButton
        self.iteration: int = iteration
        self.interfacesInterview = InterfacesInterview(self)
        self.questionsInterview = QuestionsInterview(dataQuestions, self)

        self.question = self.interfacesInterview.getMessage()
        self.answers = self.interfacesInterview.getAnswers()
        self.button = self.interfacesInterview.getButton()

        self.__guiEventShowAnswers = guiEventShowAnswers

    def responseProcessing(self):
        self.__writeAnswer()
        if not self.questionsInterview.currentQuestionIsLast():
            self.questionsInterview.goToNextQuestion()
        else:
            self.__guiEventShowAnswers()

    def getResponse(self):
        question = self.questionsInterview.getTextQuestion()
        answer = self.answers.getAnswerUser()
        return [question, answer]

    def destroy(self):
        super().destroy()
        self.button.destroy()

    def draw(self):
        super().draw()
        self.button.draw()

    def __writeAnswer(self):
        result = self.getResponse()
        self.userAnswers.setSymptom(result[0], result[1])
