print("Welcome to our theme park!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
  print("You can ride the rollercoaster! :D")
  age = int(input("What is your age? "))
  if age < 13:
      bill = 10
      print("It is $10 for a kids ticket")
  
  elif age <18:
      bill = 15
      print ("It is $15 for  a teen ticket")
  elif age >= 45 and age <= 99:
    print ("Ah, an experienced thrillseeker! Have a free ride on us :)")
  else:
      bill = 25
      print("It is $25 for an adults ticket")
  wants_photo = input("Do you want a photo taken? Type y for yes and n for no: ")
  if wants_photo == "y":
      bill += 3 #same as bill = bill + 3
    #Add $3 to price
  print (f"Your final bill is {bill}")
else:
    print("Sorry, you have to grow taller before you can ride this ride")