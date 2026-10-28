

# Celsius to Fahrenheit Converter
# Description: Converts a Celsius temperature
# to Fahrenheit using user input.
# Includes validation and string manipulation.

def main():
    print("=== Temperature Converter ===")

    while True:
        try:
            user_input = input(
                "Enter temperature in Celsius: "
            ).strip()

            Celsius = float(user_input)
            break

        except ValueError:
            print("Invalid temperature. Enter a number.")

    fahrenheit = (Celsius * 9 / 5) + 32

    print(f"\nCelsius: {Celsius:.2f}")
    print(f"Fahrenheit: {fahrenheit:.2f}")

    message = "Temperature Conversion Complete"

    print(message.lower())
    print(f"Word count: {len(message.split())}")


if __name__ == "__main__":
    main()
