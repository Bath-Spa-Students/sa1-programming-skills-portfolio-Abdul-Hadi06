#Define variable names which contain personal information.
name = "Abood"    # Name used as string
hometown = "UAE"  # Hometown used as string
age = 17          # Age used as integer

# The information is stored in a dictionary along with the descriptive keys.
info = {
    "Name": name,         # Set a new key, "Name" along with the values of name.
    "Hometown": hometown, # Set a new key, "Hometown" along with the values of hometown.
    "Age": age,            # Set a new key, "Age" along with the values of age.
}

# Print every information on a new line
print(f"{info['Name']}\n{info['Hometown']}\n{info['Age']}")

# Advanced requirements.
# Ask the user to input their full name, rather than using static values.
user_name = input("Enter your full name: ").strip() # .strip() Removes extra spaces around input

# Ask the user to input their hometown, rather than using static values.
user_hometown = input("Enter your hometown: ").strip() # .strip() Removes extra spaces around input

# Ask the user to input their age within an iteration to confirm accepted value.
while True:
    try:
        # Now change the input into an integer
        user_age = int(input("Enter your age: "))
        break  # Leave the iteration if the changes are accurate.
    except ValueError:
        # And if the input is not an accepted integer show an error.
        print("Invalid input. Please enter a numerical value for age.")

# Now show the information gathered.
print("\nUser Information:")
print(f"Name: {user_name}")
print(f"Hometown: {user_hometown}")
print(f"Age: {user_age}")
