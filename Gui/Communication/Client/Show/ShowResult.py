from Gui.Widgets.TextW import TextW
from Gui.Widgets.LabelW import LabelW
from Gui.Interfaces.Button import Button
from Gui.Interfaces.Message import Message
from Gui.Communication.Client.Show.Show import Show


class ShowResult(Show):
    def __init__(self, root, guiEvent, userAnswers, system, diseasesData, buttonBackEvent, buttonToStart,
                 settingMessage, settingButton, settingText):
        super().__init__(root, guiEvent, userAnswers, buttonBackEvent, settingMessage, settingButton)
        self.disease = system.getResult(self.userAnswers.getSymptoms(), self.userAnswers.getTypeDisease())
        self.message = Message(self.root, "Мы считаем, что у вас:", self.settingMessage)
        self.diseasesData = diseasesData
        self.subMessage = LabelW(self.message.getFrame(), f"{self.disease}", "black")
        self.text = TextW(self.message.getFrame(), self.renderText(), settingText)
        self.buttonNext = Button(self.message.getFrame(), self.guiEvent, "Найти поликлинику", self.settingButton)
        self.buttonBack.addAdditionalButton(buttonToStart, "К началу")

    def renderText(self):
        doctor = self.diseasesData.getDoctor(self.userAnswers.getTypeDisease())
        description = self.diseasesData.getDescription(self.userAnswers.getTypeDisease(), self.disease)
        self.userAnswers.setRecommendation(f"Мы рекомендуем вам записаться к специалисту: {doctor}")
        return f"{self.disease} - это {description}\n\n{self.userAnswers.getRecommendation()}"

    def settings(self):
        super().settings()
        self.subMessage.widget.configure(bg=self.settingMessage['bg'])

    def destroy(self):
        super().destroy()

    def draw(self):
        super().draw()
