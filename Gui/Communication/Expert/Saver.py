from Data.Data import Data


class Saver:
    def __init__(self, frames, diseasesData, system):
        self.system = system
        self.frames = frames
        self.diseasesData = diseasesData

    def saveNewType(self, typeDisease):
        self.diseasesData.setNewTypeDisease(typeDisease)
        Data('Data\\descriptions.json').save(self.diseasesData.getDescriptions())

    def saveRule(self, typeDisease, disease, newRule):
        if self.system.saveRule(typeDisease, disease, newRule):
            Data('Data\\rule.json').save(self.system.getRules())
            return True
        else:
            return False

    def saveDoctor(self, typeDisease, doctor):
        self.diseasesData.setDoctor(typeDisease, doctor)
        Data('Data\\doctors.json').save(self.diseasesData.getDoctors())

    def saveToFrame(self, text, typeDisease):
        self.frames.setFramesDataByType(self.__convertTextQuestionsToObject(text), typeDisease)
        self.system.setNewType(typeDisease)
        Data('Data\\frame.json').save(self.frames.getFramesData())

    def saveDescription(self, disease, text, typeDisease):
        self.diseasesData.setDescription(typeDisease, disease, text)
        Data('Data\\descriptions.json').save(self.diseasesData.getDescriptions())

    def __convertTextQuestionsToObject(self, text):
        frame = text.split('\n\n')
        questionsData = {}
        for data in frame:
            arr = data.split('\n')
            if arr[0] != '' and '?' in arr[0]:
                questionsData[arr[0]] = []
                for answer in arr[1].split('.'):
                    if answer != '':
                        questionsData[arr[0]].append(answer.strip())

        return questionsData
