from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """A more luxurious Taxi that includes a fanciness multiplier and a flagfall charge."""

    flagfall = 4.50  # Fixed additional cost per trip

    def __init__(self, name, fuel, fanciness):
        """
        Initialise a SilverServiceTaxi.

        :param name: the name of the taxi
        :param fuel: the amount of fuel
        :param fanciness: a multiplier for price per km (e.g., 2.0, 4.0)
        """
        price_per_km = 1.23 * fanciness  # base rate * fanciness factor
        super().__init__(name, fuel, price_per_km)
        self.fanciness = fanciness

    def get_fare(self):
        """
        Return the total fare including the flagfall.

        :return: float – total fare amount
        """
        return super().get_fare() + self.flagfall

    def __str__(self):
        """
        Return a string representation of the SilverServiceTaxi.

        :return: string – description of taxi including flagfall
        """
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"
