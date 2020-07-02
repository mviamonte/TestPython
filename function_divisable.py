## Program with a function that detects numbers divisible by X
def divisible (num, by_div): #need to define the function using the parameters
    """This function define if a number
    is divisible by X number
    user needs to provide
    num = the number to determine if it's divisible
    by_div= the number to divide
    """
    if num %by_div == 0: #Using the % provides if a division shows a remain
        print(f"The number {num} is divisible by {by_div}")
    else:
        print(f"The number {num} isn't divisible by {by_div}")
divisible(20,2)
