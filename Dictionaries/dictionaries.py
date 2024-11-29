file = open("Fruit.txt", "r") #open a text file called Fruit
text = file.read().lower()  #the text inside the file is placed as lower case adn read mode
file.close()
 
words_list = text.split() #This allow to split the text and create a list called words_list=[apple, banana, strawaberry]


words_dic={}    # I created an empty dictionaries
for i in words_list:   # for loop inside the list (words_list) to read every single words in list one by one
    if i not in words_dic:  #during the reading of each words inside the list, if the word is not in the dictionaries i will count as 1 es. banana:1
        words_dic[i] = 1
    else:
        words_dic[i] += 1 # otherwise, if the word is already in the disctionaries, as key, the count will increase by 1, es banana:2

words_tup = words_dic.items() #this part allow me to convert the content of the disctionaries in tuple, so i can see key(banana) and value(count)---
                            
top_words = sorted(words_tup, key=lambda x: x[1], reverse=True)  #with sorted i can sort from letter A to z or number from 0 to 100, key=lambda is a function  
                                                                #built in phyton in this case using x :x[1] 
 
                                                                #I am going to sort all words in my dictionaries, which are tuple, based on the second value 
                                                                # which is numbers of counting in my tlist of tuple

print(top_words)

for x, y in top_words:  #for loop checking 2 value in my disctionaries and prin them each time

   print(f"{x}: {y}")