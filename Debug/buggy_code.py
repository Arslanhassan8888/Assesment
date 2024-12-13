"""
This code contains some bugs and some errors.  
Find them and fix them.  
When you are done the program will print a message.
Write the message at the bottom of the code before submission
"""
def extract_and_rearrange(string): # syntax error: def should be separate. Also, I corrtected the name of the function
    str_1 = "".join(reversed(string[0:4].split('g'))).capitalize()
    str_2 = "".join(string[6:13].split('ro')) #split instead of splt
    str_3 = "".join("".join(reversed(list(string[14:20]))).split(string[17]))#Name error of str3 instead of str_3. Missing of double quotes and dot before join outside the parenthesis
    str_4 = "".join(string[21:29].split(string[23:28]))

    return str_1 + " " + str_2 + " " + str_3 + " " + str_4 #missing "+" before "str_4"

def ultra_extrct_and_rearrange(string): #":" was missed at the end of the function
    first_transform = extract_and_rearrange(string)
    return first_transform

print(ultra_extrct_and_rearrange("egthb quirock nwoGrb forijmpxv"))# to correct "andrearrange" and "extract" plus was and extra double quote at the end

"""full debugging, the program show the following message - The quick brown fox - """
