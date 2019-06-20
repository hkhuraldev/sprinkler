import time
from datetime import datetime, timedelta
import requests
import xml.etree.ElementTree as ET
import runsprinkler

zipCode="30005"

fromDate= (datetime.now() - timedelta(days=2)).isoformat()
toDate= datetime.now().isoformat()

url='https://graphical.weather.gov/xml/sample_products/browser_interface/ndfdXMLclient.php?whichClient=NDFDgenMultiZipCode&zipCodeList='+ zipCode +'&product=time-series&begin='+ fromDate +'&end='+ toDate +'&Unit=e&qpf=qpf&Submit=Submit'

print "Calling url" + url

r = requests.get(url)

#print r.status_code

#print r.content

root = ET.fromstring(r.content)

#for child in root.iter('*'):
  #print(child.tag, child.attrib)

print("Yesterday it rained"+ root[1][3][0][1].text +" inches")





fromDate= datetime.now().isoformat()
toDate= (datetime.now() + timedelta(days=1)).isoformat()

url='https://graphical.weather.gov/xml/sample_products/browser_interface/ndfdXMLclient.php?whichClient=NDFDgenMultiZipCode&zipCodeList='+ zipCode +'&product=time-series&begin='+ fromDate +'&end='+ toDate +'&Unit=e&qpf=qpf&Submit=Submit'

#print "Calling url" + url

r = requests.get(url)

#print r.status_code

#print r.content

root = ET.fromstring(r.content)

#for child in root.iter('*'):
  #print(child.tag, child.attrib)

print("Tomorrow rain will be "+ root[1][3][0][1].text + root[1][3][0][2].text + root[1][3][0][3].text + root[1][3][0][4].text + root[1][3][0][5].text +" inches")
totalRain = float(root[1][3][0][1].text) + float(root[1][3][0][2].text) + float(root[1][3][0][3].text) + float(root[1][3][0][4].text) + float(root[1][3][0][5].text)
print("Total Rain : " + str(totalRain))

if (totalRain < 0.5):
	runsprinkler.waterAll()
