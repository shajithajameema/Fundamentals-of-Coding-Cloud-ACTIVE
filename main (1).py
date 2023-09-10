def fact(n):
 if (n == 0):
   return 1
 else:
   return n*fact(n-1)
number=int(input("enter a number:"))
res=fact(number)
print("the factorial of {} is {}".format(number,res))