from rich.table import Table
from rich.layout import Layout
from rich.panel import Panel
from rich.text import Text
import os

class DashboardProvider:
    def __init__(self, log_file="game.log"):
        self.log_file = log_file

    def get_state_table(self, model):
        """Creates a formatted table of a Pydantic model's state."""
        table = Table(title=f"State: {model.__class__.__name__}", expand=True)
        table.add_column("Attribute", style="cyan")
        table.add_column("Value", style="magenta")

        for key, value in model.model_dump().items():
            table.add_row(key, str(value))
        
        return table

    def get_log_stream(self, num_lines=5):
        """Reads the last few lines from the game log."""
        if not os.path.exists(self.log_file):
            return Text("No logs found.")
        
        try:
            with open(self.log_file, "r") as f:
                lines = [line.strip() for line in f.readlines() if line.strip()]
                last_lines = lines[-num_lines:]
                return Text("\n".join(last_lines), style="dim")
        except Exception as e:
            return Text(f"Error reading logs: {e}")

    def get_layout(self, model):
        """Constructs a Rich layout for the debug dashboard."""
        layout = Layout()
        layout.split_column(
            Layout(name="upper", ratio=2),
            Layout(name="lower", ratio=1)
        )
        
        layout["upper"].update(Panel(self.get_state_table(model), title="[bold yellow]Model Inspector[/bold yellow]"))
        layout["lower"].update(Panel(self.get_log_stream(), title="[bold blue]Recent Logs[/bold blue]"))
        
        return layout
