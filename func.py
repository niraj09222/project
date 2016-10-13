
import re
import csv
from fileIO import fileReader
import pprint

from bs4 import BeautifulSoup

def getCsvInput(path):
    print "Gettint CSV Input"
    input_list = []               
    csvfile = open(path)                        # open .csv file
    readCSV = csv.reader(csvfile,delimiter=',') #reading input file in list and seperating with ','(comma)
    
    for i in readCSV:
        if i[0] != "":
            input_list.append(i[0])     #creating list of website for processing
    csvfile.close()
    return input_list 


def findPresence(site_url):                 # function to find presence of website 
    print "running:" + site_url 
    
    soup_str = fileReader(site_url)
    
   
    
    # dictionary of regex for searching
    url_templates = {'twitter.com': 'twitter\.com\/(#!\/)?[a-zA-Z0-9_]+',\
                     'facebook.com': 'facebook\.com\/(#!\/)?[a-zA-Z0-9_]+',\
            'linkedin.com': 'linkedin.com/[a-zA-Z0-9_]+',\
            'plus.google.com': 'plus.google.com/+',\
            'instagram.com': 'instagram.com/[a-zA-Z0-9_]+'}

#     for itr in url_templates:
#         print url_templates[itr]
    soup = BeautifulSoup(soup_str,'html5lib')
    urls_all=[]
    for link in soup.findAll('a'):
        urls_all.append(str(link.get('href')))
            
    urls_http=set(re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', soup_str))
    urls_non_http = set(urls_all).difference(urls_http)
    urls=[]
#     for i in urls_non_http:
#         if site_url[len(site_url)-1] == "/":
#             site_url = site_url[:-1]
#         urls.append(get_redirected_url(site_url + i))
#     urls.append(urls_http)
#     print urls
    urls = urls_http
    presence = {}
    res=[]
    #initialisation of output dictionary
    dict= {'site_url' : '',\
            'online_presence' : {}}
    
    
    # search for website presence and save in dictionary
    for i in url_templates:
        for j in urls:
            r=re.findall(url_templates[i],j)
            
            dict['site_url'] = site_url
            if r !=[]:
                #dict = {'online_presence' : {i:{'url':j}}}
                dict['online_presence'][i] = {'url':j}
    
    return dict          
            