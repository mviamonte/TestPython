def pick_evens(*args):
  even_list=[]
  for number in args:
    if number %2 ==0:
      even_list.append(number)
    else:
      continue
  return even_list
list_of_even = pick_evens(100,3,4,5,6,7,8,9,34,56)
print (list_of_even)
