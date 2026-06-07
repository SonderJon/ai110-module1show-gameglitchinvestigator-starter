# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input           | Expected Behavior | Actual Behavior | Console Output / Error |
|-----------------|-------------------|-----------------|------------------------|
| Guessed 25      | Hint "Go Higher"  | Hint "Go Lower" | N/A |
| Guessed -1      | Invalid range     | Hint "Go Lower" | N/A |
| Difficulty Hard | Range 1 to 50     | Range 1 to 100  | N/A |
| New Game        | Reset game state  | No new game     | "Start a new game" | 

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

Used Claude Code to refactor logical functions out of app.py and into logic_utils.py and to create test cases in test_game_logic.py
Correct: told Claude to fix the reversed hint bug. It suggested swapping the returns so that it correctly shows if the guess is high or low. It worked and I verified my relaunching app.py and manually checking different guesses
Wrong: told Claude to fix the wrong difficulty range bug. It correctly assigned the low, high variables with the correct ranges, but didn't update other occurances where the function was used again.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

A bug was fixed if the previously documented error no longer appeared throughout multiple tests
One test I ran manually was changing the difficulty and pressing new game to see if the ranges and secret value correctly changed
AI designed the unit tests to quickly test if functions performed as expected

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
