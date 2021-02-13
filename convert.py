# Why so sewiouws
# ~/Library/Application Support/Steam/steamapps/common/Caves of Qud/CoQ.app/Contents/Resources/Data/StreamingAssets/Base/

# importing the module. 
import xml.etree.ElementTree as ET 
from lxml.etree import XMLParser
from TextToOwO.owo import text_to_owo

# parser = XMLParser(encoding='utf-8', recover=True)

# parsing directly. 
convos = ET.parse('./Conversations_Base.xml') 

# UWUs all Text
for text in convos.iter('text'):
    text.text = text_to_owo(text.text)

# UWUS all choices
for text in convos.iter('choice'):
    if (text.text != None):
        text.text = text_to_owo(text.text)

convos.write('Conversations.xml')

# QUESTS
quests = ET.parse('./Quests_Base.xml')

for text in quests.iter('text'):
    if (text.text != None):
        text.text = text_to_owo(text.text)

# QUESTS CURRENTLY NOT WORKING
# quests.write ('Quests.xml') 

# OBJECT BLUEPRINTS
# Modified objectblueprints base that removes a few broken items from the UwU speech
objs = ET.parse('./ObjectBlueprints_Base_Mod.xml')

for text in objs.iter('part'):
    # Checks to see if the part is a render part, then changes the displayname
    if text.get('Name') == 'Render':
        if (text.get('DisplayName') == None):
            continue
        text.set ('DisplayName', text_to_owo(text.get('DisplayName')))
    
    elif text.get('Name') == 'Description':
        if (text.get('Short') == None):
            continue
        text.set ('Short', text_to_owo(text.get('Short')))

objs.write('ObjectBlueprints.xml', encoding='utf-8')

# # BOOKS
# books = ET.parse('./Books_Base.xml', parser)

# for books in books.iter('page'):
#     if (text.text != None):
#         text.text = text_to_owo(text.text)

# books.write ('Books.xml')