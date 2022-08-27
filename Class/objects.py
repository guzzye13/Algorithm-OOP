class Robot:
    def __init__(self, name, color, weight):  # Constructor
        self.name = name
        self.color = color
        self.weight = weight

    def introduce_self(self):
        print("My name is " + self.name.title())


# Object 1
r1 = Robot("Tom", "red", 30)

# Object 2
r2 = Robot("jerry", "blue", 33)

r1.introduce_self()
r2.introduce_self()