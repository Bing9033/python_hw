import re

filepath="Resources_pyparagraph/paragraph_1.txt"
wordlen=0
sentencelen=0

with open(filepath, 'r',) as paragraph:
    content=paragraph.read()
    word=content.split(' ')
    sentence=re.split("(?<=[.!?]) +", content)
    word_count = len(word)
    sentence_count=len(sentence)
    for i in word:
        wordlen += len(i)
        
    avgword=wordlen/word_count
    
    for j in sentence:
        words=j.split(' ')
        sentencelen += len(words)
    avgsentence=sentencelen/sentence_count
print("Paragraph Analysis")
print("-----------------")
print("Approximate Word Count:" + str(word_count))
print("Approximate Sentence Count:"+ str(sentence_count))
print("Average Letter Count:"+ "{:.1f}".format(avgword))
print("Average Sentence Length:" + "{:.1f}".format(avgsentence))


