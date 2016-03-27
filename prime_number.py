def is_primenum(number):
  if number == 2:
    return True
  
  for i in range(2,number):
    if number % i == 0:
      return False
  
  return True

def print_primenum(max_number):
    result = []

    for i in range(2,max_number):
        if is_primenum(i):
            result.append(i)
    
    print result

print_primenum(1000)