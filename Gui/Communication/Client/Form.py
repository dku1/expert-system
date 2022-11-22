from Gui.Widgets.LabelW import LabelW
from Gui.Widgets.ButtonW import ButtonW
from Gui.Interfaces.Button import Button
from Gui.Interfaces.Message import Message
from Gui.Communication.Communication import Communication
from Gui.Widgets.EntryWithPlaceholder import EntryWithPlaceholder


class Form(Communication):
    def __init__(self, root, guiEvent, buttonBackEvent, messageSetting, buttonSetting):
        super().__init__(root, guiEvent)
        self.mainFrame = Message(self.root, "Ваше местоположение", messageSetting)
        self.labelForCity = LabelW(self.mainFrame.getFrame(), 'Город', fg='black', bg=messageSetting['bg'])
        self.entryForCity = EntryWithPlaceholder(self.mainFrame.getFrame(), 'Барнаул')
        self.labelForOutside = LabelW(self.mainFrame.getFrame(), 'Улица', fg='black', bg=messageSetting['bg'])
        self.entryForOutside = EntryWithPlaceholder(self.mainFrame.getFrame(), 'Социалистический, 64')
        self.button = ButtonW(self.mainFrame.getFrame(), self.guiEvent, text='Поиск', width=25)
        self.buttonBack = Button(self.root, buttonBackEvent, "Назад", buttonSetting)

    def destroy(self):
        self.mainFrame.getFrame().destroy()
        self.buttonBack.destroy()

    def draw(self):
        self.mainFrame.draw()
        self.labelForCity.draw(pady=15)
        self.entryForCity.pack(padx=25)
        self.labelForOutside.draw(pady=15)
        self.entryForOutside.pack(padx=25)
        self.button.draw(pady=30)
        self.buttonBack.draw()
