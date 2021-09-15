"""
Возможно, такой вариант  скучный, up to you 
"""
my_file = open("readme.txt", 'a')
my_file.write("cool?")

text = open("readme.txt")
print(text.read())

