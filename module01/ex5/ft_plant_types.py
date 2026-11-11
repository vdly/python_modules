class Plant:
    def __init__(self, name, height, old):
        self.name = name
        self.height = height
        self.old = old

    def show(self):
        print(f"{self.name}: {self.height:.1f}cm, {self.old} days old")


class Flower(Plant):
    def __init__(self, name, height, old, colour):
        super().__init__(name, height, old)
        self.colour = colour

    bloomed = False

    def bloom(self):
        print(f"[asking the {self.name} to bloom]")
        self.bloomed = True

    def show(self):
        print(f"{self.name}: {self.height:.1f}cm, {self.old} days old")
        print(f"Colour : {self.colour}")
        if (self.bloomed is True):
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} had not bloomed yet")


class Tree(Plant):
    def __init__(self, name, height, old, trunk_diameter):
        super().__init__(name, height, old)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        print(f"[asking the {self.name} to produce shade]")
        print(f"Tree {self.name} now produces a shade of {self.height:.1f} \
cm long and {self.trunk_diameter:.1f}cm wide.")

    def show(self):
        print(f"{self.name}: {self.height:.1f}cm, {self.old} days old")
        print(f"Trunk diameter : {self.trunk_diameter:.1f}cm")


class Vegetable(Plant):
    def __init__(self, name, height, old, harvest_season, nutritional_value):
        super().__init__(name, height, old)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    days = 20

    def grow(self):
        print(f"[make {self.name} grow and age for {self.days} days] ")
        for day in range(self.days):
            self.nutritional_value += 1
            self.height += 2.1
            self.old += 1

    def show(self):
        print(f"{self.name}: {self.height:.1f}cm, {self.old} days old")
        print(f"Harvest season : {self.harvest_season}")
        print(f"Nutritional value : {self.nutritional_value}")


def ft_plant_types():
    print("=== Garden Plant Types ===")

    print("=== Flower")
    rose = Flower("Rose", 10, 30, "red")
    rose.show()
    rose.bloom()
    rose.show()

    print("\n=== Tree")
    oak = Tree("Oak", 200, 365, 5)
    oak.show()
    oak.produce_shade()

    print("\n=== Vegetable")
    tomato = Vegetable("Tomato", 5, 10, "April", 0)
    tomato.show()
    tomato.grow()
    tomato.show()


if __name__ == "__main__":
    ft_plant_types()
