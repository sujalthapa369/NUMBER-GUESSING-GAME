# NUMBER-GUESSING-GAME

This is a simple **Number Guessing Game** implemented in Python. The game challenges the user to guess a number randomly chosen by the program, between 1 and 50. The user can choose between two difficulty levels: **Easy** and **Hard**, each providing a different number of attempts to guess the number.

## How It Works
The program generates a random number between 1 and 50. The player selects a difficulty level:
- **Easy**: 10 attempts to guess the number.
- **Hard**: 5 attempts to guess the number.

The player makes a guess, and the program provides feedback on whether the guessed number is too high, too low, or correct. The game ends when the player correctly guesses the number or runs out of attempts.

## Code Explanation
The script follows these key steps:
1. **Random Number Generation**: 
   - The program uses Python's `random.randint(1,50)` to generate a random number between 1 and 50.
   
2. **User Input for Difficulty**: 
   - The player is prompted to choose a difficulty level. If the player selects "easy", they get 10 attempts. For "hard", they get 5 attempts.
   
3. **Guessing Loop**: 
   - The game enters a `while` loop where the player guesses the number.
   - The program provides feedback if the guessed number is too high or too low.
   - If the player runs out of attempts, the game ends with a loss.
   - If the correct number is guessed, the game ends with a win.

## How to Play
1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/number-guessing-game.git
   cd number-guessing-game

 
3. **Run the Python script**:
   ```bash
   python guess_the_number.py

  
4. **Game Instructions**:
   - The program will think of a number between 1 and 50.
   - Choose the difficulty level by typing `easy` or `hard`.
   - Guess the number within the given attempts.
   - The program will give hints if the number is too high or too low.
   - You win if you guess the number before your attempts run out. Otherwise, you lose!

## Future Enhancements
Some ideas for future enhancements include:
- Adding more difficulty levels.
- Implementing a scoring system.
- Adding a user-friendly GUI.
