input_user=input()
if input_user == "help" or input_user == start or input_user == stop or input_user ==quit:
  if input_user == help:
    print ('''
    command start --- Start for start the car
    command stop --- Stop for stop the car
    command quit --- Quit to exit''')
  if input_user == start:
    print ("Car started, ready to go")
else:
  print("I don't understand the command")
