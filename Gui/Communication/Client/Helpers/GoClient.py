class GoClient:
    def __init__(self, gui):
        self.__gui = gui

    def toExpert(self):
        self.__gui.communication.destroy()
        self.__gui = self.__gui.creatorCommunication.getExpert()
        self.__gui.run()

    def toClinic(self):
        city = self.__gui.communication.entryForCity.get()
        outside = self.__gui.communication.entryForOutside.get()
        self.__gui.userAnswers.setCity(city)
        self.__gui.userAnswers.setOutside(outside)

        self.__gui.communication.destroy()
        self.__gui.communication = self.__gui.creatorCommunication.getShowClinic()
        self.__gui.communication.draw()

    def toForm(self):
        self.__gui.communication.destroy()
        self.__gui.communication = self.__gui.creatorCommunication.getForm()
        self.__gui.communication.draw()

    def toShowResult(self):
        self.__gui.communication.destroy()
        self.__gui.communication = self.__gui.creatorCommunication.getShowResult()
        self.__gui.communication.draw()

    def toShowAnswers(self):
        self.__gui.communication.destroy()
        self.__gui.communication = self.__gui.creatorCommunication.getShowAnswers()
        self.__gui.communication.draw()

    def toSelectionType(self):
        self.__gui.userAnswers.clear()
        self.__gui.communication.destroy()
        self.__gui.communication = self.__gui.creatorCommunication.getTypeSelection()
        self.__gui.communication.draw()

    def toInterview(self, iteration=0):
        self.__gui.communication.destroy()
        dataQuestions = self.__gui.frames.getDataQuestionsByTypeDisease(self.__gui.userAnswers.getTypeDisease())
        self.__gui.communication = self.__gui.creatorCommunication.getInterview(dataQuestions, iteration)
        self.__gui.communication.draw()
