class Frames:
    def __init__(self, framesData):
        self.__framesData = framesData

    def getFramesData(self):
        return self.__framesData

    def setFramesDataByType(self, obj, typeDisease):
        self.__framesData["Выберите вид заболевания"][typeDisease] = obj

    def getFrameTypes(self):
        return self.__framesData["Выберите вид заболевания"].keys()

    def getDataQuestionsByTypeDisease(self, typeDisease):
        return self.__framesData["Выберите вид заболевания"][typeDisease]
