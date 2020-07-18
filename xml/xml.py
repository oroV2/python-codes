import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

serviceurl = "http://py4e-data.dr-chuck.net/comments_739364.xml"

print('Retrieving', serviceurl)

uh = urllib.request.urlopen(serviceurl)  
data = uh.read() 

print('Retrieved', len(data), 'characters')  

tree = ET.fromstring(data)  

lst = tree.findall('comments/comment')  

print("Count:", len(lst))  

total = sum([int(i.find('count').text) for i in lst])  

print("Sum:", total)
