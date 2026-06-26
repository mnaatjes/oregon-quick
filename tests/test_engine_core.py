from src.engine.core import GameEngine

def test_engine_initialization():
    engine = GameEngine()
    assert engine.running is False
    assert engine.state_manager is not None
    assert engine.renderer is not None
    assert engine.input_handler is not None
