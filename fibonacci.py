nvalue= int(input("How many terms? "))
n1, n2 = 0, 1
count = 0
if nvalue <= 0:
   print("Please enter a bigger integer")
elif nvalue == 1:
   print("Fibonacci sequence upto",nvalue)
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < nvalue:
       print(n1)
       num = n1 + n2
       n1 = n2
       n2 = num
       count += 1