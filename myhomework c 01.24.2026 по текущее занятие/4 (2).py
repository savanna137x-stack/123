class Person:
    def __init__(self, name, surname, age, phone):
        self.name =name
        self.surname =surname
        self.age = age
        self.phone = phone
    def stand_up(self): print(f"{self.name} встал")
    def sit_down(self): print(f"{self.name} сел")