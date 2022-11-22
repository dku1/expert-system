from abc import ABC
from abc import abstractmethod


class Gui(ABC):
    def __init__(self):
        self.window = None
        self.communication = None
        self.navigation = None

    def run(self):
        self.settings()
        self.communication.draw()
        self.window.run()

    def destroy(self):
        self.navigation.destroy()
        self.communication.destroy()

    @abstractmethod
    def settings(self):
        pass
