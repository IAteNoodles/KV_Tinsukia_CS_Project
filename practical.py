# Read a text file line by line and display each word separated by a #.
def question_1():
    with open(r"/content/drive/MyDrive/Practical/Q1_Source.txt") as file_handle:
        print("Text from the file:\n", open(r"/content/drive/MyDrive/Practical/Q1_Source.txt").read(), sep="")
        lines = file_handle.readlines()  # Reads all the lines and stores them as a list
        for line in lines:  # Extracts a single line from the list one by one and loops
            for word in line.split():  # Splits the string and extracts words one by one
                print(word + "# ", end="")
            print()


# Read a text file and display the number of vowels/consonants/uppercase/lowercase characters in the file
def question_2():
    vowels = ["a", "e", "i", "o", "u"]
    count = {"vowels": 0, "consonants": 0, "uppercase": 0, "lowercase": 0}
    with open(r"/content/drive/MyDrive/Practical/Q2_Source.txt") as file_handle:
        lines = file_handle.read()
        print("Text from the file:\n", lines, sep="")
        for letter in lines:  # Extracts a letter each time and runs a check
            if letter.isupper():
                count["uppercase"] += 1
            else:
                count["lowercase"] += 1
            if letter.lower() in vowels:
                count["vowels"] += 1
            else:
                count["consonants"] += 1
    print("Instances found:")
    for key in count:
        print(key, ":", count[key])


# Remove all the lines that contain the character 's" in a file and write it to another file.
def question_3():
    with open(r"/content/drive/MyDrive/Practical/Q3_Source.txt") as file_handle:
        print("Text from the file:\n", file_handle.read(), sep="")
        lines = file_handle.readlines()  # Reads all the lines and stores them as a list
        print("After refactoring:")
        for line in lines:  # Extracts a single line from the list one by one and loops
            if "s" in line.lower():
                continue
            print(line)


question_1()
question_2()
question_3()
