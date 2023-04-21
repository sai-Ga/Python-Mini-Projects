import pyshorteners as ps


long_url = input("Enter URL to shorten")
type_tiny = ps.Shortener()

short_url = type_tiny.tinyurl.short(long_url) #using tinyurl.com
print('Your shortened URL:  ', short_url)

type_bitly = ps.Shortener(api_key='4a62e38fdfe65c7355371c4b5e07872ec0c9cddb') #using bit.ly API KEY
short_bitly_url= type_bitly.bitly.short(long_url)
print('Your shortened URL:  ', short_bitly_url)
