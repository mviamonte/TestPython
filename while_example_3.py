#Write a while loop to copy the strings 'orange' of the list squares to the list new_squares. Stop and exit the loop if the value on the list is not 'orange':
squares = ['orange', 'orange', 'purple', 'blue ', 'orange']
new_squares = [] # The list has been defined by the empty [] brackets
i=0
while squares[i] == 'orange':
    new_squares.append(squares[i]) # The way to add the values to the new list is using the append function
    i=i+1
print(new_squares)