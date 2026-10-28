

# Program: Simple Interest Calculator
# Description: Calculates simple interest based
# on principal, annual rate, and time in years.
# Includes input validation and error handling.

def get_number(prompt):
    while True:
        try:
            value = float(input(prompt).strip())

            if value < 0:
                print("Please enter a non-negative number.")
                continue

            return value

        except ValueError:
            print("Invalid input. Please enter a number.")


def main():
    print("=== Simple Interest Calculator ===")

    principal = get_number("Enter principal amount: $")
    rate = get_number("Enter interest rate (%): ")
    time = get_number("Enter time in years: ")

    interest = (principal * rate * time) / 100
    total = principal + interest

    print(f"\nPrincipal: ${principal:.2f}")
    print(f"Interest Rate: {rate:.2f}%")
    print(f"Time: {time:.2f} years")
    print(f"Simple Interest: ${interest:.2f}")
    print(f"Total Amount: ${total:.2f}")

    message = "Interest Calculation Complete"

    print(message.upper())
    print(f"Number of words: {len(message.split())}")


if __name__ == "__main__":
    main()
