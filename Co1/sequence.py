s= input("Enter a sentence:")
print(s)
WordList=s.split()
print(WordList)
for i in WordList:
    print(f"{i}occurs{WordList.count (i)}times")
