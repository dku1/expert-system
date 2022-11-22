class DiseasesData:
    def __init__(self, descriptions, doctors):
        self.__descriptions = descriptions
        self.__doctors = doctors

    def setNewTypeDisease(self, typeDisease):
        self.__descriptions[typeDisease] = {}

    def getDiseasesByType(self, typeDiseases):
        return self.__descriptions[typeDiseases]

    def setDoctor(self, typeDisease, doctor):
        self.__doctors[typeDisease] = doctor

    def setDescription(self, typeDisease, disease, description):
        self.__descriptions[typeDisease][disease] = description

    def getDescriptions(self):
        return self.__descriptions

    def getDoctors(self):
        return self.__doctors

    def getDescription(self, typeDisease, disease):
        if typeDisease in list(self.__descriptions.keys()):
            if disease in list(self.__descriptions[typeDisease].keys()):
                return self.__descriptions[typeDisease][disease]
        return self.__descriptions['Робот не определил болезнь']

    def getDoctor(self, typeDisease):
        return self.__doctors[typeDisease]
