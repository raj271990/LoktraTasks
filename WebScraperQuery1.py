import requests
from bs4 import BeautifulSoup

def searchKeyword(keyword):
    # create the url
    url = 'http://www.shopping.com/products?KW=' + str(keyword)
    # get source code
    source_code = requests.get(url)
    plane_text = source_code.text
    # convert to BeautifulSoup object
    soup = BeautifulSoup(source_code.text, "html.parser")
    # get the list of all span elements
    totalResults = soup.find_all('span')
    # this variable checks for existence of keyword
    keyExists = 0
    # loop through the list of span elements and print when span tag has name attribute
    for result in totalResults:
        value=result.get('name')
        if value != None:
             print value.split(":")[1]
             keyExists = 1

    # if the keyword is not found
    if not keyExists:
        results = soup.find_all('div', {"class": "rtCol"})
        suggestions = soup.find_all('div', {"class":"rtColSuggest"})
        for result in results:
            try:
                print result.contents[1].text
            except:
                pass
        for suggestion in suggestions:
            print suggestion.text
# end of function

##################### Test Cases ####################################################################

#Test Case 1 - Keyword found
# searchKeyword("mobiles")

#Test Case 2 - Keyword not found
# searchKeyword("!@#")

################################# Points of concern ##################################################

# When keyword "123" is searched with an aim of not finding any result for a particular key,
# then in the BeautifulSoup object that get returned, contains 1 as NumItemsReturned. So scraper
# returns 1. But on website it sometimes shows no results of sometimes shows some results

# When keyword "mobiles" is searched the result on the website is not same always. Sometimes shows 704
# and sometimes 1500

# This unstability might be some other keys as well

# Seems some unstability with search API