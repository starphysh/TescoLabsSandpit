# First Python script to perform basic product search using Tesco Labs API
# The code isn't pretty, but then again, it doesn't have to be

from urllib2 import Request, urlopen, URLError
import json

MyDeveloperKey = "MIJXuSC6HkkDseMvjojb"
MyApplicationKey = "E5EBD59C5535F426DEEF"
LoginURL = 'https://secure.techfortesco.com/tescolabsapi/restservice.aspx?command=LOGIN&email=&password=&developerkey='
SearchURL = 'https://secure.techfortesco.com/tescolabsapi/restservice.aspx?command=PRODUCTSEARCH&searchtext='
    
LoginRequest = Request(LoginURL+MyDeveloperKey+'&applicationkey='+MyApplicationKey)

# Try and login to TescoLabs and obtain a Session Key
try:
	response = urlopen(LoginRequest)
	kittens = response.read()
	kittens_dict = json.loads(kittens)
	SessionKey = kittens_dict['SessionKey']
	print
	print 'Successfully logged in to TescoLabs API and obtained a Session Key'
	# print 'Session Key = [',SessionKey,']'
	print
except URLError, e:
    print 'No kittez. Got an error code:', e
    
# Lets try and lookup some products!
print "You've just entered Tesco's front door!"
product = raw_input("Type the product you want to search for and hit 'Enter'   : ").lower()
SearchRequest = Request(SearchURL+product+'&page=1&sessionkey='+SessionKey)

# Try and search for the product
try:
	response = urlopen(SearchRequest)
	product_list_raw = response.read()
	product_list = json.loads(product_list_raw)
	NumberOfThingsFound = product_list['TotalProductCount']	
	NumberOfThingsOnPage = product_list['PageProductCount']
except URLError, e:
    print 'No kittez. Got an error code:', e

if NumberOfThingsFound == 0 :
	# Boo - nothing to see here....
	print
	print 'Sorry - no ', product, 'found'
	print
	exit
else:
	# Hooray - we must have found something they stock!! 
	print
	# print product_list_raw
	print 'Successfully searched and found', NumberOfThingsFound, product, 'products. Here are the first ', NumberOfThingsOnPage

	for num in range(0, NumberOfThingsOnPage):
		print 'Product #:', num+1, product_list['Products'][num]['Name'], product_list['Products'][num]['PriceDescription']	
	print

