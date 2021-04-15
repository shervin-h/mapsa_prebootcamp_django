n = input()
n = n.strip()

d = dict()
sum = 0
for i in range(1, int(n)+1):
    d[i] = list()
    for j in range(1, i+1):
        if i % j == 0:
            d[i].append(j)
            sum += j


print(len(d), sum)

# by Shervin Hasanzadeh
