
#1
print("1. Palindrome Program ")
a="nitesh"
a1=a[::-1]
if a1==a:
    print("String is palindrome")
else:
    print("String is not palindrome")

#2
print("Factorial Program")
def factorial_recursive(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial_recursive(n-1)
f=factorial_recursive(3)
print(f)

#3
print("Fibonacci Series:")
def Fibonacci(n):
    if n<0:
        print("incoreect value")
    elif n==0:
        return 0
    elif n==1 or n==2:
        return 1
    else:
        return Fibonacci(n-1)+ Fibonacci(n-2)
print("Fibonacci series of 9 is",Fibonacci(9))
#4
print("Armstrong Number checking:")
sum=0
num=1634
print(num)
order=len(str(num))
original_num=num
while(num>0):
    digit=num%10
    sum=sum+digit**order
    num=num//10
if sum==original_num:
    print("number is armstrong number")
else:
     print("number is not armstrong number")
     
#6
print("Patterns in python :")
for x in range(10):
    print(x)
print("Simple pyramid pattern :")
for x in range(4):
    for y in range(0,x+1):
        print("*",end="")
    print("\r")
print("Square Pattern")
for x in range(4):
    for y in range(4):
        print("*",end="")
    print("\r")
#7
print("Leap year in python:")
year=2004
if (year % 400 == 0) and (year % 100 ==0):
    print(year,"is a leap year")
else:
    print(year,"is not leap year")

#8
print("Prime number program in pythom:")
num=6
if num>1:
    for i in range(2,num):
      if num%i==0:
        print(num,"is not a prime number")
        break
      else:
        print(num,"is a prime number")

#9
print("To calculate area :")
print("I.To calculate area of triangle:")
print("(a)With three sides")
#formula = (s*(s-a)(s-b)(s-c))**0.5 where s = (a+b+c)/2
a=float(5)
b=float(6)
c=float(9)
s = (a+b+c) / 2
area= (s*(s-a)(s-b)(s-c))**0.5
print('The area of traingle is' '%0.2f' %area)
print()
print("(b)With two sides")
a=float(15)
b=float(10)
area= a*b*1/2
print(area)
print()
print("II.To calculate area of rectangle:")
a=float(15.2)
b=float(0.5)
area=a*b
print(area)
print()
print("III.To calculate area of sqaure:")
a=float(20)
area=a**2
print(area)
#10
print("to reverse a list:")
l=[1,56,87,12]
print(l)
l.reverse()
print(l)
print()
#11
print("To find sum of all elements of a list:")
l=[25,12,35,47]
sum=0
for i in range(0,len(l)):
    sum+=l[i]
print(sum) 
print()
#12
print("To find min,average,max of a list:")
l=[45,89,1,5,111]
print(l)
print("minimum element in a list is ",min(l))
print("maximum element in a list is ",max(l))
print("length=",len(l))
sum=0
for i in range(0,len(l)):
 sum+=l[i]
print("sum=",sum) 
print("average element in a list is ",sum/len(l))
print()
#13
def grouping_dictionary(l):
    result={}
    for k,v in l:
        result.setdefault(k,[]).append(v)
    return result
colors=[('yellow',1),('blue',2),('yellow',3),('blue',4),('red',1)]
print("Original list :")
print(colors)
print("\n Grouping a sequence of key value pair:")
print(grouping_dictionary(colors))
print()
#14
def nested_dictionary(l1, l2, l3):
     result = [{x: {y: z}} for (x, y, z) in zip(l1, l2, l3)]
     return result
student_section = ["Yashan", "Sumit", "Yuvraj", "choori"]
student_name = ["C2", "C1", "C2", "C3"]
student_marks = [85,98,89,92]
print("Original strings:")
print(student_section)
print(student_name)
print(student_marks)
print("\nNested dictionary:")
print(nested_dictionary(student_section, student_name, student_marks))
print()
#15
print("To check if a set is subset of another set:")
def check_subset(s,S):
    if(s.issubset(S)):
        print(s ,"is a subset of ", S)
    else:
        print(s ,"is not a subset of ", S)
a={1,5,16,56}
print(a)
b={1,5,16,56,85}
print(b)
check_subset(a,b)
print()
#16
print("To create symmetric difference & set difference:")
A={15,21,5,87}
print(A)
B={15,21,55,87}
print(B)
print("Symmetric difference of A and B is ",A.symmetric_difference(B))
print("Symmetric difference of B and A is ",B.symmetric_difference(A))
print("Set difference of A and B is ",A.difference(B))
print("Set difference of B and A is ",B.difference(A))
print()
#17
print("To remove a empty tuple from list of tuples:")
def Remove(tuples):
    tuples=[t for t in tuples if t]
    return tuples
tuples=[('Sumit'),(),('yash'),('suhszz'),()]
print(Remove(tuples))
print()
#19
print("To check validity of password:")
l, u , d , s = 0 , 0 , 0 , 0
Password = 'Yashanpal6^'
lowercasealphabets='asdfghjklpoiuytrewqzxcvbnm'
uppercasealphabets='ASDFGHJKLPOIUYTREWQZXCVBNM'
digits="0123456789"
specialchar='!@#$%^&*'
if (len(Password) >= 8):
    for i in Password:
        if (i in lowercasealphabets):
            l+=1
        if (i in uppercasealphabets):
            u+=1    
        if (i in digits):
            d+=1    
        if (i in specialchar):
            s+=1
if (l>=1 and u>=1 and d>=1 and s>=1 and l+u+d+s==len(Password)):
    print("Password is valid")   
else:
    print("Password is  not valid")
[10:45 a.m., 2022-07-28] Yashanpal: print("1ST answer:")
def a_fun():
 	global yash
yash='A'
def b_fun():
 	global nitesh
nitesh='B'
b_fun()
a_fun()
print(yash)
print(nitesh)
#2
print("2nd Answer")
a = 10
def f():
 	print ('Inside f() : ', a)
def g(): 
 	a = 20
print ('Inside g() : ',a)
def h(): 
 	global a
a = 30
print ('Inside h() : ',a)

print ('global : ',a)
f()
print ('global : ',a)
g()
print ('global : ',a)
h()
print ('global : ',a)
#3
print("3rd Answer")
a_var = 10
b_var = 15
e_var = 25
d_var = 100
def a_func(a_var):
 	print("in a_func a_var =", a_var)
b_var = 100 + a_var
d_var = 2 * a_var
print("in a_func b_var =", b_var)
print("in a_func d_var =", d_var)
print("in a_func e_var =", e_var)
print(b_var + 10)
c_var = a_func(b_var)
print("a_var =", a_var)
print("b_var =", b_var)
print("c_v)