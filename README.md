Number Guessing Game

This code makes a guessing game with Tkinter. Players guess 1-50 in few tries. It uses labels, buttons, input fields. If guesses match, it ends. If not, hints guide higher/lower. Simple, engaging fun!

Libraries:

tkinter library for GUI.
random library to generate a random number.

Variables:

attempts: How many tries the player has left.
answer: Random number to guess.

Function check_answer():

Decreases attempts.
Gets player's guess from input.
Compares guess with answer.
Updates GUI label with result.
Congratulates and ends if guess is right.
Ends game if out of attempts.
Provides hints for higher/lower guesses.
