from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from Gui.Widgets.LabelW import LabelW
from Gui.Interfaces.Button import Button
from Gui.Interfaces.Message import Message
from Gui.Communication.Expert.Form.Form import Form


class NewRule(Form):
    def __init__(self, root, frames, diseasesData, typeDisease, guiEvent, buttonBackEvent, settingMessage, buttonSetting,
                 saver):
        super().__init__(root, guiEvent, buttonBackEvent, settingMessage, buttonSetting)
        self.saver = saver
        self.diseasesData = diseasesData
        self.frames = frames
        self.root = root
        self.typeDisease = typeDisease
        self.buttonBackEvent = buttonBackEvent
        self.buttonSetting = buttonSetting
        self.message = Message(root, typeDisease, settingMessage)
        self.questions = self.createQuestions()
        self.buttonBack = Button(root, buttonBackEvent, "Назад", buttonSetting)

        diseases = self.diseasesData.getDiseasesByType(self.typeDisease)
        self.diseaseCB = Combobox(self.message.getFrame(), height=30, width=70, values=list(diseases))

        self.button = Button(self.message.getFrame(), self.save, "Сохранить", buttonSetting)
        self.button.setWidthButton(50)

    def createQuestions(self):
        questions = []
        for question, answers in self.frames.getDataQuestionsByTypeDisease(self.typeDisease).items():
            questions.append({question: Combobox(self.message.getFrame(), height=30, width=70, values=answers)})
        return questions

    def destroy(self):
        super().destroy()

    def draw(self):
        self.message.draw()
        for question in self.questions:
            label = LabelW(self.message.getFrame(), list(question.keys())[0], bg='#b85042')
            label.widget.configure(width=40)
            label.draw(pady=7)
            question[list(question.keys())[0]].pack()
        label = LabelW(self.message.getFrame(), 'Заболевание', bg='#b85042')
        label.widget.configure(width=40)
        label.draw(pady=7)
        self.diseaseCB.pack(pady=5)
        self.button.draw()
        self.buttonBack.draw()

    def renderText(self):
        pass

    def save(self):
        answers = {}
        for question in self.questions:
            items = list(question.items())[0]
            answers[items[0]] = items[1].get()
        disease = self.diseaseCB.get()
        if '' not in answers.values() and '' != disease:
            if self.saver.saveRule(self.typeDisease, disease, answers):
                self.buttonBackEvent()
            else:
                messagebox.showerror("Error", "Такое правило уже есть")

    def __checkForEmptiness(self, text, disease):
        return text != '' and (disease != '' and disease != 'Название')
