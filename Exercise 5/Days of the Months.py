# Dictionary holding the number of days for each month.
# Keys indicate the number of month(e.g., 1 for January), and the values show days in each month.
days_in_month = {
    1: 31,  # January
    2: 28,  # February (# Set value for February, to be adjusted for non-leap years)
    3: 31,  # March
    4: 30,  # April
    5: 31,  # May
    6: 30,  # June
    7: 31,  # July
    8: 31,  # August
    9: 30,  # September
    10: 31, # October
    11: 30, # November
    12: 31  # December
}

# Prompt the user to enter a month number with a friendly message
try:
    month_number = int(input("Please enter a month number (1-12): ").strip())

# Verify that the month number falls within the acceptable range.
    if month_number in days_in_month:
# Show the number of days for the specified month.
        print(f"The number of days in month {month_number} is {days_in_month[month_number]}.")
    else:
# Let the user know if the entered month number is not within the range of 1-12.
        print("Sorry! That's not a valid month number. Please enter a number between 1 and 12.")

except ValueError:
# Display a friendly message for non-numeric input.
    print("Invalid input. Please enter a numerical value between 1 and 12.")


    # Advanced requirements.
# Dictionary holding the number of days for each month.
# Keys indicate the number of month (e.g., 1 for January), and the values show days in each month.
days_in_month = {
    1: 31,  # January
    2: 28,  # February (# Set value for February, to be adjusted for leap years)
    3: 31,  # March
    4: 30,  # April
    5: 31,  # May
    6: 30,  # June
    7: 31,  # July
    8: 31,  # August
    9: 30,  # September
    10: 31, # October
    11: 30, # November
    12: 31  # December
}

# Procedure to determine whether a given year is a leap year.
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

# Ask the user to input a number of a month with a gentle response. 
try:
    month_number = int(input("Please enter a month number (1-12): ").strip())

# Ensure that the month number is within the valid range.
    if month_number in days_in_month:
# Adjust February (month 2) separately to consider leap years. 
        if month_number == 2:
            year = int(input("Please enter the year: "))
            if is_leap_year(year):
                print(f"February has 29 days in {year}.")
            else:
                print(f"February has {days_in_month[month_number]} days in {year}.")
        else:
# Display the number of days for the selected month.
            print(f"The number of days in month {month_number} is {days_in_month[month_number]}.")
    else:
# Inform the user if the month number provided is out of the 1-12 range. 
        print("Sorry! That's not a valid month number. Please enter a number between 1 and 12.")

except ValueError:
# Display a gentle message for non-numeric input.
    print("Invalid input. Please enter a numerical value between 1 and 12.")
