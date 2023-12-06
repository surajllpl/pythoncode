const prompt = require("prompt-sync")({sigint:true});
//console.log("Hello Word")


let f_no = parseInt(prompt("Enter first no"));
let op = (prompt("Enter operation: \n 1. Addition \n 2. Substraction \n 3. Multipication \n 4. Divided \n"));
let s_no = parseInt(prompt("Enter second no :- "));



function add(a,b){
    
   let result=a+b;
   
    console.log("Addition = ",result);
    return result;
}
   
function  sub(a,b){
    result=a-b;
    ans = "{a} - {b} =",result;
    console.log ("substraction = ",result);
    return result;
    }

    function mul(a,b){
    result=a*b;
    ans = "{a} * {b} =",result;
    console.log ("Multiplication",result);
    return result;
 }

 function div(a,b){
    result=a/b;
    ans = "{a} / {b} =",result;
    console.log ("Divided = ",result);
    return result;
 }

 temp=0;
con=0;
i=0;

while(temp==0){

   if(con==1){
    
    // print("ans  =  ", res)
    op = prompt("Enter operation: \n 1. Addition \n 2. Substraction \n 3. Multipication \n 4. Divided \n 5. clear\n 6. History\n 7. Other operation\n");
       
    if (op=="5"){
      //  history.clear()
        // ans=" "
        console.log("History Clear...\n");
        con=1;
    }
    else if (op=="6"){
        console.log("All operation History....!")
        //console.log(history)
            // ans=" "
        }
    
    else if (op=="7"){
            con=0
            temp=0
          //  res.clear()
            //history.clear()
            
            break;
    
    }   
        else{      
                f_no = a;
                i+=1;
                con=0;
                s_no = parseInt(prompt("Enter second no :- "));
            
    } 
   }
   else {
       switch(op){
        case "1":
          
            // addition(f_no,s_no)
    
           a = add(f_no,s_no);
           console.log(a);
            
            con=1;
            continue;
        case "2":

            a=sub(f_no,s_no);
            con=1;
            continue;
        case "3":

            a=mul(f_no,s_no);
            con=1;
            continue;
        case "4":

            a=div(f_no,s_no);
            con=1;
            continue;
       
   }}}
   