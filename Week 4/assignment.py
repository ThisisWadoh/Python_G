# Modifying a file and writing on another file
def modify_file (input_file, output_file):
    try:
        with open("Week 4/Wadoh.txt", "r") as infile:
            content = infile.read()

        #Modify: Convert to CAPS
        modify_content = content.upper()

        #Writing on new file
        with open("Week 4/Output.txt", "w") as outfile:
            outfile.write(modify_content)

        print(f"File successfully modified & written on {output_file}")

    except FileNotFoundError:
        print(f"The file {input_file} was not found.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

input_file = "Week 4/Wadoh.txt"
output_file = "Week 4/Output.txt"

modify_file (input_file, output_file)

#Error Handling Non-Existing Files:
try:
    with open("Wadoh.txt", "r") as file:
        content = file.read()
except:
    print("File not found. Check file location.")
    