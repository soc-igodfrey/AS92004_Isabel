'''
Isabel Godfrey
1.1 internal
Version 1
Quiz
29/04/2025
'''

import random

# --- Intro ---
name = input("Hi there! What's your name? ")
print("Nice to meet you, " + name + "!")

yes_no = input("Would you like to play a quiz game? (y or n): ")
yes_no = yes_no[0].lower()

if yes_no == 'y':
    print("Awesome! Let's get started!")
elif yes_no == 'n':
    print("Aww, maybe next time. Goodbye!")
    exit()
else:
    print("Hmm, I'll take that as a yes. Let's play!")

# --- Question, options, and answers ---
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

# --- Get number of questions ---
MIN = 5
MAX = 10

while True:
    try:
        num_questions = int(input("How many questions would you like? Please pick between 5-10 questions: "))
        if MIN <= num_questions <= MAX:
            break
        else:
            print("Please enter a number between 5 and 10.")
    except ValueError:
        print("Please enter an interger.")
    except:
      print("Unexpected error. Please try again")

# --- Randomly pick unique questions ---
used_indexes = []
selected_questions = []
selected_options = []
selected_answers = []

while len(used_indexes) < num_questions:
    index = random.randint(0, len(questions) - 1)
    if index not in used_indexes:
        used_indexes.append(index)
        selected_questions.append(questions[index])
        selected_options.append(options[index])
        selected_answers.append(answers[index])

# --- Show selected questions and answers (for now) ---
for i in range(num_questions):
    print("\nQuestion " + str(i + 1) + ": " + selected_questions[i])
    for option in selected_options[i]:
        print(option)
    print("(Correct answer: " + selected_answers[i].upper() + ")")  
