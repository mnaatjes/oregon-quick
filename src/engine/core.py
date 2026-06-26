import time
import logging
from src.engine.states.manager import StateManager
from src.engine.renderer import Renderer
from src.engine.input import InputHandler
from src.engine.observability.logger import setup_logger
from src.models.wagon import Wagon

class GameEngine:
    def __init__(self):
        self.logger = setup_logger()
        self.logger.info("Initializing Game Engine...")

        # Core Game State
        self.wagon = Wagon()

        # Subsystems
        self.state_manager = StateManager()
        self.renderer = Renderer(self)
        self.input_handler = InputHandler()

        self.running = False
        self.tick_count = 0
        self.logger.info("Engine initialized.")

    def start(self):
        self.logger.info("Starting Game Engine loop.")
        self.running = True
        while self.running:
            try:
                self._run_loop()
            except KeyboardInterrupt:
                self.logger.info("Interrupt caught. Opening Control Console.")
                self.renderer.obs_manager.control.open()
            except Exception as e:
                self.logger.error(f"Engine crashed: {e}", exc_info=True)
                self.running = False

    def _run_loop(self):
        from rich.live import Live

        # We use Rich's Live display to keep the dashboard static on screen
        with Live(self.renderer.obs_manager.get_debug_layout(self), refresh_per_second=4) as live:
            while self.running:
                # 1. Process Input (Placeholder)
                action = self.input_handler.get_action()
                
                # 2. Update Logic (The "Tick")
                self.tick_count += 1
                self.state_manager.update(self) # Pass engine context to states
                
                # 3. Render
                live.update(self.renderer.obs_manager.get_debug_layout(self))
                
                # Control simulation speed
                time.sleep(1.0) # One tick per second
