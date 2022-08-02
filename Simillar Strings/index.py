str1 = "This"
str2 = "This"

synonyms1 = [""]
synonyms2 = ["", ""]


def checkSimillar(str1, str2, synonyms1, synonyms2):
    if len(str1.split()) != len(str2.split()):
        return False
    synSet1 = set(synonyms1)
    synSet2 = set(synonyms2)
    hashVal = {}
    for i in str1.split():
        if i in synonyms1:
            hashVal[i] = synSet1
        if i in synonyms2:
            hashVal[i] = synSet2
    print(hashVal)
    for i in range(len(str1.split())):
        word1 = str1.split()[i]
        word2 = str2.split()[i]
        if word1 == word2:
            continue
        if word1 != word2 and (word1 not in hashVal or word2 not in hashVal[word1]):
            return False

    return True


returnVal = checkSimillar(str1, str2, synonyms1, synonyms2)
print(returnVal)
