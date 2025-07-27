sen=input("Enter a sentence: ")
char=input("Enter a letter to filter : ")

words=sen.split()
def sen_len(word_list):
    return len(word_list)

totWords=sen_len(words)
print("Total words: ",totWords)

def sen_long(word_list):
    long_words=[]
    for word in word_list:
      if len(word) > 5:
        long_words.append(word)
    return long_words

def Filter(word_list,character):
    filtered_words=[word for word in word_list if char in word]
    return filtered_words


senLong=sen_long(words)
print("words longer than 5 letters:",len(senLong),"->",senLong)

filtered_words=Filter(words,char)
print(f"Words containing '{char}': {filtered_words}")