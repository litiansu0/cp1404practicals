from random import randint
from prac_09.car import Car


class UnreliableCar(Car):
    """A Car that may not always drive based on a reliability percentage."""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar instance."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Attempt to drive the car.

        Only drive if a random number (0–100) is less than the reliability.
        Return the distance actually driven (could be 0).
        """
        if randint(0, 100) < self.reliability:
            return super().drive(distance)
        return 0
