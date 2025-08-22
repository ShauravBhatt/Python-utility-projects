
"""                                                                                                                
Challenge: Minutes Alive Calculator                                                                               
                                                                                                                   
Write a Python script that calculates approximately how many minutes old a person is, based on their age in years. 
                                                                                                                   
Your program should:                                                                                               
1. Ask the user for their age in years (accept float values too).                                                  
2. Convert that age into:                                                                                          
   - Total days                                                                                                    
   - Total hours                                                                                                   
   - Total minutes                                                                                                 
3. Display the result in a readable format.                                                                        
                                                                                                                   
Assumptions:                                                                                                       
- You can use 365.25 days/year to account for leap years.                                                          
- You don't need to handle time zones or exact birthdates in this version.                                         
                                                                                                                   
Example:                                                                                                           
Input:                                                                                                             
  Age: 25                                                                                                          
                                                                                                                   
Output:                                                                                                            
  You are approximately:                                                                                           
    - 9,131 days old                                                                                               
    - 219,144 hours old                                                                                            
    - 13,148,640 minutes old                                                                                       
                                                                                                                   
Bonus:                                                                                                             
- Add comma formatting for large numbers                                                                           
- Let the user try again without restarting the program                                                            
"""                                                                                                                

def calculate_minutes(age):
    days_in_year = 365.25
    hours_in_day = 24
    minutes_in_hour = 60

    total_days = age * days_in_year
    total_hours = total_days * hours_in_day
    total_minutes = total_hours * minutes_in_hour

    return round(total_days) , round(total_hours) , round(total_minutes)


while True:
    try:
        age = float(input("\nEnter your age in years: "))
        days , hours , minutes = calculate_minutes(age)

        print("You are approaximately: ")
        print(f"\t- {days:,} days old.")
        print(f"\t- {hours:,} hours old.")
        print(f"\t- {minutes:,} minutes old.\n")

        again = input("would you like try to again (y/n) : ").strip().lower()
        
        if again not in  ['y', 'yes', '']:
            print("Good Bye !!")
            break
        
    except:
        print("Please enter a valid age !!") 
