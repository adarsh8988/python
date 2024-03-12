a = ["this is a car", "this is a bus", "this is a train"]
for sentence in a:
    words = []
    start = 0
    for i in range(len(sentence)):
        if sentence[i] == ' ':
            word = sentence[start:i]
            words.append(word)
            start = i + 1
    words.append(sentence[start:])
    print(words)
