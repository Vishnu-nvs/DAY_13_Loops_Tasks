
#Find out the Given number is Prime or not ?

a=13
count=0
for x in range(1,16):
    if a%x ==0:
        count=count+1
        # count+=1
if count ==2:
    print("Given number is Prime")
else:
    print("Given number is Not Prime")
    