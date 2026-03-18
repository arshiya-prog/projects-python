#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

updated_list = []

with open("/Users/arshiya/Desktop/Coding/Python/projects-python/mail_merge/Input/Letters/starting_letter.txt") as starting_data:
    list_of_lines = starting_data.readlines()

mod_line = list_of_lines[0]
list_of_lines.remove(mod_line)

with open("/Users/arshiya/Desktop/Coding/Python/projects-python/mail_merge/Input/Names/invited_names.txt") as names:
    name_list = names.readlines()   # puts each line as an element in a list

for name in name_list:
    n = name.strip()    # removes the leading and trailing spaces from a string
    updated_list.append(mod_line.replace("[name],\n", f"{n},\n"))     # .replace() replaces the keyword string with the str specified

for i in range(len(name_list)):
    with open(f"/Users/arshiya/Desktop/Coding/Python/projects-python/mail_merge/Output/ReadyToSend/letter_for_{name_list[i]}.txt", "w") as letter:
        letter.write(f"{updated_list[i]}")
        for j in range(len(list_of_lines)):
            letter.write(f"{list_of_lines[j]}")