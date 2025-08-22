"""                                                                                                             
 Challenge: Emoji Enhancer for Messages                                                                         
                                                                                                                
Create a Python script that takes a message and adds emojis after specific keywords to make it more expressive. 
                                                                                                                
Your program should:                                                                                            
1. Ask the user to input a message.                                                                             
2. Add emojis after certain keywords (like "happy", "love", "code", "tea", etc.).                               
3. Print the updated message with emojis.                                                                       
                                                                                                                
Example:                                                                                                        
Input:                                                                                                          
  I love to code and drink tea when I'm happy.                                                                  
                                                                                                                
Output:                                                                                                         
  I love ❤️ to code 💻 and drink tea 🍵 when I'm happy 😊.                                                      
                                                                                                                
Bonus:                                                                                                          
- Make it case-insensitive (match "Happy" or "happy")                                                           
- Handle punctuation (like commas or periods right after keywords)                                              
                                                                                                                
"""          

import string

emoji_dict = {
    "happy": "😊",
    "love": "❤️",
    "code": "💻",
    "tea": "🍵",
    "coffee": "☕",
    "sad": "😢",
    "angry": "😠",
    "birthday": "🎉",
    "party": "🥳",
    "food": "🍽️",
    "sleep": "😴",
    "music": "🎶",
    "rain": "🌧️",
    "sun": "☀️",
    "star": "⭐",
    "fire": "🔥",
    "cool": "😎",
    "hello": "👋",
    "bye": "👋",
    "idea": "💡",
    "work": "🛠️",
    "book": "📚"
}

user_message = input("Enter your text message: ")

enhanced_message = ""

for str in user_message.split():
    word = str.strip(string.punctuation).lower()
    if word in emoji_dict.keys():
        enhanced_message += f" {str} {emoji_dict[word]} "
    else:
        enhanced_message += f" {str} "

print(enhanced_message.strip())

