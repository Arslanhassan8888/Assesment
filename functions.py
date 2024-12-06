def cels_to_fah(value):
    result=(value*(9/5))+32
    return result

def fah_to_cels(value):
    result=(value -32)*(5/9)
    return result

conversion= input("Please enter 'c' if you want to convert from Celsius to Fahrenheit or enter 'f' if you want to convert from Fahrenheit to Celsius: ").lower()

if conversion == 'c':
    try:
        temp_celsius = float(input("Please enter the temperature value: "))
        value_in_fahrenheit = cels_to_fah(temp_celsius)
        print(temp_celsius, "Celsius are", value_in_fahrenheit, "Farhenheit")
    except ValueError:
        print("Invalid temperature value. Please enter a numeric value.")

elif conversion == 'f':
    try:
        temp_fahrenheit = float(input("Please enter the temperature value: "))
        value_in_celsius = fah_to_cels(temp_fahrenheit)
        print(temp_fahrenheit, "Fahrenheit are", value_in_celsius, "Celsius")
    except ValueError:
        print("Invalid temperature value. Please enter a numeric value.")

else:
    print("Invalid entry, please enter 'c' or 'f'")

                         
    
