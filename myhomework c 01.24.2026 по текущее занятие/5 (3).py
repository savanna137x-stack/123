class Restaurant:
    def __init__(self):
        self.menu = []
    def add_dish(self, dish):
        self.menu.append(dish)
        print(f"блюдо '{dish}' добавлено в меню")

    def remove_dish(self, dish):
        if dish in self.menu:
            self.menu.remove(dish)
            print(f"блюдо '{dish}' удалено из меню")
        else:
            print("такого нет в меню")

    def make_order(self, order_list):
        print("Ваш заказ:")
        for dish in order_list:
            if dish in self.menu:
                print(f" {dish}")
            else:
                print(f" {dish} извините этого блюда нет в меню")


rest = Restaurant()
rest.add_dish("Пицца")
rest.add_dish("Паста")
rest.make_order(["Пицца", "Борщ"])


