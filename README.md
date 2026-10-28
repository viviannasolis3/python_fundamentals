# python_fundamentals

## Project Overview

This repository contains three Python programs demonstrating fundamental programming concepts, including user input, data validation, string manipulation, mathematical calculations, and exception handling.

The purpose of this project is to practice writing simple Python programs that solve real-world problems while preventing common input errors.

## Programs

### 1. Circle Area Calculator
**File:** `circle_area.py`

This program asks the user to enter the radius of a circle and calculates its area using:

Area = 3.14 × radius²

The program validates numeric input, prevents negative radius values, and displays the calculated area.

### 2. Temperature Converter
**File:** `temperature_converter.py`

This program converts Celsius temperatures into Fahrenheit using:

Fahrenheit = (Celsius × 9/5) + 32

The program accepts positive, negative, and decimal temperatures and handles invalid inputs.

### 3. Simple Interest Calculator
**File:** `simple_interest.py`

This program calculates simple interest using:

Simple Interest = (Principal × Rate × Time) / 100

The program collects three numeric inputs and displays the calculated interest and total amount.

## How to Run

1. Install Python 3.x.
2. Download or clone this repository.
3. Open the project folder in Visual Studio Code or a terminal.
4. Run each program using the following commands:

```bash
python circle_area.py
python temperature_converter.py
python simple_interest.py
```

5. Follow the instructions displayed in the terminal.

## Python Concepts Demonstrated

- User input using `input()`
- Numeric conversion using `float()`
- Input validation using conditional statements
- Exception handling using `try` and `except ValueError`
- String transformation using `upper()` and `lower()`
- String analysis using `len()` and `split()`
- Output formatting using f-strings
- Loops for repeated input validation

## Testing and Edge Cases

The following are test cases to run to verify program behavior:

| Program | Test Input | Expected Result |
|---|---|---|
| Circle Area | 5 | Area = 78.50 |
| Circle Area | -3 | Reject negative radius |
| Circle Area | abc | Display error and retry |
| Circle Area | Empty input | Display error and retry |
| Temperature Converter | 0 | 32.00°F |
| Temperature Converter | 100 | 212.00°F |
| Temperature Converter | -40 | -40.00°F |
| Temperature Converter | hello | Display error and retry |
| Simple Interest | 1000, 5, 2 | Interest = $100.00 |
| Simple Interest | 0, 5, 2 | Interest = $0.00 |
| Simple Interest | -500 | Reject negative principal |
| Simple Interest | abc | Display error and retry |

These tests cover valid values, invalid text, negative numbers, zero values, and empty input.

## Assumptions

- Python 3.x is installed.
- Users enter numeric values when prompted.
- Negative radius, principal, interest rate, and time values are not permitted.
- Negative Celsius temperatures are allowed.
- Interest is calculated using the simple interest formula without compounding.
- No external Python libraries are required.

## Conclusion

These programs demonstrate how Python can perform practical calculations while handling user input safely. They also reinforce the importance of readable code, string operations, and exception handling.
