#Another while loop using the !0 as comparison operator
x=10
y=1
while(y!= x):
    print(y)
    y=y+1
#Write a while loop to display the values of the Rating of an album playlist stored in the list PlayListRatings. 
#If the score is less than 6, exit the loop. The list PlayListRatings is given by: PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]
PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]
i=0
while PlayListRatings[i] >6:
    print (PlayListRatings[i])
    i=i+1


#Another way to do it
<!-- 
PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]
i = 1
Rating = PlayListRatings[0]
while(Rating >= 6):
    print(Rating)
    Rating = PlayListRatings[i]
    i = i + 1