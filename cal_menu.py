from calculator import add
print("!!.....WELCOME.....!!")

f_no = int(input("Enter first no :- "))
op = input("Enter operation: \n 1. Addition \n 2. Substraction \n 3. Multipication \n 4. Divided \n ")
s_no = int(input("Enter second no :- "))

history = [] # empty list declaration
res = []


def add(a,b):
    
    result=a+b
    ans = f"{a} + {b} =",result
    history.append(ans)
    res.append(result)
    print("Addition = ",result)
    return result

   
def sub(a,b):
    result=a-b
    ans = f"{a} - {b} =",result
    history.append(ans)
    res.append(result)
    print ("substraction = ",result)
    return result


def mul(a,b):
    result=a*b
    ans = f"{a} * {b} =",result
    history.append(ans)
    res.append(result)
    print ("Multiplication",result)
    return result


def div(a,b):
    result=a/b
    ans = f"{a} / {b} =",result
    history.append(ans)
    res.append(result)
    print ("Divided = ",result)
    return result

def fib(a,r):
    b = a + 1
    for i in range (r):
        c = a + b
        print(c)
        a = b
        b = c 
        ans = f"{a} + {b} =",c
        history.append(ans)
        res.append(c)
    print("Fibbonaci series = ",res)
    return c    

   
def arm():
    num = int(input("Enter a number: "))


    sum = 0

    
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10

    if num == sum:
        print(num,"is Armstrong ")
    else:
        print(num,"is not Armstrong ")


def cube(a,b):
    result=a*b
    ans = f"{a} * {b} =",result
    history.append(ans)
    res.append(result)
    print ("Multiplication",result)
    return result


# def div(a,b):
#     result=a/b
#     ans = f"{a} / {b} =",result
#     history.append(ans)
#     res.append(result)
#     print ("Divided = ",result)
#     return result


# def history:


temp=0
con=0
i=0

while(temp==0):
   
   if(con==1):
    
    # print("ans  =  ", res)
    op = input("""Enter operation: \n 1. Addition \n 2. Substraction \n 3. Multipication \n 4. Divided \n 
    5. clear\n 6. History\n 7. Other operation\n""")
       
    if op=="5":
        history.clear()
        # ans=" "
        print("History Clear...\n")
        con=1 
    elif op=="6":
            print("All operation History....!")
            print(history)
            # ans=" "
    elif op=="7":
            con=0
            temp=0
            res.clear()
            
            break
    else:       
                f_no = res[i]
                i+=1
                con=0
                s_no = int(input("Enter second no :- "))
            
                

   else:
       match op:
        case "1":
          
            # addition(f_no,s_no)
    
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
               # case "5":
           
             
        # case "6":
             
        #     print(history)
       
             
        # case "7":
        #     break
           
          
else:
    print("exit")


# f_no = int(input("Enter no :- "))
op = input("Enter operation: \n 1. fibonacis \n 2. Square Root \n 3. Cube  \n ")

# s_no = int(input("Enter second no :- "))

while(True):
     
    if(con==1):
    
    # print("ans  =  ", res)
        op = input("""Enter operation: \n 1. fibonacis \n 2. Armstrong no \n 3. Cube  \n 5. clear\n 6. History\n 7. Exit\n""")
       
        if(op=="5"):
            history.clear()
        # ans=" "
            print("History Clear...\n")
            con=1 
        elif(op=="6"):
            print("All operation History....!")
            print(history)
            # ans=" "
        elif(op=="7"):
            break 
        else:       
                # f_no = res[i]
                # f_no = res[s_no]

                # i+=1
                con=0
            
                

    else:
       match op:
        case "1":
            f_no = int(input("Enter first no :- "))
          
            # addition(f_no,s_no)
            s_no = int(input("Enter rane 0f serize :- "))
            fib(f_no,s_no)
            
            con=1
        case "2":

            arm()
            con=1
        case "3":

            cube(f_no,s_no)
            con=1
        case "4":

            div(f_no,s_no)
            con=1


        # case "5":
           
             
        # case "6":
             
        #     print(history)
       
             
        # case "7":
        #     break
           
          
else:
    print("exit")






