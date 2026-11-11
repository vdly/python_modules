class Plant:
    class Stats:
        def __init__(self) -> None:
            self.grew = 0
            self.aged = 0
            self.showed = 0

    def __init__(self, name: str, height: float, old: int) -> None:
        self.name = name
        self.height = height
        self.old = old
        self.stats = self.Stats()

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.old} days old")
        self.stats.showed += 1

    @staticmethod
    def older_than_year(days: int) -> None:
        print(f"Is {days} more than a year? ->", end=" ")
        if days > 365:
            print("True")
        else:
            print("False")

    @classmethod
    def create_anon(cls):
        return cls("Unknown plant", 0, 0)


class Flower(Plant):
    def __init__(self, name: str, height: float, old: int, colour: str):
        super().__init__(name, height, old)
        self.colour = colour
        self.bloomed = False

    def bloom(self) -> None:
        self.bloomed = True

    def grow(self) -> None:
        self.height += 8
        self.stats.grew += 1

    def age(self) -> None:
        self.old += 1
        self.stats.aged += 1

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.old} days old")
        print(f"Colour : {self.colour}")
        if (self.bloomed is True):
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} had not bloomed yet")
        self.stats.showed += 1


class Seed(Flower):
    def __init__(self, name: str, height: float, old: int, colour: str,
                 seeds: int):
        super().__init__(name, height, old, colour)
        self.seeds = seeds
        self.bloomed = False

    def bloom(self) -> None:
        self.bloomed = True
        self.seeds += 42

    def grow(self) -> None:
        self.height += 30
        self.stats.grew += 1

    def age(self) -> None:
        self.old += 20
        self.stats.aged += 1

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.old} days old")
        print(f"Colour : {self.colour}")
        if (self.bloomed is True):
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} had not bloomed yet")
        print(f"Seeds: {self.seeds}")
        self.stats.showed += 1


class Tree(Plant):
    def __init__(self, name: str, height: float, old: int,
                 trunk_diameter: float):
        super().__init__(name, height, old)
        self.trunk_diameter = trunk_diameter
        self.shade_produced = 0
        self.shaded = 0

    def produce_shade(self) -> None:
        print(f"[asking the {self.name} to produce shade]")
        print(f"Tree {self.name} now produces a shade of {self.height:.1f} \
cm long and {self.trunk_diameter:.1f}cm wide.")
        self.shaded += 1

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.old} days old")
        print(f"Trunk diameter : {self.trunk_diameter:.1f}cm")
        self.stats.showed += 1


def stats(plant: Plant) -> None:
    print(f"[statistics for {plant.name}]")
    print(f"Stats: {plant.stats.grew} grow, {plant.stats.aged} age,\
 {plant.stats.showed} show")
    if isinstance(plant, Tree):
        print(f"{plant.shaded} shade")


def ft_plant_types() -> None:
    print("=== Garden Plant Types ===")

    print("=== Check year-old")
    Plant.older_than_year(30)
    Plant.older_than_year(400)

    print("\n=== Flower")
    rose = Flower("Rose", 15, 10, "red")
    rose.show()
    print(f"[asking the {rose.name} to bloom and grow]")
    rose.bloom()
    rose.grow()
    rose.show()
    stats(rose)

    print("\n=== Tree")
    oak = Tree("Oak", 200, 365, 5)
    oak.show()
    stats(oak)
    oak.produce_shade()
    stats(oak)

    print("\n=== Seed")
    sunflower = Seed("Sunflower", 80, 45, "yellow", 0)
    sunflower.show()
    print(f"[asking the {sunflower.name} to grow, age and bloom]")
    sunflower.grow()
    sunflower.age()
    sunflower.bloom()
    sunflower.show()
    stats(sunflower)

    print("\n=== Anonymous")
    anon = Plant.create_anon()
    anon.show()
    stats(anon)


if __name__ == "__main__":
    ft_plant_types()
