from input import get_input   # i am calling the function from differnt modules
from operation import calculate
from output import save_to_txtfile

def main():  # main fuction --when i call this function i will call the other 3 functions.. fisrt to gert user entries, second to process the operation and stored
    #the result of the operation in asnwer. third function will save the operation into txt file calle calculation.txt
    
    num1, num2, operator = get_input()
    
    answer = calculate(num1, num2, operator)
    
    save_to_txtfile(answer)

if __name__ == "__main__":    #calling the main function
    main()
