
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

temp=0
con=0
i=0

while(temp==0):
   
   if(con==1):
    
    print("ans  =  ", res)
    op = input("Enter operation: \n 1. Addition \n 2. Substraction \n 3. Multipication \n 4. Divided \n 5. clear\n 6. History\n 7. Exit\n")
       
    if(op=="5"):
        history.clear()
        ans=" "
        print("History Clear...\n")
        con=1 
    elif(op=="6"):
            print(history)
            ans=" "
    elif(op=="7"):
            break
    else:       
                f_no = res[i]
                i+=1
                con=0
                s_no = int(input("Enter second no :- "))
            
                
    
       
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
        # case "5":
           
             
        # case "6":
             
        #     print(history)
       
             
        # case "7":
        #     break
           
          
else:
    print("exit")




