###Guess game with three attempts
number = 40
counter = 1
guess = int(input ("Introduce a number:"))
if number !=guess:
  if counter !=3:
   guess = int(input ("Introduce another number:"))
   counter=counter+1
  else:
    print ("You ran out of attemtps") 
else:
  print (f"Y")
