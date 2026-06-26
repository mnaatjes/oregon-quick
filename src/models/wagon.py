from pydantic import BaseModel

class Wagon(BaseModel):
    health: int = 100
    food: int = 0
    oxen: int = 0
    distance_traveled: int = 0
