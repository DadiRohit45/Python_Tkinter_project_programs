Smart Kids Learning Games:
A fun, interactive educational desktop application designed for children. Built entirely in Python using the tkinter library, this lightweight graphical interface offers three different game modes to test and develop fundamental skills in math, general knowledge, and spelling.

FEATURES:
➕ Math Quiz: Automatically generates random arithmetic equations (addition, subtraction, multiplication, and division) using numbers 1 through 10.
🧠 GK Quiz: A general knowledge trivia mode that asks fun, basic questions (e.g., animal facts, colors).
📚 Spelling Game: An anagram puzzle where kids must unscramble jumbled letters to spell common words correctly (like "apple", "school", and "computer").

Instant Visual Feedback:
The application immediately lets the user know if their answer is correct with celebratory emojis, or gently encourages them to try again if they get it wrong. Color-coded text (black for correct, red for incorrect) helps reinforce the learning process.

PREREQUISITES:
To run this application, you only need:
Python 3.x: Ensure Python is installed on your system.
(Note: tkinter and random are standard Python libraries and come pre-installed. You do not need to download any external packages!)

How to Run the Game:
1.Download or copy the code into a file named kids_games.py.
2.Open your computer's terminal or command prompt.
3.Navigate to the directory where you saved kids_games.py.

Execute the script by running the following command:
command:"python kids_games.py"
"A light blue window will pop up. Click any of the three colored game buttons to generate a question, type your guess in the white box, and click SUBMIT ANSWER!"

Behind the Code:
This project showcases fundamental Python programming concepts, including:
GUI Development: Using tkinter to design a kid-friendly, colorful layout with exact button placement (.place() and .pack()).
Event Handling: Connecting button clicks to specific Python functions (lambda commands) to dynamically update the screen text.
Data Structures: Using Python dictionaries ({}) to store General Knowledge questions and Spelling word pairs.
Dynamic Evaluation: Utilizing Python's eval() function to instantly calculate the randomly generated math strings.
