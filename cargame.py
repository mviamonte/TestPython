command = "" #Empty variable
while command !="quit": #Programs runs while the quit command is not called
  command = input("> ").lower()
  if command == "start":
    print ("Car started")
  elif command == "stop":
    print ("Car stopped")
  elif command == "help":
    print ("""
start --- For start the car
stop --- For stop the car
quit --- For quit the game""")
else:
  print("The game has been terminated") 
