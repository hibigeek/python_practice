def is_leapyear(year):
  if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    return True
  else:
    return False

def print_leapyear(maxnum):
  for i in range(1,maxnum+1):
    if is_leapyear(i):
      print i


print_leapyear(2016)