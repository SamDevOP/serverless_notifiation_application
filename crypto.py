import urllib.request
url = "https://api.lunarcrush.com/v2?data=assets&key={API_KEY_HERE}&symbol=BTC"
x=urllib.request.urlopen(url).read()
print(x['price'])