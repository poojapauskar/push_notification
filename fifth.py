import json,httplib
connection = httplib.HTTPSConnection('api.parse.com', 443)
connection.connect()
connection.request('POST', '/1/installations', json.dumps({
       "deviceType": "ios",
       "deviceToken": "159c56095527c7df693781f014264148c85940d3638368dcd12a9ef0fd3ec15e",
       "channels": [
         ""
       ]
     }), {
       "X-Parse-Application-Id": "hxQEClVPGEnsBtcaUPDmN9kEpyx17j3A3nqbSj9c",
       "X-Parse-REST-API-Key": "D6RgO6YFBTFaQ2zvAcV41wuCsXMV86rhpj4hjCmy",
       "Content-Type": "application/json"
     })
result = json.loads(connection.getresponse().read())
print "creating the installation"
print result

import json,httplib
connection = httplib.HTTPSConnection('api.parse.com', 443)
connection.connect()
connection.request('PUT', '/1/installations/7j0mWcwVPj', json.dumps({
       "channels": [
         "Giants"
       ]
     }), {
       "X-Parse-Application-Id": "hxQEClVPGEnsBtcaUPDmN9kEpyx17j3A3nqbSj9c",
       "X-Parse-REST-API-Key": "D6RgO6YFBTFaQ2zvAcV41wuCsXMV86rhpj4hjCmy",
       "Content-Type": "application/json"
     })
result = json.loads(connection.getresponse().read())
print "creating an installation with channel Giants"
print result

import json,httplib
connection = httplib.HTTPSConnection('api.parse.com', 443)
connection.connect()
connection.request('GET', '/1/installations', '', {
       "X-Parse-Application-Id": "hxQEClVPGEnsBtcaUPDmN9kEpyx17j3A3nqbSj9c",
       "X-Parse-Master-Key": "brJ9WSOPdFuEd9txnpeMBwd9XjKWLS1N7giFhvEt"
     })
result = json.loads(connection.getresponse().read())
print "getting all installations"
print result

import json,httplib
connection = httplib.HTTPSConnection('api.parse.com', 443)
connection.connect()
connection.request('POST', '/1/push', json.dumps({
       "channels": [
         "Giants"
       ],
       "data": {
         "alert": "Hello"
       }
     }), {
       "X-Parse-Application-Id": "hxQEClVPGEnsBtcaUPDmN9kEpyx17j3A3nqbSj9c",
       "X-Parse-REST-API-Key": "D6RgO6YFBTFaQ2zvAcV41wuCsXMV86rhpj4hjCmy",
       "Content-Type": "application/json"
     })
result = json.loads(connection.getresponse().read())
print "sending push notification to giant channel"
print result
