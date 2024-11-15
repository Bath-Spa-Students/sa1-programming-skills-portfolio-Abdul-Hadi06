# Provide a list of names to look over.
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

# Ask the user to input the name they are finding.
# strip() Removes extra spaces around the input.
find_name = input("Input the name which is to be found:").strip()

# Mark if the name appears in the search results.
found = False

# Iterate through each name in the list to check if it relates the input of the user.
for name in names:
# Transform both names to lowercase to ensure the search is not affected by case.
    if name.lower() == find_name.lower():
# Adjust 'found' as True and notify the user if a match is identified.
        found = True
        print(f"Congrats! '{find_name}' is in the list.")
        break  
    # End the loop as soon as the name is found.

# Inform the user if the loop ends and the name was not found.
if not found:
    print(f"Unfortunately, '{find_name}' is not in the list.")
