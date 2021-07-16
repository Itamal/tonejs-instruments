# -*- coding: utf-8 -*-
"""
Created on Sun Jul 11 21:57:17 2021

@author: Ita
"""
from bs4 import BeautifulSoup
import urllib.request
import re


dictionary =     {'-' : '-',
                  'A' : 'A4',
                  'B' : 'B4',
                  'C' : 'C4',
                  'D' : 'D4',
                  'E' : 'E4',
                  'F' : 'F4',
                  'G' : 'G4',
                  'Ab' : 'Ab4',
                  'Bb' : 'Bb4',
                  'Cb' : 'Cb4',
                  'Db' : 'Db4',
                  'Eb' : 'Eb4',
                  'Fb' : 'Fb4',
                  'Gb' : 'Gb4',
                  'A#' : 'A#4',
                  'B#' : 'B#4',
                  'C#' : 'C#4',
                  'D#' : 'D#4',
                  'E#' : 'E#4',
                  'F#' : 'F#4',
                  'G#' : 'G#4',
                  
                  '^A' : 'A5',
                  '^B' : 'B5',
                  '^C' : 'C5',
                  '^D' : 'D5',
                  '^E' : 'E5',
                  '^F' : 'F5',
                  '^G' : 'G5',
                  '^Ab' : 'Ab5',
                  '^Bb' : 'Bb5',
                  '^Cb' : 'Cb5',
                  '^Db' : 'Db5',
                  '^Eb' : 'Eb5',
                  '^Fb' : 'Fb5',
                  '^Gb' : 'Gb5',
                  '^A#' : 'A#5',
                  '^B#' : 'B#5',
                  '^C#' : 'C#5',
                  '^D#' : 'D#5',
                  '^E#' : 'E#5',
                  '^F#' : 'F#5',
                  '^G#' : 'G#5',
                  
                  '.A' : 'A3',
                  '.B' : 'B3',
                  '.C' : 'C3',
                  '.D' : 'D3',
                  '.E' : 'E3',
                  '.F' : 'F3',
                  '.G' : 'G3',
                  '.Ab' : 'Ab3',
                  '.Bb' : 'Bb3',
                  '.Cb' : 'Cb3',
                  '.Db' : 'Db3',
                  '.Eb' : 'Eb3',
                  '.Fb' : 'Fb3',
                  '.Gb' : 'Gb3',
                  '.A#' : 'A#3',
                  '.B#' : 'B#3',
                  '.C#' : 'C#3',
                  '.D#' : 'D#3',
                  '.E#' : 'E#3',
                  '.F#' : 'F#3',
                  '.G#' : 'G#3',
                  
                  '*A' : 'A6',
                  '*B' : 'B6',
                  '*C' : 'C6',
                  '*D' : 'D6',
                  '*E' : 'E6',
                  '*F' : 'F6',
                  '*G' : 'G6',
                  '*Ab' : 'Ab6',
                  '*Bb' : 'Bb6',
                  '*Cb' : 'Cb6',
                  '*Db' : 'Db6',
                  '*Eb' : 'Eb6',
                  '*Fb' : 'Fb6',
                  '*Gb' : 'Gb6',
                  '*A#' : 'A#6',
                  '*B#' : 'B#6',
                  '*C#' : 'C#6',
                  '*D#' : 'D#6',
                  '*E#' : 'E#6',
                  '*F#' : 'F#6',
                  '*G#' : 'G#6',
    }

urls = [
        'https://noobnotes.net/a-whole-new-world-aladdin/',
        'https://noobnotes.net/tale-as-old-as-time-beauty-beast-disney/',
        'https://noobnotes.net/colors-wind-pocahontas-disney/',
        'https://noobnotes.net/prince-ali-aladdin-disney/',
        'https://noobnotes.net/under-the-sea-the-little-mermaid-disney/',
        'https://noobnotes.net/circle-life-lion-king-disney/',
        'https://noobnotes.net/remember-me-coco-disney/',
        'https://noobnotes.net/when-you-wish-upon-a-star-pinocchio-disney/',
        'https://noobnotes.net/the-bare-necessities-the-jungle-book/',
        'https://noobnotes.net/close-to-you-carpenters/',
        'https://noobnotes.net/youve-got-friend-toy-story-disney/'
        ]
songs = []

def get_and_translate(url):
    print('running on ', url)
    source = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(source, 'html.parser')
    mini1 = soup.findAll('div', {'class':'post-content'})
    soup2 = BeautifulSoup(str(mini1[0]), "html.parser")
    mini2 = soup2.findAll('p')
    
    result = []
    for elem in mini2:
        if len(elem) > 1:
            j = 0
            for i in elem:
                if (j == 0):
                    i = str(i).replace("<br/>", "")

                    if (str(i)[0] == '<'): 
                        i = str(i)[str(i).find('>')+1:str(i).rfind('<')]
                    temp = str(i).replace("-", " - ")
                    temp = str(temp)
                    for u in range(7):
                        #print(temp)
                        temp = temp.replace("\xa0", " ")
                        temp = temp.replace("  "," ")
                        temp = temp.strip()
                    #print(temp)
                    #print(re.split(' ', temp))
                    result += re.split(' ', temp)
                    # print(result)
                    #print('~~$$$$~~~~~~~',j,i)
                j += 1
    
    name = re.split('/', url)
    name = name[len(name)-2]
    final_res = [name.replace("-"," ")]
    for i in range(0,len(result)):
        if result[i] in dictionary:
            final_res.append(dictionary[result[i]])
        else:
            print('~ oh no!',result[i], name)
            return 'BAD BAD BAD BAD'
    print('query succesful on', url)
    return final_res

for i in range(0,len(urls)):
    songs.append(get_and_translate(urls[i]))
    
print(songs)