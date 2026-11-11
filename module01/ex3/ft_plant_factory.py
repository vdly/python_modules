class Plant:
    def __init__(self, name: str, height: float, old: int):
        self.name = name
        self.height = height
        self.old = old

    def grow(self) -> None:
        self.height += 0.8

    def age(self) -> None:
        self.old += 1

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.old} days old")


def ft_plant_factory() -> None:
    print("=== Plant Factory Output ===")

    rose = Plant("Rose", 25, 30)
    oak = Plant("Oak", 200, 365)
    cactus = Plant("Cactus", 5, 90)
    sunflower = Plant("Sunflower", 80, 45)
    fern = Plant("Fern", 15, 120)

    print("Created: ", end="")
    rose.show()
    print("Created: ", end="")
    oak.show()
    print("Created: ", end="")
    cactus.show()
    print("Created: ", end="")
    sunflower.show()
    print("Created: ", end="")
    fern.show()


if __name__ == "__main__":
    ft_plant_factory()
