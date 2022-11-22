from Gui.Widgets.TextW import TextW
from Gui.Widgets.LabelW import LabelW
from Gui.Interfaces.Message import Message
from Gui.Communication.Client.Show.Show import Show


class ShowClinic(Show):
    def __init__(self, root, guiEvent, userAnswers, buttonBackEvent, clinic, settingMessage, settingButton,
                 settingText):
        super().__init__(root, guiEvent, userAnswers, buttonBackEvent, settingMessage, settingButton)
        self.clinicData = clinic
        self.message = Message(root, f'{self.getConcreteData("name")}', self.settingMessage)
        self.subMessage = LabelW(self.message.getFrame(), f"{self.getConcreteData('url')}")
        self.text = TextW(self.message.getFrame(), self.renderText(), settingText)
        self.buttonBack.addAdditionalButton(self.guiEvent, "К началу")

    def settings(self):
        self.subMessage.widget.configure(fg='#191970', bg=self.settingMessage['bg'])

    def renderText(self):
        return f"Телефон: {self.getConcreteData('Phones')[0]['formatted']}\n\n" \
               f"Расписание: {self.getConcreteData('Hours')['text']}\n\nАдрес: {self.getConcreteData('address')}\n\n" \
               f"{self.userAnswers.getRecommendation()}"

    def getConcreteData(self, dataName):
        return self.clinicData[dataName]

    def draw(self):
        self.message.draw()
        self.subMessage.draw()
        self.text.draw()
        self.buttonBack.draw()
        self.settings()
