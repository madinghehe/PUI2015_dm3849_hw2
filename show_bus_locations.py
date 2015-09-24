import json
import sys
import csv
import urllib2
if __name__=='__main__':
    #key = '37e65b06-ad6d-402c-977a-22345d1c2ec9'
    #bus = 'B52'
    url = 'http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s' % (sys.argv[1],sys.argv[2])
    request = urllib2.urlopen(url)
    metadata = json.loads(request.read())
    count = 0
    
    for i in metadata['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']:
        
        print 'Bus %d is at Latitude %s and Longitude %s' % (count, i['MonitoredVehicleJourney']['VehicleLocation']['Latitude'], i['MonitoredVehicleJourney']['VehicleLocation']['Longitude'])
        count += 1
