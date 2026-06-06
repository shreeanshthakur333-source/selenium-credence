def fib(n):
    a,b=0,1
    for i in range(n):
      print(a, end=" ")
      a,b= b,b+a
fib(10)

#Added new line to test git pull request