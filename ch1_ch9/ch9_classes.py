# Creating the Dog Class
class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes"""
        # variables prefixed with self are available to other methods in class
        self.name = name  
        self.age = age
    
    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")

my_dog = Dog('Willie', 6)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog's age is {my_dog.age}.")
my_dog.sit()
my_dog.roll_over()

# Creating Multiple Instances
your_dog = Dog('Lucy', 3)
print(f"\nYour dog's name is {your_dog.name}")
print(f"Your dog's age is {your_dog.age}")
your_dog.sit()
your_dog.roll_over()


# Creating the Car Class
class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")
    
    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles
    
    def fill_gas_tank(self):
        """Fills up the car's gas tank"""
        print(f"The {(self.get_descriptive_name()).title()} now has a full tank of gas")
        
my_new_car = Car('audi','a4',2019)
print(f"\n{my_new_car.get_descriptive_name()}")
my_new_car.read_odometer()

# Modifying an Attribute's Value Directly
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# Modifying an Attribute's Value using the new Method
my_new_car.update_odometer(22)
my_new_car.read_odometer()

# Incrementing an Attribute's Value using the new Method
my_used_car = Car('subaru', 'outback', 2015)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()
my_used_car.fill_gas_tank()

# Create a Battery class that can be used as an attribute in the Electric Car class below
class Battery:
    """A simple attempt to model a bettery for an electric car."""

    def __init__(self,battery_size=75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size
    
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"This car can go about {range} miles on a full charge.")


# Create a child class ElectricCar of the Parent Class Car - Inheritance
class ElectricCar(Car):
    """ Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank(self):
        """Electric car's don't have gas tanks."""
        print("This car doesn't need a gas tank!")


my_tesla = ElectricCar('tesla','model s', 2019)
print(my_tesla.get_descriptive_name())

# A Class Instance as an Attribute
my_tesla.battery.describe_battery()

# Now you can add to the Battery Class without cluttering the Electric car class
my_tesla.battery.get_range()

# You can import classes in the same way that you import functions
# it is recomended to use "import car" where car.py includes the car class
# This avoides naming conflicts with things in your main program file
# then use it "my_tesla = car.ElectricCar('tesla','model s',2019)"