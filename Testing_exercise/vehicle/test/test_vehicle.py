from unittest import TestCase, main

from project.vehicle import Vehicle


class TestVehicle(TestCase):

    def setUp(self):
        self.car = Vehicle(20.5, 131)

    def test_default_fuel_consumption_class_attribute_is_correct(self):
        self.assertEqual(1.25, self.car.DEFAULT_FUEL_CONSUMPTION)

    def test_correct_initialization(self):
        self.assertEqual(20.5, self.car.fuel)
        self.assertEqual(20.5, self.car.capacity)
        self.assertEqual(131, self.car.horse_power)
        self.assertEqual(self.car.DEFAULT_FUEL_CONSUMPTION, self.car.fuel_consumption)

    def test_drive_reduces_fuel(self):
        self.car.drive(2)
        expected = 18
        self.assertEqual(expected, self.car.fuel)

    def test_drive_raises_when_fuel_not_enough(self):
        self.car.fuel = 0

        with self.assertRaises(Exception) as ex:
            self.car.drive(20)

        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_refuel_raises_when_fuel_more_than_capacity(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(100)

        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refuel_adds_fuel_to_vehicle(self):
        self.car.fuel = 6
        self.car.refuel(1)
        self.assertEqual(7, self.car.fuel)

    def test_str_returns_correct_message(self):
        self.car.fuel = 6
        self.car.refuel(1)
        expected = f"The vehicle has 131 " \
               f"horse power with 7 fuel left and {self.car.DEFAULT_FUEL_CONSUMPTION} fuel consumption"

        self.assertEqual(expected, self.car.__str__())


if __name__ == '__main__':
    main()