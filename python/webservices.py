""" 
Wire protocol: what we send on the wire => coming from many programming lang
Py Dictionary => Serialize => Agreeing on wire format => De-serialize
 Agreeing on wire format : i.e : json, XML
 """

# XML : extensible markup language
""" 
primary purpose is to help info systems share structured data
Tags, Attribut, Serialize/De-serialize
XML Basics
1. Start Tag
2. End Tag
3. Text Content
4. Attribute
5. Self Closing Tag
Line ends do not matter, white space is generally discarded on text elements.
We indent only to be readable

Basically XML has a document, contract & validator
Many XML Schema Language:
- Document type definition
- Standard Generalized markup language
- XML Schema from w3c (XSD)
"""

""" XML Schema : praticular schema about xml that renders an opinion about XML is supposed to look like 
Many XML Schema languages
i.e : XSD XML Schema (W3c spec)  
- we will focus on the w3c version
- it's often called "W3C Schema" because schema is considered generic
- More commonly it is called XSD because the file names end in .xsd
"""

# XSD Structure
""" 
- xs:element
- xs:sequence
- xs:complexType
Contract: 
<xs:complexType name=”person”>
  <xs:sequence>
    <xs:element name="lastname" type="xs:string"/>
    <xs:element name="age" type="xs:integer"/>
    <xs:element name="dateborn" type="xs:date"/>
  </xs:sequence>
</xs:complexType>

Document:
<person>
   <lastname>Severance</lastname>
   <age>17</age>
   <dateborn>2001-04-17</dateborn>
</person>

 """

# XSD Constraints
""" 
<xs:element name="person">
  <xs:complexType>
    <xs:sequence>
      <xs:element name="full_name" type="xs:string"  
          minOccurs="1" maxOccurs="1" /> # a constraint
      <xs:element name="child_name" type="xs:string" 
            minOccurs="0" maxOccurs="10" />
    </xs:sequence>
  </xs:complexType>
</xs:element>

<person>
  <full_name>Tove Refsnes</full_name> # should having max and min occurs = "1"
  <child_name>Hege</child_name>
  <child_name>Stale</child_name>
  <child_name>Jim</child_name>
  <child_name>Borge</child_name>
</person>
 """

# XSD Data Type
""" 
<xs:element name="customer" type="xs:string"/>
<xs:element name="start" type="xs:date"/>
<xs:element name="startdate" type="xs:dateTime"/>
<xs:element name="prize" type="xs:decimal"/>
<xs:element name="weeks" type="xs:integer"/>
<xs:simpleType>
    <xs:restriction base="xs:string">
        <xs:enumeration value="FR" />
        <xs:enumeration value="UK" />
    </xs:restriction base="xs:string">
</xs:simpleType>

i.e:
<customer>John Smith</customer>
<start>2002-09-24</start>
<startdate>2002-05-30T09:30:10Z</startdate>
<prize>999.50</prize>
<weeks>30</weeks>
<Country>UK</Country>

Data/Time Format
2002-05-30T09:30:10Z
- 2002-05-30: year-month-day
- 09:30:10: time of day
- T/Z : Timezone typically specify in UTC/GMT rather than local time zone
 """

import xml.etree.ElementTree as ET
data = '''<person>
  <name>Chuck</name>
  <phone type="intl">
     +1 734 303 4456
   </phone>
   <email hide="yes"/>
</person>'''

tree = ET.fromstring(data)
print('Name:',tree.find('name').text)
print('Attr:',tree.find('email').get('hide'))

input = '''<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Brent</name>
        </user>
    </users>
</stuff>'''

stuff = ET.fromstring(input)
lst = stuff.findall('users/user')
print('User count:', len(lst))
for item in lst:
    print('Name', item.find('name').text)
    print('Id', item.find('id').text)
    print('Attribute', item.get("x"))


# 2. JSON
import json
jsonData = '''{
  "name" : "Mita",
  "phone" : {
    "type" : "intl",
    "number" : "0812342323"
   },
    "email" : {
     "hide" : "yes"
   }
}'''

info = json.loads(jsonData)
print('Name: ', info["name"])
print('Hide: ', info["email"]["hide"])

multipleData = '''
[
    {
        "id": "0001",
        "x": 2,
        "name":"mita"
    },
    {
        "id": "0002",
        "x": 2,
        "name":"mita mita"
    }
]
'''

loadJson= json.loads(multipleData)
print('User count:', len(loadJson))
for item in loadJson:
    print('Name', item['name'])
    print('Id', item['id'])
    print('Attribute', item['x'])
