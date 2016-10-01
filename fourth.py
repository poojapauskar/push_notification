import http.client, urllib
conn = http.client.HTTPSConnection("api.pushover.net:443")
conn.request("POST", "/1/messages.json",
  urllib.parse.urlencode({
    "token": "apq6X7LjusBoBxJCKhmXWiHcBpaQUy",
    "user": "ufi7wvqXdysTRQGsJs9tEGhrfMQ8N3",
    "message": "hello world",
  }), { "Content-type": "application/x-www-form-urlencoded" })
conn.getresponse()