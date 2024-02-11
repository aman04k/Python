lower=int(input("Enter a number first: "))
uper=int(input("Enter a number second: "))

for num in range(lower,uper+1):
    count=0
    for i in range(1, num+1):
        if num%i==0:
            count=count+1
    if count ==2:
        print(num)        



