from Gui.Nav.Nav import Nav


class NavExpert(Nav):
    def __init__(self, gui):
        super().__init__(gui)

    def initCommands(self):
        self.navigationMenu.add_command(label="На главную", command=self.gui.goCommunications.toMain)
        self.navigationMenu.add_command(label="Интерфейс клиента", command=self.gui.switch)

    def destroy(self):
        super().destroy()
