import urllib3
#from urllib3 import requests
#import urllib3.requests
import requests
import json
import webbrowser
import os
import datetime as dt
import subprocess as sp
from requests.exceptions import HTTPError
from bs4 import BeautifulSoup as bs

def get_site():
    site = input('Below please input the article URL: \n')
    return site

def get_method():
    openmethod = input('Do you want to open this in a new tab in Chrome? Y/N').lower()
    return openmethod

def get_content(site):
    #request and retreive article contents in HTML
    res = requests.get(site)
    soup = bs(res.content,'html.parser')
    everything = ''
    #summary list section
    ptct = 1 #setting a bullet point counter
    for a in soup.find_all('ul', {'class':'summary-list'}):
        summary = '''
        Below are the highlights of this article:
        ----------------------------------------------------------------------------------------
        '''
        for b in a:
            summary += f'\n{ptct}. {b.text}\n'
            ptct += 1
    #Whole article section
    okdiv = soup.find_all('div', id = 'piano-inline-content-wrapper')
    for x in okdiv: #soup.find_all('ul', class_= 'summary-list'):
        article = '''
        Below is the actual article:
        ----------------------------------------------------------------------------------------
        '''
        for y in x.find_all('p'):
            article += f'\n{y.get_text()}\n'

    #Combining both summary and article
    everything = summary + article
    return everything

def browser_open(everything):
    #declaring variables in filename
    currtime = dt.datetime.now().strftime('%Y%m%d%H%M')
    title = 'article'
    savefolder = r'C:\Users\wsun\Documents\DailyNews'
    savepath = os.path.join(savefolder,currtime + title + '.txt') #createing file path combining above info
    browloc = r'C:\Program Files (x86)\Google\Chrome\Application\chrome'
    #saving file to the destination 
    file1 = open(savepath, 'w+') #creating a file in designated path
    file1.write(everything) #writing extracted article to saved file
    file1.close() #close file
    #open the txt in chrome 
    sp.call([browloc,savepath])

def open_here(everything):
    print (everything)
    
def execution():
    site = get_site()
    openmethod = get_method()
    everything = get_content(site)
    if openmethod == 'y':
        browser_open(everything)
    elif openmethod == 'n':
        open_here(everything)

