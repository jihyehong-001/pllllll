try:
    message = input("Enter a short note: ")

    with open("notes.txt", "w") as file:
        file.write(message + "\n")

    print("\nSaved successfully!\n")

    print("Reading file content:")
    with open("notes.txt", "r") as file:
        print(file.read())

    new_message = input("\nEnter another note: ")

    with open("notes.txt", "a") as file:
        file.write(new_message + "\n")

    print("\nUpdated file content:")
    with open("notes.txt", "r") as file:
        print(file.read())

except FileNotFoundError:
    print("Error: File not found.")
except Exception as e:
    print("An error occurred:", e)
  
