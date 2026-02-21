def fibonacciSeries (n):
    # if(n == 0): return 0;
    # if(n == 1): return 1;
    if(n==1 or n==0): return n;
    return fibonacciSeries(n-2)+fibonacciSeries(n-1);
