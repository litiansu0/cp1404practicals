"""CP1404/CP5632 Practical - Car class example."""

class Car:
    """Represent a Car object."""

    def __init__(self, name, fuel=0):
        """Initialise a Car instance with name and fuel."""
        self.name = name
        self.fuel = fuel
        self._odometer = 0

    def add_fuel(self, amount):
        """Add amount to the car's fuel."""
        self.fuel += amount

    def drive(self, distance):
        """Drive the car, updating fuel and odometer."""
        driven_distance = min(distance, self.fuel)
        self.fuel -= driven_distance
        self._odometer += driven_distance
        return driven_distance

    def __str__(self):
        """Return a string representation of the car."""
        return f"{self.name}: fuel={self.fuel} units, odometer={self._odometer} km"