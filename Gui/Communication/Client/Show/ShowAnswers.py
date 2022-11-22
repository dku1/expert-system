from Gui.Widgets.TextW import TextW
from Gui.Widgets.LabelW import LabelW
from Gui.UserAnswers import UserAnswers
from Gui.Interfaces.Button import Button
from Gui.Interfaces.Message import Message
from Gui.Communication.Client.Show.Show import Show


class ShowAnswers(Show):
    def __init__(self, root, guiEvent, userAnswers: UserAnswers, buttonBackEvent, settingMessage, settingButton,
                 settingText):
        super().__init__(root, guiEvent, userAnswers, buttonBackEvent, settingMessage, settingButton)
        self.message = Message(self.root, self.userAnswers.getTypeDisease(), self.settingMessage)
        self.subMessage = LabelW(self.message.getFrame(), "Ваши ответы", "black")
        self.text = TextW(self.message.getFrame(), self.renderText(), settingText)
        self.buttonNext = Button(self.message.getFrame(), self.guiEvent, "Узнать результат", self.settingButton)
        self.subMessage.widget.configure(bg=settingMessage['bg'])

    def renderText(self):
        result = ''
        for question, answer in self.userAnswers.getSymptoms().items():
            result += f'{question}\n{answer}\n\n'
        return result

    def destroy(self):
        super().destroy()

    def draw(self):
        super().draw()
