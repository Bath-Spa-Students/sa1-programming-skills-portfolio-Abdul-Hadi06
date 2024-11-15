# Function to determine whether a given integer is odd or even.
def check_odd_even(integer):
# An integer is even if it is divisible by two.
    if integer % 2 == 0:
        return f"{integer} is even."
    else:
# An integer is odd if it is not divisible by two.
        return f"{integer} is odd."

# Key function to process user input and provide the output.
def main():
# Request the user to input an integer.
    try:
        user_integer = int(input("Enter an integer: "))

# Get the output message by executing the check_odd_even function. 
        output_message = check_odd_even(user_integer)

        # Print the output message.
        print(output_message)
    except ValueError:
# Show an error message if the user inputs a value that is not an integer.
        print("Invalid input. Enter an integer.")

# Execute just the main function if the script is executed instantly.
if __name__ == "__main__":
    main()