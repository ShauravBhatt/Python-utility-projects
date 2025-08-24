"""                                                                                       
Challenge: Set a Countdown Timer                                                          
                                                                                          
Create a Python script that allows the user to set a timer in seconds. The script should: 
                                                                                          
1. Ask the user for the number of seconds to set the timer.                               
2. Show a live countdown in the terminal.                                                 
3. Notify the user when the timer ends with a final message.      
                                                                                          
Bonus:                                                                                    
- Format the remaining time as MM:SS                                                    
- Prevent negative or non-integer inputs                                                  
"""                                                                                       

import time 

while True:
    try:
        seconds = int(input("⏰ Enter the time in second: "))
        if seconds < 1:
            print("Please enter a positive number !!")
            continue
        break

    except ValueError:
        print("Invalid input please enter valid number !!")

print("\n⏳ Timer started...\n")

for remaining in range(seconds , 0 , -1):
    mins , secs = divmod(remaining,60)
    time_format = f"{mins:02}:{secs:02}"
    print(f"⌛ Time left: {time_format}" , end="\r")
    time.sleep(1)

print("\n\n🔔 Time's up !!!")
    
