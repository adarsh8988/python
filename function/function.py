# functions
# parameters
# postionsal parameters
# def sum(a,b):
#     c=a+b
#     print(c)
# sum(2,3)

# keyword parameters
# def subtract(a,b):
#     print('the value of a=',a)
#     print('the value of y=',b)
#     c=a-b
#     print(c)
# subtract(2,3)

# default parameters
# def sum(x=10,y=10):
#     z=x+y
#     print(z)
# sum(1)

# def table(a):
#     for i in range(1,11):
#         print(f"{a}x{i}={a*i}")
# table(9)

# x = (1, 2, 3, 1, 4, 4, 4, 5, 1, 1)
# count_dict = {}
# for i in range(1, 6):
#     count_dict[i] = x.count(i)
# print(count_dict)

# def sum(*args):
#     count_dict={}
#     for i  in args:
#          count_dict[i] = x.count(i)
#     print (count_dict)  
# x = (1, 2, 2, 3, 1, 4, 4, 4, 5, 1, 1)
# sum(*x)




# def sum(*a):
#     dic={} 
#     for i in a:
#         dic[i]= x.count(i)
#     print(dic)
# x= (1, 2, 2, 3, 1, 4, 4, 4, 5, 1, 1)
# sum(1,2,4)
    
# output_series = [i if i % 2!= 0 else str(i) * i for i in range(0,10)]
# print(output_series)


# dict. comprehession
# zx={x:x+10 for x in range(1,7)}
# print(zx)

    
# lst=[i*2 for i in range(1,11)]
# print(lst)

# table=[(f"2 x {i} = {2*1}") for i in range (1,11)  ]
# print(table)
#  decorators


# def decorater(z): 
#     def abc():
#         print("a")
#         z()
#         print("y")
#     return abc

# @decorater
# def xyz():
#     print("d")
# xyz()

# @decorater
# def name():
#     print("c")
# name()



# lst=[2,3,3,2,34,6,7,8,66]
# a=reduce()


# partial functions
from functools import partial

def xyz(a, b):
    c = a ** b  # 3 ** 3  3 x 3 x 3
    print(c)
    
xyz(3, 3)


xy = partial(xyz, b = 2)

xy(4)

















