''' 
Isabel Godfrey
1.1 internal
Version 1
Quiz
29/04/2025
'''

import random

# set up constants
# this will make by code more robust as i can just change the constant instead of having to change the number whenever it is used.
MIN_QUESTIONS = 5
MAX_QUESTIONS = 10
OPTION_KEYS = ['a', 'b', 'c', 'd']
POSITIVE_FEEDBACK = "Correct. YAY!!\n"
NEGATIVE_FEEDBACK = "Sorry, that was wrong. The correct answer was: "

# set up user input functions
#having iputs as their own functions means i will be able to change them here where they are seperate instead of having to go through and try find them in my big block of code
#this also make my code easier to read
def get_user_name():
    name = input("Hi there! What's your name? ")
    print("Nice to meet you, " + name + "!\n")
    return name

# the try and expect and the whil loop make my code robust by not breaking when ivalid input is put in and give error messages to help the user put in valid input
def ask_to_play():
    while True:
        try: 
            yes_no = input("Would you like to play a quiz game? (y or n): ")
            yes_no = yes_no[0].lower()

            if yes_no == 'y':
                print("Awesome! Let's get started!\n")
                return True
            elif yes_no == 'n':
                print("Aww, maybe next time. Goodbye!\n")
                return False
            else:
                print("Hmm, I'll take that as a yes. Let's play!\n")
                return True
        except:
            print("Please enter yes or no")

def get_number_of_questions():
    while True:
        try:
            num = int(input("How many questions would you like? Please pick between " + str(MIN_QUESTIONS) + "-" + str(MAX_QUESTIONS) + ": "))
            if MIN_QUESTIONS <= num <= MAX_QUESTIONS:
                return num
            else:
                print("Please enter a number between 5 and 10.")
        except ValueError:
            print("Please enter an integer.")
        except:
            print("Unexpected error. Please try again")

def ask_question(index, question, options, correct_answer):
    print("\nQuestion " + str(index + 1) + ": " + question)
    for option in options:
        print(option)
    while True:
        player_answer = input("Your answer (a, b, c, or d):").lower()
        if player_answer in OPTION_KEYS:
            break
        else:
            print("Please enter a valid option: a, b, c, or d.\n")
    if player_answer == correct_answer:
        print(POSITIVE_FEEDBACK)
        return True
    else:
        correct_index = OPTION_KEYS.index(correct_answer)
        correct_text = options[correct_index]
        print(NEGATIVE_FEEDBACK + correct_text + "\n")
        return False
        
def get_percentage(score, num_questions):
    percentage = score / num_questions * 100 
    percentage = int(percentage)  # Convert to integer
    print("Your score was " + str(percentage) + "%. Well done!")

    if percentage == 100:
        print("Perfect score! You're a usability superstar! ⭐")
    elif percentage > 50:
        print("You passed! Great job! 🎉")
    else:
        print("You didn't pass this time, but don't give up! Try again and you'll improve. 💪")

    return percentage
  

# this is the main game function. By defining the functions baove now i can just type them in to the main game to make coding this part faster and less room for error
def gameplay():
    score = 0
    name = get_user_name()

    if not ask_to_play():
        return

    num_questions = get_number_of_questions()

    questions = [
        "Jakob Nielsen's 10 Usability Heuristics are best thought of as", 
        "When you're using a computer, it's good if it always tells you what's going on. Which heuristic is this?", 
        "It helps if the things on a screen look and act like things in the real world. Which is the best example of this?",
        "The saying 'U HAVE CHARM' helps remember some rules. What does the 'A' stand for?",
        "The main idea of 'Error prevention' is to:",
        "Making things faster for experienced users, like using shortcuts, is part of which heuristic?",
        "If buttons and menus look and work the same way everywhere in an app, which rule is it following?",
        "It's easier to choose from a list than to have to remember what to type. This is the idea behind:",
        "When you make a mistake, the app should:",
        "Letting users undo things they've done is important for:"
    ]

    options = [
        ["A. Strict rules for how to code websites and apps.", "B. General tips for making things easy to use.",
         "C. Things every app must have to be official.", "D. A list of all the cool features you can add."],
        ["A. Being the same and working the same way everywhere.", "B. Showing you what's happening right now.", 
         "C. Stopping you from making mistakes.", "D. Having help if you need it."],
        ["A. Using complicated computer words in error messages", 
         "B. Putting information in an order that makes sense like in real life.", 
         "C. Having lots of extra information to explain everything", 
         "D. Letting you change how the screen looks with different colours."],
        ["A. 'Algorithms' making the program run fast", "B.'Looks good and keeps it simple'.", 
         "C. 'Able to be used by everyone'.", "D. 'Things you can click on to do stuff'."],
        ["A. Tell you clearly when you've done something wrong.", "B. Help you fix your mistakes quickly.", 
         "C. Stop you from making mistakes in the first place.", "D. Give you lots of instructions so you don't mess up."],
        ["A. Being the same and working the same way everywhere.", 
         "B. Being able to do things in different ways and quickly.", 
         "C. Remembering things for you instead of making you remember.", "D. Having help if you need it."],
        ["A. Showing you what's happening right now.", "B. Looking like things in the real world.", 
         "C. Being the same and working the same way everywhere.", "D. Stopping you from making mistakes."],
        ["A. Being the same and working the same way everywhere.", "B. Letting you control things and undo mistakes.", 
         "C. Showing you options so you don't have to remember.", "D. Having a simple and good-looking design."],
        ["A. Just tell you that something went wrong.", "B. Let you go back and try again.", 
         "C. Tell you what the problem is and how to fix it.", "D. Stop you from making any more mistakes."],
        ["A. Showing you what's happening right now.", "B. Letting you be in charge and fix mistakes.", 
         "C. Stopping you from making mistakes.", "D. Having a simple and good-looking design."]
    ]

    answers = ["b", "b", "b", "b", "c", "b", "c", "c", "c", "b"]

    used_indexes = []
    selected_questions = []
    selected_options = []
    selected_answers = []
    
#this loop makes sure differnt questions are selected so there are no double ups
    while len(used_indexes) < num_questions:
        index = random.randint(0, len(questions) - 1)
        if index not in used_indexes:
            used_indexes.append(index)
            selected_questions.append(questions[index])
            selected_options.append(options[index])
            selected_answers.append(answers[index])

    for i in range(num_questions):
        if ask_question(i, selected_questions[i], selected_options[i], selected_answers[i]):
            score += 1
    get_percentage(score, num_questions)

#this runs the game
gameplay()


