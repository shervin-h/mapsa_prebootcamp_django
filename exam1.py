'''
1. فرض کنید که N تا ماژیک داریم که هرکدام از آن ها رنگی دارند که آن رنگ را با عدد نشان میدهیم .
 حالا مساله ایی که  ذهنمون رو مشغول کرده اینه که از کدوم رنگ کمترین تعداد ماژیک رو داریم.
 بهمون کمک کنید تا رنگ ماژیکی که تعدادش کمتر از همه است رو پیدا کنیم.
 همچنین اگر بیش از یک رنگ داشتیم که تعداد ماژیک‌هایش کمتر مساوی از بقیه بود، بین اون رنگ‌ها، آن رنگی را چاپ کنید که عددش از بقیه کمتر است.
# number of markers:
1 <= N <= 100
# color_range of markers:
1 <= m <= 1000
question :
3
1 1 2
answer : 2
question :
5
1 2 1 3 4
answer : 2
'''

n = input()
m = input().strip().split()

numbers = list()
for i in range(0, int(n)):
    numbers.append(int(m[i]))

# print(numbers)

numbers.sort()
for item in numbers:
    if numbers.count(item) < 2:
        print(item)
        break




### second way ###

# d = dict()
# for marker in numbers:
#     d[marker] = numbers.count(marker)
#
# # print(d)
#
# for k, v in d.items():
#     if v < 2:
#         print(k)
#         break


# by Shervin Hasanzadeh

