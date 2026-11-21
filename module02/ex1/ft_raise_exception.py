def input_temprature(temp_str: str) -> int:
    str_int = int(temp_str)

    return str_int


def test_temprature() -> None:
    data = ["25", "abc", 100, -50]

    print("=== Garden Temprature Checker ===\n")
    for item in data:
        try:
            print(f"Input data is '{item}'")
            temp = input_temprature(item)
            if temp > 40:
                raise ValueError(f"{temp}°C is too hot for \
plants (max 40°C)")
            elif temp < 0:
                raise ValueError(f"{temp}°C is too cold for \
plants (min 0°C)")
        except ValueError as err:
            print(f"Caught input_temperature error: {err}\n")
        else:
            print(f"Temprature is now {temp}°C\n")
    print("All test completed - program didn't crash!")


if __name__ == "__main__":
    test_temprature()
