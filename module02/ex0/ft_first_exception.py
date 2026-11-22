def input_temperature(temp_str: str) -> int:
    str_int = int(temp_str)

    return str_int


def test_temperature() -> None:
    data = ["25", "abc"]

    print("=== Garden Temperature ===\n")
    for item in data:
        try:
            print(f"Input data is '{item}'")
            temp = input_temperature(item)
        except ValueError as err:
            print("Caught input_temperature error:", err)
        else:
            print(f"Temperature is now {temp}°C\n")
    print("\nAll test completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
