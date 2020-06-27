#there is a list of 100 numbers and we want to print every element of the list until reach 237
numbers = [
    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
    615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
    743, 527
]
#print(len(numbers)) how to determine the amount of elements in the list
i=0 # define the start counter to index the list and go through the list
while (numbers[i] != 237): #Starting from the first element of the list and comparing with the 237. I need to use this way to use every elemnt of the list until reach 237, then stop
    print (f"We haven't reach 237 yet, the number is {numbers[i]} and it's the index {i} in the list")
    i=i+1
    
