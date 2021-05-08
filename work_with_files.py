"""
یک فانکشن داریم که از کاربر نام دوتا فایل رو دریافت میکند.
در هر فایلی که کاربر نام آن را به ما میدهد یک دیکشنری داریم.
در فایل اول دیکشنری ما به این صورت است که :
Name : ID

و در فایل دوم دیکشنری ما این شکلی است :
ID : Color

در خروجی از شما فایلی میخواهیم که دیکشنری درون آن به این صورت باشد :
Name : Color

اگر ID اسم در فایل اول با ID رنگ در فایل دوم برابر باشد.

به مثال زیر توجه کنید :

First_File :
Dara : 1
Sara : 2

Second_File :
1 : Blue
2 : Red

Output_File :
Dara : Blue
Sara : Red
"""


def func(file1: str, file2: str):
    f_1 = open(file1, mode='r', encoding='UTF-8')
    f_2 = open(file2, mode='r', encoding='UTF-8')

    f1 = eval(f_1.read())
    f2 = eval(f_2.read())

    d = dict()
    for person in f1.keys():
        for id in f2.keys():
            if f1[person] == id:
                d[person] = f2[id]
                break

    f_1.close()
    f_2.close()

    new_file = open('new_file.txt', 'w', encoding='UTF-8')
    new_file.write(str(d))
    new_file.close()


func('file_1.json', 'file_2.json')

#by Shervin Hasanzadeh
