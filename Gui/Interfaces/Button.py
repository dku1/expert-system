from tkinter.constants import RIGHT

from Gui.Widgets.ButtonW import ButtonW
from Gui.Widgets.LabelFrameW import LabelFrameW


class Button:
    def __init__(self, root, command, text, settingButton):
        self.__root = root
        self.__command = command
        self.__labelFrameBgColor = settingButton['labelFrameBgColor']
        self.__labelFrame = LabelFrameW(self.__root, bg=self.__labelFrameBgColor)
        self.__widget = ButtonW(self.__labelFrame.widget, self.__command, text, width=settingButton['width'])
        self.__widget.widget.configure(bg=settingButton['bg'])

    def setWidthButton(self, width):
        self.__widget.widget.configure(width=width)

    def addAdditionalButton(self, command, text):
        self.__additionalButton = ButtonW(self.__labelFrame.widget, command, text)
        self.__additionalButton.draw(side=RIGHT, padx=13, pady=13)

    def removeAdditionalButton(self):
        self.__additionalButton.widget.destroy()

    def update(self):
        self.destroy()
        self.__labelFrame = LabelFrameW(self.__root, bg=self.__labelFrameBgColor)
        self.__widget = ButtonW(self.__labelFrame.widget, self.__command)

    def destroy(self):
        self.__labelFrame.widget.destroy()
        self.__widget.widget.destroy()

    def draw(self):
        self.__labelFrame.draw()
        self.__widget.draw(side=RIGHT, padx=13, pady=13)
