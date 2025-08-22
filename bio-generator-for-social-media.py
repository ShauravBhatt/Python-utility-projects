"""                                                                                                                                                                         
Challenge: Stylish Bio Generator for Instagram/Twitter                                                                                                                      

Create a Python utility that asks the user for a few key details and generates a short, stylish bio that could be used for social media profiles like Instagram or Twitter. 

Your program should:                                                                                                                                                        
1. Prompt the user to enter their:                                                                                                                                          
   - Name                                                                                                                                                                   
   - Profession                                                                                                                                                             
   - One-liner passion or goal                                                                                                                                              
   - Favorite emoji (optional)                                                                                                                                              
   - Website or handle (optional)                                                                                                                                           

2. Generate a stylish 2-3 line bio using the inputs. It should feel modern, concise, and catchy.                                                                            

3. Add optional hashtags or emojis for flair.                                                                                                                               

Example:                                                                                                                                                                    
Input:                                                                                                                                                                      
  Name: Riya                                                                                                                                                                
  Profession: Designer                                                                                                                                                      
  Passion: Making things beautiful                                                                                                                                          
  Emoji: 🎨                                                                                                                                                                 
  Website: @riya.design                                                                                                                                                     

Output:                                                                                                                                                                     
  🎨 Riya | Designer                                                                                                                                                        
  💡 Making things beautiful                                                                                                                                                
  🔗 @riya.design                                                                                                                                                           

Bonus:                                                                                                                                                                      
- Let the user pick from 2-3 different layout styles.                                                                                                                       
- Ask the user if they want to save the result into a `.txt` file.                                                                                                          
"""
import textwrap

name = input("Enter your name: ").strip().title()
profession = input("Enter your profession: ").strip().capitalize()
passion = input("Enter your passion or goal in one-liner: ").strip().capitalize()
emoji = input("Favorite Emoji (optional): ").strip()
website = input("Enter your website or handle (optional): ").strip()

print("\nChoose your style:")
print("\t1. Simple Lines")
print("\t2. Vertical Flair")
print("\t3. Emoji Sandwich (Your emoji is mandatory!)")

style = int(input("\nEnter 1, 2 or 3: ").strip())

def generate_bio(name, profession, passion, emoji, website, style):
    if style == 1:
        bio = f"{emoji} {name} | {profession}\n~ {passion}"
        if website:
            bio += f"\n~ {website}"
        return bio

    elif style == 2:
        bio = f"{emoji} {name} | {profession}\n💡 {passion}"
        if website:
            bio += f"\n🔗 {website}"
        return bio

    elif style == 3:
        if not emoji:
            return "❗ Style 3 requires an emoji! Please run again."
        bio = f"{emoji * 3}\n{name} | {profession}\n{passion}"
        if website:
            bio += f"\n{website}"
        bio += f"\n{emoji * 3}"
        return bio

    else:
        return "❗ Invalid style selected. Please choose 1, 2, or 3."

result = generate_bio(name, profession, passion, emoji, website, style)

print("\n" + "*" * 50)
print(result)
print("*" * 50)

save = input("Do you want to save the bio to a file? (y/n): ").strip().lower()
if save in ['y', 'yes', '']:
    filename = f"{name.lower().replace(' ', '_')}_bio.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(result)
    print(f"✅ Bio saved to '{filename}'")
else:
    print("👍 Thanks for using the Bio Generator!")

