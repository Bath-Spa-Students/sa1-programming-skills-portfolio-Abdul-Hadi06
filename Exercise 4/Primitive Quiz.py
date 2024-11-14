#Essential requirements.
#Requesting the user to answer
answer = input("What is the capital of France? ").strip()
#Waiting for the output.
if answer.upper() == "PARIS":
    print("Correct! The answer is PARIS.")
else:
    print("Incorrect. The correct answer is PARIS.")

# Advanced requirements.
#Quiz
Questions = {
    "Russia": "Moscow",
    "Ukraine": "Kyiv",
    "Denmark": "Copenhagen",
    "Sweden": "Stockholm",
    "Norway": "Oslo",
    "Finland": "Helsinki",
    "Germany": "Berlin",
    "Spain": "Madrid",
    "Belgium": "Brussels",
    "Netherlands": "Amsterdam"
}
#To count the score.    
score = 0
#To ask the questions and waiting for the output.
for country, capital in questions.items():
    answer = input(f"What is the capital of {country}? ").strip()
    if answer.lower() == capital.lower():
        print("Correct!")
        score += 1
    else:
        print(f"Incorrect. The correct answer is {capital}.")
    
    print(f"\nYour final score: {score}/{len(questions)}")
