import xml.etree.cElementTree as ET
import sys

BUNDLEID = '__BUNDLEID__'
bundle_identifier = sys.argv[1]

BUNDLEVER = '__BUNDLEVER__'
bundle_version = sys.argv[2]

TITLE = '__TITLE__'
title = sys.argv[3]

output = "app.plist"

tree = ET.ElementTree(file='test.plist')

root = tree.getroot()

for i in tree.iter(tag='string'):
    if i.text == BUNDLEID:
        i.text = str(bundle_identifier)
    elif i.text == BUNDLEVER:
        i.text = str(bundle_version)
    elif i.text == TITLE:
        i.text = str(title)

tree.write(output)
