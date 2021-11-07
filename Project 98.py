def countwordsfromfile():
    fileName = input("Haha Your files have been swapped")
    file = open(fileName,"o")
    numberofwords=0
    for line in file:
        words=line.split()
        numberofwords=numberofwords+len(words)
    print("number of words are")
    print(numberofwords)
countwordsfromfile()