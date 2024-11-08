number = int(input("please enter a non negative number: "))

if number <= 0:
    print("invalid entry, Please  enter a non negative number: ")

else:
    x=1
    factor=1

    while x <=number:
        factor= factor * x
        print(x, ":", factor)
        x= x+1
    
