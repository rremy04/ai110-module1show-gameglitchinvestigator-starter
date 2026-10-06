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

- [To guess the secret number and the game will reveal through baloons if you've guessed the right number ] Describe the game's purpose.
- [Even when I typed what eneded up being the secret number it wasn't saying that I found it. Also, I noticed that the history wouldnn't contain all of my previous guesses so I can't even remember what I previously guessed. And the number attempts stop decreasing. Also the game would send the wrong message a e.g sending Higher when it should be Lower and vice versa.] Detail which bugs you found.
- [ I refactored app.py functions to logic_utils.py and added more tests to make sure the code was working and also changed the tests to instead except tuples] Explain what fixes you applied.


## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. User should enter a guess based on the range the game difficulty requires, he enters 20
2. Game returns Higher, and theirs a reduction in score  
3. User enters a guess 42, and the history is updated with the previous choices.
4. The score updates, and outputs baloons in congratulations
5. Game ends after the correct guess

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
platform darwin -- Python 3.13.7, pytest-9.1.1, pluggy-1.6.0
rootdir: /Users/rissahremy/code-path.org/AI-Class/ai110-module1show-gameglitchinvestigator-starter
plugins: anyio-4.15.1
collected 9 items                                                                                      

tests/test_game_logic.py .........                                                               [100%]

========================================== 9 passed in 0.01s ===========================================
(.venv) (base) rissahremy@Mac ai110-module1show-gameglitchinvestigator-starter % 

```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
