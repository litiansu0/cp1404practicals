"""
CP1404/CP5632 Practical - Client code to use the Car class.
Note that the import has a folder (module) in it.
This is why we name our folders with no spaces or capitals, as valid module names.
"""

from prac_06.car import Car


"""Demo code to use the modified Car class."""

from prac_06.car import Car

def main():
    """Test the Car class with modifications."""
    # Original car with name
    my_car = Car("My Car", 180)
    my_car.drive(30)
    print(f"Original car fuel: {my_car.fuel}")
    print(my_car)

    # New limo object with added fuel and name
    limo = Car("Limo", 100)
    limo.add_fuel(20)
    print(f"\nLimo fuel: {limo.fuel}")
    
    # Attempt to drive 115 km
    driven = limo.drive(115)
    print(f"Limo driven {driven} km")
    print(limo)

if __name__ == "__main__":
    main()