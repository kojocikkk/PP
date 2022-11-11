# Word counter. Below the code which check the sentiment of text.
# first he code count the words in positive and negative comments.
# Then You can write Your comment and after that aplication shows what kind of sentence You wrote.
# No data to check sentiment chech ( for now).

import glob
import os
POSITIVE = r'data/aclImdb/train/pos/*.txt'
NEGAVITE = r'data/aclImdb/train/neg/*.txt'
positive_files =glob.glob(POSITIVE)
negative_files= glob.glob(NEGAVITE)

#print(positive_files)
negative_comments= []
positive_comments=[]

zdanie = input('Podaj slowo do sprawdzenia: ')
zdanie = zdanie.lower().split()

for file in positive_files:
    with open(file, 'r',encoding='utf-8' )as p_stream:
        positive= p_stream.read().lower().replace('<br />',' ')

        positive_comments.append(positive.split())

for file in negative_files:
    with open(file, 'r',encoding='utf-8' )as p_stream:
        negative= p_stream.read().lower().replace('<br />',' ')
        negative_comments.append(negative.split())
sentence_sentiment = 0

for word in zdanie:
    counter_p = 0
    counter_n = 0
    for wyraz in positive_comments:
        #for znak in word:
        if word in wyraz:
            counter_p +=1 
    
    for wyraz in negative_comments:
        #for znak in word:
        if word in wyraz:
            counter_n +=1 

    counter_a =counter_p + counter_n

    word_sentiment = (counter_p-counter_n) / counter_a

    
    sentence_sentiment +=word_sentiment
    score= sentence_sentiment /len(zdanie)

    print(word, word_sentiment)
    if counter_a !=0 :
        word_sentiment = (counter_p-counter_n) / counter_a
    else:
        word_sentiment = 0.0


if score > 0.0:
    print("Komentarz jest pozytywny ")
else:
    print("Komentarz jest negatywny ")
print(score)
