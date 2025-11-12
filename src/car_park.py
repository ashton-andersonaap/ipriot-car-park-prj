from sensor import Sensor
from display import Display
class Carpark:


    def __init__(self, capacity, location, plates=None):
        self.location = location
        self.capacity = capacity
        self.plates = plates or []
        self.displays = []
        self.sensors = []

    def __str__(self):
        return f"Car Park at {self.location} with {self.capacity} bays."

    def register(self, component):
        if not isinstance(component,(Sensor, Display)):
            raise TypeError("Object must be a sensor or display")
        if isinstance(component, Display):
            self.displays.append(component)
        elif isinstance(component, Sensor):
            self.sensors.append(component)
