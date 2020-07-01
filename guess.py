##Guess game with three attempts
secret_number = 10 # The secret number has to be defined
counter = 0 #Counter startint point
counter_limit=3 # The limit of the counter
while counter < counter_limit: # The conditions of maximum three attempts
    guess = int(input ("Introduce a number:"))
    counter = counter + 1
    if secret_number == guess:
      print (f"You guess, the number is {secret_number}")
      break
else: #The else condition to show user the lack of attemtps
  print ("You ran out of attempts")
