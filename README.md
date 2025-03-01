# Palindromic & Turkish ID Number Validator

## Description

This Python program allows users to check whether a given number is both palindromic and conforms to the Turkish ID number rules.
Additionally, it can generate random numbers that meet these criteria.

## Features

- **Validate User Input:**
  - Ensures the number consists of 11 digits.
  - Checks if the number is palindromic.
  - Validates whether the number conforms to Turkish ID number rules.
- **Generate Random Numbers:**
  - Generates random palindromic numbers.
  - Generates random Turkish ID numbers following official rules.

## How It Works

### Option 1: User Input Validation

1. The user is prompted to enter an 11-digit number.
2. The program checks if the number:
   - Contains only digits.
   - Has exactly 11 digits.
   - Is a palindrome.
3. If all checks pass, the number is confirmed as a valid Turkish ID and palindrome.
4. If any check fails, the user is asked to input another number.

### Option 2: Random Number Generation

1. The program generates 5 palindromic numbers.
2. The program generates 5 valid Turkish ID numbers.
3. The generated numbers are displayed to the user screen.

## Usage

Run the script and select an option:

- **Option 1:** Enter a number to check its validity.
- **Option 2:** Generate and display valid numbers.

```bash
python script.py
```

## Functions

### `number_feedback()`

Prompts the user to enter an 11-digit number and validates it.

### `inverse_num(number)`

Checks whether the number is palindromic.

### `check_first_and_last_digit(number)`

Ensures the first and last digits are not zero.

### `verification_check(number)`

Performs mathematical checks for Turkish ID validity.

### `second_verification_check(number)`

Final verification for Turkish ID number validation.

### `randomize_numbers()`

Generates and prints palindromic and Turkish ID numbers.

### `generate_random_numbers()`

Creates a random palindromic number.

### `generate_random_ID()`

Generates a valid Turkish ID number.

## Example Output

```
Type 1 to find out if the numbers you entered are palindromic and ID number compatible
Type 2 to see numbers that are palindromic and conform to TC in mixed form
Input: 1
Please enter an 11-digit number: 12345432112
Your number has 11 digits but is not palindromic
```

## Requirements

- Python 3.x
- No additional dependencies required

## Author

Developed by Mehmet Efe Uçan

## License

This project is licensed under the MIT License.

