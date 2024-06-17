# # wap n which accept  positional arguments, return sum of n element

# # fun name should be add()

# # result should be:
# # add(3,3,3,3)=>12
# # add(3,2)=>5


# # def add(*args):
# #     sum=0
# #     for el in args:
# #         sum=sum+el
# #     return sum

# # a=add(9,3,4)
# # b=add(3,2)
# # print(a,b)

# # print element of args
# def add(*args):
#     for el in args:
#         # kjslkjf
#         print(el)
# add(6,7,4)



# # keyword arguments

# # name valae pair

# def greet(**kwargs):
#     print(kwargs)#dict return

# greet(name='somethig',lastname='ohter')
# # greet(a,b)

# # task:
# # wap to print key and value of keyword arguments


# def greet(**kwargs):
#     print(kwargs)#dict return
#     for key, value in kwargs.items():
#         print(key, value)



# greet(name='somethig',lastname='ohter')


# # remeber in defult parameter
# # def add(b,c,a=3,):
# #     pass

# # lambda funciton
# # syntax -> lambda args:expression


# sum= lambda a,b:  a+b
# print(sum(2,3))
# # without lambda
# # *arggs 

# a= lambda *a: a
# # def add(a,b ):
# #     return a+b


# # higher order function
# # map 
# # filter
# # map(function, iterable)

# el=[2,3,4]
 
# # def sq(e):
# #     return e*e
# s= lambda e: e*e
# sq=list(map(s,el))
# print(sq)


# sq=list(map(lambda e: e*e,el))
# print(sq)

# # filter
# # return odd only using list comprehension
# li=[1,2,3,4,5]
# odd=[el for el in li if not el%2==0]
# print(odd)
# # n=[el*el for el in li]
# # print(n)
# # def even(e):
# #     if e%2==0:
# #         return e

# # even=filter(even, li)
# # print(even)


# element=[1,2,3]
# # {key:value for lopp}
# new_dict={el:el*el for el in element}


# # ternary operator
# #  ret?urn 
# # person= male or felmale
 
# person ='male'
# if person=='male':
#     print( 'he is male')
# else:
#     print( 'she is female')
# print('he is male' if person=='male' else 'she is female')

# indexab
# ordered
# immutable


# slicing
# [::]


string="he is a boy"
# feature
# enumerate=
# for el in string:
#     print(el)


li=['college','school','university']
# print all element and its corsspoding index value
# enumerate
for index,el in enumerate(li):
    print(index,el)


myst='university is shit'
# using slicing print last 3 char of mystr
# using slicing revese the string
print('reverse of myst is:', myst[::-1])
print('last 3 char is:', myst[:-4:-1])

# some methods in string
# upper()
# lower()
# title()
# capitalize()


# print()
# myst.replace('shit','good')
name_str='alice boby antare jantare'
# split()
name=name_str.split()
print(name)
# name=['alice','boby','antare','jantare']

name_str1='alice@boby@antare@jantare'
# print(name_str1.split('@',1))

# syntax of split : string.split('', max_split)

# join()

my_list=['str','char','int']
# ouptut-> 'str@char@int'
# syntax-> 'join garne str'.join(list)
a='@'.join(my_list)
print(my_list,a)

# some operator in string
# repetation *
b='ho'
# output->'hohoho'
print(b*3)

a='hoin'
# concatination +
# output->hohoin
print(a+b)

digit='1234a'
print(digit.isalnum())

# palindrome
'radar'


# def ispalindrome(string):
#     reverse=string[::-1]
#     if string==reverse:
#         return True
#     else:
#         return False
    
# a=ispalindrome('radar')
# b=ispalindrome('notradar')
# print(a)
# print(b)


# def ispalindrome(string):
#     reverse=string[::-1]
#     return True if reverse==string else False
    
# a=ispalindrome('radar')
# b=ispalindrome('notradar')
# print(a)
# print(b)

ispalindrome= lambda string:  True if string[::-1]==string else False


print(ispalindrome('radar'))


def divide(number, divisor):
    
    try:
        print(number/divisor)
        # li=[1,2,3]
        # print(li[4])
    except ZeroDivisionError:
        print('divison by zero is not allowed')
    except:
        print('out of index')
    else:
        print('is execute if try block execute without exception')
    finally:
        print('it execute always')


divide(10,5)
# divide(10,0)

def exceptionraise(string):
    try:
        if not string.isdigit():
            raise "not digit"
        else:
            print(string)
    except:
        print('not digit')

exceptionraise('12w')


# break continue pass

for el in range(1,5):
    if el==3:
        continue
    else:
        print(el)


for el in [1,2,3,4,5,6]:
   pass


# for else
for el in [1,2,3,4,5,6]:
    if el==100:
        break
    else:
        print(el)
else:
    print('else is executed')
# question
# wap to check prime number using for else