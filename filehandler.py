input_file = open('students_input.txt', 'w')
input_file.write("Paul, Intro to programming, 50, 25\n")
input_file.write("Paul, Web Scripting, 60, 25\n")
input_file.write("Paul, Web Development, 70, 50\n")
input_file.write("\n")
input_file.write("Mike, Intro to programming, 70, 40\n")
input_file.write("Mike, Web Scripting, 50, 25\n")
input_file.write("Mike, Web Development, 40, 20\n")
input_file.close()

output_file = open('students_output.txt', 'r')
print(output_file.read())
output_file.close()

list1=[name,mark,weight]

def calculate_grade(weighted_mark):
        if weighted_mark >= 70:
            return "Distinction"
        elif weighted_mark >= 60:
            return "Merit"
        elif weighted_mark >= 50:
            return "Pass"
        else:
            return "Fail"


input_file =open('students_input.txt','r')
for line in input_life:
    parts = line.split(', ')
    name = parts[0]  
    mark = int(parts[1])  
    weight = float(parts[2])        
input_file.close()

output_file= open('students_outputs,txt', 'w')
for name, marks_weights in list1():
    total = (mark * (weight / 100) 
    grade = calculate_grade(total)
    output_file_obj.write(name, total, grade\n)
output_file_obj.close()





