n = int(input("put number , n ="))

fib_list = []
for i in range (n):
    if (i ==0 or i ==1):
        fib_list.append(1)
    else :
        fib_list.append(fib_list[i-1]+fib_list[i-2])

fib_list = list(map(str , fib_list))
show = ",".join(fib_list)
print(show)