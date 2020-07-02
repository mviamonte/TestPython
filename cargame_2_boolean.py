command = "" #Empty variable
started=False
while True: #Programs always runs, the condition are met in the next block of code
  command = input("> ").lower() # input using a "fake" prompt and forcing to be lowercase
  if command == "start":
    if started == False:
      print ("Car started")
      started == True
    else:
      print ("Car already started")
  elif command == "stop":
    if started == False:
      print ("Car stopped")
    else:
      print ("Car already stopped")
  elif command == "help":
    print ("""
start --- For start the car
stop --- For stop the car
quit --- For quit the game""")
  elif command == "quit":
    print("The game has been terminated")
    break
  else:
    print ("Sorry i don't understand")
