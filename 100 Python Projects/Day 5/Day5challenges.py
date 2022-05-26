#challenge 1
# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
#student_heights = {190, 124, 165, 182, 148, 175, 180}


total_height = 0 
for height in student_heights:
  total_height += height
print(total_height)

number_of_students = 0
for height in student_heights:
  number_of_students += 1
print(number_of_students)

average_height = round(total_height / number_of_students)
print(average_height)



#Challenge 2 
# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score


print(f"The highest score in the class is: {highest_score}")

#Challenge 3
#adding up even numbers from 1 to 100 = 2550
#Write your code below this row 👇
number_total = 0
for number in range (2, 101, 2):
    number_total += number
print(number_total)

#Challenge 4 (Fizz Buzz)
#Write your code below this row 👇

for number in range (1, 101):
    if number % 3 == 0 and number % 5 == 0:
         print("FizzBuzz")
    elif number % 3 == 0:
        print ("Fizz")
    elif number % 5 == 0: 
        print ("Buzz")
    else:
        print (number)
