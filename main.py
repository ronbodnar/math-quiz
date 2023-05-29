# Import modules
import sys
import math
import random
import operator

# Used to keep track of the number of questions answered correctly
score = 0

def start_game():
    global score
    
    print("######################## Welcome to Math Quiz ########################")
    print()
    print("Valid Inputs:")
    print("\t+   ~ Addition")
    print("\t-   ~ Substraction")
    print("\t*   ~ Multiplication")
    print("\t/   ~ Division")
    print("\tall ~ Random equations with all operations\n")
    
    # Prompt the user for their preferred problem type
    operator_type = prompt_user("Please enter an operator or type \"all\" (no quotes) to begin the game:", ["+", "-", "*", "/", "all"], "You must enter a valid operator or type \"all\" (no quotes) to begin.")
    
    # If the user enters division or 'all', output a warning
    if operator_type == '/' or operator_type == 'all':
        print("[NOTE]: Enter only the quotient for your response, ignoring any remainder. Number should not be a decimal.\n")
        
    problems_to_ask = prompt_user("How many problems do you want to solve? (1 - 10)", [1, 10], "You must enter a number between 1 and 10.")
    
    problems_answered = 0
    
    # Loop until the number of problems answered is equal to the number of problems to be asked
    while problems_answered < problems_to_ask:
        ask_question(operator_type)
        problems_answered = problems_answered + 1;
        
    print()
    print("You have answered {}/{} problems correctly, which is a total of {}%".format(score, problems_answered, (score/problems_answered)*100))

def ask_question(operator_type):
    global score
    # Define a list of operators and their functions to be used for 'all' quiz type
    operators = [('+', operator.add), ('-', operator.sub), ('*', operator.mul), ('/', operator.truediv)]
    
    # If the user wants all types of problems
    if operator_type == 'all':
        # Set the operator and its respective function randomly
        operation, function = random.choice(operators)
        
        # Select the first number randomly but modify the number if the operation is division
        first_number = random.randrange(1, 20 if operation != '/' else 200)
        
        # Select the second number randomly but modify the number if the operation is division
        second_number = random.randrange(1, 20 if operation != '/' else first_number)
        
        problem = "{} {} {} = ".format(first_number, operation, second_number)
        answer = math.floor(function(first_number, second_number))
    
    # If the user wants addition problems only.
    if operator_type == '+':
        first_number = random.randrange(1, 300)
        second_number = random.randrange(1, 300)
        problem = "{} {} {} = ".format(first_number, '+', second_number)
        answer = first_number + second_number
    
    # If the user wants subtraction problems only.
    if operator_type == '-':
        first_number = random.randrange(100, 300)
        second_number = random.randrange(50, 200)
        problem = "{} {} {} = ".format(first_number, '-', second_number)
        answer = first_number - second_number
    
    # If the user wants multiplication problems only.
    if operator_type == '*':
        first_number = random.randrange(1, 20)
        second_number = random.randrange(1, 20)
        problem = "{} {} {} = ".format(first_number, '*', second_number)
        answer = first_number * second_number
    
    # If the user wants division problems only.
    if operator_type == '/':
        first_number = random.randrange(1, 300)
        second_number = random.randrange(1, first_number)
        problem = "{} {} {} = ".format(first_number, '/', second_number)
        answer = math.floor(first_number / second_number)
        
    while True:
        try:
            response = int(input(problem))
            # If the response provided is equal to the calculated answer, give them a point.
            if response == answer:
                score = score + 1
                
            break # Exit the loop.
        
        # Listen for invalid responses and output a warning to the user, then repeat the equation.
        except ValueError:
            print("[INVALID INPUT] You must provide a number for your answer.\n")
            continue

def prompt_user(prompt_text, acceptable_inputs, error_text):
    while True:
        try:
            if type(acceptable_inputs[0]) is str:
                response = input(prompt_text + " ")
                
                if response.lower() not in acceptable_inputs:
                    print(f"[INVALID INPUT] {error_text} {response} is not valid.\n")
                    continue
                
                return response
            elif type(acceptable_inputs[0]) is int:
                response = int(input(prompt_text + " "))
                
                if (response < acceptable_inputs[0] or response > acceptable_inputs[1]):
                    print(f"[INVALID INPUT] You must enter a number between {acceptable_inputs[0]} and {acceptable_inputs[1]}. {response} is out of range.\n")
                    continue
                
                return response
                
            # If acceptable input list is not a string or integer, gracefully exit program
            else:
                print("[INVALID INPUT] Acceptable input type not supported.");
                sys.exit(1)
        
        # If input is not of the same type requested, inform the user and prompt to re-enter their input
        except ValueError:
            print("[INVALID INPUT] " + error_text + "\n")
            continue
        
        
# Driver
start_game()
