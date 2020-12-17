def fibo(n):
   if n <= 1:
       return n
   else:
       return(fibo(n-1) + fibo(n-2))

x = input("Enter number of terms:")
y = int(x)
if y <= 0:
   print("Wrong input.")
else:
   print("Fibonacci series:")
   for i in range(y):
       print(fibo(i))