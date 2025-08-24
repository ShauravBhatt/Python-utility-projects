"""                                                                    
Challenge: Password Strength Checker & Suggestion Tool                
                                                                       
Build a Python script that checks the strength of a password based on: 
1. Length (at least 8 characters)                                      
2. At least one uppercase letter                                       
3. At least one lowercase letter                                       
4. At least one digit                                                  
5. At least one special character (e.g., @, #, $, etc.)                
                                                                       
Your program should:                                                   
- Ask the user to input a password.                                    
- Tell them what's missing if it's weak.                               
- If the password is strong, confirm it.                               
- Suggest a strong random password if the input is weak.               
                                                                       
Bonus:                                                                 
- Hide password input using `getpass` (no echo on screen).             
"""                                                                    

import random
import string
import getpass

def check_password_strength(password):
    issues = []
 
    if len(password) < 8:
        issues.append("Password too short (min 8 characters)")

    if not any(c.islower() for c in password):
        issues.append("Add at least one lowercase letter")

    if not any(c.isupper() for c in password):
        issues.append("Add at least one uppercase letter")

    if not any(c.isdigit() for c in password):
        issues.append("Add at least one digit")

    if not any(c in string.punctuation for c in password):
        issues.append("Add at least one special character")

    return issues

def generate_strong_password(length=12):
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]

    chars = string.ascii_letters + string.digits + string.punctuation

    password += (random.choice(chars) for _ in range(length-4))

    random.shuffle(password)

    return "".join(password)


password = getpass.getpass("Enter the password (Note: It isn't visible to you) : ")

issues = check_password_strength(password)

if not issues :
    print("\nStrong Password , you're good to go !!")

else:
    print("\nWeak Password, apply following suggestions: ")
    for issue in issues:
        print(f"- {issue}")
    print()

    suggestion = generate_strong_password()
    print("Suggesting you a strong password: ", end="")
    print(suggestion)

