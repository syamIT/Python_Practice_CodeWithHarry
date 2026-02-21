# fibonacci Series

# 0 1 1 2 3 5 8 13 21
'''
fib(0) = 0
fib(1) = 1
fib(2) = fib(0) + fib(1)

'''
print ("============= Fibonacci Series : ===============");
def fibonacciSeries (n):
    # if(n == 0): return 0;
    # if(n == 1): return 1;
    if(n==1 or n==0): return n;
    return fibonacciSeries(n-2)+fibonacciSeries(n-1);


n = int(input())
ranged = n+1
for i in range(ranged):
    print(fibonacciSeries(i), end=' ');
print("\n")
print(fibonacciSeries(n), end=' ');