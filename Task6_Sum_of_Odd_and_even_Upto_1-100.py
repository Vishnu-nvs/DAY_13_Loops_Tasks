#Findout Sum of Odd Numbers and Some of Even numbers  upto 1-100 using for loop.

sum=0
odd=0
for x in range (1,101):
    if x%2 ==0:
      sum=sum+x
    else:
     odd=odd+x  
print("sum of even Number",sum)
print("sum of odd Number",odd)    
    