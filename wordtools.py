import re


def cleanword(line):
    wordList2 =[]
    wordList1 = line.split()
    for word in wordList1:
        cleanWord = ""
        for char in word:
            if char in "?+=-!,@$()'":
                char = ""
            cleanWord += char
        wordList2.append(cleanWord)
    return wordList2[0]

def has_dashdash(line):
    for i in range(len(line)-1):
        if line[i] == "-" and line[i+1] == "-":
            return True
    return False

def extract_words(line):
    wordList2 =[]
    wordList1 = line.split()
    for word in wordList1:
        cleanWord = ""
        for char in word:
            if char in "?+=-!,@$()'.":
                char = ""
                if len(cleanWord):
                    wordList2.append(cleanWord)
                    cleanWord = ""
            else:
                cleanWord += char
        if len(cleanWord):
            wordList2.append(cleanWord)
            cleanWord = ""
    print(wordList2)
    return wordList2[0]


def wordcount(word, line):
    count = 0
    for w in line:
        if word == w:
            count += 1
    return count
        

def wordset(line):
    wordList = []
    wordList.append(line[0])
    for word1 in line:
        has = False
        for word2 in wordList:
            if word1 == word2:
                has = True
        if not has:
            wordList.append(word1)
    print(wordList)
    return wordList

def longestword(line):
    mlen = 0
    for word in line:
        le = len(word)
        if mlen < le:
            mlen = le
    return mlen 

print(cleanword("what?") == "what")
print(cleanword("'now!'") == "now")
print(cleanword("?+='w-o-r-d!,@$()'") == "word")
print(has_dashdash("distance--but"))
print(not has_dashdash("several"))
print(has_dashdash("spoke--"))
print(has_dashdash("distance--but"))
print(not has_dashdash("-yo-yo-"))
print(extract_words("Now is the time! 'Now', is the time?Yes, now.") == ['now','is','the','time','now','is','the','time','yes','now'])
print(extract_words("she tried to curtsey as she spoke--fancy") == ['she','tried','to','curtsey','as','she','spoke','fancy'])
print(wordcount("now",["now","is","time","is","now","is","is"]) == 2)
print(wordcount("is",["now","is","time","is","now","the","is"]) == 3)
print(wordcount("time",["now","is","time","is","now","is","is"]) == 1)
print(wordcount("frog",["now","is","time","is","now","is","is"]) == 0)
print(wordset(["now", "is", "time", "is", "now", "is", "is"]) == ["is", "now", "time"])
print(wordset(["I", "a", "a", "is", "a", "is", "I", "am"]) == ["I", "a", "am", "is"])
print(wordset(["or", "a", "am", "is", "are", "be", "but","am"]) == ["a", "am", "are", "be", "but", "is", "or"])
print(longestword(["a", "apple", "pear", "grape"]) == 5)
print(longestword(["a", "am", "I", "be"]) == 2)
print(longestword(["this","supercalifragilisticexpialidocious"]) == 34)
print(longestword([ ]) == 0)