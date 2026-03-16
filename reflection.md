# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

When I first ran the game I guessed 80 for the secret, and the hint told me to go lower, I guessed 40 and even guessed down to 1, and it still told me to go lower a secret. In my next try, I guessed 60, it told me to go higher, then lower after my next guess, and no matter how times I guessed with binary search it seemed like I could not get the exact number. So after addressing this initial problem with the randomization of the secret number, another broken part of the code was how the hard mode was much easier than the normal mode and also how the new game functionality did not work well,  that is when I clicked the new game button, it would not start a new game.

---

## 2. How did you use AI as a teammate?

- For this, I used Claude code agent (Sonnet 4.6 on high thinking). All of the AI suggestions were very correct, I would say, mostly because I followed best practices such as being very precise in my prompts,  attaching the relevant files and limiting the scope to one specific task at time. In addition, I also used a custom mode, which I made "/discuss", where I would go back and forth with the AI to ensure that it had enough context at hand before allowing it to then implement or suggest code for me.

- However, one of the suggestions which I did not appreciate was when I asked the AI to help me write and fix some of the tests, and it's suggestions included an unnecessary variable name change

- Overall, I verified AI's results by running the program and observed its functionality compared to before the changes.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

- For most of the bugs, I decided the fix was real when I ran the game myself saw it behave correctly, for example guessing a number higher than the secret and the hint going "Go LOWER!" . I also ran pytest, which collected 6 tests total, and while the 3 new tests I wrote with the AI passed immediately, the 3 original starter tests were failing because they were comparing the full tuple return value of check_guess against a plain string, which was a pre-existing issue in the starter code and not something my fixes broke. The AI helped me design the two new tests for the swapped hints bug and the type-flip bug, and I would say it was useful here because I described what I expected versus what happened and it translated that directly into assert statements, which is a pattern I want to keep using.



---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- The way I would explain Streamlit to a friend is that every time you click a button or type something, Streamlit re-runs your entire Python script from top to bottom. Now state is sort of like a dictionary that streamlink uses to store values. So each time we "re-ran", The Streamlit program would store this value in the dictionary, basically saving it from being erased when we reran.
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

- The one habit that I will take from this, and it's something I've been thinking about a lot since I started coding with Agents some months back, is to apply sort of test-driven development. I will discuss with AI and come out with really robust tests that would help to ensure that whatever code the AI generates is right, especially during moments when I may fail to catch some errors in the code, especially edge cases.
- Something I think I would do when working with AI next time is to sort of treat it as a really smart lookup, and pair-programmer and focus more on actually writing the code myself. I think I would use AI for things like large code refactors.
- I had once tried to vibe code an entire application, and long story short, it was absolute slop. Working with this project showed me that AI-generated code or AI pair programming can actually be really good, provided I keep the scope really specific and minimal, staying precise in my task prompts, and being actively involved in the entire coding process, understanding every line of code that AI generates and going back and forth with the AI.