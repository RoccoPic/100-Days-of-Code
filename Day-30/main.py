#FileNotFound

try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["DLSJLFJSD"])
except FileNotFoundError:
    file = open("a_file.txt","w")
except KeyError as error_message:
    print(f"The key {error_message} does not exist")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File was closed")