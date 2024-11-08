mark = int(input("please enter your mark to get the mark: "))

if mark <= 20 or mark >=100:
    print("invalid eneter, Please enter avlid number between 20 and 100")
else:
    if 70<= mark <=100:
        print("the grade is A")
    elif 60<= mark <=69:
        print("the grade is B")
    elif 50<= mark <=59:
        print("the grade is C")
    elif 40<= mark <=49:
        print("the grade is D")
    elif 30<= mark <=39:
        print("the grade is E")
    else:
        print("the grade is F")
        
        

