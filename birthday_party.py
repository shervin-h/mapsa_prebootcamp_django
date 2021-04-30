'''
یک مهمونی تولد داریم که داخل اون سه نفر خیلی گرسنه هستن ( hungry )
 و دو نفر سیر سیر ( not_hungry ) ،
  اخری هم اصلا معمولی نه گرسنه نه سیر  ( ok )،
   چطور صاحب مهمونی کیک رو به حالتی تقسیم کنه که هر شیش نفر به یک اندازه سیر بشوند

hungry = 4 * not_hungry
hungry = 2 * ok
ok = 2 * not_hungry
4 * not_hungry = 2 * ok => not _hungry = 0.5 ok
راهنمایی :
خروجی یک دیکشنری از درصد ها خواهد بود که جمعشون 100 میشه
'''

number_of_hungry_people = [4 * ('not_hungry',)] * 3                 # ['hungry'] * 3
number_of_not_hungry_people = [('not_hungry',)] * 2                 # ['not hungry'] * 2 => 0.5 ok * 2 = ok
number_of_ok_people = [2 * ('not_hungry',)] * 1

total = number_of_hungry_people + number_of_not_hungry_people + number_of_ok_people
# print(total)

s = 0
for person in total:
    for i in person:
        if i == 'not_hungry':
            s += 1

d = dict()
i = 1
for person in total:
    hunger_rate = person.count('not_hungry')
    if hunger_rate == 4:
        d[f'person {i}th is hungry'] = (hunger_rate / s) * 100
    elif hunger_rate == 2:
        d[f'person {i}th is ok'] = (hunger_rate / s) * 100
    else:
        d[f'person {i}th is not_hungry'] = (hunger_rate / s) * 100
    i += 1


print(d)

# by Shervin Hasanzadeh
