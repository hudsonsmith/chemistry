import random
from os import system, name

# Prefixes for numbers of atoms
prefixes = {
    1: "mono",
    2: "di",
    3: "tri",
    4: "tetra",
    5: "penta",
    6: "hexa",
    7: "hepta",
    8: "octa",
    9: "nona",
    10: "deca"
}

def clear() -> None:
    """Clears the console screen."""
    system("clear")

# Function to conduct the prefix quiz
def prefix_quiz():
    print("Welcome to the Prefix Quiz!")
    while True:
        # Randomly choose a number between 1 and 10
        number = random.randint(1, 10)
        
        # Ask the question twice
        for _ in range(2):
            clear()
            answer = input(f"What is the prefix for {number} atom(s)? ").strip().lower()
            correct_answer = prefixes[number]
            
            if answer == correct_answer:
                print("Correct!")
                break
            else:
                print(f"Wrong! The correct answer is '{correct_answer}'.")

            input("Hit [ENTER] to continue...")


# Run the prefix quiz
prefix_quiz()
