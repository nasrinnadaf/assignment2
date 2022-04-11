import math
second = int(input("put your number? "))

clock = second // 3600
minute = second % 60
second = minute - clock 
print (clock , (":"), minute , (":") , second , ("sanie ")) 