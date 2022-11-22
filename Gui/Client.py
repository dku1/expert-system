from Gui.Gui import Gui
from Gui.UserAnswers import UserAnswers
from Gui.Nav.NavClient import NavClient
from Gui.Communication.Communication import Communication
from Gui.Communication.Client.Helpers.GoClient import GoClient
from Gui.Communication.Client.Helpers.CreatorClient import CreatorClient


class Client(Gui):
    def __init__(self, frames, system, diseasesData, clinicRequest, app, window, setting):
        super().__init__()
        self.app = app
        self.window = window
        self.system = system
        self.frames = frames
        self.setting = setting
        self.diseasesData = diseasesData
        self.clinicRequest = clinicRequest

        self.userAnswers: UserAnswers = UserAnswers()

        self.goCommunications = GoClient(self)
        self.creatorCommunication = CreatorClient(self)
        self.communication: Communication = self.creatorCommunication.getTypeSelection()

    def switch(self):
        super().destroy()
        self.app.gui = self.app.getExpert()
        self.app.gui.run()

    def settings(self):
        self.window.root.title('Медицинская ЭС (клиент)')
        self.window.root.configure(bg=self.setting['window']['bg'])

    def run(self):
        self.navigation = NavClient(self)
        super().run()
