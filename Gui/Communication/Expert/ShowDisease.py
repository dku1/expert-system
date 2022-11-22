from tkinter import END
from Gui.Widgets.TextW import TextW
from Gui.Interfaces.Button import Button
from Gui.Interfaces.Message import Message


class ShowDisease:
    def __init__(self, root, disease, description, buttonBackEvent, messageSetting, buttonSetting, textSetting,
                 typeDisease, saver):
        self.saver = saver
        self.disease = disease
        self.typeDisease = typeDisease
        self.buttonBackEvent = buttonBackEvent
        self.message = Message(root, disease, messageSetting)
        self.text = TextW(self.message.getFrame(), description, textSetting)
        self.button = Button(root, lambda: buttonBackEvent(typeDisease), "Назад", buttonSetting)
        self.buttonSave = Button(self.message.getFrame(), self.save, "Сохранить", buttonSetting)

    def save(self):
        text = self.text.widget.get("1.0", END)
        self.saver.saveDescription(self.disease, text.strip(), self.typeDisease)
        self.buttonBackEvent(self.typeDisease)

    def destroy(self):
        self.message.destroy()
        self.button.destroy()

    def draw(self):
        self.message.draw()
        self.text.draw()
        self.buttonSave.draw()
        self.button.draw()
