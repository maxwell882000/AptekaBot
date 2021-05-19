import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
def get(url):
    t = BeautifulSoup(requests.get(url).content, features="lxml")
    
    m = t.find('meta', {'property':"twitter:title"})
    message = ''
    m = str(m)
    for i in m[15:]:
        if i == " ":
            break
        else:
            message += i
    return message
a = []
for i in range(9101, 11782): 
    print(i)
    text = get('https://telegram.me/figaroooo/{}'.format(str(i)))
    a.append(text)
p = pd.Series(a)

print(p.value_counts())

