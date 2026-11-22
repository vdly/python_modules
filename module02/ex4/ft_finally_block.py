class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error") -> None:
        super().__init__(message)


def wilt_check(plant: str, is_wilting: bool) -> None:
    if is_wilting is True:
        # raise PlantError()
        raise PlantError(f"The {plant} plant is wilting!")


def water_check(tank_capacity: int, current_level: int) -> None:
    if current_level == 0:
        # raise WaterError()
        raise WaterError("Not enough water in the tank!")


def water_plant(plant_name: str) -> None:
    if plant_name == plant_name.capitalize():
        print(f"Watering {plant_name}: [OK]")
    else:
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")


def test_watering_system() -> None:
    print("=== Garden Watering System ===\n")

    print("Testing valid plants...")
    print("Opening water system")
    try:
        water_plant("Tomato")
        water_plant("Lettuce")
        water_plant("Carrot")
    except PlantError as err:
        print(f"Caught PlantError: {err}")
        print("... ending test and returning to main")
    finally:
        print("Closing watering system\n")

    print("Testing invalid plants...")
    print("Opening water system")
    try:
        water_plant("Tomato")
        water_plant("lettuce")
        water_plant("carrot")
    except PlantError as err:
        print(f"Caught PlantError: {err}")
        print("... ending test and returning to main")
    finally:
        print("Closing watering system\n")
        print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
