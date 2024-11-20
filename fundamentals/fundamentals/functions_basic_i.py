#1
def number_of_food_groups():
    return 5
print(number_of_food_groups())
    #the output is 5

#2
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
    #the output is error because "number_of_days_in_a_week_silicon_or_triangle_sides()" is not defined

#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())
    #the output is 5 because when we have a return, the program stops executing and what is after return will not be executed

#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())
    the output is 5 because we have a return

#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)
    the output is 5

#6
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))
    #the output for "add(1,2)" is 3 and the output for "add(2,3)" is 5 and the output for "print(add(1,2) + add(2,3))" is 8
    #CORRECTION: there is no return to save the result of add(1,2) and the result of add(2,3) so it can not print (add(1,2) + add(2,3))

#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))
    #str will transform an integer into string, so str(b)=str(2)="2" and the same with str(c)=str(5)="5"
        #and strings can not be added,so the result is "25"

#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())
    #at first the code will print 100, then it moves to the conditional where the condition(b < 10) is false so it will go to else and print 10
        # and also we have return 7 out of the conditional, it will be printed normal so the output is 100,10,7
    #CORRECTION: it will print 100 and in the conditional we have 2 returns (10 and 7) and when we have the return the function exits
        #so the code will print(100,10)

#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
    #for the first function b < c so it will print 7, 
    #for the second function b > c so it will print 14
    # then it will print the sum of the 2 functions (7 + 14 = 21)

#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))
     b+c = 3 + 5 = 8

#11
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)
    #first print 500
    #second print 500
    #then we call the function foobar() so it will print 300
    #the function is not executed anymore so it will print 500 

#12
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)
    #this code will print the same results as the previous code (500, 500, 300, 500). the return has no effect in this code

#13
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)
    #this call will print 500 and 500 but since we call the function b = 300
    #so this will print 500 , 500 , 300 , 300

#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()
    #this code will print what inside the function foo() ==> 1 , 2
    #CORRECTION: we call the function foo()
        #at first it prints 1
        #then takes the value in the function bar() = 3
        #then print 2

#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)
    # y = foo() so we will call the function foo()
        #print(1)
    # x = bar() so we will call the function bar()
        # x = 3 and we return 5
    # then we return 10 of foo()
    # ==> 1 , 3 , 5 , 10



