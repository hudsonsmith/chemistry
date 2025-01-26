import random
from os import system, name

# Polyatomic ions with simplified formulas and charges
polyatomic_ions = {
    "Acetate": {"formula": "C2H3O2", "charge": -1},
    "Ammonium": {"formula": "NH4", "charge": +1},
    "Bicarbonate": {"formula": "HCO3", "charge": -1},
    "Carbonate": {"formula": "CO3", "charge": -2},
    "Hydroxide": {"formula": "OH", "charge": -1},
    "Nitrate": {"formula": "NO3", "charge": -1},
    "Phosphate": {"formula": "PO4", "charge": -3},
    "Sulfate": {"formula": "SO4", "charge": -2}
}

def clear() -> None:
    """Function to clear the screen."""
    system("clear") if name == "posix" else system("cls")

def polyatomic_quiz():
    print("Welcome to the Polyatomic Ion Quiz!")
    while True:
        clear()
        # Select a random polyatomic ion
        ion_name = random.choice(list(polyatomic_ions.keys()))
        ion_info = polyatomic_ions[ion_name]

        # Ask for the formula
        while True:
            answer_formula = input(f"What is the formula for {ion_name}? ").strip()
            if answer_formula == ion_info["formula"]:
                print("Correct formula!")
                break  # Exit the loop if the answer is correct
            else:
                print(f"Wrong! The correct formula is {ion_info['formula']}. Try again.")
                input()
                clear()

        # Ask for the charge
        while True:
            answer_charge = input(f"What is the charge of {ion_name}? ").strip()
            try:
                answer_charge = int(answer_charge)
            except ValueError:
                print("Invalid input, please enter a number for the charge.")
                continue
            
            if answer_charge == ion_info["charge"]:
                print("Correct charge!")
                break  # Exit the loop if the answer is correct
            else:
                print(f"Wrong! The correct charge is {ion_info['charge']}. Try again.")

        input("Hit [ENTER] to continue...")

# Run the quiz
polyatomic_quiz()
