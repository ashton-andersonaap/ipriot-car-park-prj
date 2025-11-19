from sensor import Sensor
from display import Display
from pathlib import Path
from datetime import datetime
class CarPark:


    def __init__(self, location=None, capacity=None, plates=None, displays = None, sensors = None, log_file=Path("log_file.txt")):
        self.location = location if location is not None else ""
        self.capacity = int(capacity) if capacity is not None else 0
        self.plates = plates if plates is not None else []
        self.displays = displays if displays is not None else []
        self.sensors = sensors if sensors is not None else []
        self.log_file = log_file if isinstance(log_file, Path) else Path(log_file)
        if not self.log_file.exists():
            self.log_file.touch()
    def __str__(self):
        return f"Car Park at {self.location} with {self.capacity} bays."

    def register(self, component):
        if not isinstance(component,(Sensor, Display)):
            raise TypeError("Object must be a sensor or display")
        if isinstance(component, Display):
            self.displays.append(component)
        elif isinstance(component, Sensor):
            self.sensors.append(component)


    def add_car(self, plate):
        self.plates.append(plate)
        self.update_displays()
        self._log_car_activity(plate, "entered")


    def remove_car(self,plate):
        self.plates.remove(plate)
        self.update_displays()
        self._log_car_activity(plate, "exited")

    @property
    def available_bays(self):
        if self.capacity <= 0:
            return 0
        return max(self.capacity - len(self.plates), 0)

    def update_displays(self):
        data = {"available_bays": self.available_bays, "temperature": 25}
        for display in self.displays:
            display.update(data)


    def _log_car_activity(self, plate, action):
        with self.log_file.open("a") as f:
            f.write(f"{plate} {action} at {datetime.now(): %Y-%m-%d %H:%M:%S}\n")
