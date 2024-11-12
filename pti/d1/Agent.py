class Agent:
    def __init__(self, name, measurement):
        self.name = name
        self.measurement = measurement
        self.connections = []

    def add_connection(self, other):
        if other not in self.connections:
            self.connections.append(other)

    def remove_connection(self, other):
        if other in self.connections:
            self.connections.remove(other)

    def update_measurement(self, new_measurement):
        self.measurement = new_measurement

    def __repr__(self):
        return f"{self.name}({self.measurement})"