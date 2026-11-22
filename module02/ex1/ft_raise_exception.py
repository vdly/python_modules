def input_temperature(temp_str: str) -> int:
    str_int = int(temp_str)

    if str_int > 40:
        raise ValueError(f"{str_int}°C is too hot for \
plants (max 40°C)")
    elif str_int < 0:
        raise ValueError(f"{str_int}°C is too cold for \
plants (min 0°C)")

    return str_int


def test_temperature() -> None:
    data = ["25", "abc", "100", "-50"]

    print("=== Garden temperature Checker ===\n")
    for item in data:
        try:
            print(f"Input data is '{item}'")
            temp = input_temperature(item)
        except ValueError as err:
            print(f"Caught input_temperature error: {err}\n")
        else:
            print(f"Temperature is now {temp}°C\n")
    print("All test completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
