num = int(input("Enter a number"))
if num <2:
    print("This is not prime number")
else:
    for i in range(2,num):
        if num%i==0:
            print("This is not Prime number")
            break
    else:
        print("This is prime number")        