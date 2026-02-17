number = int(input("Enter a number: "))
i = 2
flag = 0

while i <= number // 2:
    if number % i == 0:
        flag = 1
        break
    i += 1

if flag == 1:
    print("Not prime")
else:
    print("Prime")   

    
    
