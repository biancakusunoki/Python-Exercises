import random #Random library to make the code work

"""
    This program takes as input the number of sides on a dice.
    It simulates rolling the dice with that many sides
    Then, it prints the outcome of the roll.
"""

def main():
    
    num = input("""How many sides does your dice have? 
    Answer: """)
    num2 = random.randint(1, int(num)) #generates a random number from 1 to the user input number
    #Example, 1 to 62 if the user input 62. Then it generates some random number between the 1 to 62, example 24).

    print(f"Your roll is {num2}") #picks and show a random number between 1 to the input of the user


if __name__ == '__main__':
    main()
