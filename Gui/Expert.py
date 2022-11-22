from Gui.Gui import Gui
from Gui.Nav.NavExpert import NavExpert
from Gui.Communication.Expert.Saver import Saver
from Gui.Communication.Expert.Helpers.GoExpert import GoExpert
from Gui.Communication.Expert.Helpers.CreatorExpert import CreatorExpert


class Expert(Gui):
    def __init__(self, frames, rules, system, diseasesData, app, window, setting):
        super().__init__()
        self.app = app
        self.window = window
        self.setting = setting
        self.system = system

        self.rules = rules
        self.frames = frames
        self.diseasesData = diseasesData
        self.saver = Saver(self.frames, self.diseasesData, system)

        self.goCommunications = GoExpert(self)
        self.creatorCommunication = CreatorExpert(self)
        self.communication = self.creatorCommunication.getMain()

    def switch(self):
        super().destroy()
        self.app.gui = self.app.getClient()
        self.app.gui.run()

    def settings(self):
        self.window.root.title('Медицинская ЭС (эксперт)')
        self.window.root.configure(bg=self.setting['window']['bg'])

    def run(self):
        self.navigation = NavExpert(self)
        super().run()
