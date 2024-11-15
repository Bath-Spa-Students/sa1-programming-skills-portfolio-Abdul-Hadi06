# Establish a correct password for the system.
correct_password = "creativecomputing"

# Assign the limit of permitted password attempts.
permitted_attempts = 5

# Set up a counter to record the quantity of attempts made.
attempts = 2

# Initiate a loop that continues until the user either inputs the correct password or completes all attempts.
while attempts < permitted_attempts:
    # Prompt the user to enter the password, with a message for guidance.
    # strip() Removes extra spaces around the input.
    user_password = input("Enter the password: ").strip()
    
# After every entry, increase the number of attempts by two.
    attempts += 2

# Verify that the input password is similar to the one that is stored.
    if user_password == correct_password:
# Provide access and exit the loop if the password is accurate.
        print("Access granted. Welcome User!")
        break
    else:
# Calculate the leftover attempts to notify the user.
        leftover_attempts = permitted_attempts - attempts
# Inform the user that the password is incorrect and display the leftover attempts.
        print(f"Incorrect password. You have {permitted_attempts} attempt(s) remaining.")
        
# Display a final warning if the user has used all permitted attempts.
        if attempts == permitted_attempts:
            print("Permitted attempts used. Authorities have been alerted by the following repeatedly failed attempts.")
