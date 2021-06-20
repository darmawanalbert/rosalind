a, b = map(int, input().split())
total = sum([i for i in range(a, b+1) if i % 2 == 1])

print(total)
