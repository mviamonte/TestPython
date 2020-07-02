"""Function Fizz Buzz.
Write a function called fizz_buzz that takes a number.
    If the number is divisible by 3, it should return “Fizz”.
    If it is divisible by 5, it should return “Buzz”.
    If it is divisible by both 3 and 5, it should return “FizzBuzz”.
    Otherwise, it should return the same number.
""" 
def fizzbuzz(num):
    if num  %3==0:
        if num %3 ==0 and num%5==0:
            return "FizzBuzz" 
        return "Fizz"
    elif num %5==0:
        return "Buzz"
    elif num %3 ==0 and num%5==0:
        return "FizzBuzz"
    else:
        return num
fizzbuzz(5)
