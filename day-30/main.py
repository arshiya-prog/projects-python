try:
    file = open("/Users/arshiya/Desktop/Coding/Python/projects-python/day-30/file.txt")
    dic = {"Key": "Value"}
    print(dic["Key"])
except FileNotFoundError:
    file = open("/Users/arshiya/Desktop/Coding/Python/projects-python/day-30/file.txt", "w")
    file.write("Something...")
except KeyError as error_msg:
    print(f"The key {error_msg} does not exist.")
else:
    content = file.read()
    print("Something")
finally:
    raise TypeError("This a made-up error.")