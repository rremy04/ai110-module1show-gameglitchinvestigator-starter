# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
- 1) The game work the first time I ran it, however the attempts wasn't decreasing as I type in more possible answer In app.py line 109 
st.info(
    f"Guess a number between 1 and 100. "
    f"Attempts left: {attempt_limit - st.session_state.attempts}"
) 2) When I did type in the correct answer it's as if the program froze. Line140 in app.py doesn't go away, if st.session_state.status != "playing":
    if st.session_state.status == "won":
        st.success("You already won. Start a new game to play again.")
    else:
        st.error("Game over. Start a new game to try again.")
    st.stop()
or dissapear when I've started a new game
**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| 23    | Go HIGHER!        | Go LOWER!       |    app.py
| 99| st.error("Game over. Start a new game to try again.") | Out of attempts! the Secre was 31. Score: -5 | app.py
| 31| You already won. Start a new game to play again | Game over. Start a new game to try again. | app.py|

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.
- ANSWER:
- Did not Accept: fixing check_guess by flipping the if/else statements I rejected the sugesstion because it caused a TypeError 
- Accepted: After seeing the TypeError it then gave a correct suggestion by wanting to see what logic_utils.py says again and then suggested to refactor the contents to logic_utils.py then change the if/else statement 


## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?
- ANSWER: I asked Claude to generate a pytest case in test_game_logic.py to make sure
- That I'm on the right direction, it generated guess_too_low, guesss_too_high 
- guess_below_secret_is_too_low, test_too_high_tells_player_to_go_lower() amongst others
- It helped me understand the tests because I used it to help walked me through the current output and why the starter tests neded to be changed.
- "The cause tests/test_game_logic.py:1: in <module> from logic_utils import check_guess
E   ModuleNotFoundError: No module named 'logic_utils' logic_utils.py sits in the project root, but the test file is in tests/. When you run plain pytest, Python only adds the tests/ folder to its import path, not the folder above it, so it can't see logic_utils. Fix options
Quick fix: run pytest through Python, which adds the current folder to the path: bash python -m pytest"
- I ran to see if the test is above the secret or below the secret if it would send the right answer of it saying Go Lower or Go Higher

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Streamlit re-runs your whole script on every interaction, and st.session_state is the only place that remembers anything between runs.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
- ANSWER: I didn't tell the agent to just do all of the work for me I asked it to give suggestions, and then I asked it for further hints if I was stuck in order to solve the problem for myself.
- Next time instead of trying to go through line by myself to understand it I would hoenstly just drop the code first in my agent to give a quick summary to save time. 
- It changed the way I think because you have to test your code to make sure it works, because when generated, at first glance it can look correct until you actually run it and there are actual bugs, so it's really important.
