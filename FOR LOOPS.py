'''1 to 10'''
# for i in range (1,11):
#     print(i)

'''even num b/w 1 to 20'''
# for i in range(1,21):
#     if i%2==0:
#         print(i)

'''odd num b/w 1 to 20'''
# for i in range(1,21):
#     if i%2!=0:
#         print(i)

'''5 table using for loop'''
# for i in range(1,11):
#     a=i*5
#     print("5","x",i,"=",a)

'''print each character'''
# name="pavan"
# for i in name:
#     print(i)

'''print all elements of list'''
# fruits=["apple","banana","cherry","mango"]
# for i in fruits:
#     print(i)

'''sum of first natural numbers'''
# sum=0
# for i in range(1,11):
#     sum+=i
# print(sum)

'''find the factrioal'''
# num=int (input("enter the  num:-"))
# fact=1
# for i in range(1,num+1):
#     fact=fact*i
# print(fact)

'''square of 1 to 10 num'''
# for i in range (1,11):
#     print(i**2)

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




# stu_d=[]
# n=int(input("enter the how many records do you want to enter:-"))
# for i in range(n):
#     d={}
#     d['id']=int(input("enter the id:-"))
#     d['name']=input("enter the name:-")
#     d['marks']=int(input("enter the marks:-"))
#     stu_d.append(d)
# print(stu_d)

# b={'id':n+1,'name':'kowshik','marks':98}
# stu_d.append(b)
# print(stu_d)

value=eval(input("enter the name or id:-"))
#here eval function accepct any datatype of data as input ,no need to 
#convert the  datatype like int(),float() etc.
b=[{'id':1,'name':'pavan','marks':98},
   {'id':2,'name':'sai','marks':98},
   {'id':3,'name':'nari','marks':98}]
for i in b:
 if i['id']==value or i['name']==value:
    print(i)