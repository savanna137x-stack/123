class Car:
    count = 0
    def __init__(self, name, mileage, country):
        self.name = name
        self.mileage = mileage
        self.country = country
        Car.count += 1
    def __eq__(self, other):
        if isinstance(other, Car):
            return self.country == other.country
        return False
    def reset_mileage(self):
        self.mileage = 0
        print(f"Километраж для {self.name} обнулен.")
    @classmethod
    def get_count(cls):
        return cls.count


def generate_cars(n):
    car_list = []
    for i in range(n):
        new_car = Car(f"Model_{i}", i * 1000, f"Country_{i % 3}")
        car_list.append(new_car)
    return car_list

def sort_cars(car_list, attr):
    return sorted(car_list, key=lambda x: getattr(x, attr))
my_cars = generate_cars(5)

print(f"Создано машин: {Car.get_count()}")
sorted_by_mileage = sort_cars(my_cars, "mileage")
print("\nСортировка по километражу:")
for car in sorted_by_mileage:
    print(car)

sorted_by_name = sort_cars(my_cars, "name")

car_a = Car("BMW", 100, "Germany")
car_b = Car("Audi", 200, "Germany")
print(f"\nBMW и Audi из одной страны? {car_a == car_b}")


car_a.reset_mileage()
print(car)
