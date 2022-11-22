from Gui.Communication.Expert.Main import Main
from Gui.Communication.Expert.ShowRules import ShowRules
from Gui.Communication.Expert.Form.NewType import NewType
from Gui.Communication.Expert.Form.NewRule import NewRule
from Gui.Communication.Expert.ShowDisease import ShowDisease
from Gui.Communication.Expert.TypeForAdded import TypeForAdded
from Gui.Communication.Expert.ShowDiseases import ShowDiseases
from Gui.Communication.Expert.TypeForRules import TypeForRules
from Gui.Communication.Expert.Form.UpdateType import UpdateType
from Gui.Communication.Expert.Form.NewDisease import NewDisease
from Gui.Communication.Expert.TypeForDiseases import TypeForDiseases


class CreatorExpert:
    def __init__(self, gui):
        self.__gui = gui
        self.typeForShowDisease = None
        self.mainActions = [
            self.__gui.goCommunications.toTypeForAdded,
            self.__gui.goCommunications.toTypeForDiseases,
            self.__gui.goCommunications.toShowRules,
        ]

    def getNewRule(self, typeDiseases):
        return NewRule(self.__gui.window.root, self.__gui.frames, self.__gui.diseasesData, typeDiseases,
                       "Событие", self.__gui.goCommunications.toShowRules,
                       self.__gui.setting['message'], self.__gui.setting['button'], self.__gui.saver)

    def getTypeForRules(self):
        return TypeForRules(self.__gui.window.root, self.__gui.goCommunications.toShowRules,
                            self.__gui.frames.getFrameTypes(),
                            self.__gui.goCommunications.toNewRule, self.__gui.setting['message'],
                            self.__gui.setting['radioButton'], self.__gui.setting['button'])

    def getShowRules(self):
        return ShowRules(self.__gui.window.root, self.__gui.rules, self.__gui.goCommunications.toTypeForRules,
                         self.__gui.goCommunications.toMain, self.__gui.setting['message'],
                         self.__gui.setting['button'], self.__gui.setting['text'])

    def getNewDisease(self):
        return NewDisease(self.__gui.window.root, self.typeForShowDisease, "Событие",
                          self.__gui.goCommunications.toShowDiseases, self.__gui.setting['message'],
                          self.__gui.setting['text'], self.__gui.setting['button'], self.__gui.saver)

    def getShowDisease(self, disease):
        return ShowDisease(self.__gui.window.root, disease,
                           self.__gui.diseasesData.getDescription(self.typeForShowDisease, disease),
                           self.__gui.goCommunications.toShowDiseases, self.__gui.setting['message'],
                           self.__gui.setting['button'], self.__gui.setting['text'], self.typeForShowDisease,
                           self.__gui.saver)

    def getShowDiseases(self, typeDiseases):
        self.typeForShowDisease = typeDiseases
        return ShowDiseases(self.__gui.window.root, typeDiseases,
                            self.__gui.diseasesData.getDiseasesByType(typeDiseases),
                            self.__gui.goCommunications.toTypeForDiseases, self.__gui.goCommunications.toNewDisease,
                            self.__gui.setting['message'],
                            self.__gui.setting['button'], self.__gui.setting['radioButton'],
                            self.__gui.goCommunications.toShowDisease)

    def getNewType(self):
        return NewType(self.__gui.window.root, self.__gui.setting['message'], self.__gui.setting['text'],
                       self.__gui.setting['button'], self.__gui.saver,
                       self.__gui.goCommunications.toMain, self.__gui.goCommunications.toTypeForAdded)

    def getUpdateType(self, typeDiseases):
        return UpdateType(self.__gui.window.root, self.__gui.goCommunications.toTypeForAdded, typeDiseases,
                          self.__gui.frames, self.__gui.setting['message'],
                          self.__gui.setting['text'], self.__gui.setting['button'], self.__gui.goCommunications.toMain,
                          self.__gui.saver)

    def getTypeForDiseases(self):
        return TypeForDiseases(self.__gui.window.root, self.__gui.goCommunications.toMain,
                               self.__gui.frames.getFrameTypes(), self.__gui.goCommunications.toShowDiseases,
                               self.__gui.setting['message'], self.__gui.setting['radioButton'],
                               self.__gui.setting['button'])

    def getTypeForAdded(self):
        return TypeForAdded(self.__gui.window.root, self.__gui.goCommunications.toMain,
                            self.__gui.frames.getFrameTypes(), self.__gui.goCommunications.toUpdateType,
                            self.__gui.setting['message'], self.__gui.setting['radioButton'],
                            self.__gui.setting['button'], self.__gui.goCommunications.toNewType)

    def getMain(self):
        return Main(self.__gui.window.root, self.mainActions, self.__gui.setting['message'],
                    self.__gui.setting['radioButton'])
