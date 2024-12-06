def calculate(num1, num2, operator):#this function will perform calculation taking values from the previous function Get_input(), now those value are used to perform the calculations
    if operator == "+":    #if condition is applied to perform the operator choosed by the user
        result = num1 + num2  #calcuation result will be saved in the variable result
        answer = f"The sum of {num1} and {num2} is {result}" #save the into the variable answer
        print(answer) #will print the message for the user
    elif operator == "-":
        result = num1 - num2
        answer = (f"The difference between {num1} and {num2} is {result}")
        print(answer)
    elif operator == "*":
        result = num1 * num2
        answer = (f"The product of {num1} and {num2} is {result}")
        print(answer)
    elif operator == "/":
        if num2 != 0:    #the second number must be different from zero
            result = num1 / num2
            answer = (f"The quotient of {num1} and {num2} is {result}")
            print(answer)
        else:
            result = None  #None indicate python will not performs any calcuation if in the division the secoond number is zero
            print("Error: Division by zero is not allowed.")  #message that will display, no divison allowed
    else:
        result = None    #same as last condition, if the user will insert a wrong operator. no operation will run
        print("Error: Invalid operator. Supported operators are +, -, *, /.") # message that will display when i will call the variable operator

    return answer   #the function will return to this to variable result
