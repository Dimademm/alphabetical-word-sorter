fileName = input("Enter file: ")

try:
    with open(fileName, "r") as file:
        wordsList = []

        for line in file:
            words = line.split()
            for word in words:
                if word not in wordsList:
                    wordsList.append(word)

    wordsList.sort()
    print(wordsList)
except FileNotFoundError:
    print(f"File '{fileName}' not found.")