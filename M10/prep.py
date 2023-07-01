# Error Handling Prep Content

# Error Handling is when something doesn't go the way its supposed to on things that I don't have control over (syntax error, runtime error, logic error)

# Syntax error
x = 42
y = 206
if x == y:
    print('Success!!')

# Runtime error
# This code will fail when run
x = 42
y = 0
try:
    print(x/y)
except ZeroDivisionError as e:
    print('Sorry, something went wrong')
except:
    print('Something really went wrong')
finally:
    print('This always run on success or failure')

# Logic error: always make sure that boolean is correct, that x is greater than y
x = 206
y = 42
if x > y:
    print(str(x) + ' is greater than ' + str(y))
# Debugging is when I know that there is something wrong with my own code. 

# When you get errors look at stack trace and find your mistake, stack overflow is best friend and always take a break

# Example 1

""" try:
    # Write normal code here. This block must include
    # code that falls into two groups:
    # 1. Code that may cause an exception to be raised
    # 2. Code that depends on the results of the code
    #    in the first group
except ZeroDivisionError as zero_div_err:
    # Code that the computer executes if the code in the try
    # block caused a function to raise a ZeroDivisionError.
except ValueError as val_err:
    # Code that the computer executes if the code in the
    # try block caused a function to raise a ValueError.
except (TypeError, KeyError, IndexError) as error:
    # Code that the computer executes if the code in the
    # try block caused a function to raise a TypeError,
    # KeyError, or IndexError.
except Exception as excep:
    # Code that the computer executes if the code in the try
    # block caused a function to raise any exception that
    # was not handled by one of the previous except blocks.
except:
    # Code that the computer executes if the code in the
    # try block caused a function to raise anything that
    # was not handled by one of the previous except blocks.
else:
    # Code that the computer executes after the code
    # in the try block if the code in the try block
    # did not cause any function to raise an exception.
finally:
    # Code that the computer executes after all the other
    # code in try, except, and else blocks regardless of
    # whether an exception was raised or not. """

# Example 2

def main():
    try:
        text = input("Please enter a number: ")
        integer = round(text)
        print(integer)

    except TypeError as type_err:
        print(type_err)

if __name__ == "__main__":
    main()

# Example 3

def main():
    try:
        number = float(input("Please enter a number: "))
        print(number)

    except ValueError as val_err:
        print(val_err)

if __name__ == "__main__":
    main()
# Example 4

def main():
    try:
        players = int(input("Enter the number of players: "))
        teams = int(input("Enter the number of teams: "))

        players_per_team = players / teams

        print(f"Each team should have {players_per_team} players")

    except ZeroDivisionError as zero_div_err:
        print(zero_div_err)

if __name__ == "__main__":
    main()

# Example 5

def main():
    try:
        # Create a list that contains three family names.
        surnames = ["Smith", "Lopez", "Marsh"]

        # Attempt to change the surname at index 3. Because
        # there are only three names in the surnames list and
        # therefore the last index is 2, this statement will
        # fail and cause the computer to raise an IndexError.
        surnames[3] = "Olsen"

    except IndexError as index_err:
        print(index_err)

if __name__ == "__main__":
    main()
# Example 6

def main():
    try:
        # Create a list that contains three family names.
        surnames = ["Smith", "Lopez", "Marsh"]

        # Attempt to print the surname at index 3. Because
        # there are only three names in the surnames list and
        # therefore the last index is 2, this statement will
        # fail and cause the computer to raise an IndexError.
        print(surnames[3])

    except IndexError as index_err:
        print(index_err)

if __name__ == "__main__":
    main()
# Example 7

def main():
    try:
        # Create a dictionary with student IDs as
        # the keys and student names as the values.
        students = {
            "42-039-4736": "Clint Huish",
            "61-315-0160": "Amelia Davis",
            "10-450-1203": "Ana Soares",
            "75-421-2310": "Abdul Ali",
            "07-103-5621": "Amelia Davis"
        }

        # Attempt to find the key "50-420-1021",
        # which is not in the dictionary. This will
        # cause the computer to raise a KeyError.
        name = students["50-420-1021"]

        print(name)

    except KeyError as key_err:
        print(type(key_err).__name__, key_err)

if __name__ == "__main__":
    main()
# Example 8

def main():
    try:
        with open("products.vcs", "rt") as products_file:
            for row in products_file:
                print(row)

    except FileNotFoundError as not_found_err:
        print(not_found_err)

if __name__ == "__main__":
    main()
# Example 9

def main():
    try:
        with open("contacts.csv", "rt") as contacts_file:
            for row in contacts_file:
                print(row)

    except PermissionError as perm_err:
        print(perm_err)

if __name__ == "__main__":
    main()

# Example 10
"""
The owner of Sam's Sandwich Shop requested this program,
which computes the number of sandwiches per employee
that his employees made in his restaurant in one day.
"""

def main():
    try:
        # Get the number of sandwiches made today and the
        # number of employees who worked today from the user.
        sandwiches = int(input("Number of sandwiches made today: "))
        employees = int(input("Number of employees who worked today: "))

        # Compute the number of sandwiches per employee
        # that were made today in the restaurant.
        sands_per_emp = sandwiches / employees

        # Print the results for the user to see.
        print(f"{sands_per_emp:.1f} sandwiches per employee")

    except ValueError as val_err:
        print(f"Error: {val_err}")
        print("You entered text that is not an integer. Please")
        print("run the program again and enter an integer.")

    except ZeroDivisionError as zero_div_err:
        print(f"Error: {zero_div_err}")
        print("You entered 0 for the number of employees.")
        print("Please run the program again and enter an integer")
        print("larger than 0 for the number of employees.")


# Call main to start this program.
if __name__ == "__main__":
    main()

# Example 11

import csv

DATE_INDEX = 0
START_MILES_INDEX = 1
END_MILES_INDEX = 2
GALLONS_INDEX = 3


def main():
    try:
        # Open the fuel_usage.csv file.
        filename = "fuel_usage.csv"
        with open(filename, "rt") as usage_file:

            # Use the standard csv module to get
            # a reader object for the CSV file.
            reader = csv.reader(usage_file)

            # The first line of the CSV file contains
            # headings and not fuel usage data, so this
            # statement skips the first line of the file.
            next(reader)

            # Print headers for the three columns.
            print("Date,Start,End,Gallons,Miles/Gallon")

            # Process each row in the CSV file.
            for row_list in reader:

                # From the current row of the CSV file, get
                # the date, the starting and ending odometer
                # readings, and the number of gallons used.
                date = row_list[DATE_INDEX]
                start_miles = float(row_list[START_MILES_INDEX])
                end_miles = float(row_list[END_MILES_INDEX])
                gallons = float(row_list[GALLONS_INDEX])

                # Call the miles_per_gallon function.
                mpg = miles_per_gallon(
                        start_miles, end_miles, gallons)

                # Display the results for one row.
                mpg = round(mpg, 1)
                print(date, start_miles, end_miles,
                        gallons, mpg, sep=",")

    except FileNotFoundError as not_found_err:
        print(f"Error: cannot open {filename}"
                " because it doesn't exist.")

    except PermissionError as perm_err:
        print(f"Error: cannot read from {filename}"
                " because you don't have permission.")

    except ZeroDivisionError as zero_div_err:
        print(f"Error: {filename} contains a"
                " zero in the gallons column.")


def miles_per_gallon(start_miles, end_miles, gallons):
    """Compute and return the average number of miles
    that a vehicle traveled per gallon of fuel.

    Parameters
        start_miles: starting odometer reading in miles.
        end_miles: ending odometer reading in miles.
        gallons: amount of fuel used in U.S. gallons.
    Return: miles per gallon
    """
    mpg = abs(end_miles - start_miles) / gallons
    return mpg


# Call main to start this program.
if __name__ == "__main__":
    main()
# Example 12

def main():
    gender = input("Enter your gender (M or F): ")

    weight = get_float("Enter your weight in kg: ", 20, 500)
    height = get_float("Enter your height in cm: ", 60, 250)
    age = get_float("Enter your age in years: ", 10, 120)

    bmr = basal_metabolic_rate(gender, weight, height, age)
    print(f"Your basal metabolic rate is {bmr} calories per day.")


def get_float(prompt, lower_bound, upper_bound):
    """Get a number from the user, validate that the user
    entered a number and not some other text, validate that
    the number is between a lower and upper bound, and then
    return the number. If the user enters an invalid number,
    this function will prompt the user repeatedly until the
    user enters a valid number.

    Parameters
        prompt: A string to display to the user.
        lower_bound: The smallest number that the user may enter.
        upper_bound: The largest number that the user may enter.
    Return: The number entered by the user.
    """
    while True:
        try:
            text = input(prompt)
            number = float(text)
            if number < lower_bound:
                print(f"{number} is too small.")
                print("Please enter another number.")
            elif number > upper_bound:
                print(f"{number} is too large.")
                print("Please enter another number.")
            else:
                # If the computer gets to this line of code,
                # the user entered a valid number between
                # lower_bound and upper_bound, so exit the loop.
                break

        except ValueError as val_err:
            # The user entered at least one character that is
            # not part of a floating point number, so print a
            # message asking the user to enter a number.
            print(f"{text} is not a number.")
            print("Please enter a number.")

    return number


def basal_metabolic_rate(gender, weight, height, age):
    """Calculate and return a person's basal metabolic rate
    in calories per day. weight must be in kilograms, height
    must be in centimeters, and age must be in years.
    """
    if gender.upper() == "F":
        bmr = 447.593 + 9.247 * weight \
                + 3.098 * height - 4.330 * age
    else:
        bmr = 88.362 + 13.397 * weight \
                + 4.799 * height - 5.677 * age
    return bmr


# Call main to start this program.
if __name__ == "__main__":
    main()