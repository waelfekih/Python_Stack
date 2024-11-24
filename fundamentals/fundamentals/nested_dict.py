 #! 1.Update Values in Dictionaries and Lists   

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

    # change value 10 to 15
x[1][0] = 15
print(x)

    # change student's last name
students[0]['last_name'] = "Braynt"
print(students)

    # change 'Messi' to 'Andres'
sports_directory['soccer'][0] = "Andres"
print(sports_directory)

    # Change the value 20 in z to 30
z[0]['y'] = 30
print(z)

 #! 2.Iterate Through a List of Dictionaries
def iterateDictionary(students) :
    students = [
            {'first_name':  'Michael', 'last_name' : 'Jordan'},
            {'first_name' : 'John', 'last_name' : 'Rosales'},
            {'first_name' : 'Mark', 'last_name' : 'Guillen'},
            {'first_name' : 'KB', 'last_name' : 'Tonel'}
        ]

    for i in range (0 , len(students)  , 1):
        print(students[i]['first_name']) 
        print(students[i]['last_name'])

some_list = iterateDictionary(students)
print(some_list)

#! 3.Get Values From a List of Dictionaries
print("EXERCICE 3")
def iterateDictionary2(students) :

    students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
        ]
    
    for j in range (0 , len(students) ):
        print(students[j]['first_name'])
       
fn = iterateDictionary2(students)
print(fn)

def iterateDictionary2(students) :

    students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
        ]

    for j in range (0 , len(students) ):
        print(students[j]['last_name'])
       
ln = iterateDictionary2(students)
print(ln)

#! 4.Iterate Through a Dictionary with List Values
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
    }
def printInfo():
    print("num of locations:" ,len(dojo['locations']) ,"locations")
    for m in range (0 , len(dojo['locations']) , 1) :
        print(dojo['locations'] [m])
    

    print("num of instuctors:" ,len(dojo['instructors']) ,"instructors")
    for n in range (0 , len(dojo['instructors']) , 1) :
        print(dojo['instructors'] [n])
    
locins = printInfo()

print(locins)