class GoExpert:
    def __init__(self, gui):
        self.__gui = gui

    def toNewRule(self, typeDiseases):
        self.__gui.communication.destroy()
        self.__gui.communication = self.__gui.creatorCommunication.getNewRule(typeDiseases)
        self.__gui.communication.draw()

    def toTypeForRules(self):
        self.__gui.communication.destroy()
        self.__gui.communication = self.__gui.creatorCommunication.getTypeForRules()
        self.__gui.communication.draw()

    def toShowRules(self):
        self.__gui.communication.destroy()
        self.__gui.communication = self.__gui.creatorCommunication.getShowRules()
        self.__gui.communication.draw()

    def toNewDisease(self):
        self.__gui.communication.destroy()
        self.__gui.communication = self.__gui.creatorCommunication.getNewDisease()
        self.__gui.communication.draw()

    def toShowDisease(self, disease):
        self.__gui.communication.destroy()
        self.__gui.communication = self.__gui.creatorCommunication.getShowDisease(disease)
        self.__gui.communication.draw()

    def toShowDiseases(self, typeDiseases):
        self.__gui.communication.destroy()
        self.__gui.communication = self.__gui.creatorCommunication.getShowDiseases(typeDiseases=typeDiseases)
        self.__gui.communication.draw()

    def toTypeForDiseases(self):
        self.__gui.communication.destroy()
        self.__gui.communication = self.__gui.creatorCommunication.getTypeForDiseases()
        self.__gui.communication.draw()

    def toNewType(self):
        self.__gui.communication.destroy()
        self.__gui.communication = self.__gui.creatorCommunication.getNewType()
        self.__gui.communication.draw()

    def toMain(self):
        self.__gui.communication.destroy()
        self.__gui.communication = self.__gui.creatorCommunication.getMain()
        self.__gui.communication.draw()

    def toUpdateType(self, typeDiseases):
        self.__gui.communication.destroy()
        self.__gui.communication = self.__gui.creatorCommunication.getUpdateType(typeDiseases)
        self.__gui.communication.draw()

    def toTypeForAdded(self):
        self.__gui.communication.destroy()
        self.__gui.communication = self.__gui.creatorCommunication.getTypeForAdded()
        self.__gui.communication.draw()
