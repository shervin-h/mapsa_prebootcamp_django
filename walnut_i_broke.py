measures = input()
measures = measures.strip()
measures = measures.split(' ')

n = int(measures[0])
x = int(measures[1])
y = int(measures[2])


if n % x == 0:
    print(int(n/x), 0)
elif n % y == 0:
    print(int(n/y), 0)
else:
    temp = n % x
    if temp % y == 0:
        print(int(n/x), int(temp/y))
    else:
        print(-1)

# by Shervin Hasanzadeh
