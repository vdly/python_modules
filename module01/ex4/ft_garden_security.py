class Plant:
    def __init__(self, name, height, old):
        self.name = name
        self._height = height
        self._old = old

    #setter methods
    def set_height(self, height):
        if height > 0:
            self._height = height
        else:
            print("Error, height can't be negative")
            print("Height update rejected")

    def set_age(self, age):
        if age > 0:
            self._old = age
        else:
            print("Error, age can't be a negative")
            print("Age update rejected")

    # getter methods
    def get_height(self):
        return self._height

    def get_age(self):
        return self._old

    def show(self):
        print(f"{self.name}: {self._height:.1f}cm, {self._old} days old")


def ft_garden_security():
    print("=== Garden Security System ===")

    rose = Plant("Rose", 15, 10)
    print("Plant created:", end=" ")
    rose.show()

    rose.set_height(25)
    rose.set_age(30)

    print(f"\nHeight updated: {rose.get_height()}cm")
    print(f"Age updated: {rose.get_age()}cm\n")

    print("Rose: ", end="")
    rose.set_height(-1)
    print("Rose: ", end="")
    rose.set_age(-1)

    print("\nCurrent state:", end=" ")
    rose.show()


if __name__ == "__main__":
    ft_garden_security()