#Script to interact with a REST API and determine a unique identifier for a location entered by the user
import urllib
import json

serviceurl = 'http://python-data.dr-chuck.net/geojson?'

while True:
    address = raw_input('Enter location:\n')
    if len(address) < 1:
        break
    else:
        url = serviceurl + urllib.urlencode({'sensor':'false','address':address})
        print 'Retrieving',url
        urlopen = urllib.urlopen(url)
        data = urlopen.read()
        print 'Retrieved', len(data),'characters'
        try:
            js = json.loads(str(data))
        except:
            js = None
        if 'status' not in js or js['status'] != 'OK':
            print '===Failure to Retrieve==='
            #print data
            continue
        else:
            print json.dumps(js, indent=4)
            print 'Place_ID:',js['results'][0]['place_id']
            continue           
