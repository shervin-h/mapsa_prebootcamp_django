'''
yesterday, David and John went bank robbery and managed to steal bank's vault.
At home they want to know type of things in the vault.
help them do the job fast, so they don't get caught by police.

input:
( "gold", 1000, ("navid check", 3542),["neda watch",500],{"sanad khone" :"felan ja"}, {"name" :"navid", "pass" :"qwerty 1234"} )

and the output is
{str : 1,dict:2,list:1,tuple:1,set:0,}
'''

items = eval(input())

d = {str: 0, dict: 0, list: 0, tuple: 0, set: 0, int: 0}
for item in items:
    if type(item) == str:
        d[str] += 1
    elif type(item) == dict:
        d[dict] += 1
    elif type(item) == list:
        d[list] += 1
    elif type(item) == tuple:
        d[tuple] += 1
    elif type(item) == set:
        d[set] += 1
    elif type(item) == int:
        d[int] += 1

print(d)

# by Shervin Hasanzadeh
