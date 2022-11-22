from tkinter import END
from Gui.Widgets.TextW import TextW
from Gui.Interfaces.Button import Button
from Gui.Interfaces.Message import Message
from Gui.Communication.Expert.Form.Form import Form


class UpdateType(Form):
    def __init__(self, root, buttonBackEvent, typeDisease, frames, settingMessage, textSetting, buttonSetting,
                 guiEvent, saver):
        self.dataType = frames.getDataQuestionsByTypeDisease(typeDisease)
        self.saver = saver
        super().__init__(root, guiEvent, buttonBackEvent, settingMessage, buttonSetting)
        self.frames = frames
        self.typeDisease = typeDisease
        self.message = Message(root, typeDisease, settingMessage)
        self.text = TextW(self.message.getFrame(), self.renderText(), textSetting)
        self.button = Button(self.message.getFrame(), self.save, "Сохранить", buttonSetting)

    def destroy(self):
        super().destroy()

    def draw(self):
        self.message.draw()
        self.text.draw()
        self.button.draw()
        self.buttonBack.draw()

    def renderText(self):
        result = ''
        for question, answers in self.dataType.items():
            result += f'{question}\n{". ".join(answers)}\n\n'
        return result

    def save(self):
        text = self.text.widget.get("1.0", END)
        self.saver.saveToFrame(text, self.typeDisease)
        self.guiEvent()

