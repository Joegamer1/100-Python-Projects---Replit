import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆
num_items = len(names)
#Write your code below this line 👇
#print("There are" + {num_items} + "potential bill payers today")
#prints number of participants

random_choice = random.randint(0, num_items - 1)
person_who_will_pay = names[random_choice]
print (f"The person who needs to pay is person number {random_choice} today!")
print (person_who_will_pay + " is the lucky 'winner'!")