import math


def add(a,b):
    print("Addition = ",a+b)

def sub(a,b):
    print ("substraction = ",a-b)

def mul(a,b):
    print ("Multiplication",a*b)

def div(a,b):
    print ("Divided = ",a/b)
temp=0
while(temp==0):
    first_no = int(input("Enter the first no"))
    second_no = int(input("Enter the second no"))    

    op = input("Enter operation: \n 1. Addition \n 2. Substraction \n 3. Multipication \n 4. Divided \n 5. Other operation \n ")

    match op:
        case "1":
            add(first_no,second_no)
                
        case "2":
            sub(first_no,second_no)
            
        case "3":
            mul(first_no,second_no)
            
        case "4":
            div(first_no,second_no)
            
        case "5":
            op=input("Please enter 1 2 3 4 choice")
          
else:
    print("exit")
    temp=1
        
    

# op = input("Enter operation: \n 1. Addition \n 2. Substraction \n 3. Multipication \n 4. Divided \n")
# if (op=="1"):
#         add(first_no,second_no)
#         temp =1  
# elif(op=="2"):
#         sub(first_no,second_no)
#         temp =1  
# elif(op=="3"):
#     mul(first_no,second_no)
#     temp =1  
# elif(op=="4"):
#     div(first_no,second_no)
#     temp = 1
# else:
#     print("Please enter 1 2 3 4 choice")  

