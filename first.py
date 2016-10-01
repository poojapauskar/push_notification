import json,httplib
connection = httplib.HTTPSConnection('api.parse.com', 443)
connection.connect()
connection.request('POST', '/1/installations', json.dumps({
       "deviceType": "ios",
       "deviceToken": "BEF62791B70AF1E44BB6F441DAF66C85608493250FCD8C7FE9116F1DAE978F5F",
       "channels": [
         ""
       ]
     }), {
       "X-Parse-Application-Id": "hxQEClVPGEnsBtcaUPDmN9kEpyx17j3A3nqbSj9c",
       "X-Parse-REST-API-Key": "D6RgO6YFBTFaQ2zvAcV41wuCsXMV86rhpj4hjCmy",
       "Content-Type": "application/json"
     })
result = json.loads(connection.getresponse().read())
print result