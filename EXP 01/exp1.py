import xml.etree.ElementTree as ET
tree = ET.parse('country_data.xml')

root = tree.getroot() #Get the root element
print('root tag : ',end='')
print(root.tag) #root tag
print('\n\n')

#Print all the tags and attributes that are present within the child tag
print('all children and attribs : ',end='')
for child in root:  
    print (child.tag, child.attrib)
print('\n\n')

#Get the first child of root element
print('first child of root element : ',end='')
print(root[0].tag,root[0].attrib)
print('\n\n')

#Get the attribute for the child of the root element.
print('Iterate through all the tags with a specific name neighbour : ',end='')
for neighbor in root.iter('neighbor'):  #Iterate through all the tags with a specific name.
    print (neighbor.attrib)
print('\n\n')

#add an updated attribute to the rank element:
for rank in root.iter('rank'):
     new_rank = int(rank.text) + 1
     rank.text = str(new_rank)
     rank.set('updated', 'yes')

#we want to remove all countries with a rank higher than 50:
for country in root.findall('country'):
     rank = int(country.find('rank').text)
     if rank > 50:
         root.remove(country)

tree.write('output.xml')