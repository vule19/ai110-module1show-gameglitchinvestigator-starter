# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
The game is open as a web page. Then user can start type their guesses. After submit, the hint will tell if user should should make a higher or lower guess.
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
The hint were backward: instead of lower, it says to go lower. History does not append new guess after hitting submit.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
Claude
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
AI suggest when reset, it should reset to 0 instead of 1
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
I did not see any incorrection yet.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I rerun the code and test the wrong logic to verify it works this time.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
i manally verify the hint when input is lower or higher than the number
- Did AI help you design or understand any tests? How?
Yes

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
Every time the user interacts with the app (clicks a button, types in a box), Streamlit reruns the entire Python script from top to bottom
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Everytime click anything on a webpage, the whole page reloads
- What change did you make that finally gave the game a stable secret number?
Wrapping the random.randint() call in if "secret" not in st.session_state:

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
Writing pytest cases before trusting that a function works
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
Verify AI suggestions against the actual code before accepting them.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
AI-generated code looks polished and confident, but that surface quality can hide real logic errors. I now treat AI output as a first draft that needs the same skeptical review I'd give any other code.