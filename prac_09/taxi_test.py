from prac_09.taxi import Taxi

def main():
    """Test Taxi class with distance and fare calculation."""
    # 1. create a Taxi instance
    my_taxi = Taxi("Prius 1", 100)

    # 2. drive 40km
    my_taxi.drive(40)
    print(my_taxi)
    print(f"Fare for 40 km: ${my_taxi.get_fare():.2f}")

    # 3. reset the fare and drive another 100km
    my_taxi.start_fare()
    my_taxi.drive(100)
    print(my_taxi)
    print(f"Fare for 100 km: ${my_taxi.get_fare():.2f}")


main()
