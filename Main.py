class Bus:

    def __init__(self, driver, num_seats, bus_color):
        self.driver = driver
        self.num_seats = 12
        self.color = bus_color


bus = Bus("Matthew", "12", ["black", "green", "purple"])

print(bus.driver)
print(bus.num_seats)
print(bus.color[2])
