class Fridge:
    def __init__(self, manufactur, emkost, model):
        self.manufactur =manufactur
        self.emkost=emkost
        self.model = model
    def open_door(self): print("Дверца открыта")
    def close_door(self): print("Дверца закрыта")
    def turn_on(self): print("Холодил")