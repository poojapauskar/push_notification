import json,httplib
connection = httplib.HTTPSConnection('api.parse.com', 443)
connection.connect()
connection.request('POST', '/1/installations', json.dumps({
       "deviceType": "ios",
       "deviceToken": "bef62791b70af1e44bb6f441daf66c85608493250fcd8c7fe9116f1dae978f5f",
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

# import json,httplib
# connection = httplib.HTTPSConnection('api.parse.com', 443)
# connection.connect()
# connection.request('GET', '/1/installations/VaidT28got', '', {
#        "X-Parse-Application-Id": "hxQEClVPGEnsBtcaUPDmN9kEpyx17j3A3nqbSj9c",
#        "X-Parse-REST-API-Key": "D6RgO6YFBTFaQ2zvAcV41wuCsXMV86rhpj4hjCmy"
#      })
# result = json.loads(connection.getresponse().read())
# print "getting the installation"
# print result


# import json,httplib
# connection = httplib.HTTPSConnection('api.parse.com', 443)
# connection.connect()
# connection.request('PUT', '/1/installations/VaidT28got', json.dumps({
#        "deviceType": "ios",
#        "deviceToken": "bef62791b70af1e44bb6f441daf66c85608493250fcd8c7fe9116f1dae978f5f",
#        "channels": [
#          "",
#          "foo"
#        ]
#      }), {
#        "X-Parse-Application-Id": "hxQEClVPGEnsBtcaUPDmN9kEpyx17j3A3nqbSj9c",
#        "X-Parse-REST-API-Key": "D6RgO6YFBTFaQ2zvAcV41wuCsXMV86rhpj4hjCmy",
#        "Content-Type": "application/json"
#      })
# result = json.loads(connection.getresponse().read())
# print "creating a channel"
# print result



# import json,httplib
# connection = httplib.HTTPSConnection('api.parse.com', 443)
# connection.connect()
# connection.request('DELETE', '/1/installations/VaidT28got', '', {
#        "X-Parse-Application-Id": "hxQEClVPGEnsBtcaUPDmN9kEpyx17j3A3nqbSj9c",
#        "X-Parse-Master-Key": "brJ9WSOPdFuEd9txnpeMBwd9XjKWLS1N7giFhvEt"
#      })
# result = json.loads(connection.getresponse().read())
# print "Delete installation"
# print result

import json,httplib
connection = httplib.HTTPSConnection('api.parse.com', 443)
connection.connect()
connection.request('PUT', '/1/installations/DsuLSeMgT1', json.dumps({
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
