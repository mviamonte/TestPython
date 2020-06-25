#List the index and the elements of a list. Not sure how the enumerate works...Still need to have both counters, including the i even if
#did not need the i to print it 
squares=['red', 'yellow', 'green', 'purple', 'blue']
for i, square in enumerate(squares):
    print(i, square)


# Write your code below and press Shift+Enter to execute
Genres=[ 'rock', 'R&B', 'Soundtrack', 'R&B', 'soul', 'pop']
for i,genre in enumerate(Genres):
    print(Genres[i])

# Write your code below and press Shift+Enter to execute
Genres=[ 'rock', 'R&B', 'Soundtrack', 'R&B', 'soul', 'pop']
for genre in enumerate(Genres):
    print(genre)
(0, 'rock')
(1, 'R&B')
(2, 'Soundtrack')
(3, 'R&B')
(4, 'soul')
(5, 'pop')

#Simpliest yet effective way to do it. Basically, the i counter takes every element of the "Genres" list to iterate
#Then it print the counter with every value
Genres=[ 'rock', 'R&B', 'Soundtrack', 'R&B', 'soul', 'pop']
for i in Genres:
    print(i)
