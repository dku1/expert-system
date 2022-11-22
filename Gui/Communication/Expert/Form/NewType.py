from tkinter import END
from tkinter.constants import LEFT
from Gui.Widgets.TextW import TextW
from Gui.Interfaces.Button import Button
from Gui.Interfaces.Message import Message
from Gui.Widgets.LabelFrameW import LabelFrameW
from Gui.Communication.Expert.Form.Form import Form
from Gui.Widgets.EntryWithPlaceholder import EntryWithPlaceholder


class NewType(Form):
    def __init__(self, root, settingMessage, textSetting, buttonSetting, saver, guiEvent,
                 buttonBackEvent):
        super().__init__(root, guiEvent, buttonBackEvent, settingMessage, buttonSetting)
        self.saver = saver
        self.message = Message(root, "Вид заболеваний", settingMessage)
        self.phone = LabelFrameW(self.message.getFrame(), bg='#a7beae')
        self.entryForTitle = EntryWithPlaceholder(self.phone.widget, 'Название')
        self.entryForDoctor = EntryWithPlaceholder(self.phone.widget, 'Врач')
        self.text = TextW(self.message.getFrame(), self.renderText(), textSetting)
        self.button = Button(self.message.getFrame(), self.save, "Сохранить", buttonSetting)
        self.__settings()

    def destroy(self):
        super().destroy()

    def draw(self):
        self.message.draw()
        self.phone.draw()
        self.entryForTitle.pack(side=LEFT, padx=6)
        self.entryForDoctor.pack(padx=6)
        self.text.draw()
        self.button.draw()
        self.buttonBack.draw()

    def renderText(self):
        return ''

    def save(self):
        text = self.text.widget.get("1.0", END).strip()
        typeDisease = self.entryForTitle.get().strip()
        doctor = self.entryForDoctor.get().strip()
        if self.__checkForEmptiness(text, typeDisease, doctor):
            self.saver.saveToFrame(text, self.entryForTitle.get())
            self.saver.saveDoctor(typeDisease, doctor)
            self.saver.saveNewType(typeDisease)
            self.guiEvent()

    def __checkForEmptiness(self, text, typeDisease, doctor):
        return text != '' and (typeDisease != '' and typeDisease != 'Название') and (doctor != '' and doctor != 'Врач')

    def __settings(self):
        self.entryForTitle.configure(width=21)
        self.entryForDoctor.configure(width=21)
