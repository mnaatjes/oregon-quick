from src.engine.states.base import BaseState

class TravelState(BaseState):
    def enter(self):
        pass

    def update(self, engine):
        # Basic survival logic per tick
        if engine.wagon.food > 0:
            engine.wagon.food -= 2
            engine.wagon.distance_traveled += 5
            engine.logger.info(f"Traveling: Food remaining: {engine.wagon.food}, Miles: {engine.wagon.distance_traveled}")
        else:
            engine.wagon.health -= 5
            engine.logger.warning("Out of food! Wagon health is deteriorating.")

    def exit(self):
        pass
