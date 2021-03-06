class Car(object):
    """
    Attributes:
        doors: An integer representing the number of doors the car has.
        model: The model of the car as a string.
        manufacturer: The integral year the car was built.
        colour: The colour the car has.
    """
    def __init__ (self, doors, model, manufacturer, colour):
         self.doors = doors  # instance variable unique to each instance
         self.model = model
         self.manufacturer = manufacturer
         self.colour = colour

    def __str__(self):
        return str (self.doors , self.model, self.manufacturer, self.colour)

    def drive_car(self):
        print("car is moving!")

    def change_paint(self, colour):
        self.colour = colour

    def lock_car(self):
        print("you can't open the car now, muahahaha!")

    def make_car_sound():
        print ("Vroom!")

mustang = Car(4, 'Mustang', 'Ford', 'red')

mustang.change_paint("blue")
print(mustang.colour)
