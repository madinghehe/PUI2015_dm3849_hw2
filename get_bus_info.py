import json
import sys
import csv
import urllib2
if __name__=='__main__':
    
    key = '37e65b06-ad6d-402c-977a-22345d1c2ec9'
    bus = 'B52'
    url = 'http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s' % (sys.argv[1],sys.argv[2])
    request = urllib2.urlopen(url)
    metadata = json.loads(request.read())
    
    count = 0
    item = metadata['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
    print 'Bus Line = %s' % sys.argv[2]
    print 'Number of Active = %d' % len(item)
    
    with open(sys.argv[3], 'w') as csvFile:
        
        writer = csv.writer(csvFile)
        headers = ['Latitude', 'Longitude', 'Stop Name', 'Stop Status']
        writer.writerow(headers)
        for i in item:
            Lat = i['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
            Long = i['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
            name = i['MonitoredVehicleJourney']['MonitoredCall']['StopPointName']
            status = i['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']
            if status == i['MonitoredVehicleJourney']['OnwardCalls'] =={}:
                name = 'NA'
                status = 'NA'
            observe = [Lat, Long, name, status]
            writer.writerow(observe)
        
       
        
            #print '% 50s : %s, %s' % (stationName, stationLat, stationLon)
