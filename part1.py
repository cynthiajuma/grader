#code works
from string import punctuation
from collections import Counter

#function for TTR for an entire text
def text_TTR(text):
    #open and read file
    with open(text, "r",encoding='utf-8') as F:
        text = F.read()
        lines = text.splitlines()
        tokens = []
    for word in text.split():
        tokens.append(word.strip(punctuation).lower())
    types = Counter(tokens) 
    TTR = len(types)/len(tokens)
    return TTR
print("text TTR:",text_TTR("finalpaper.txt"))

#normalize the function by breaking into chunks
def book_segments(textfile):
    #open and read file
    with open(textfile, "r",encoding='utf-8') as F:
        text = F.read()
        words = text.split()
        segments = []
        n = 2
    for i in range(0, len(words), n):
        segments.append(" ".join(words[i:i+n]))   
    return segments

#find the TTR for segments and return the average TTR
def segments_TTRs(filename):
    with open(filename, "r",encoding='utf-8') as F:
        text = F.read()
        segments = book_segments(filename)
    avg = 0 
    segments_TTRs = {}
    for segment in segments:
        types = Counter(segment[1].split())
        segment_TTR = len(types)/len(segment.split())
        avg += segment_TTR
        
    avg = avg / len(segments)
    return avg
print ("average TTR for segments:",segments_TTRs("finalpaper.txt"))
        