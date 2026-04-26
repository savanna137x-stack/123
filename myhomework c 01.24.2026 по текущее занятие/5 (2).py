class House:
    def __init__(self, floors, area, rooms):
        self.floors = floors
        self.area = area
        self.rooms = rooms
    def calculate_cost(self, price_per_meter):
        return self.area*price_per_meter
