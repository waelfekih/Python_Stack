# 1) Basic: print integers from 0 to 150
for i in range(151):
    print(i)


# 2) Multiples of 5
for j in range(5,1001,5):
    print(j)

# 3) Counting the dojo way
for k in range (1, 101):
    
    if k % 10 == 0:
        print("Coding Dojo")
    elif k % 5 == 0:
        print("Coding")
    else: print(k)

# 4) Whoa. That Sucker's Huge
sum = 0
for l in range(0,500000):
    if l % 2 == 1: 
        sum = sum + l

print (sum)

# 5) Countdown by Fours
for m in range (2018,0,-4):
    print (m)

# 6) Flexible Counter
lowNum = 4
highNum = 20
mult = 6
for n in range(lowNum , highNum , 1 ):
    if n % mult == 0:
        print(n)