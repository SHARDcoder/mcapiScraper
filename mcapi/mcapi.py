"""
MIT License

Copyright (c) 2018 SHARDcoder

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import requests

class query():
	def __init__(self):
		pass
	
	def __main__(self):
		pass
	
	def get_url(self, ip):
		baseUrl = 'https://use.gameapis.net/mc/query/info/'
		
		url = baseUrl + ip
		
		return url
	
	def get_status(self, ip):
		rawData = requests.get(self.get_url(ip))
		
		rawDataLines = rawData.text.splitlines()
		
		relevant = rawDataLines[1]
		
		status = relevant[14:-1]
		
		return status
	
	def get_version(self, ip):
		rawData = requests.get(self.get_url(ip))
		
		rawDataLines = rawData.text.splitlines()
		
		relevant = rawDataLines[5]
		
		status = relevant[16:-2]
		
		return status
	
	def get_onlinePlayers(self, ip):
		rawData = requests.get(self.get_url(ip))
		
		rawDataLines = rawData.text.splitlines()
		
		relevant = rawDataLines[8]
		
		status = relevant[18:-1]
		
		return status
	
	def get_maxPlayers(self, ip):
		rawData = requests.get(self.get_url(ip))
		
		rawDataLines = rawData.text.splitlines()
		
		relevant = rawDataLines[9]
		
		status = relevant[15:]
		
		return status
