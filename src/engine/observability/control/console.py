from rich.prompt import Prompt
from rich.console import Console
from src.engine.observability.control.commands import CommandHandler

class CommandConsole:
    def __init__(self, engine):
        self.engine = engine
        self.handler = CommandHandler(engine)
        self.console = Console()

    def open(self):
        """Pauses the game and opens an interactive command prompt."""
        self.engine.logger.info("Command Console opened.")
        self.console.print("\n[bold reverse yellow] --- GOD MODE CONSOLE --- [/bold reverse yellow]")
        self.console.print("[dim]Type 'exit' to resume simulation or 'help' for commands.[/dim]\n")

        while True:
            cmd_line = Prompt.ask("[bold green]Admin[/bold green]")
            
            if not cmd_line:
                continue
                
            result = self.handler.execute(cmd_line)
            
            if result == "EXIT_CONSOLE":
                break
            
            self.console.print(f"[blue]>[/blue] {result}")
            self.engine.logger.info(f"Console Command: {cmd_line} -> {result}")

        self.console.print("[yellow]Resuming simulation...[/yellow]\n")
        self.engine.logger.info("Command Console closed.")
