from Gui.Nav.Nav import Nav


class NavClient(Nav):
    def __init__(self, gui):
        super().__init__(gui)

    def initCommands(self):
        self.navigationMenu.add_command(label="К началу", command=self.gui.goCommunications.toSelectionType)
        self.navigationMenu.add_command(label="Найти поликлинику", command=self.gui.goCommunications.toForm)
        self.navigationMenu.add_command(label="Интерфейс эксперта", command=self.gui.switch)

    def destroy(self):
        super().destroy()
