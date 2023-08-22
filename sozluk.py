from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.firefox.options import Options
import sys
import json

options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)
driver.get("http://www.dildernegi.org.tr/TR,274/turkce-sozluk-ara-bul.html")

def getWordsOfLetter(letter, num):
    elem = driver.find_element(By.ID, "txtSozlukText")
    elem.clear()
    elem.send_keys(letter)
    elem.send_keys(Keys.RETURN)

    words = []

    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="divWait1"][contains(@style, "display: none")]')))
    worde = driver.find_element(By.XPATH, '//*[@id="upSozluk"]/div/table/tbody/tr[1]/td[1]/a')
    print(worde.text)
    counter = 1
    wordcount = 1
    columns = 3
    if num < columns:
        columns = num
    while wordcount <= num:
        try:
            for i in range(columns):
                worde = driver.find_element(By.XPATH, '//*[@id="upSozluk"]/div/table/tbody/tr['+str(counter)+']/td['+str(i+1)+']/a')
                words.append(worde.text.split(",")[0].split(" ")[0])
                wordcount += 1
        except NoSuchElementException:
            break

        counter += 1
    
    return words

def getAllWords(totalnum):
    words = []
    letters = "abcçdefghıijklmnoöprsştuüvyz"
    
    if totalnum < len(letters):
        for i in range(totalnum):
            wordslet = getWordsOfLetter(letters[i], 1)
            words += wordslet
    else:
        for letter in letters:
            wordslet = getWordsOfLetter(letter, int(totalnum/len(letters)))
            words += wordslet
        if len(words) < totalnum:
            for i in range(totalnum-(len(words)*len(letters))):
                wordsfill = getWordsOfLetter(letters[i], 1)
                words += wordsfill

    driver.quit()

    words = [word.lower() for word in words]

    return sorted(words)

words = getAllWords(int(sys.argv[1]))
print(words)
dictionary = {
    "dictionary": words
}

with open("dict.json", "w", encoding="utf-8") as dictfile:
    json.dump(dictionary, dictfile, ensure_ascii=False)