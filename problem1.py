class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        pass

    def move(self):
        pass

    def eat(self):
        pass

class Yirtqichlar(Animal):
    def __init__(self, name):
        super().__init__(name)

    def bite(self):
        print(f"{self.name} dushmanni tishlaydi.")

    def hunt(self):
        print(f"{self.name} ov qiladi.")

    def roar(self):
        print(f"{self.name} nori tortadi.")

class Otxorlar(Animal):
    def __init__(self, name):
        super().__init__(name)

    def chew_grass(self):
        print(f"{self.name} o't yeydi.")

    def run(self):
        print(f"{self.name} tez yuguradi.")

    def swim(self):
        print(f"{self.name} suzadi.")

lion = Yirtqichlar("Lion")
deer = Otxorlar("Deer")

lion.bite()
lion.hunt()
lion.roar()

deer.chew_grass()
deer.run()
deer.swim()
