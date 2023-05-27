class Car:
    def __init__(self, color="Белый", type="Иномарка", year="2004", status=False):
        self.color = color
        self.type = type
        self.year = year
        self.status = status


    def show_info(self):
        print("Year: ", self.year)
        print("Type: ", self.type)
        print("Color: ", self.color)

    def turn_on(self):
        self.status = True
        print(f"Автомобиль заведен")

    def turn_off(self):
        self.status = False
        print(f"Автомобиль зуглушен")

    def setYear(self, year):
        self.year = year
        print(f"Присвоен год выпуска: {self.year}")

    def setType(self, type):
        self.type = type
        print(f"Присвоен тип: {self.type}")

    def setColor(self, color):
        self.color = color
        print(f"Присвоен цвет: {self.color}")




car_truck = Car()
car_truck.setYear("1984")
car_truck.setType("Truck")
car_truck.setColor("Red")
car_truck.show_info()
print("\n")

car_bugate = Car()
car_bugate.turn_off()
car_bugate.turn_on()
car_bugate.setYear("1917")
car_bugate.show_info()
print("\n")