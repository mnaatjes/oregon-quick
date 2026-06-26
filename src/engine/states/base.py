from abc import ABC, abstractmethod

class BaseState(ABC):
    @abstractmethod
    def enter(self):
        pass

    @abstractmethod
    def update(self, engine):
        pass

    @abstractmethod
    def exit(self):
        pass
