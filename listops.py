my_list = [10, 20, 30, 40, 50, 70, 80, 90, 100, 110]

def full_list(my_list):
   
    print("List:", my_list)

def calculate_sum(my_list):
    
    print("The sum of the list is:", sum(my_list))
    
largest = max(my_list)
smallest = min(my_list)
def largest_number(my_list):
    print(f"The largest number of the list is: {largest}") 

def smallest_number(my_list):
    print(f"The samllest number of the list is: {smallest}") 

def reverse_list(lst):
    my_list.reverse()
    print("List in reverse order:", my_list)



full_list(my_list)
calculate_sum(my_list)
largest_number(my_list)
smallest_number(my_list)

reverse_list(my_list)
# print again the largest and smallest in the reversed list
largest_number(my_list)
smallest_number(my_list)
