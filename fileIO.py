import requests
from bs4 import BeautifulSoup
import os,errno
from fileinput import filename

def get_filename(site_url):
    s=site_url
    flag = s.find("http://")
    if flag == -1:
        
        filename = s.split('https://')[1]
        
    else:
        filename = s.split('http://')[1]
    
    if filename[len(filename)-1] == "/":
        filename = filename[:-1]
    return filename
    
def fileReader(site_url):
    print "Reader function"
     # Open a file
    folder_name = "./downloaded_site/"
    filename = get_filename(site_url)
    fo = open(folder_name+filename+".txt", "r+")     # open file for read content
    str1 = fo.read();                       # reading file into str1 string
                            # assigning str1 into soup_str
    # Close opend file
    fo.close()                              #closing file
    return str1
    
    
    
def fileWriter(site_url):
    print "Writer function"
    filename = get_filename(site_url)
    
    
    folder_name = "./downloaded_site/"
    if not os.path.exists(os.path.dirname(folder_name)):
        try:
            os.makedirs(os.path.dirname(folder_name))
        except OSError as exc: # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise
    print folder_name+filename+".txt"
    fo = open(folder_name+filename+".txt", "wb")     # open file for writing html content
    
    r = requests.get(site_url)              # load website in r    
    cnt = r.content                         
    s = BeautifulSoup(cnt,'html5lib')       # parse content using html5lib parser
#     soup_str = str(s)
    
    # Open a file
    
    fo.write(str(s));                       # writing all html content into file
    
    # Close opend file
    fo.close()     
def outputWriter(data):
    print "Output Writer function"
    filename = get_filename(data["site_url"])
    
    
    folder_name = "./output_data/"
    if not os.path.exists(os.path.dirname(folder_name)):
        try:
            os.makedirs(os.path.dirname(folder_name))
        except OSError as exc: # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise
    print folder_name+filename+".txt"
    fo = open(folder_name+filename+".txt", "wb")     # open file for writing html content
    
    
    # Open a file
    
    fo.write(str(data));                       # writing all html content into file
    
    # Close opend file
    fo.close()                   