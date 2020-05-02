import requests
import json
import csv
from htmlparser import Parser

pages = []
with open('pages.csv', 'r') as pagesFile:
	pagesList = csv.reader(pagesFile, delimiter=',')
	for item in pagesList:
		pages.append(item)

authDetails = {}
with open('authDetails.json') as authFile:
	fileString = authFile.read()
	authDetails = json.loads(fileString)


# This should be a user with at least READ access to the page(s) in question
apiToken = authDetails['api-token']
username = authDetails['username']
endpointBase = authDetails['endpoint']

for pageId in pages[0]:
	print(f'Now processing the following page: {pageId}')
	# All that is needed here is the title of the page to grab
	data = f"""{{
		"title": "{pageId}"
	}}"""
	
	endpoint = f'{endpointBase}/rest/api/content/{pageId}?expand=body.storage'

	r = requests.get(endpoint, data=data, auth=(username, apiToken))
	rJson = r.json()
	pageContent = rJson['body']['storage']['value']

	parsedHtml = Parser()
	parsedHtml.feed(pageContent)
