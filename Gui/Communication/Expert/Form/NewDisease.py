from tkinter import END
from tkinter.constants import LEFT
from Gui.Widgets.TextW import TextW
from Gui.Interfaces.Button import Button
from Gui.Interfaces.Message import Message
from Gui.Widgets.LabelFrameW import LabelFrameW
from Gui.Communication.Expert.Form.Form import Form
from Gui.Widgets.EntryWithPlaceholder import EntryWithPlaceholder


class NewDisease(Form):
    def __init__(self, root, typeDisease, guiEvent, buttonBackEvent, settingMessage, textSetting, buttonSetting, saver):
        super().__init__(root, guiEvent, buttonBackEvent, settingMessage, buttonSetting)
        self.saver = saver
        self.typeDisease = typeDisease
        self.buttonBackEvent = buttonBackEvent
        self.message = Message(root, "Заболевание", settingMessage)
        self.phone = LabelFrameW(self.message.getFrame(), bg='#a7beae')
        self.entryForTitle = EntryWithPlaceholder(self.phone.widget, 'Название')
        self.text = TextW(self.message.getFrame(), self.renderText(), textSetting)
        self.buttonBack = Button(root, lambda: buttonBackEvent(typeDisease), "Назад", buttonSetting)
        self.button = Button(self.message.getFrame(), self.save, "Сохранить", buttonSetting)
        self.__settings()

    def destroy(self):
        super().destroy()

    def draw(self):
        self.message.draw()
        self.phone.draw()
        self.entryForTitle.pack(side=LEFT, padx=6)
        self.text.draw()
        self.button.draw()
        self.buttonBack.draw()

    def renderText(self):
        return ''

    def save(self):
        text = self.text.widget.get("1.0", END).strip()
        disease = self.entryForTitle.get().strip()
        if self.__checkForEmptiness(text, disease):
            self.saver.saveDescription(disease, text, self.typeDisease)
            self.buttonBackEvent(self.typeDisease)

    def __checkForEmptiness(self, text, disease):
        return text != '' and (disease != '' and disease != 'Название')

    def __settings(self):
        self.entryForTitle.configure(width=43)
