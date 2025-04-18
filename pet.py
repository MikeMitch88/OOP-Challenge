class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []

    def eat(self):
        if self.hunger > 0:
            self.hunger = max(0, self.hunger - 3)
            self.happiness = min(10, self.happiness + 1)
            print(f"🍖 \033[94m{self.name}\033[0m! is eating. Yum!")
        else:
            print(f"🍽️ \033[94m{self.name}\033[0m! is not hungry.")

    def sleep(self):
        if self.energy < 10:
            self.energy = min(10, self.energy + 5)
            print(f"💤 \033[94m{self.name}\033[0m! is sleeping. Sweet dreams!")
            # \033[94m{pet.name}\033[0m!
        else:
            print(f"😴 \033[94m{self.name}\033[0m! is already well-rested.")

    def play(self):
        if self.energy > 0 and self.happiness < 10:
            self.energy = max(0, self.energy - 2)
            self.happiness = min(10, self.happiness + 2)
            self.hunger = min(10, self.hunger + 1)
            print(f"🎾 \033[94m{self.name}\033[0m! is playing. So much fun!")
        elif self.energy == 0:
            print(f"😓 \033[94m{self.name}\033[0m! is too tired to play.")
        elif self.happiness == 10:
            print(f"😊 \033[94m{self.name}\033[0m! is already super happy!")

    def train(self, trick):
        if self.happiness > 0:
            self.tricks.append(trick)
            self.happiness = min(10, self.happiness + 1)
            print(f"🎓 \033[94m{self.name}\033[0m! learned a new trick: \033[92m{trick}\033[0m! Amazing!")
        else:
            print(f"😔 \033[94m{self.name}\033[0m! is too sad to learn new tricks.")

    def show_tricks(self):
        if self.tricks:
            print(f"🤹 \033[94m{self.name}\033[0m! knows the following tricks: {', '.join(self.tricks)}")
        else:
            print(f"🙃 \033[94m{self.name}\033[0m! doesn't know any tricks yet.")

    def get_status(self):
        print(f"📋 \033[94m{self.name}\033[0m!'s status:")
        print(f"🍗 Hunger: {self.hunger}")
        print(f"⚡ Energy: {self.energy}")
        print(f"😊 Happiness: {self.happiness}")
        print(f"🤹 Tricks: \033[94m{', '.join(self.tricks) if self.tricks else 'None'}\033[0m!".upper())  # Cyan color for tricks