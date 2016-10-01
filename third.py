import httplib, urllib
conn = httplib.HTTPSConnection("api.pushover.net:443")
conn.request("POST", "/1/messages.json",
  urllib.urlencode({
    "token": "apq6X7LjusBoBxJCKhmXWiHcBpaQUy",
    "user": "ufi7wvqXdysTRQGsJs9tEGhrfMQ8N3",
    "message": "hello",
    "device":"my_device",
    # "title":"Bitjini"
  }), { "Content-type": "application/x-www-form-urlencoded" })
# print conn.getresponse()
conn.getresponse()




