name=str(input())
name.split()
print("Hello there ",name)
num1=int(input("Enter 2 numbers to perforn calculations"))
num2=int(input())
print("Analysing the number \nwe get: ")
if( num1>0):
    print("number 1 is positive")
elif(num1<0):
    print("number 1 is negitive")

if( num2>0):
    print("number 2 is positive")
elif(num2<0):
    print("number 2 is negitive")

if(num1>num2):
    print("number 1 is  \bgreater ")

else:
    print("number 2 is greater")

choices =int(input (print ("Select operation to perform :","\n1. Addtion",'\n2. Subptaction',"\n3. Multiplication",'\n4. Divide',"\n5. Square root of both numbers","\n6. Factorial of 2 numbers")))

if(choices==1):
    print('You choose Addition.')
    print("Addition: ",num1+num2)
elif(choices==2):
    print('You choose Subpraction.')
    print("number 1 - number 2: ",num1-num2)
    print("number 2 - number 1: ",num2-num1)
elif(choices==3):
    print('You choose multiplication.')
    print("number 1 * number 2: ",num1*num2)
elif(choices==4):
    print('You choose division.')
    print("number 1 / number 2: ",num1/num2)
    print("number 2 / number 1: ",num2/num1)
elif(choices==5):
    print('You choose square root.')
    print('Square root of number 1 is:',num1**2,"\n Square root of number 2 is:",num2**2)
   
elif(choices==6): 
    fact1=1
    print('You choose factorial.')
    for i in range(1,num1):
        fact1=fact1*i
    print("Factorial of number 1 is:",fact1)
    fact2=1
    for i in range(1,num2):
        fact1=fact1*i
    print("Factorial of number 2 is:",fact2)
else:
    print("Invalid input")
   

      
      

   
