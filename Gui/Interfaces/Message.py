from Gui.Widgets.LabelFrameW import LabelFrameW


class Message:
    def __init__(self, root, text: str, settingMessage):
        self.__root = root
        self.__widget = self.getWidgetWithText(text)
        self.settingMessage = settingMessage

    def getWidgetWithText(self, text: str):
        return LabelFrameW(self.__root, text)

    def settings(self):
        self.getFrame().configure(background=self.settingMessage['bg'])
        self.getFrame().configure(fg=self.settingMessage['fg'])

    def destroy(self):
        self.__widget.widget.destroy()

    def getFrame(self):
        return self.__widget.widget

    def draw(self):
        self.settings()
        self.__widget.draw(expand=True, padx=50, pady=50)
