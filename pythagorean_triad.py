n = int(input())

# a = b = c = 0
# for i in range(1, n + 1):
#     for j in range(i, n + 1):
#         for k in range(j, n + 1):
#             if k*k == i*i + j*j and i+j+k == n:
#                 a, b, c = i, j, k
#                 break
#             elif i*i == j*j + k*k and i+j+k == n:
#                 a, b, c = i, j, k
#                 break
#             elif j*j == i*i + k*k and i+j+k == n:
#                 a, b, c = i, j, k
#                 break
#
# if a != 0:
#     print(a, b, c)
# else:
#     print('Impossible')


a, b, c, m = 0, 0, 0, 2
l = list()
while c < n:
    for i in range(1, m):
        a = m * m - i * i
        b = 2 * m * i
        c = m * m + i * i

        if c > n:
            break
        if a + b + c == n:
            l.extend([a, b, c])
            break
    m = m+1

if not l:
    print('Impossible')
else:
    l.sort()
    print(l[0], l[1], l[2])
