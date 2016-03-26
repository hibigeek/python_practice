"""
これはｎ桁の数を探すゲームです。
適当な数を入れると桁も数字もあっていれば「Hit」としその個数が、
数字はあっているが桁が異なっていれば「Blow」としてその個数が出力されます。
それを繰り返すことで答えを探すことができます。このゲームを作成しなさい。
答えの数は乱数を使って毎回別の答えを用意しましょう。
具体的には
正解が1234だとして
4321　と入力　4blow
1245　と入力　2hit　1blow
なおルール上4422などのゾロ目の正解は出ないようにしましょう。
また、先頭が0だとn桁の数字じゃなくなるのでせっかくなので0は発生させないようにしましょう。
"""
import random

print "Hit & Blow"
a = []
digit = 0
while digit < 1:
  digit = int(raw_input("Choice play digit:  "))

r = random.randint(1, 9)
while len(a) != digit:
	 if r not in a:
		 a.append(r)
	 r = random.randint(1, 9)


guess = []
s = 0
while s != digit:
	 while len(guess) != digit:
		 x = int(raw_input("Input Your guess one by one:"))
		 if x not in guess:
			 guess.append(x)
			 print guess
		 else:
			 print "Can't input same number"

   
   #リストを集合型にして論理積をとる。そうすると、リストの中の重複したものがreturnされる。ただし順不同
   #a =[1,2,3,4] & b = [4,3,2,0] -> c [2,3,4]
	 c = set(a)
	 d = set(guess)
	 c &= d
	 s = 0

	 for i in range(digit):
		 if a[i] == guess[i]:
			 s += 1
	 print str(len(c) - s) + "Blow"
	 print str(s) + "Hit"
	 guess = []
print "You Win!"