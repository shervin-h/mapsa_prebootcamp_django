degrees = input()
degrees = degrees.strip()
degrees = degrees.split(' ')


def sum_angles(degs):
    sum = 0
    for i in degs:
        if int(i) <= 0 or int(i) > 178:
            return False
        else:
            sum += int(i)

    if sum == 180:
        return True
    else:
        return False


if sum_angles(degrees):
    print("Yes")
else:
    print("No")

# by Shervin Hasanzadeh
