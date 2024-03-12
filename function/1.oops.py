# constructor
# class xyz:
#     def __init__(self):
#         print("this is a car")
# obj=xyz()
        
    
# Attribute
# class xyz:
#     def __init__(self):
#         # a=int(input("enter a number "))
#         # b=int(input("enter a number "))
#         self.num1=2
#         self.num2=3
#         # print(a+b)
#         print(self.num1+self.num2)
# obj=xyz()

# inheritance : 
# types

# 1) single inh.: one parent and one child
# class cls1:
#     def method1(self):
#         print("this is a car")
#     def method2(self):
#         print("this is a bus")
# # obj=cls1()
# # obj.method1()
# class cls2(cls1):
#     def method3(self):
#         print("this is a bike")
# obj=cls2()
# obj.method1()

#2 multiple inh.: 
# class cls1:
#     def method1(self):
#         print("this is a car")
#     def method2(self):
#         print("this is a bus")
# # obj=cls1()
# # obj.method1()
# class cls2(cls1):
#     def method3(self):
#         print("this is a bike")
# class cls3(cls1,cls2):
#     def method4(self):
#         print("this is a bike")
# obj=cls3()
# obj.method1()
# # 3 multilevel inh: when lower clas inherit uper clas
# # 4 hirarical inh.
# # 5 hybrid inh. when combine one or multiple class
# class cls4(cls2,cls3):
#     def method

# abstraction
# abstract class
# abstract method
# interface

# abstraction: ( unnessary data hiding)
# abc=abstract base class
# from abc import ABC, abstractmethod
# class cls1(ABC):
#     @abstractmethod
#     def car(self):
#         # print("this is a car")
#         pass
#     @abstractmethod
#     def bus(self):
#         # print("this is a bus")
#         pass
# class cls2(cls1):
#     def train(self):
#         print("this is a train")
        
#     def car(self):
#         print("this is a car")
        
#     def bus(self):
#         print("this is a bus")
# obj=cls2()
# obj.car()

# Encapsulation: when you bind up multiple things in a single unit is called encapsulation

# access spacifires
# 1) public member= simple
# 2) proteced member=_
# 3) private member=__


# class cls1():
#     def __init__(self):
#         self.name="moris"
#         self.age=20
#     def info(self):
#         print('this is info')
    
# class cls2(cls1):
#     def data(self):
#         print('this is a data')
        
# obj=cls2()
# # obj.info()
# print(obj.name)

# polymorphism : poly+morphism
# poly=many and morphism = forms
# when one thing have multiple forms.
# types
# 1) compile time poly.
#    method overloading
#    operator overloading
# 2) run time poly.
#    method overriding

# class method:
#     def sum (self, x = None , y = None , z= None):
#         if(x != None and y !=  None and z != None):
#             xyz = x + y + z
#             print(xyz)
            
#         elif (x != None and y != None):
#             xyz = x+ y
#             print(xyz)
        
#         elif x != None:
#             xyz  = x
#             print(xyz)
            
# obj = method()
# obj.sum(10)

#  polymorphism
# class cls:
#     def sum(self,x=None , y = None , z = None):
#         if(x !=None and y !=None and z !=None):
#             # xyz=x+y+z
#             print(x*y*z) 
            
#         elif(x !=None and y !=None):
#             # xyz=x+y
#             print(x*y)
            
#         elif x !=None:
#             print(x)
# ob=cls()
# ob.sum(10,2)

# duck typing

# class dog:
#     def speak(self):
#         print("woow")
        
# class cat:
#     def speak(self):
#         print("meiooooo")
# class duck:
#     def speak(self):
#         print("quack")
        
# ob=dog()
# ob1=cat()
# ob2=duck()
# ob1.speak()

# # def voice(x):
# #     x.speak()
# # voice(ob1)






























































        
