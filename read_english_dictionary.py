import json
from os import system, name

def clear():
    if name == 'nt':
        _ = system('cls')

exclude = ""
green = [0,0,0,0,0]
yellow = {}
with open('words_dictionary.json') as f:
    data = json.load(f) 
def printres():
    global exclude, green, yellow 
    cnt = 0
    for word in data: 
        s = str(word) 
        i = 0
        write = True
        ans = 0
        for letter in s:
            if type(green[i]) is str:
                if green[i] != letter:
                    write = False
            else:
                for l in yellow:
                    if letter == l:
                        if i + 1 in yellow[l]:
                            write = False
                            break
                        else: ans += 1
            i += 1
            if letter in exclude: 
                write = False
                break
        for letter in yellow:
            if letter not in s:
                write = False
        if write == True and ans >= len(yellow):
            print(s)
            cnt += 1
    print(cnt)
def check(s1, s2):
    global exclude, green, yellow 
    cnt = 0
    for letter in s2:
        s1 = s1.replace(letter.lower(), "")
        if letter != "0":
            if letter.isupper() is True: 
                if letter.lower() in yellow and letter.lower() not in s2:
                    yellow.pop(letter.lower())
                green[cnt] = letter.lower()
            else:
                if letter in yellow:
                    yellow[letter].append(cnt + 1)
                else: yellow[letter] = [cnt + 1]
        cnt += 1
    exclude += s1

while True:
    ex = str(input())
    hint = str(input())
    clear()
    check(ex, hint)
    printres()
    print(exclude)
    print(green)
    print(yellow)