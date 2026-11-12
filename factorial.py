#!/usr/bin/env python3
# Created By: Sam V
# Date: Nov 11, 2026
# This program calculates the factorial of a user-defined whole number (0 or greater).


def main():
    while True:
        try:
            user_input = input("Enter a whole number (0 or greater): ")
            number = int(user_input)

            if number < 0:
                print(
                    "Error: Factorials cannot be negative. Please try again (0 or greater)."
                )
            else:
                break  # Valid whole number entered; exit the input loop
        except ValueError:
            print(
                "Error: Invalid entry. Please enter a valid whole number (0 or greater)."
            )

    # 2. Factorial Calculation using a simulated do..while loop
    factorial = 1
    counter = 1

    while True:
        # Multiply only if the number is greater than 0 (handles 0! = 1)
        if number > 0:
            factorial *= counter
            counter += 1

        # Exit condition checked at the end (simulating 'while (counter <= number)')
        if counter > number:
            break

    print(f"{number}! = {factorial}")


if __name__ == "__main__":
    main()
