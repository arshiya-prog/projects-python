import pandas

data = pandas.read_csv("/Users/arshiya/Desktop/Coding/Python/projects-python/NATO_alphabets/nato_phonetic_alphabet.csv")
nato_dict = {row["letter"]:row.code for (index, row) in data.iterrows()}
#you can use both notations, row.column_name or row["column_name"]

user_input = input("Enter your name: ").upper()
code_words = [nato_dict[string] for string in user_input]
print(code_words)