import csv
import time
import re
from html.parser import HTMLParser  
from urllib.request import urlopen  
from urllib import parse

def SearchingText():
    sitesfile=open("news_site.csv", "r")  #websites collection
    reader = csv.reader(sitesfile)
    for row in reader:
       wordOnTheWebsite(row[0])
       time.sleep(6)
       
def tag_visible(element):
    if element.parent.name in [title', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True


def text_from_html(body):
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)  
    return u" ".join(t.strip() for t in visible_texts)


sitesfile=open("news_site.csv", "r")
    reader = csv.reader(sitesfile)
    for row in reader:
       html = urllib.urlopen(row[0]).read()
       print(text_from_html(html))
