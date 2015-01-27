'''
Author: Douglas Kelly
Description: This is a web spider which looks at the sec website and creates a few objcts based on pages found there
'''

# Import libs
import requests
import re
import json

# Set up configuration values
govWebsitePrefix = 'http://www.sec.gov'
govWebsite = {'url': govWebsitePrefix + '/divisions/enforce/friactions/friactions2002.shtml'}
websitesToCollect = 5
dictionaryOfWeblinks = {}
listOfWeblinks = []
litigationReGex = '\/litigation/.+.htm'

# Retreive base website
r = requests.get(govWebsite['url'])
govWebsite['html'] = r.text

m = re.findall(litigationReGex, govWebsite['html'])

# Form a list of all the urls found on the website
for i in range(0, websitesToCollect):
    listOfWeblinks.append(m[i])

# Iterate through the list and build the dictionary of urls to objects
for url in listOfWeblinks:
    r = requests.get(govWebsitePrefix + url)
    release = re.findall('Rel. No..+/', r.text)[0]
    release = release.split(' ')[2]
    title = re.findall('<i>Securities and Exchange Commission.+', r.text, re.IGNORECASE)
    if len(title) > 0:
        title = re.findall('Securities and Exchange Commission.+', title[0], re.IGNORECASE)
    else:
        title = 'No title found'

    if(len(re.findall('-', release))):
        release = release.split('-')[1]

    values = re.findall('\$\d+.\d million|billion', r.text)
    standardVals = re.findall('\$\d+,\d+', r.text)

    allValues = values + standardVals
    dictionaryOfWeblinks[url] = {
        'amounts': allValues,
        'case': title[0],
        'release' : int(release)
    }

# Jsonify the dictionary and print to console
print(json.dumps(dictionaryOfWeblinks))

# Run a for loop for good measure over the dictionary and print it out
for key in dictionaryOfWeblinks.keys():
    print('{')
    print(key)
    print(dictionaryOfWeblinks[key])