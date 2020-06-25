#Weight converter and narrowing the variable L and K to only two options per unit, in this case we can use the 
#if / elif / else to avoid unit =! than the expected "L/l or K/k" letters
weight = float(input("Enter your weight"))
unit=input("Kilos(k) or Lbs(L)")
if unit=="L" or unit=="l":
    converted_weight=weight*0.453592
    unit_string="Kg(K)"
    print("Your weight is ",converted_weight,"",unit_string )
elif unit=="k" or unit=="K":
    converted_weight=weight*2.204620
    unit_string="Lbs(L)"
    print("Your weight is",converted_weight,"",unit_string )
else:
    print("ERROR: You must enter your unit using K/k or L/l")
