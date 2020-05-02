from html.parser import HTMLParser

class Parser(HTMLParser):	
	tableDict = {}
	inTable = False
	enteringHeaderData = False
	enteringTableRow = False
	headerList = []
	dataList = []
	enteringTableData = False
	currentDataHeader = 0

	def end_table(self):
		print(self.tableDict)
		self.tableDict = {}
		self.headerList = []
	
	def handle_starttag(self, tag, attrs):
		# Enable variables to tell the data reader where in the dict to
		# enter the data
		if (tag == 'table'):
			self.inTable = True
		elif (tag == 'th'):
			self.enteringHeaderData = True
		elif (tag == 'td'):
			self.enteringTableData = True
		elif (tag == 'tr'):
			self.enteringTableRow = True
		

	def handle_endtag(self, tag):
		# Disable variables to tell the data reader that the tag is done
		if (tag == 'table'):
			self.inTable = False
			self.end_table()
		elif (tag == 'th'):
			self.enteringHeaderData = False
		elif (tag == 'td'):
			self.enteringTableData = False
		elif (tag == 'tr'):
			self.enteringTableRow = False
			self.currentDataHeader = 0

	def handle_data(self, data):
		# Check to see if header or table data is being read
		if (self.enteringHeaderData == True):
			# Run this so long as headerList is not empty
			if (self.headerList != []):
				# Adds new header to the dict named header(next avaliable number)
				# then set the first list item to the name of the header
				self.tableDict['header' + str(self.headerList[-1] + 1)] = [data]
				# Add this header count to the list
				self.headerList.append(self.headerList[-1] + 1)
			else:
				# Does the same as above code but instead initializes the dict and list
				self.tableDict['header' + str(0)] = [data]
				self.headerList.append(0)
			self.enteringHeaderData = False

		elif (self.enteringTableData == True):
			currentHeader = 'header' + str(self.currentDataHeader)
			dataList = self.tableDict[currentHeader]
			dataList.append(data)
			# Append the table data to the appropriate header
			self.tableDict[currentHeader] = dataList
			self.enteringTableData = False
			if (self.currentDataHeader >= self.headerList[-1]):
				self.currentDataHeader = 0
			else:
				self.currentDataHeader += 1