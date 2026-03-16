# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [x] Describe the game's purpose. This is a number guessing game built with Streamlit where you try to guess a secret number within a set number of attempts, with hints telling you whether to go higher or lower and a score that rewards you for guessing in fewer tries.

- [x] Detail which bugs you found. The hint messages were swapped, that is when your guess was too high it told you to go higher and vice versa. The secret number was also being cast to a string on even-numbered attempts which broke numeric comparison entirely, for example "9" > "10" evaluates to True in Python string ordering. Hard mode had a range of 1–50 which was actually easier than Normal's 1–100. The new game button did not reset score, status, or history, so the game stayed in a won/lost state even after clicking it. The win formula also had an extra +1 that made the bonus collapse too fast, and wrong guesses on even attempts would sometimes award +5 points instead of deducting.

- [x] Explain what fixes you applied. Swapped the hint messages in check_guess so "Too High" says "Go LOWER!" and "Too Low" says "Go HIGHER!". Removed the type-flip logic so the secret is always compared as an integer. Fixed the new game handler to reset all session state including score, status, and history, and to use the difficulty-based range instead of a hardcoded 1–100. Fixed the win formula by removing the extra +1 and simplified wrong-guess scoring to always deduct 5 points. Also refactored all core logic out of app.py into logic_utils.py to separate UI from game logic.

## 📸 Demo

- [check] ![Demo of working app](<Screenshot 2026-03-15 at 9.41.38 PM.png>)

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
