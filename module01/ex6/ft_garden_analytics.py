class Plant:
    def __init__(self, name, height, old):
        self.name = name
        self.height = height
        self.old = old

    def show(self):
        print(f"{self.name}: {self.height:.1f}cm, {self.old} days old")
