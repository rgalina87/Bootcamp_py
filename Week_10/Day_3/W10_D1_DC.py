import requests
from xml.etree import ElementTree, ElementInclude

response = requests.get("https://news.google.com/rss?x=1571747254.2933&hl=en-US&gl=US&ceid=US:en")
json_response = response.json()
print(json_response())

tree = ElementTree.parse(json_response)
root = tree.getroot()
ElementInclude.include(root)