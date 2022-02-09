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


# ///////////////////////////////


# 2 Iterate Through a List of Dictionaries

students2 = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)

# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

# Create a function iterateDictionary(some_list) that, given a list of dictionaries, the function loops through each dictionary in the list and prints each key and the associated value. For example, given the following list:
print()

def iterateDictionary(list):
    for i in range (0, len(list)):
        print(f"first_name - {list[i]['first_name']}, last_name - {list[i]['last_name']}")
    
iterateDictionary(students2)

# Get Values From a List of Dictionaries

# Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name, the function prints the value stored in that key for each dictionary. For example:
#iterateDictionary2('first_name', students) should output:
#Michael
#John
#KB
#And iterateDictionary2('last_name', students) should output:
#Jordan
#Rosales
#Guillen
#Tonel
print()
def iterateDictionary2(n,list):
    for i in range (0, len(list)):
        print(f"{list[i][n]}")
    
iterateDictionary2('first_name',students2)
print()
iterateDictionary2('last_name',students2)


