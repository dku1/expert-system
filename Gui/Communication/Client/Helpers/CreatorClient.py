from Gui.Communication.Client.Form import Form
from Gui.Communication.Client.Show.ShowClinic import ShowClinic
from Gui.Communication.Client.Show.ShowResult import ShowResult
from Gui.Communication.Client.Show.ShowAnswers import ShowAnswers
from Gui.Communication.Client.Question.Interview import Interview
from Gui.Communication.Client.Question.TypeSelection import TypeSelection


class CreatorClient:
    def __init__(self, gui):
        self.__gui = gui

    def getShowClinic(self):
        city = self.__gui.userAnswers.getCity()
        outside = self.__gui.userAnswers.getOutside()
        return ShowClinic(self.__gui.window.root, self.__gui.goCommunications.toSelectionType,
                          self.__gui.userAnswers, self.__gui.goCommunications.toForm,
                          self.__gui.clinicRequest.get(city, outside),
                          self.__gui.setting['message'], self.__gui.setting['button'], self.__gui.setting['text'])

    def getForm(self):
        return Form(self.__gui.window.root,
                    self.__gui.goCommunications.toClinic, self.__gui.goCommunications.toShowResult,
                    self.__gui.setting['message'], self.__gui.setting['button'])

    def getShowResult(self):
        return ShowResult(self.__gui.window.root, self.__gui.goCommunications.toForm,
                          self.__gui.userAnswers, self.__gui.system,
                          self.__gui.diseasesData, self.__gui.goCommunications.toShowAnswers,
                          self.__gui.goCommunications.toSelectionType,
                          self.__gui.setting['message'], self.__gui.setting['button'], self.__gui.setting['text'])

    def getShowAnswers(self):
        return ShowAnswers(self.__gui.window.root, self.__gui.goCommunications.toShowResult, self.__gui.userAnswers,
                           lambda: self.__gui.goCommunications.toInterview(
                               iteration=self.__gui.userAnswers.getLastAnswer()),
                           self.__gui.setting['message'], self.__gui.setting['button'], self.__gui.setting['text'])

    def getInterview(self, dataQuestions, iteration):
        return Interview(self.__gui.window.root, dataQuestions,
                         self.__gui.goCommunications.toSelectionType,
                         self.__gui.userAnswers, self.__gui.goCommunications.toShowAnswers,
                         self.__gui.setting['message'], self.__gui.setting['button'], self.__gui.setting['radioButton'],
                         iteration)

    def getTypeSelection(self):
        return TypeSelection(self.__gui.window.root, self.__gui.frames.getFrameTypes(),
                             self.__gui.goCommunications.toInterview, self.__gui.userAnswers,
                             self.__gui.setting['message'], self.__gui.setting['radioButton'])
