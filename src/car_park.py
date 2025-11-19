from sensor import Sensor
from display import Display
class CarPark:


    def __init__(self, location=None, capacity=None, plates=None, displays = None, sensors = None):
        self.location = location if location is not None else ""
        self.capacity = int(capacity) if capacity is not None else 0
        self.plates = plates if plates is not None else []
        self.displays = displays if displays is not None else []
        self.sensors = sensors if sensors is not None else []

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

    def remove_car(self,plate):
        self.plates.remove(plate)
        self.update_displays()

    @property
    def available_bays(self):
        if self.capacity <= 0:
            return 0
        return max(self.capacity - len(self.plates), 0)

    def update_displays(self):
        data = {"available_bays": self.available_bays, "temperature": 25}
        for display in self.displays:
            display.update(data)



