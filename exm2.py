m = 4
n = 6
l = []

count = 1

for i in range(m):
    for j in range(n):
        l.append(count)
        count += 1
    else:
        print(l)
        l.clear()
