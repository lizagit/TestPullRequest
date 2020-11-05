def RecursionFibonacci(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))
      
def IterativeFibonacci(n):
    f1, f2 = 0, 1
    for i in range(n):
        f1, f2 = f2, f1 + f2
    return f1+f2

print(IterativeFibonacci(4))
nterms = 10
if nterms <= 0:
    print("Please enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(RecursionFibonacci(i))      
