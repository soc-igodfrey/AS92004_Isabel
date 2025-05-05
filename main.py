'''
Isabel Godfrey
1.1 internal
Version 1
Quiz
29/04/2025
'''

#Set up question and answer banks
questions = (" Jakob Nielsen's 10 Usability Heuristics are best though of as", 
              "When you're using a computer, it's good if it always tells you what's going on. Which heuristic is this?", 
              "It helps if the things on a screen look and act like things in the real world. Which is the best example of this?",
              "The saying 'U HAVE CHARM' helps remember some rules. Wha t does the 'A' stand for?",
              "The main idea of 'Error prevention' is to:",
              "Making things faster for experienced users, like using shortcuts, is part of which heuristic?",
              "If buttons and menus look and work the same way everywhere in an app, which rule is it following?",
              "It's easier to choose from a list than to have to remember what to type. This is the idea behind:",
              "When you make a mistake, the app should:",
              "Letting users undo things they've done is important for:",
              )

options = (("A. Strict rules for how to code websites and apps.", "B. General tips for making things easy to use.",
             "C. Things every app must have to be official.", "D. A list of all the cool features you can add."),
            ("A. Being the same and working the same way everywhere.", "B. Showing you what's happening right now.", "C. Stopping you from making mistakes.", "D. Having help if you need it."),
            ("A. Using complicated computer words in error messages", "B. Putting information in an order that makes sense like in real life.", "C. Having lots of extra information to explain everything", "D. Letting you change how the screen looks with different colours."),
            ("A. 'Algorithms' making the program run fast", "B.'Looks good and keeps it simple'.", "C. 'Able to be used by everyone'.", "D. 'Things you can click on to do stuff'."),
           ( "A. Tell you clearly when you've done something wrong.", "B. Help you fix your mistakes quickly.", "C. Stop you from making mistakes in the first place.", "D. Give you lots of instructions so you don't mess up."),
            ("A.  Being the same and working the same way everywhere.", "B. Being able to do things in different ways and quickly.", "C. Remembering things for you instead of making you remember.", "D. Having help if you need it."),
            ("A. Showing you what's happening right now.", "B. Looking like things in the real world.", "C. Being the same and working the same way everywhere.", "D. Stopping you from making mistakes."),
           ("A. Being the same and working the same way everywhere.", "B. Letting you control things and undo mistakes.", "C. Showing you options so you don't have to remember.", "D. Having a simple and good-looking design."),
            ("A. Just tell you that something went wrong.", "B.  Let you go back and try again.", "C.  Tell you what the problem is and how to fix it.", "D. Stop you from making any more mistakes."),
            ("A. Showing you what's happening right now.", "B. Letting you be in charge and fix mistakes.", "C. Stopping you from making mistakes.", "D. Having a simple and good-looking design."),
          )

correct_answer = ["b", "b", "b", "b", "c", "b", "c", "", "", "", ]

#Set Up variables

score = 0

#user input variables

name = input("What is your name?")

yes_no = input("Hello, would you like to play a game? ")

# make it all lower case and the first letter so more answers are expected
yes_no = yes_no[0].lower()



# if statements, Have an else statement as well encase they dont enter yes or no so the code keeps running making it more robust. 
if yes_no == 'y':
    print("Okay, let's get started!")
elif yes_no == 'n':
    print("Aww, I'm sad to see you go. Bye.")
else:
    print("Hmmmm, was that a yes or a no? Imma say yes. Let's play!")

#set up constant because they help make code more robust
MIN = 5

MAX = 10

# get number of questions from try and except as it helps make my code more user friendly and robust, while using a loop so it runs again till imput is valid
while True:
    try:
        num_questions = int(input("How many questions would you like? Please pick between 5-10 questions: "))
        if 5 <= num_questions <= 10:
            break 
        else:
            print("Please enter a number between 5 and 10.")
    except ValueError:
        print("Error, please enter a valid number.")
    except:
        print("Unexpected error. Please try again")
  
  


