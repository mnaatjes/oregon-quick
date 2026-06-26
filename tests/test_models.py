from src.models.wagon import Wagon

def test_wagon_initialization():
    wagon = Wagon()
    assert wagon.health == 100
    assert wagon.food == 0
    assert wagon.distance_traveled == 0

def test_wagon_updates():
    wagon = Wagon(food=50, distance_traveled=10)
    assert wagon.food == 50
    assert wagon.distance_traveled == 10
