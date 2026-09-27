Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#For Loop
# Writing Multiplication Table using For Loop

>>> for i in range(1,13):
...     print(i,'*5','=',i*5)
... 
...     
1 *5 = 5
2 *5 = 10
3 *5 = 15
4 *5 = 20
5 *5 = 25
6 *5 = 30
7 *5 = 35
8 *5 = 40
9 *5 = 45
10 *5 = 50
11 *5 = 55
12 *5 = 60
>>> 
>>> for i in range(12,21):
...     print('5*',i,'=',5*i)
... 
...     
5* 12 = 60
5* 13 = 65
5* 14 = 70
5* 15 = 75
5* 16 = 80
5* 17 = 85
5* 18 = 90
5* 19 = 95
5* 20 = 100
>>> 
for i in range(1,20,2):
    print('2*',i,'=',2*i)

    
2* 1 = 2
2* 3 = 6
2* 5 = 10
2* 7 = 14
2* 9 = 18
2* 11 = 22
2* 13 = 26
2* 15 = 30
2* 17 = 34
2* 19 = 38

# Displaying Output Vertically using For Loop

for i in range(0,10):
    print(i,end=' ' )

    
0 1 2 3 4 5 6 7 8 9 

for i in range(10,0,1):
    print(i,end=' ' )

    
for i in range(10,0,-1):
    print(i,end=' ' )

    
10 9 8 7 6 5 4 3 2 1 

for i in range(10,0,-2):
    print(i,end=' ' )

    
10 8 6 4 2 

# Writing Program to Check Order Status using For Loop with Dictionary

Order_Status = {'Order 1': 'Delivered', 'Order 2': 'Not Delivered','Order 3': 'Not Delivered','Order 4': 'Delivered'}

for Order, Status in Order_Status.items():
    if Status == 'Delivered':
        print(Order, 'has been delivered')
    else:
        print(Order,'is in Progress')

        
Order 1 has been delivered
Order 2 is in Progress
Order 3 is in Progress
Order 4 has been delivered
