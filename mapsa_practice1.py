'''
We take two "k" and "n" numbers from the user.
Then we write the numbers 1 in a line like this:
First we write all odd numbers from "1" to "n" ascending and then all even numbers "1" to "n" descending.
In the output, tell me what number is in the position of "K th"?
'''

n = input("Please enter an integer: ")
k = input("Please enter another integer: ")

n = int(n)
k = int(k)

odd = list()
even = list()
for i in range(1, n + 1):
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

odd.sort()
even.reverse()

numbers = odd + even
print(numbers)
k = k - 1   # Because human starts indexing from 1 but the machine from zero
print(numbers[k])

# by Shervin Hasanzadeh
