fib = [0,1]

for i in range(2, 25+1):
    fib.append(fib[i-1] + fib[i-2])

n = int(input())
print(fib[n])
