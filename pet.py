class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []

    def eat(self):
        if self.hunger > 0:
            self.hunger -= 3
            self.happiness += 1
            print(f"{self.name} is eating.")
        
        # TODO

    def sleep(self):
        if self.energy < 10:
            self.energy += 5
            print(f"{self.name} is sleeping.")
        # TODO

    def play(self):
        if self.energy > 0 and self.happiness < 10:
            self.energy -= 2
            self.happiness += 2
            self.hunger += 1
            print(f"{self.name} is playing.")
        # TODO

    def train(self, trick):
        if self.happiness > 0:
            self.tricks.append(trick)
            self.happiness += 1
            print(f"{self.name} learned a new trick: {trick}.")
        # TODO

    def show_tricks(self):
        if self.tricks:
            print(f"{self.name} knows the following tricks: {', '.join(self.tricks)}")
        else:
            print(f"{self.name} doesn't know any tricks.")
        # TODO

    def get_status(self):
        print(f"{self.name}'s status:")
        print(f"Hunger: {self.hunger}")
        print(f"Energy: {self.energy}")
        print(f"Happiness: {self.happiness}")

        # TODO
