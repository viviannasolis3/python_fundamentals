

# Circle Area Calculator
# Description: Calculates the area of a circle using
# a radius entered by the user.
# Includes input validation and string operations.

def main():
    print("=== Circle Area Calculator ===")

    while True:
        try:
            user_input = input("Enter the radius: ").strip()
            radius = float(user_input)

            if radius < 0:
                print("Radius cannot be negative. Try again.")
                continue

            break

        except ValueError:
            print("Invalid input. Please enter a number.")

    area = 3.14 * radius ** 2

    print(f"\nRadius: {radius:.2f}")
    print(f"Area of the circle: {area:.2f}")

    message = "Calculation Complete"
    print(message.upper())
    print(f"Message length: {len(message)}")


if __name__ == "__main__":
    main()
