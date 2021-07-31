import bitly_api
from pyshorteners import Shortener
import requests

def expandd():
	short_url =input("Enter the URL: ")
	  
	API_Key = "bdc878983e0877a2739b47fdc92f1cb14766e011"
	    
	print(requests.get(short_url).url)

def shorten():
	BITLY_ACCESS_TOKEN = "bdc878983e0877a2739b47fdc92f1cb14766e011"

	b = bitly_api.Connection(access_token = BITLY_ACCESS_TOKEN)

	response = b.shorten(input("ENter the URL: "))
	print(response)

print('1: Shortener--')
print('2: Expander--')

choice = input('choose: ')
shorten() if choice == 1 else expandd()