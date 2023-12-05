
print("!!.....WELCOME.....!!")

f_no = float(input("Enter first no :- "))
op = input("Enter operation: \n 1. Addition \n 2. Substraction \n 3. Multipication \n 4. Divided \n ")
s_no = float(input("Enter second no :- "))

res =[0]
i=0



def add(a,b):
    
    result=a+b
    res[i]=result
    print("Addition = ",result)
    # con=1  

def sub(a,b):
    result=a-b
    res[i]=result
    print ("substraction = ",result)

def mul(a,b):
    result=a*b
    res[i]=result
    print ("Multiplication",result)

def div(a,b):
    result=a/b
    res[i]=result
    print ("Divided = ",result)
temp=0
con=0
# result=0
while(temp==0):
   
   if(con==1):
    
    print("result =  ", res[i])
    op = input("Enter operation: \n 1. Addition \n 2. Substraction \n 3. Multipication \n 4. Divided \n 5. Exit\n")
    if(op=="5"):
        break
    else:
        s_no = float(input("Enter second no :- "))
        f_no = res[i]
        con=0
   else:
    match op:
        case "1":
            add(f_no,s_no)
            con=1
        case "2":
            sub(f_no,s_no)
            con=1
        case "3":
            mul(f_no,s_no)
            con=1
        case "4":
            div(f_no,s_no)
            con=1
        case "5":
            # break
            temp=1
           
          
else:
     print("exit")



