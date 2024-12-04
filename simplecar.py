import random

class Car:
    def __init__(self, speed, color, model):
        self.speed = speed
        self.color = color
        self.model = model

    def accelerate(self, amount):
        self.speed += amount

    def brake(self, amount):
        self.speed -= amount
        if self.speed < 0:
            self.speed = 0

    def get_speed(self):
        return self.speed

    def describe(self):
        print(f"This is a {self.color} {self.model} car, currently traveling at {self.speed} mph.")

# Create a car instance
my_car = Car(50, "red", "Ford Mustang")

# Play a simple game
while True:
    print("\nWhat do you want to do?")
    print("1. Accelerate")
    print("2. Brake")
    print("3. Check speed")
    print("4. Describe car")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        acceleration = int(input("Enter acceleration amount: "))
        my_car.accelerate(acceleration)
        print("Accelerating...")
    elif choice == "2":
        braking = int(input("Enter braking amount: "))
        my_car.brake(braking)
        print("Braking...")
    elif choice == "3":
        print(f"Current speed: {my_car.get_speed()} mph")
    elif choice == "4":
        my_car.describe()
    elif choice == "5":
        print("Exiting the game. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")