def input_temprature(temp_str: str) -> int:
    str_int = int(temp_str)

    return str_int


def test_temprature() -> None:
    data = ["25", "abc"]

    print("=== Garden Temprature ===\n")
    for item in data:
        try:
            print(f"Input data is '{item}'")
            temp = input_temprature(item)
        except ValueError as err:
            print("Caught input_temperature error:", err)
        else:
            print(f"Temprature is now {temp}°C\n")
    print("\nAll test completed - program didn't crash!")


if __name__ == "__main__":
    test_temprature()
