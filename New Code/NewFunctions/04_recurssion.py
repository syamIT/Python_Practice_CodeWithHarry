# fibonacci series : 0 1 1 2 3 5 8 13 21 34 55 89 144 233 .....
def fibonacciSeries(n):
    # Basecase 
    if(n==0 or n==1):
        return n;
    else:
        return fibonacciSeries(n-1)+fibonacciSeries(n-2);

res = fibonacciSeries(13)
print(res)