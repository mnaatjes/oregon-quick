import logging
from src.engine.observability.inspection.dashboard import DashboardProvider
from src.engine.observability.control.console import CommandConsole

class ObservabilityManager:
    def __init__(self, engine):
        self.logger = logging.getLogger('OregonQuick.Observability')
        
        # Initialize Providers
        self.dashboard = DashboardProvider()
        self.control = CommandConsole(engine)

    def dispatch(self, engine):
        """Dispatches game state to all active observability tools."""
        # For now, we only have the dashboard
        pass

    def get_debug_layout(self, engine):
        """Returns the dashboard layout for the current wagon."""
        return self.dashboard.get_layout(engine.wagon)
