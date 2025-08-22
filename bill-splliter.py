"""
 Challenge: Simple Bill Splitter

Write a Python script that helps split a bill evenly between friends.

Your program should:
1. Ask how many people are in the group.
2. Ask for each person's name.
3. Ask for the total bill amount.
4. Calculate each person's share of the bill.
5. Display how much each person owes in a clean, readable format.

Example:
Total bill: ₹1200  
People: Aman, Neha, Ravi

Each person owes: ₹400

Final output:
  Aman owes ₹400  
  Neha owes ₹400  
  Ravi owes ₹400

Bonus:
- Round to 2 decimal places
- Print a decorative summary box
"""

total_people = int(input("\nHow many people in the group: "))

friends_group = []

print("")

for i in range(total_people):
    name = input(f"Person {i+1} name : ").strip()
    if name == "":
        raise Exception("Name shouldn't be empty !!")
    friends_group.append(name)

def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number !!")


total_bill = get_float("\nEnter the total bill amount: ")

per_person_amount = round(total_bill/total_people , 2)

print(f"\nEach person owes: {per_person_amount}\n")

print("*" * 30)

for name in friends_group:
    print(f"{name.capitalize()} owes {per_person_amount} rupees.")

print("*" * 30)
