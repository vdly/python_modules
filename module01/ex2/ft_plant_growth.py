class Plant:
    def __init__(self, name, height, old):
        self.name = name
        self.height = height
        self.old = old

    def grow(self):
        self.height += 0.8

    def age(self):
        self.old += 1

    def show(self):
        print(f"{self.name}: {self.height:.1f}cm, {self.old} days old")


def ft_plant_growth():
    print("=== Garden Plant Growth ===")

    rose = Plant("Rose", 25, 30)

    day = 1
    rose.show()
    for day in range(1, 8):
        print(f"=== Day {day} ===")
        rose.age()
        rose.grow()
        rose.show()

    total_growth = round(0.8 * day, 1)
    print(f"Growth this week: {total_growth}cm")

if __name__ == "__main__":
    ft_plant_growth()
