#Opening a file
# file = open("Week 4/Wadoh.txt", "r")
# print(file)

#Reading a file
#Method 1:
# file = open("Week 4/Wadoh.txt", "r")
# content = file.read()
# print(content)
# file.close()

#Method 2: Using 'with'
# with open("Week 4/Wadoh.txt", "r") as file:
#     content = file.read()
#     print(content)

#Reading line by line:
# with open("Week 4/Wadoh.txt", "r") as file:
#     content = file.readlines()
#     print(content)

#Listing line after line without spacing:
# with open("Week 4/Wadoh.txt", "r") as file:
#     for line in file:
#         print(line.strip())

#Appending a file
# with open("Week 4/Wadoh.txt", "a") as file:
#     content = file.write("Hello Python!") 
#     print("content appended successfully")

#Appending in the next line
with open("Week 4/Wadoh.txt", "a") as file:
    content = file.write("\nWe move regardless!") 

#Appending Multiple lines
lines_to_append = [
    "\nI have a wife."
    "\nHer name is Wairimu."
    "\nWe have two kids and we're so in love."
]
with open("Week 4/Wadoh.txt", "a") as file:
    content = file.writelines(lines_to_append) 

print("Multiple lines appended")
