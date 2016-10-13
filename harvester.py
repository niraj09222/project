
import selenium.webdriver as webdriver
import urllib2
from bs4 import BeautifulSoup
import pprint
import requests
import urllib2
import json


def twitter_harvester(twitter_url,link):
    print "twitter harvester called" +  " " + twitter_url +  " " +  link

    try:
        url = link
        driver = webdriver.PhantomJS()
        driver.get(url)
        soup = BeautifulSoup(driver.page_source,'html5lib')
    except:
        print "Error while reading data from twitter"
   
    dict = {}
    try:
        dict["url"] = link
        dict["icon_url"]= str(soup.find_all('img',class_="ProfileAvatar-image")[0]['src'])
        dict["cover_image_url"] = str(soup.find_all('div',class_="ProfileCanopy-headerBg")[0].find_all('img')[0]['src'])
    #     dict["short_description"] = "short description"
        dict["company_overview"] = str(soup.find_all('p',class_="ProfileHeaderCard-bio u-dir")[0].getText())
    #     dict["long_description"] = "long description"
    except:
        print "Error while reading data from twitter"

    return dict

def instagram_harvester(instagram_url,link):
    print "instagram harvester called"  +  " " +  instagram_url +  " " +  link

    try:
        url = link
        driver = webdriver.PhantomJS()
        driver.get(url)
        soup = BeautifulSoup(driver.page_source,'html5lib')
    except:
        print "Error while reading data from instagram"
   
    dict = {}
    try:
        dict["url"] = link
       
        dict["icon_url"]= str(soup.find_all('img',class_="_8gpiy _r43r5")[0]['src'])
    #     dict["cover_image_url"] = "cover image url"
    #     dict["short_description"] = "short description"
    #     dict["company_overview"] = "company overview"
    #     dict["long_description"] = "long description"
    except:
        print "Error while reading data from instagram"

    return dict

def google_harvester(google_url,link):
    print "google harvester called"  +  " " +  google_url +  " " +  link

    try:    
        url = link
        driver = webdriver.PhantomJS()
        driver.get(url)
        soup = BeautifulSoup(driver.page_source,'html5lib')
    
    except:
        print "Error while reading data from google plus"

    dict = {}
    try:
        dict["url"] = link
        dict["icon_url"]= str(soup.find_all('img',class_="fa-kz Zxa")[0]['src'])
        dict["cover_image_url"] = str(soup.find_all('img',class_="aGb hXa z3Hx4b")[0]['src'])
        dict["company_overview"] = str(soup.find_all(itemprop='description')[0]['content'])
    except:
        print "Error while reading data from google plus"

    return dict


def fb_harvester(fb_url,link):
    print "facebook harvester called"  +  " " +  fb_url +  " " +  link
    
    short_description =""
    about =""
    long_description =""

    try:
        
        url = link+"/about/"
        driver = webdriver.PhantomJS()
        driver.get(url)
        soup = BeautifulSoup(driver.page_source,'html5lib')
        
        all_text = soup.find_all('div',class_="_50f4")
        pp = pprint.PrettyPrinter(indent=4)
        
        for i in all_text:
            if i.getText() == "Company Overview":
                about = all_text[all_text.index(i) + 1].getText()
            if i.getText() == "Short description":
                short_description = all_text[all_text.index(i) + 1].getText()
            if i.getText() == "Long description":
                long_description = all_text[all_text.index(i) + 1].getText()
    except:
        print "Error while reading data from facebook1"
    
    dict = {}
    try:
       
        dict["url"] = url
        dict["short_description"] = str(short_description)
        dict["company_overview"] = str(about)
        dict["long_description"] = str(long_description)
        
        try:
           
            dict["icon_url"]= str(soup.find_all('img',class_="profilePic img")[0]['src'])
            dict["cover_image_url"] = str(soup.find_all('img',class_="coverPhotoImg photo img")[0]['src'])
            
        except:
            try:
                
                dict["icon_url"]= str(soup.find_all('img',class_="_4jhq img")[0]['src'])
                dict["cover_image_url"] = str(soup.find_all('img',class_="_4on7 _3mk2 img")[0]['src'])
                
            except:
                print "Error while reading data from facebook3"
    except:
        print "Error while reading data from facebook2"

    return dict




def linkedin_harvester(linkedin_url,link):
    print "linkedin harvester called"  +  " " +  linkedin_url +  " " +  link

    try:
        url=link
        driver = webdriver.PhantomJS()
        driver.get(url)
        soup = BeautifulSoup(driver.page_source,'html5lib')
    except:
        print "Error while reading data from linkedin"
   
   
    dict = {}
    try:
        dict["url"] = link  
        dict["icon_url"]= str(soup.find_all('img',class_="image")[0]['src'])
        dict["cover_image_url"] = str(soup.find_all('img',class_="hero-img")[0]['src'])
       
        dict["company_overview"] = str(soup.find_all('div',class_="specialties")[0].find("p").getText())
       
        dict["long_description"] = str(soup.find_all('div',class_="basic-info-description")[0].find("p").getText())
    except:
        print "Error while reading data from linkedin"

    return dict



