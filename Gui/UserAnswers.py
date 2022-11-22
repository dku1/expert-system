class UserAnswers:
    def __init__(self):
        self.__typeDisease = None
        self.__symptoms = {}
        self.__city = None
        self.__outside = None
        self.__recommendation = "Пройдите опрос для получения рекомендаций"

    def setRecommendation(self, recommendation):
        self.__recommendation = recommendation

    def getRecommendation(self):
        return self.__recommendation

    def setCity(self, city):
        self.__city = city

    def getCity(self):
        return self.__city

    def setOutside(self, outside):
        self.__outside = outside

    def getOutside(self):
        return self.__outside

    def setTypeDisease(self, typeDisease: str):
        self.__typeDisease = typeDisease

    def getTypeDisease(self):
        return self.__typeDisease

    def getLastAnswer(self):
        return len(self.__symptoms) - 1

    def getSymptoms(self):
        return self.__symptoms

    def setSymptom(self, question, answer):
        self.__symptoms[question] = answer

    def clear(self):
        self.__typeDisease = None
        self.__symptoms = {}
        self.__city = None
        self.__outside = None
        self.__recommendation = "Пройдите опрос для получения рекомендаций"
