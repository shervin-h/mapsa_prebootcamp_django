# str_num = input("Please enter an integer (1≤n≤10^18): ")
str_num = input()
str_num = str_num.strip()


def single_num(n):
    num = 0
    if len(n) > 1:
        for i in n:
            num += int(i)
        return single_num(str(num))
    else:
        return int(n)


if str_num.isnumeric():
    print(single_num(str_num),end='')
else:
    print("Please enter correct number !!!")

# by Shervin Hasanzadeh
