# coding: utf-8
#ゾロ目判定 numberには任意の整数
def is_repdigit(number):
    if all(y == str(number)[0] for y in str(number)[1:]):
        return True
    else:
        return False