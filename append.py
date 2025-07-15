filename = "output.txt"
user_input = input("Enter text to write to the file: ")
with open(filename, "w") as file:
    file.write(user_input + "\n")
print("Data successfully written to output.txt.")
additional_input = input("Enter additional text to append: ")
with open(filename, "a") as file:
    file.write(additional_input + "\n")
print("Data successfully appended.")
print("\nFinal content of output.txt:")
with open(filename, "r") as file:
    for line in file:
        print(line.strip())