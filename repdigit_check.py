# coding: utf-8
#ゾロ目判定 numberには任意の整数
def is_repdigit(number):
  if all(y == str(number)[0] for y in str(number)[1:]):
      return True
  else:
      return False

def has_repdigit(number):
    repdigits = ["00","11","22","33","44","55","66","77","88","99"]

    for repdigit in repdigits:
      if repdigit in str(number):
        return True
  
    return False

has_repdigit(111111111111111)