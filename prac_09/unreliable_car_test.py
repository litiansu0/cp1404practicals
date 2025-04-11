from prac_09.unreliable_car import UnreliableCar


def main():
    """Test the UnreliableCar with different reliability levels."""
    good_car = UnreliableCar("Good", 100, 80)
    bad_car = UnreliableCar("Bad", 100, 10)

    for i in range(1, 10):
        print(f"\nAttempting to drive {i}km:")
        good_distance = good_car.drive(i)
        bad_distance = bad_car.drive(i)
        print(f"{good_car.name:5} drove {good_distance} km")
        print(f"{bad_car.name:5} drove {bad_distance} km")

    print("\nFinal states:")
    print(good_car)
    print(bad_car)


main()
