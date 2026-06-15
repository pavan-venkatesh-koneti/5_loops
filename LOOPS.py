'''find the even numbers from 100 to 200'''
# for i in range(101,201):
#     if i%2==0:
#         print(i)

'''1 to 100'''
# for i in range(1,101):
#     print(i)
'''odd number 1 to 100'''
# for i in range(1,101):
#     if i%2==1:
#         print(i)
'''5 multiples from 1 to 100'''
# for i in range(1,101):
#     if i%5==0:
#         print(i)
'''taking float values from list'''
# a=[1,3,"pavan",1.1,3.4,"sai",3+6j]
# for i in a:
#     if type(i)==float:
#         print(i)
'''5 table using for loop'''
# for i in range(1,11):
#     a=i*5
#     print("5","x",i,"=",a)

''' 20 to 1'''
# for i in range(20,0,-1):
#     print (i)

'''count of even numbers'''
# count=0
# for i in range(1,51):
#     if i%2==0:
#         count+=1
# print("the count of even numbers from 1 to 50 :-",count)

'''prime number'''
# num=int(input("enter the number:-"))
# count=0
# for i in range(1,num+1):
#  if num%i==0:
#      count+=1
# if count==2:
#     print (num,"is prime number")
# else:
#     print(num,"is not prime number")
'''factors'''
# num=int(input("enter the number:-"))
# for i in range(1,num):
#     if num%i==0:
#         print(i,"is factors",num,end=", ")
'''removing dublecates in string'''
# name1="pavan"
# name2=""
# for i in name1:
#     if i not in name2:
#         name2=name2+i
# print(name2)
    
'''perfect num'''
#num=int (input("enter the number:-"))
# perfect=0
# for i in range(1,num):
#     if num%i==0:
#         perfect+=i
# if perfect==num:
#     print("perfect number")
# else:
#     print("not perfect number")

'''armstrong number'''
# num=int (input("enter the number:-"))
# sum=0
# for i in range(num):
#     a=i*len(num)
#     sum+=a
# print(sum)

'''armstrong number'''
# num=int(input("enter the num:-"))
# string=str(num)
# size=len(string)
# count=0
# for i in string:
#     count+=int(i)**size
# if count==num:
#     print("armstrong")
# else:
#     print("not armstrong")

