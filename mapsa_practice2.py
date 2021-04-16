'''
As input, you first take a number "n", then in the next line you receive "n" another number.
A T-prime number is called if it has exactly 3 divisors.
For "n" number received, say whether they are T-Prime or not.
'''

n = input("Please enter an integer: ")
nums = input()

n = int(n.strip())
nums = nums.strip()
nums = nums.split(' ')

numbers = list()     # nums is a new list with n member, user may have entered more punctuation than "n" in second line
try:
    for i in range(0, n):
        numbers.append(int(nums[i]))
except IndexError as e:
    print(e)

# We can also take numbers from the user in "n" lines instead of taking all the numbers in one line.
# numbers = list()
# for i in range(0, n):
#     numbers.append(int(input()))

counter = dict()
for i in numbers:
    counter[i] = 0
    for j in range(1, i + 1):
        if i % j == 0:
            counter[i] += 1

# print(counter)

for k, v in counter.items():
    if v == 3:
        print("Yes")
    else:
        print("No")

# by Shervin Hasanzadeh
