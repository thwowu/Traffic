import pandas as pd
from dateutil.parser import parse
import numpy as np
from nltk.tokenize import TweetTokenizer,  word_tokenize
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline

# Reading user_agent information, and return the system info. 

def system(text):
    
    if text == "Carbon":
        return "Carbon"
        
    elif text == "AdsBot-Google (+http://www.google.com/adsbot.html)":
        return "AdsBot-Google"
    
    else:   
        d= text.split('/')
        
        if d[0] == "Sogou web spider":
            return "Sogou"
    
        elif d[0] == "WordPress":
            return "WordPress"
    
        elif d[0] == "facebookexternalhit":
            return "facebookexternalhit"
        
        else:
            words = word_tokenize(d[1])
        
            if words[2] == "compatible":
                
                if words[4] is ")":
                    return ""
                else:
                    if words[4] == "Linux" or words[4] == "X11":
                        return "Android"
                    else:
                        return words[4]

            else:
                if words[2] == "Linux" or words[2] == "X11":
                    return "Android"
                else:
                    return words[2]

# Further categorize the system types into devices

def device(input):
    bot = ['AdsBot-Google', 'BLEXBot', 'Carbon', 'Exabot',
           'Facebot', 'Googlebot', 'MSIE', 'Sogou', 'WordPress', 
           'YandexBot', 'adidxbot', 'bingbot', 'coccocbot-web',
           'facebookexternalhit']
    mobile = ['Android', 'iPad', 'iPhone']
    desktop = ['Macintosh','Windows']
    
    if input in mobile:
        return "mobile"
    elif input in desktop:
        return "desktop"
    else:
        return "bot"

# extraiting tagging information from target url, reconstructing them into a list

import sys

def url_sp(text):
    d = text.split('&')

    if len(d) > 1:
        try:
            k = d[0].split('?')
            nn = k[1].split('=')
            del d[0]
            doubled = [num.split('=') for num in d if '=' in num]
            return nn + sum(doubled, [])
            
        except:
            print(sys.exc_info()[0],"occured.")
            print(d)

    else:
        #print(text)
        k = d[0].split('?')
        if len(k) > 1:
            nn = k[1].split('=')
            return nn 

# read the data and add new attributes 
data['time'] = data['@timestamp'].apply(lambda x: parse(x)) 
data['system'] = data['user_agent'].apply(lambda x: system(x))  
data['trait'] = data['target_url'].apply(lambda x: url_sp(x))  
data['device'] = data['system'].apply(lambda x: device(x))  
