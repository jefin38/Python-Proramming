def word_count(str):
    counts = dict()
    words = str.split()
    for word in words:
        if word in counts:
            counts[word]+=1
        else:
            counts[word] =1
            print(counts)
a =input("enter a string")
word_count(a)
