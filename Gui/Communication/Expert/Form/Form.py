from abc import abstractmethod
from Gui.Interfaces.Button import Button
from Gui.Communication.Communication import Communication


class Form(Communication):
    def __init__(self, root, guiEvent, buttonBackEvent, settingMessage, buttonSetting):
        super().__init__(root, guiEvent)
        self.settingMessage = settingMessage

        self.message = None
        self.buttonBack = Button(root, buttonBackEvent, "Назад", buttonSetting)

    @abstractmethod
    def draw(self):
        pass

    def destroy(self):
        self.message.destroy()
        self.buttonBack.destroy()

    @abstractmethod
    def renderText(self):
        pass

    @abstractmethod
    def save(self):
        pass

