import unittest
from display import Display
from car_park import CarPark
from sensor import EntrySensor

class TestSensor(unittest.TestCase):

    def setUp(self):
        self.car_park = CarPark()
        self.sensor = EntrySensor(1, True, self.car_park)


    def test_sensor_intialised_with_all_attributes(self):
        self.assertIsInstance(self.sensor, EntrySensor)
        self.assertEqual(self.sensor.id, 1)
        self.assertEqual(self.sensor.is_active, True)
        self.assertIsInstance(self.sensor.car_park, CarPark)

    def test_detect_vehicle(self):
        plate = self.sensor.detect_vehicle()
        self.assertIsNotNone(plate)
        self.assertTrue(plate.startswith("FAKE-"))
        self.assertEqual(len(plate), 8)