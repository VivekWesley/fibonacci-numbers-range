f1 = 0
f2 = 1
f3 = 0

print("pick a start point")
lower = input()
print("pick an end point")
upper = input()

if int(lower)== 0 or int(upper)== 0 or int(upper)-int(lower) == 0 or int(lower)<0 or int(upper)<0:
    print("ERR.. invalid entry!! Range can't start or end with zero and should not be negative numbers")
elif int(lower) > int(upper) or int(upper)-int(lower)==0:
    print("ERR.. start point shouldn't be larger than end point value. Also start and end values shoudn't be same!!") 
elif int(lower)>=1 and int(upper)>=1:
    print("Fibonacci numbers between", lower, "and", upper, "are:")
    for f3 in range(3, int(upper)):
        f3 = int(f1)+ int(f2)
        f1 = int(f2)
        f2 = int(f3)
        if int(f3) >= int(lower): 
            if int(f3) >= int(upper):
                break
            else:
                print(f3)
                
            
        
            

        
