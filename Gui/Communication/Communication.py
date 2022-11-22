from abc import ABC
from abc import abstractmethod


class Communication(ABC):
    def __init__(self, root, guiEvent):
        super().__init__()
        self.root = root
        self.guiEvent = guiEvent

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def destroy(self):
        pass
