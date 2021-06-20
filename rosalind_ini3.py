s = input()
a, b, c, d = map(int, input().split())

print("{} {}".format(s[a:b+1], s[c:d+1]))
