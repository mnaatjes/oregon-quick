from rich.console import Console
from src.engine.observability.manager import ObservabilityManager

class Renderer:
    def __init__(self, engine):
        self.console = Console()
        self.obs_manager = ObservabilityManager(engine)

    def render_debug(self, engine):
        """Render the debug dashboard using the observability manager."""
        layout = self.obs_manager.get_debug_layout(engine)
        self.console.print(layout)

