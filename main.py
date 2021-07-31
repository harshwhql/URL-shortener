import bitly_api
from pyshorteners import Shortener
import requests
BITLY_ACCESS_TOKEN = "INPUT_YOUR_ ACCESS_TOKEN_HERE"

def expandd():
	short_url =input("Enter the URL: ")
	     
	print(requests.get(short_url).url)

def shorten():
	b = bitly_api.Connection(access_token = BITLY_ACCESS_TOKEN)

	response = b.shorten(input("ENter the URL: "))
	print(response)

print('1: Shortener--')
print('2: Expander--')

choice = input('choose: ')
shorten() if choice == 1 else expandd()
