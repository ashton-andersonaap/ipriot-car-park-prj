from sensor import Sensor
from display import Display
class Carpark:


    def __init__(self, capacity, location, plates=None, displays = None, sensors = None):
        self.location = location
        self.capacity = capacity
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
        if (len(self.plates)>(self.capacity)):
            return 0
        else:
            return self.capacity - len(self.plates)

    def update_dipslays(self):
        data = {"available_bays": self.available_bays, "temperature": 25}
        for display in self.displays:
            display.update(data)



