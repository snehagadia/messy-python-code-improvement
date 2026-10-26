def calculate_sum(number):
    """Return the sum of integers from 1 to number."""
    if number < 0:
        raise ValueError("Please enter a non-negative number.")

    return sum(range(1, number + 1))


def main():
    try:
        number = int(input("Enter a non-negative number: "))
        result = calculate_sum(number)
        print(f"Sum is: {result}")
    except ValueError as error:
        print(f"Invalid input: {error}")


if __name__ == "__main__":
    main()
