with open("file.text",'r') as file:
    text=file.read()
    words=text.split()

    print("\nWords in the file")
    for word in words:
        print(word)
    length = int(input("\nEnter the word length to search for: "))
    found_words = [word for word in words if len(word) == length]
    for word in found_words:
        print(word)
