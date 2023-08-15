import requests

URL = 'https://sozluk.gov.tr/gts_id?id='
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36"
}
entry_count = 99501

def getWord (word_id):
    res = requests.get(url = URL + str(word_id), headers = headers)
    data = res.json()
    return data[0]["madde"]

def getAllWords (word_count, letter_limit):
    wordList = []
    
    counter = 1
    for c in range(entry_count+1):
        if counter % int(entry_count/word_count) != 0:
            counter = counter+1
            c = c+1
            continue
        word = getWord(counter)
        if len(word) >= letter_limit and ' ' not in word:
            wordList.append(word)
        else:
            c = c-1
        counter = counter+1
    
    wordList.sort()

    return wordList

wordList = getAllWords(10, 3)
print(wordList)