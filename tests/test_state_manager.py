import pytest
from src.engine.states.manager import StateManager
from src.engine.states.base import BaseState

class MockState(BaseState):
    def __init__(self):
        self.entered = False
        self.exited = False
        self.updated = False

    def enter(self):
        self.entered = True

    def update(self):
        self.updated = True

    def exit(self):
        self.exited = True

def test_state_manager_transition():
    manager = StateManager()
    state1 = MockState()
    state2 = MockState()

    manager.transition_to(state1)
    assert manager.current_state == state1
    assert state1.entered is True

    manager.transition_to(state2)
    assert manager.current_state == state2
    assert state1.exited is True
    assert state2.entered is True

def test_state_manager_update():
    manager = StateManager()
    state = MockState()
    manager.transition_to(state)
    manager.update()
    assert state.updated is True
