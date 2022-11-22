class QuestionsInterview:
    def __init__(self, dataQuestions, interview):
        self.__interview = interview
        self.__dataQuestions = dataQuestions

    def currentQuestionIsLast(self):
        return self.__interview.iteration + 1 == self.getCountQuestions()

    def goToPreviousQuestion(self):
        self.__interview.iteration -= 1
        self.__interview.interfacesInterview.updatedInterfaces()

    def goToNextQuestion(self):
        self.__interview.iteration += 1
        self.__interview.interfacesInterview.updatedInterfaces()

    def getCountQuestions(self):
        return len(list(self.__dataQuestions))

    def getTextQuestion(self):
        return list(self.__dataQuestions)[self.__interview.iteration]

    def getAnswers(self):
        return self.__dataQuestions[self.getTextQuestion()]
