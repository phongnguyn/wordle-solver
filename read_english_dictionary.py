import json
from os import system, name

def clear():
    if name == 'nt':
        _ = system('cls')
clear()

exclude = 'lyachundms'
green = ['p','o',0,0,0]
yellow = {
    'e' : [3]
}
with open('new_words_dictionary.json') as f:
    data = json.load(f) 
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
    if write == True and ans >= len(yellow):
        print(s)