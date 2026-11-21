class GardenError(Exception):
    def __init__(self, message:str ="Unknown garden error") -> None:
        self.message = message
        super().__init__(self.message)


class PlantError(GardenError):
    def __init__(self, message:str ="Unknown plant error") -> None:
        self.message = message
        super().__init__(self.message)


class WaterError(GardenError):
    def __init__(self, message:str ="Unknown water error") -> None:
        self.message = message
        super().__init__(self.message)


def wilt_check(plant:str, is_wilting:bool) -> None:
    if is_wilting is True:
        # raise PlantError()
        raise PlantError(f"The {plant} plant is wilting!")


def water_check(tank_capacity:int, current_level:int) -> None:
    if current_level == 0:
        # raise WaterError()
        raise WaterError("Not enough water in the tank!")


def custom_error() -> None:
    print("=== Custom Garden Errors Demo ===\n")

    print("Testing PlantError...")
    try:
        wilt_check("tomato", True)
    except PlantError as err:
        print(f"Caught PlantError: {err}\n")

    print("Testing WaterError...")
    try:
        water_check(10, 0)
    except WaterError as err:
        print(f"Caught WaterError: {err}\n")

# Python isn't saying "catch only GardenError instances."
# It's saying "catch GardenError AND any class that inherits from it."
    print("Testing catching all garden errors...")
    try:
        wilt_check("Tomato", True)
    except GardenError as err:
        print(f"Caught GardenError: {err}")

    try:
        water_check(10, 0)
    except GardenError as err:
        print(f"Caught GardenError: {err}\n")


custom_error()
