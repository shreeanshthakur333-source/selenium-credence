def fib(n):
    a,b=0,1
    for i in range(n):
      print(a, end=" ")
      a,b= b,b+a
fib(5)