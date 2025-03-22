class Car:
    def __init__(self, model, year, manufacturer, engine_capacity, color, price):
        self.__model = model
        self.__year = year
        self.__manufacturer = manufacturer
        self.__engine_capacity = engine_capacity
        self.__color = color
        self.__price = price

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year

    def get_manufacturer(self):
        return self.__manufacturer

    def get_engine_capacity(self):
        return self.__engine_capacity

    def get_color(self):
        return self.__color

    def get_price(self):
        return self.__price


    def set_model(self, model):
        self.__model = model

    def set_year(self, year):
        self.__year = year

    def set_manufacturer(self, manufacturer):
        self.__manufacturer = manufacturer

    def set_engine_capacity(self, engine_capacity):
        self.__engine_capacity = engine_capacity

    def set_color(self, color):
        self.__color = color

    def set_price(self, price):
        self.__price = price


    def display_info(self):
        print(f"Model: {self.__model}")
        print(f"Year: {self.__year}")
        print(f"Manufacturer: {self.__manufacturer}")
        print(f"Engine Capacity: {self.__engine_capacity}L")
        print(f"Color: {self.__color}")
        print(f"Price: ${self.__price}")
        print("-" * 30)

car1 = Car("Toyota Supra", 2022, "Toyota", 3.0, "Red", 55000)
car1.display_info()


print("Old price:", car1.get_price())
car1.set_price(53000)
print("New price:", car1.get_price())



