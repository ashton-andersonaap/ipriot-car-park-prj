from car_park import CarPark
from sensor import EntrySensor, ExitSensor
from display import Display

moondalup_carpark = CarPark("Moondalup", 100, log_file="moondalup.txt")
moondalup_carpark.write_config("moondalup_config.json")
loaded_carpark = CarPark.from_config("moondalup_config.json")

entry_sensor = EntrySensor(1, True, loaded_carpark)
exit_sensor = ExitSensor(2, True, loaded_carpark)

display = Display(1,  loaded_carpark, "Welcome to Moondalup", True)

for i in range(10):
    entry_sensor.detect_vehicle()

for i in range(2):
    exit_sensor.detect_vehicle()
