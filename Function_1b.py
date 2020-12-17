def fibo(n):
   k=0
   while k<=n:
       if n <= 1:
       	return n
       else:
           return(n+(n-1))
        k=k+1
    

x = input("Enter number of terms:")
y = int(x)
if y <= 0:
   print("Wrong input.")
else:
   print("Fibonacci series:")
   for i in range(y):
       print(fibo(i))