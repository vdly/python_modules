class Plant:
    def __init__(self, name: str, height: float, old: int):
        self.name = name
        self.height = height
        self.old = old

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.old} days old")


class Flower(Plant):
    def __init__(self, name: str, height: float, old: int, colour: str):
        super().__init__(name, height, old)
        self.colour = colour

    bloomed = False

    def bloom(self) -> None:
        self.bloomed = True

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.old} days old")
        print(f"Colour : {self.colour}")
        if (self.bloomed is True):
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} had not bloomed yet")


class Tree(Plant):
    def __init__(self, name: str, height: float, old: int, t_diameter: float):
        super().__init__(name, height, old)
        self.t_diameter = t_diameter

    def produce_shade(self) -> None:
        print(f"Tree {self.name} now produces a shade of {self.height:.1f} \
cm long and {self.t_diameter:.1f}cm wide.")

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.old} days old")
        print(f"Trunk diameter : {self.t_diameter:.1f}cm")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, old: int, harvest_szn: str,
                 nutritional_value: int):
        super().__init__(name, height, old)
        self.harvest_szn = harvest_szn
        self.nutritional_value = nutritional_value

    days = 20

    def grow(self) -> None:
        for day in range(self.days):
            self.nutritional_value += 1
            self.height += 2.1
            self.old += 1

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.old} days old")
        print(f"Harvest season : {self.harvest_szn}")
        print(f"Nutritional value : {self.nutritional_value}")


def ft_plant_types() -> None:
    print("=== Garden Plant Types ===")

    print("=== Flower")
    rose = Flower("Rose", 10, 30, "red")
    rose.show()
    print(f"[asking the {rose.name} to bloom]")
    rose.bloom()
    rose.show()

    print("\n=== Tree")
    oak = Tree("Oak", 200, 365, 5)
    oak.show()
    print(f"[asking the {oak.name} to produce shade]")
    oak.produce_shade()

    print("\n=== Vegetable")
    tomato = Vegetable("Tomato", 5, 10, "April", 0)
    tomato.show()
    print(f"[make {tomato.name} grow and age for {tomato.days} days] ")
    tomato.grow()
    tomato.show()


if __name__ == "__main__":
    ft_plant_types()
