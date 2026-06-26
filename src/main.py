from src.engine.core import GameEngine
from src.engine.states.travel import TravelState

def main():
    # 1. Initialize Engine
    engine = GameEngine()
    
    # 2. Setup Initial State & Data
    engine.wagon.food = 100
    engine.wagon.oxen = 4
    engine.state_manager.transition_to(TravelState())
    
    # 3. Start the Live Simulation
    # This will run until interrupted (Ctrl+C)
    engine.start()

if __name__ == "__main__":
    main()
