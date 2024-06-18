import os

# Simulated user input
user_input = '/etc/passwd'

# Vulnerable code
def read_file(filename):
    file_path = filename
    with open(file_path, 'r') as file:
        content = file.read()
    return content

file_content = read_file(user_input)
print(file_content)
