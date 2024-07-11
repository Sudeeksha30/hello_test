class Vehcile:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        return "engine started!"

    def stop_engine(self):
        return "engine stopped!"

    def display_info(self):
        print(f"{self.year} {self.make} {self.model}")


vehcile = Vehcile("generic make", "generic model", 2004)

vehcile.display_info()
print(vehcile.stop_engine())
print(vehcile.start_engine())


#child class

class Car(Vehcile):
    def __init__(self, make, model, year, doors):
        super().__init__(make, model, year)
        self.doors = doors

    def honk(self):
        return "Car honks : Beep Beep!"

    def display_info(self):
        print(f"{self.make} {self.model} {self.year} {self.doors} doors")


car = Car("Toyota","Innova","2003","4")
car.display_info()
print(car.honk())

class Bike(Vehcile):
    def __init__(self, make, model, year, type_of_bike):
        super().__init__(make, model, year)
        self.type_of_bike = type_of_bike

    def horn(self):
        return "tring tring!"

    def display_info(self):
        print(f"{self.make} {self.model} {self.year} {self.type_of_bike} bike")

bike = Bike("Eicher bikes", "Royalenfield", "2007", "Road")
bike.display_info()
print(bike.horn())
print(bike.stop_engine())
print(car.stop_engine())
