from prac_09.silver_service_taxi import SilverServiceTaxi


def test_silver_service_taxi():
    """
    Test the SilverServiceTaxi class with a sample drive.

    A SilverServiceTaxi with fanciness 2 should multiply base rate by 2.
    This test drives 18 km and prints the resulting fare and description.
    """
    fancy_taxi = SilverServiceTaxi("Fancy Taxi", 100, 2)
    fancy_taxi.drive(18)
    fare = fancy_taxi.get_fare()
    print(fancy_taxi)
    print(f"Fare for 18km: ${fare:.2f}")


test_silver_service_taxi()
