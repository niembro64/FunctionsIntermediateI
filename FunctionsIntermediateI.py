# Update Values in Dictionaries and Lists

x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# 1 Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
print()
x[1][0] = 15
print(x)

# 2 Change the last_name of the first student from 'Jordan' to 'Bryant'
print()
print(students[0]['first_name'])
students[0]['first_name'] = "Bryant"
print(students[0]['first_name'])

# 3 In the sports_directory, change 'Messi' to 'Andres'
print()
print(sports_directory['soccer'][0])
sports_directory['soccer'][0] = "Andres"
print(sports_directory['soccer'][0])

# 4 Change the value 20 in z to 30
print()
print(z[0]['y'])
z[0]['y'] = 30
print(z[0]['y'])