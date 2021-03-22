#!/usr/bin/python3
import requests
import os
from time import ctime
from random import randint
from tqdm import tqdm

ffmpeg_path = 'C:/ffmpeg/bin/ffmpeg.exe'

alblum = 'TTS'
artist = 'amogha0x00'
year = ctime()[-4:]
home = os.getenv('HOME')
user_agents = [
'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
'Mozilla/5.0 (X11; U; Linux Core i7-4980HQ; de; rv:32.0; compatible; JobboerseBot; http://www.jobboerse.com/bot.htm) Gecko/20100101 Firefox/38.0',
'Mozilla/5.0 (X11; U; Linux Core i7-4980HQ; de; rv:32.0; compatible; JobboerseBot; https://www.jobboerse.com/bot.htm) Gecko/20100101 Firefox/38.0',
'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:49.0) Gecko/20100101 Firefox/49.0',
'Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0',
'Mozilla/5.0 (X11; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0',
'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:21.0) Gecko/20130331 Firefox/21.0',
'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
'Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36',
'Mozilla/5.0 (Linux; Android 6.0.1; SM-G532M Build/MMB29T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36',
]

def mkdir(path):
    if not os.path.exists(path):
        os.makedirs(path)

def ask_usr():

    #Config
    #save_path = '{HOME}/Music/'.format(HOME=home)
    save_path = ''
    down_path = '.tts_tmp/'
    url = 'https://translate.google.com/translate_tts'
    LANG_MAP = {'afrikaans': 'af', 'albanian': 'sq', 'amharic': 'am', 'arabic': 'ar', 'armenian': 'hy', 'azerbaijani': 'az', 'basque': 'eu', 'belarusian': 'be', 'bengali': 'bn', 'bosnian': 'bs', 'bulgarian': 'bg', 'catalan': 'ca', 'cebuano': 'ceb', 'chichewa': 'ny', 'chinese (simplified)': 'zh-cn', 'chinese (traditional)': 'zh-tw', 'corsican': 'co', 'croatian': 'hr', 'czech': 'cs', 'danish': 'da', 'dutch': 'nl', 'english': 'en', 'esperanto': 'eo', 'estonian': 'et', 'filipino': 'tl', 'finnish': 'fi', 'french': 'fr', 'frisian': 'fy', 'galician': 'gl', 'georgian': 'ka', 'german': 'de', 'greek': 'el', 'gujarati': 'gu', 'haitian creole': 'ht', 'hausa': 'ha', 'hawaiian': 'haw', 'hebrew': 'iw', 'hindi': 'hi', 'hmong': 'hmn', 'hungarian': 'hu', 'icelandic': 'is', 'igbo': 'ig', 'indonesian': 'id', 'irish': 'ga', 'italian': 'it', 'japanese': 'ja', 'javanese': 'jw', 'kannada': 'kn', 'kazakh': 'kk', 'khmer': 'km', 'korean': 'ko', 'kurdish (kurmanji)': 'ku', 'kyrgyz': 'ky', 'lao': 'lo', 'latin': 'la', 'latvian': 'lv', 'lithuanian': 'lt', 'luxembourgish': 'lb', 'macedonian': 'mk', 'malagasy': 'mg', 'malay': 'ms', 'malayalam': 'ml', 'maltese': 'mt', 'maori': 'mi', 'marathi': 'mr', 'mongolian': 'mn', 'myanmar (burmese)': 'my', 'nepali': 'ne', 'norwegian': 'no', 'pashto': 'ps', 'persian': 'fa', 'polish': 'pl', 'portuguese': 'pt', 'punjabi': 'pa', 'romanian': 'ro', 'russian': 'ru', 'samoan': 'sm', 'scots gaelic': 'gd', 'serbian': 'sr', 'sesotho': 'st', 'shona': 'sn', 'sindhi': 'sd', 'sinhala': 'si', 'slovak': 'sk', 'slovenian': 'sl', 'somali': 'so', 'spanish': 'es', 'sundanese': 'su', 'swahili': 'sw', 'swedish': 'sv', 'tajik': 'tg', 'tamil': 'ta', 'telugu': 'te', 'thai': 'th', 'turkish': 'tr', 'ukrainian': 'uk', 'urdu': 'ur', 'uzbek': 'uz', 'vietnamese': 'vi', 'welsh': 'cy', 'xhosa': 'xh', 'yiddish': 'yi', 'yoruba': 'yo', 'zulu': 'zu', 'Filipino': 'fil', 'Hebrew': 'he'}
    params = {
        'ie': 'UTF-8',
        'q': '',
        'tl': LANG_MAP['english'],
        'client': 'gtx'
    }
    option = input("File(f) or terminal?(t)? : ").lower()
    if option == 'f':
        #file_path = '{HOME}/.ttosrc'.format(HOME=home)
        
        file_path = input("Path to file(both txt and pdf will work) : ")
        
        #file_path = 'tts_file.txt'#'paper.pdf'#
        
        extention = file_path.split('.')[-1].lower()

        with open(file_path,'rb') as f: #, encoding='utf-8'
            if extention == 'pdf':
                import PyPDF2
                reader = PyPDF2.PdfFileReader(f)
                input_list = ''.join([reader.getPage(i).extractText() for i in range(0, reader.numPages)])
            else:
                input_list = (f.read().decode('UTF-8')) #.encode('UTF-8', 'ignore')
    else:
        input_list = input("Enter the data :\n")
    input_list = input_list.replace('\n', ' ').replace('\r', '')
    if len(input_list) >= 200:
        input_list = input_list.split('.')
    else:
        input_list = [input_list]
    #print(input_list)
    down_audio(url, input_list, params, down_path, save_path)


def down_audio(url, input_list, params, down_path, save_path):
    mkdir(down_path)
    count = 0
    
    # removes first entry if it is empty string and generates title
    while input_list[0] == '':
        input_list.remove('')
    
    title = input_list[0][:input_list[0][10:].find(" ") + 10]
    title = title.replace("*", "_").replace(" ", "_").replace("-", "_")
    
    for sentence in input_list:#, desc='Downloading audio files', unit='sentance'):
        headers = {'User-Agent': user_agents[randint(0, len(user_agents) - 1)]}
        if sentence == '':
           continue
        if len(sentence) >= 200:
            if ',' in sentence:
                sub_sentence = sentence.split(',')
            else:
                sub_sentence = [sentence]
            sentence = []
            for subs in sub_sentence:
                subs_len = len(subs)
                if subs_len >= 200:
                    subs = subs.split()
                    join_words = ''
                    for word in subs:
                        add_words = 1
                        word_len = len(word)
                        join_words_len = len(join_words)
                        if word_len >= 200:
                            print('too lenthy word detected!!')
                            exit()
                        max_len_sen = subs_len//((subs_len//200) + 1)
                        if join_words_len + word_len >= max_len_sen:
                            if join_words_len == 0:
                                sentence.append(word)
                                add_words = 0
                            else:
                                sentence.append(join_words) 
                                join_words = ''
                        if add_words:
                            join_words += ' ' + word
                    sentence.append(join_words)
                else:
                    sentence.append(subs)
        else:
            sentence = [sentence]
        print(sentence)
        for sub_sentence in sentence:
            params['q'] = sub_sentence
            resp = requests.get(url, params=params, headers=headers)
            with open(down_path + "data"+str(count)+".mp3", "wb") as f:
                f.write(resp.content)
            count += 1
        
    merge_audio(count, down_path, save_path, title)


def merge_audio(count, down_path, save_path, title):
    metadata = '-metadata title="{title}" -metadata alblum="{alblum}" -metadata artist="{artist}" -metadata year="{year}" '.format(title=title, alblum=alblum, artist=artist, year=year)
    
    # generates file name from title 
    file_name = title.replace(".", "_").replace(",", "_").replace(":", '-')
    for invalid_char in '"\'*<>?\\|/':
        file_name = file_name.replace(invalid_char, '')
    save_path += file_name
    
    # so that exiting file does not get over writed
    file_count = 0
    if os.path.isfile(save_path + '.mp3'):
        while os.path.isfile(save_path + str(file_count) + '.mp3'):
            file_count += 1
        save_path += str(file_count) + '.mp3'
    else:
        save_path += '.mp3'
    cmd = ffmpeg_path + ' -i ' + down_path + 'data0.mp3 -acodec copy ' + metadata + save_path
    if count > 1:
        cmd = ffmpeg_path +' -y -i "concat:'
        for i in range(count - 1):
            cmd += down_path + 'data' + str(i) + '.mp3|'
        cmd += down_path + 'data' + str(i+1) + '.mp3" -acodec copy ' + metadata + save_path
        
    print('Running : ' + cmd)
    os.system(cmd)
    if input('Remove unwanted files? [y/n] : ').lower() == 'y':
        clean(down_path)

def clean(path):
    cmd = 'rm -rf '+ path
    os.system(cmd)

ask_usr()
