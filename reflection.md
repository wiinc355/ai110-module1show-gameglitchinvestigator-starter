# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
When I first ran the game, it looked very basic and not very engaging for the user. The interface was plain and did not have anything that really grabbed the player’s attention or made them want to keep playing. It felt more like a simple prototype than a finished game. Because of this, the overall experience did not spark much interest
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
 I noticed a couple of clear bugs at the start. First, the scoring results were not accurate and did not always reflect what happened during gameplay. Second, the New Game button did not properly reset the game. In order to start a new game, I had to refresh the browser manually, which should not be necessary for normal gameplay.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
I used Copilot as my teammate for this project. I used it to help me debug game-state issues, explain why Streamlit reruns were affecting behavior, and suggest small testable code changes. I treated AI as a guide, not an autopilot, so I still validated each suggestion myself. That approach helped me move faster while still understanding what changed.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
One AI suggestion that was correct was to implement and test the guess-comparison logic in `logic_utils.py` and add a regression test for hint direction. Copilot suggested asserting that a high guess returns `Too High` and a hint containing `LOWER`, which directly targets the reversed-hint bug. This suggestion was correct because once I implemented the function and added the test, `pytest` passed and the game logic matched expected behavior. I verified it by running the test suite and confirming `4 passed`, including the new regression test.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
One AI suggestion that was incorrect/misleading was earlier logic around hint behavior that could point in the wrong direction (for example, returning a “go higher” style hint when the guess was already too high). It looked plausible at first, but it conflicted with actual gameplay expectations. I verified it was misleading by manually testing high/low guesses in the app and by writing a targeted regression test that checks for `LOWER` on high guesses. That test-driven check exposed the mismatch and confirmed the original suggestion needed correction.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I decided a bug was really fixed only after I could reproduce it first and then make it stop happening consistently. For example, I tested the New Game flow multiple times in a row because it had been unreliable before. I also checked that related behavior still worked, like attempts, score, and status updating correctly after reset. If it worked once but failed on another rerun, I treated it as not fixed yet.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
I ran manual tests by entering high, low, and correct guesses to confirm the game feedback matched the guess result. I also used the existing pytest tests for guess logic to check expected outcomes like win, too high, and too low. That showed me core comparison logic was mostly fine, but integration behavior in the Streamlit app still needed attention. In other words, passing a simple test did not guarantee the full user flow was correct.
After implementing the repair and adding a regression test for hint direction, I reran `pytest` and confirmed all tests passed (`4 passed`).
- Did AI help you design or understand any tests? How?
Yes, AI helped me think in terms of test cases instead of just random clicking. Copilot suggested checking both valid and edge cases, like resetting mid-game and handling repeated reruns. It also helped me separate logic tests from UI behavior tests, which made debugging less confusing. That guidance made my testing more intentional and helped me catch issues earlier.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
I would explain Streamlit reruns as the app script running again from top to bottom every time a user interacts with a widget. At first that felt confusing, because it looked like values were randomly changing, but really the script was just restarting each interaction. Session state is what keeps important values (like score, attempts, and secret number) from resetting on every rerun. Once I understood that, debugging became easier because I could track exactly what should persist versus what should be recalculated.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
One habit I want to reuse is writing down a quick test checklist before making changes. In this project, I learned that testing only the “happy path” is not enough, so I now include edge cases like reset behavior and repeated interactions. I also want to keep using focused prompts for AI, where I ask it to explain why a fix works instead of only giving code. That made my debugging process faster and helped me understand the logic better.
- What is one thing you would do differently next time you work with AI on a coding task?
Next time, I would verify AI suggestions in smaller steps instead of applying bigger chunks all at once. When I tested each change immediately, it was much easier to isolate what caused a new issue. I would also ask AI to suggest test cases first, then code changes second. That order would probably reduce rework and make my fixes more reliable.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
This project showed me that AI-generated code can speed up debugging, but it still needs human review and testing to be trustworthy. I now see AI as a helpful collaborator, not an autopilot.
