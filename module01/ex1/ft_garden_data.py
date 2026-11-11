class Plant:
    def __init__(self, name: str, height: float, old: int):
        self.name = name
        self.height = height
        self.old = old

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.old} days old")


def ft_garden_data() -> None:
    print("=== Garden Plant Registry ===")

    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)
    cactus = Plant("Cactus", 15, 120)

    rose.show()
    sunflower.show()
    cactus.show()


if __name__ == "__main__":
    ft_garden_data()
