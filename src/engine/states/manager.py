import logging
from src.engine.states.base import BaseState

class StateManager:
    def __init__(self):
        self.logger = logging.getLogger('OregonQuick.StateManager')
        self.current_state: BaseState = None

    def transition_to(self, state: BaseState):
        prev_state_name = self.current_state.__class__.__name__ if self.current_state else "None"
        new_state_name = state.__class__.__name__

        self.logger.info(f"Transitioning state: {prev_state_name} -> {new_state_name}")

        if self.current_state:
            self.current_state.exit()
        
        self.current_state = state
        self.current_state.enter()

    def update(self, engine):
        if self.current_state:
            self.current_state.update(engine)
