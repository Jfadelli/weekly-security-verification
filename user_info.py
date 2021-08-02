import os

file_name = "user_info.txt"
user_directory = input("Input directory path: ")

file = open(file_name, "w")
file.write(user_directory)
file.close()
