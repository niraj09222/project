
import csv

from func import findPresence
from func import getCsvInput
from fileIO import fileReader
from fileIO import fileWriter,outputWriter
import threading

from harvester import fb_harvester,google_harvester,twitter_harvester,instagram_harvester,linkedin_harvester


import pprint

#path = "data.csv"       #path of .csv input file                         
path = raw_input("Enter csv filename as <filename>.csv:")
pp = pprint.PrettyPrinter(indent=4)


input_list = getCsvInput(path)

output = []
output2 = []



def harvest(argument,url):
    if argument == "instagram.com" :
        return instagram_harvester(argument,url)
    elif argument == "facebook.com" :
        return fb_harvester(argument,url)
    elif argument == "plus.google.com" :
        return google_harvester(argument,url)
    elif argument == "linkedin.com" :
        return linkedin_harvester(argument,url)
    elif argument == "twitter.com" :
        return twitter_harvester(argument,url)
    
class myThread (threading.Thread):
    def __init__(self,i):
        threading.Thread.__init__(self)
        
        self.name = i
    def run(self):
        print "Starting " + self.name
        ThreadHandler(self.name)
        print "Exiting " + self.name

    
final_output=[]
def ThreadHandler(i):
    fileWriter(i)
    output3=[]
    output3.append(findPresence(i))
    for i in output3:
        op = i["online_presence"]
        for j in op:
            print op[j]["url"]
            op[j] = harvest(j,op[j]["url"])
    final_output.append(i)
    outputWriter(i)
thread=[]
j=0
for i in input_list:
   thread.append(myThread(i))

for i in thread:  
    i.start()
    
for i in thread:  
    i.join()    
pp.pprint(final_output)
print "main exiting!"