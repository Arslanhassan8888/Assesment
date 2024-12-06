def get_input():
    valid_operator = ['+', '-', '*', '/'] #the only options that customer can choose
    try:                                    #try except for ValueError, mean the program will not crash if the customer
                                            #will insert letter insetad of numbers
        num1 = float(input("Enter the first number: ")) #float convert the number string into number
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.") 
        return get_input()                    #if error has been raised the function will start from starting point

    operator = input("Enter an operator (+, -, *, /): ")# in this function the user have to choose one of the operator and save it in operator
    if operator not in valid_operator:      #the user choice will be verify if exist in valid_operator-- if exist the program will carry on

        print("Invalid operator. Please choose from (+, -, *, /).")# otherwise will show teh error message and it will suggest to choose again the operator
        return get_input() # in case of wrong choice, the function will start again

    return num1, num2, operator
#When you separate multiple values with commas in a return 
# statement, Python automatically creates a tuple to hold these values. the 3 value we get from the user now are returning 
#and saved as tuple, which will be break as es. num1=5 num2=10 operator = +
