# 1) CountDown
def countdown(n):
    down = []
    for i in range (n,-1,-1):
          down.append(i)
    return down
        
x = countdown(5)
print(x)

# 2) Print and Return
def printNreturn(a,b):
     list1 = [a,b]
     print (a)
     return b

y = printNreturn(4,12)
print(y)

# 3) First plus Length
def firstPlusLength(list_2):
     
     sum = list_2[0] + len(list_2)
     return sum
z = firstPlusLength([5,4,8,6,0,52,78,100])
print(z)

# 4) Values Greater than Second 
def greaterThanSecond(list_3):
    list_4 = []
     
    if len(list_3) > 2: 
        for j in range (0 , len(list_3)  , 1 ):
            if list_3[j] > list_3[1]:
                list_4.append(list_3[j])

        print ("new length = " ,len(list_4))
        return list_4
    else: 
        return False

w = greaterThanSecond([2,5,8,77,1,3,26,4,14,50])
print(w)

# 5) This Length, That Value
def length_and_value(size, value):
    list_5 = []

    for n in range (0 , size , 1):
        list_5.append(value)
    
    return list_5

v = length_and_value(5, 10)
print(v)
    



            
                 


