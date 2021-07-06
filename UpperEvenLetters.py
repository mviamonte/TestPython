def upper_string(input_string):
  new_string=""
  letter=input_string
  size = len(input_string)
  for counter in range (size):
    if counter %2 == 0:
      new_string = new_string+letter[counter].upper()
      #new_string.append(letter[counter].upper())
    else:
      new_string = new_string+letter[counter]
      #new_string.append(letter[counter])
  return new_string
result = upper_string("Floccinaucinihilipilification ")
print (result)
