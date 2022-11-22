from system import System
from Data.Data import Data
from Gui.window import Window
from Gui.Client import Client
from Gui.Expert import Expert
from Data.Frames import Frames
from Data.DiseasesData import DiseasesData
from Data.ClinicRequest import ClinicRequest


class App:
    def __init__(self):
        self.rules: Data = Data('Data\\rule.json').get()
        self.doctors: Data = Data('Data\\doctors.json').get()
        self.framesData: Data = Data('Data\\frame.json').get()
        self.descriptions: Data = Data('Data\\descriptions.json').get()

        self.clientSettings = Data('settings\\client.json').get()
        self.expertSettings = Data('settings\\expert.json').get()

        self.clinicRequest: ClinicRequest = ClinicRequest()

        self.system: System = System(self.rules)
        self.frames: Frames = Frames(self.framesData)
        self.diseasesData: DiseasesData = DiseasesData(self.descriptions, self.doctors)

        self.window = Window(550, 600, 'Экспертная система')

        self.gui = self.getClient()

    def getClient(self):
        return Client(self.frames, self.system, self.diseasesData, self.clinicRequest, self, self.window,
                      self.clientSettings)

    def getExpert(self):
        return Expert(self.frames, self.rules, self.system, self.diseasesData, self, self.window, self.expertSettings)

    def start(self):
        self.gui.run()


app = App()
app.start()
