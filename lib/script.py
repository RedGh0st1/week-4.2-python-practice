from capitals import states
import random
# The game should not present the states in alphabetical order—use random.shuffle() to keep things interesting.
# Welcome players with a friendly greeting when the game starts.
# Track their score and show them how they're doing after each question.
# When all 50 states have been covered, ask the user if they'd like to play again.
# Your program should prompt the user to identify the capital of each given state.
# userInput = input("What is the capital of Alabama? ")
# Keep a running tally of how many answers are correct and incorrect. 
# After cycling through all 50 states, the user should be asked whether they want to play again.
# You might want to create a small test list of states and capitals to try out your code before working with all 50 states.
# random.shuffle()


# prompt to Welcome players with a friendly greeting when the game start to timed?
#  then the question "what is capital of state:"
#  create a variable to keep track of the user's score.
#  create a variable to keep  correct answer
    # create a response that is correct answer and number correct so far.
#  create a variable to keep incorrect answer
   # create a response saying its the wrong answer
#  Use a loop to iterate through the dictionary of states and capitals.
name = input("What is your name? ")
print(f"Welcome to the State Capitals Quiz! {name}")
print("Let's test your knowledge of U.S. states and their capitals.")

score = 0
incorrect_answer = 0
correct_answer = 0

for state in states:
    user_input = input(f"What is the capital of {state['name']}? ").lower()
    if user_input == state["capital"]:
       print("you are correct!")
       print("Your score is {score}!")
       score += 1
       correct_answer += 1
    else:
        print("You are incorrect! {score}")
        incorrect_answer += 1
    print(user_input)
    print(state)
