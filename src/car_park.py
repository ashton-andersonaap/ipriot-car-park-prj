class Carpark:

    def __init__(self, capacity, location, plates=None, displays=None):
        self.location = location
        self.capacity = capacity
        self.plates = plates or []
        self.displays = displays or []

    def __str__(self):
        return f"Car Park at {self.location} with {self.capacity} bays."

