import re
import os
import xmltodict, json

import urllib.request 
from PIL import Image 
import requests


i = 0
with open('AI db7.txt', 'r', encoding='utf-8') as fp:
    contents = fp.readlines()
    ##catalog = line.split(',')[0]
    for line in contents:
        element = line.split(',True,')
        catalog = element[1]

        #print(element[0])
        ##print(catalog)
        #if "hat" in catalog.lower(): continue
        if "garment" in catalog.lower(): continue

        x = re.findall('path="img/[^ ]*"', catalog)
        # x = re.findall('path=', catalog)
        # print(x)
        #i += 1
        # print(i)

        #o = xmltodict.parse(catalog)
        ##json.dumps(o) # '{"e": {"a": ["text", "text"]}}'
       #print(o)
        
        #if  i == 1: break

        if x:
            style = element[0].split(',')[0]
            print(style + ',')
            #res = len(catalog.encode('utf-8'))
            #print(x)
            n = 0
            for url in x:
                #print(url)
                path = url.split('=')[1].replace('"','')
                path = 'https://embed.widencdn.net/' + path
                path = path + "?position=S&crop=no&color=F2F2F2"
                print(path)
                if not os.path.exists("input\style-" + style): 
      
                    # if the demo_folder directory is not present  
                    # then create it. 
                    os.makedirs("input\style-" + style) 
                    #urllib.request.urlretrieve(path, "shoe-" + str(n) + ".jpeg")

                response = requests.get(path)
                with open("input\style-" + style + "/" + "item-" + str(n) + ".jpeg", 'wb') as file:
                    file.write(response.content)

                # with open("input\style-" + style + "/" + "shoe-" + str(n) + ".jpeg", '+w') as text:
                #     text.write(file_text)

                n += 1 
                    

            #print('size = ' + str(res))
            i += 1
            print(i)
