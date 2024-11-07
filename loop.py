# Input from the user
number = int(input("Enter a non-negative integer: "))

# Check if the input is non-negative
if number < 0:
    print("Please enter a non-negative integer.")
else:
    i = 1
    while i <= number:
        factorial = 1
        j = 1
        while j <= i:
            factorial *= j
            j += 1
        print(i, ":", factorial)
        i += 1

    

