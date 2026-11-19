def garden_operation(operation_number: int) -> None:
    if (operation_number == 0):
        int("abc")
    elif (operation_number == 1):
        42/0
    elif (operation_number == 2):
        open("text.txt")
    elif (operation_number == 3):
        "42" + 24
    else:
        return


def test_error_types():
    op_num = [0, 1, 2, 3, 4]

    print("=== Garden Error Types Demo ===")
    for item in op_num:
        print(f"Testing operation {item}...")
        try:
            garden_operation(item)
        except ValueError as err:
            print("Caught ValueError:", err)
        except ZeroDivisionError as err:
            print("Caught ZeroDivisionError:", err)
        except FileNotFoundError as err:
            print("Caught FileNotFoundError:", err)
        except TypeError as err:
            print("Caught TypeError:", err)
        else:
            print("Operation completed successfully")
    print("\nAll operations type tested successfully!")

if __name__ == "__main__":
    test_error_types()