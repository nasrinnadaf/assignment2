import math
student = int(input("tedad student ha :"))
b = []
for i in range (student ):
    score = float(input("write their score:"))
    b.append(score)

print("average", sum(b)/ student)
print ( " max class", max(b))
print(" min class", min(b))