import random

# Prefixes for numbers of atoms
prefixes = {
    1: "mono-",
    2: "di-",
    3: "tri-",
    4: "tetra-",
    5: "penta-",
    6: "hexa-",
    7: "hepta-",
    8: "octa-",
    9: "nona-",
    10: "deca-"
}

# Function to generate a random compound name
def generate_compound():
    num_carbons = random.randint(1, 10)  # Randomly select number of carbons
    num_hydrogens = random.randint(1, 10)  # Randomly select number of hydrogens
    
    # Build the compound name
    compound_name = f"{prefixes[num_carbons]}carbon {prefixes[num_hydrogens]}hydride"
    
    return compound_name, num_carbons, num_hydrogens

# Function to conduct the quiz
def quiz():
    print("Welcome to the Random Compound Name Quiz!")
    while True:
        # Generate a random compound
        compound_name, num_carbons, num_hydrogens = generate_compound()
        
        # Ask for the IUPAC name of the generated compound
        answer = input(f"What is the IUPAC name for the compound with {num_carbons} carbon(s) and {num_hydrogens} hydrogen(s)? ").strip().lower()
        
        # Create the correct answer based on generated values
        correct_answer = f"{prefixes[num_carbons]}carbon {prefixes[num_hydrogens]}hydride"
        
        if answer == correct_answer:
            print("Correct!")
        else:
            print(f"Wrong! The correct answer is '{correct_answer}'.")


# Run the quiz
quiz()

