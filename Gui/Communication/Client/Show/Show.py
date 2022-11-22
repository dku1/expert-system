from abc import abstractmethod
from Gui.Interfaces.Button import Button
from Gui.Communication.Communication import Communication


class Show(Communication):
    def __init__(self, root, guiEvent, userAnswers, buttonBackEvent, settingMessage, settingButton):
        super().__init__(root, guiEvent)
        self.settingButton = settingButton
        self.settingMessage = settingMessage
        self.buttonBackEvent = buttonBackEvent
        self.userAnswers = userAnswers
        self.message = None
        self.subMessage = None
        self.text = None
        self.buttonNext = None
        self.buttonBack = Button(self.root, self.buttonBackEvent, "Назад", self.settingButton)

    @abstractmethod
    def renderText(self):
        pass

    def settings(self):
        self.buttonNext.setWidthButton(50)

    def destroy(self):
        self.message.destroy()
        self.buttonBack.destroy()

    def draw(self):
        self.message.draw()
        self.subMessage.draw()
        self.text.draw()
        self.buttonNext.draw()
        self.buttonBack.draw()
        self.settings()
