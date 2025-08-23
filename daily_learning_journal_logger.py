"""                                                                                                                                             
 Challenge: Daily Learning Journal Logger                                                                                                       
                                                                                                                                                
Build a Python script that allows you to maintain a daily learning journal. Each entry will be saved into a `.txt` file along with a timestamp. 
                                                                                                                                                
Your program should:                                                                                                                            
1. Ask the user what they learned today.                                                                                                        
2. Add the entry to a file called `learning_journal.txt`.                                                                                       
3. Each entry should include the date and time it was written.                                                                                  
4. The journal should **append** new entries rather than overwrite.                                                                             
                                                                                                                                                
Bonus:                                                                                                                                          
- Add an rating (1-5) for how productive the day was.                                                                                  
- Show a confirmation message after saving the entry.                                                                                           
- Make sure the format is clean and easy to read when opening the file.                                                                         
                                                                                                                                                
Example:                                                                                                                                        
📅 2025-06-14 — 10:45 AM                                                                                                                        
Today I learned about how list comprehensions work in Python!                                                                                   
Productivity Rating: 4/5                                                                                                                        
"""

from datetime import datetime
import textwrap

class userInputException(Exception):
    pass

try: 
    user_input = input("❓Enter what you have learned today: ").strip()
    if user_input == "":
        raise userInputException
    rating = int(input("⭐Today's Productivity rating (1-5) according to you: ").strip())
    if not 1 <= rating <=5 : 
        raise ValueError
    time = datetime.now()
    timestamp = f"📅 {time.strftime('%A, %d %B %Y, %I:%M %p')}"

    final_draft = f"\n{timestamp}\n\n{textwrap.fill(user_input,50)}\n\nProductivity Rating: {rating}/5\n\n{'-'*50}\n"

    with open("learning_journal.txt" , "a" , encoding="UTF-8") as file:
        file.write(final_draft)
        print("Your Entry is saved in file !!")

except ValueError:
    print("Error: Enter valid rating only !!")

except userInputException:
    print("Error: Empty task not allowed enter something like 'None' !!")

