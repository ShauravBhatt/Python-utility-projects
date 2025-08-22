"""
 Challenge: Self-Intro Script Generator

Create a Python script that interacts with the user and generates a personalized self-introduction.

Your program should:
1. Ask the user for their name, age, city, profession, and favorite hobby.
2. Format this data into a warm, friendly paragraph of self-introduction.
3. Print the final paragraph in a clean and readable format.

Example:
If the user inputs:
  Name: Priya
  Age: 22
  City: Jaipur
  Profession: Software Developer
  Hobby: playing guitar

Your script might output:
  "Hello! My name is Priya. I'm 22 years old and live in Jaipur. I work as a Software Developer and
   I absolutely enjoy playing guitar in my free time. Nice to meet you!"

Bonus:
- Add the current date to the end of the paragraph like: "Logged on: 2025-06-14"
- Wrap the printed message with a decorative border of stars (*)
"""

import datetime

try:
    name = input("Enter your name: ").strip().title()
    age_input = input("Enter your age: ")
    if not age_input.isdigit():
        raise ValueError("Age should be in integer !!") 
    age = int(age_input)
    city = input("Enter your city: ").strip().capitalize()
    profession = input("Enter your profession: ").strip().capitalize()
    hobby = input("Enter your favourite hobby: ").strip().capitalize()

    if name == "" or city == "" or profession == "" or hobby == "":
        raise ValueError("Empty values are not allowed.")

except ValueError as ve :
    print(f"Unexpected Error: {ve}\nPlease try again with correct inputs !!")

except Exception as e:
    print(f"Unexpected Error: {e}\nPlease try fixing error !!")

else:
    intro_message = (
        f"Hello! My name is {name}. "
        f"I'm {age} years old and live in {city}. " 
        f"I work as a {profession} and\n"
        f"I absolutely enjoy {hobby} in my free time. Nice to meet you!\n"
    )
    
    date = datetime.date.today().isoformat()
    border = "*"*95

    intro_message += f"\nLogged In: {date}"

    final_intro = f"{border}\n\n{intro_message}\n\n{border}"

    print(final_intro)

