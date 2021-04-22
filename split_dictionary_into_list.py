'''
Write a Python program to split a given dictionary of lists into list of dictionaries.

Input :
{'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}

Output :
[{'Science': 88, 'Language': 77}, {'Science': 89, 'Language': 78}, {'Science': 62, 'Language': 84}, {'Science': 95, 'Language': 80}]
'''

input_dict = eval(input())

keys = list(input_dict.keys())
values = list(input_dict.values())

result_dict = [{keys[0]: values[0][i], keys[-1]: values[-1][i]} for k, v in input_dict.items() for i in range(0, len(v) - 1)]

print(str(result_dict))

# by Shervin Hasanzadeh
