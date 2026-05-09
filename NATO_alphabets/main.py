import pandas

data = pandas.read_csv("/Users/arshiya/Desktop/Coding/Python/Python_Projects/NATO_alphabets/nato_phonetic_alphabet.csv")
nato_dict = {row["letter"]:row.code for (index, row) in data.iterrows()}
#you can use both notations, row.column_name or row["column_name"]

# is_on = True
# while is_on:
#     user_input = input("Enter your name: ").upper()
#     try:
#         code_words = [nato_dict[string] for string in user_input]
#         is_on = False
#     except KeyError:
#         print("Sorry, letters in the alphabet please.\n")
#     else:
#         print(code_words)

def generate_phonetic():
    user_input = input("Enter your name: ").upper()
    try:
        code_words = [nato_dict[string] for string in user_input]
    except:
        print("Sorry, letters in the alphabet please.\n")
        generate_phonetic()
    else:
        print(code_words)

generate_phonetic()