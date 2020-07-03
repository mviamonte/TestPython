numbers=[5,1,5,1,5] #List of iteration, we can just multiply the element of the list using * x. This is the fanciest way to do it. 
for i in numbers: # first loop defined by the value of the list
  output="" #clearing the variable "output" for the second loop
  for j in range(i):# times the second loop occurs and how many "x" will be added to the variable. 
    output+="x"
  print(output)
