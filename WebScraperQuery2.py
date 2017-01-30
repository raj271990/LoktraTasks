# importing required classes
import requests
from bs4 import BeautifulSoup

def allResultsPerPage(keyword, pagenumber):
    # Create the url
    url = 'http://www.shopping.com/products~PG-' + str(pagenumber) + '?KW=' + str(keyword)
    # get source code
    source_code = requests.get(url)
    plane_text = source_code.text
    # convert to BeautifulSoup object
    soup = BeautifulSoup(plane_text, "html.parser")
    # get the list of all the products on a page
    allProducts = soup.find_all("a", {"class":"productName "})
    # this variable checks for existence of keyword or existence of page in case key exists
    key_page_Exists = 0
    # loop through the product and print its title and link to the product
    for product in allProducts:
        product_title = product.get('title')
        if product_title != None:
            link_to_prod = 'http://www.shopping.com' + product.get('href')
            print product_title + '\n' + link_to_prod + '\n'
            key_page_Exists = 1


    # if the keyword is not found or page is not found
    if not key_page_Exists:
        results = soup.find_all('div', {"class": "rtCol"})
        suggestions = soup.find_all('div', {"class":"rtColSuggest"})
        for result in results:
            try:
                print result.contents[1].text
            except:
                pass
        for suggestion in suggestions:
            print suggestion.text
# End of function


################################# Test Cases ##################################

# Test Case 1 - Key and page both found
# allResultsPerPage("mobiles", 2)

# Test Case 2 - Key not found
# allResultsPerPage("!@#", 1)

# Test Case 3 - Key exists but page do not exist
# allResultsPerPage("mobiles", 100)
