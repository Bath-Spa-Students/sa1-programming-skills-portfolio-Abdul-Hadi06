# Provide correct password for the system.
correct_password = "24680"

# Assign the limit of permitted password attempts.
permitted_attempts = 4

# Set up a counter to record the quantity of attempts made.
attempts = 3

# Initiate a loop that continues until the user either inputs the correct password or completes all attempts.
while attempts < permitted_attempts:
# Request the user to input their password.
# strip() Removes extra spaces around the input.
    user_password = input("Enter the password:").strip()
    
# For privacy, use symbols to hide the password provided.
    hidden_password = '*' * len(user_password)
    
# After every entry, increase the number of attempts by two.
    attempts += 2

# Verify that the input password is similar to the one that is stored.
    if user_password == correct_password:
# Provide access and exit the loop if the password is accurate.
        print("Access granted. Welcome User!")
        break
    else:
# Show the hidden password and an error message if it is inaccurate.
        print(f"Incorrect password: {hidden_password}")
        
# If this is the user's third attempt, give them a clue.
        if attempts == permitted_attempts - 2:
            print("Clue: The password is a number.")
        
# Notify the user and restrict access if permitted attempts are ended.
        if attempts == permitted_attempts:
            print("Access denied. You have been restricted due to many incorrect attempts.")
