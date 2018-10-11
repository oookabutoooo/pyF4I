import json
import base64
import time, datetime
import sys, csv

#For Python 3
#import urllib.request, urllib.parse, urllib.error, urllib, http.client

#For Python 2
import urllib, httplib


##### FaceAPI #####
subscriptionKey = 'aa25941a79c34280ae41264c87c10581'
baseURL = 'eastus.api.cognitive.microsoft.com'
#appType = 'application/json'
appType = 'application/octet-stream'

faceAttributes = 'age,gender'

headers = {
	'Content-Type': appType,
	'Ocp-Apim-Subscription-Key': subscriptionKey,
}

#For Python 3
#params = urllib.parse.urlencode({

#For Python 2
params = urllib.urlencode({
	'returnFaceId': 'true',
	'returnFaceLandmarks': 'false',
	'returnFaceAttributes': faceAttributes,
})

def getTime():

	time = datetime.datetime.now()
	charTime = time.strftime('%Y%m%d-%H_%M_%S')

	return charTime

def readInput(fname):

	binData = open(fname, 'rb').read()

	return binData


def writeData(fname, data):

	open(fname, 'wb').write(data)


def calcTh(data, time):

	return data * 8 / time / 1000000


def FaceConnect(baseURL):

	#For Python 3
	#conn = http.client.HTTPSConnection(baseURL)

	#For Python 2
	conn = httplib.HTTPSConnection(baseURL)

	return conn

def FaceDetect(binImg):

	try:
		conn = FaceConnect(baseURL)

		conn.request("POST", "/face/v1.0/detect?%s" %params, binImg, headers)
		response = conn.getresponse()
		result = response.read()
		rxParsed = json.loads(result)

		conn.close()

		return rxParsed
	
	except Exception as e:
		print("Error")


def setLOG(fname):

	f = open(fname, 'a')
	writer = csv.writer(f, lineterminator='\n')

	return writer


if __name__ == '__main__':

	args = sys.argv

	if len(args) != 2:
		print("Usage:python program.py [Input file name (without file extension]")
		exit(1)

	fname = args[1] + ".png"
	binImg = readInput(fname)

	start = time.time()
	result = FaceDetect(binImg)
	elapsedTime = time.time() - start

	print("Detection time: {0} (sec)".format(elapsedTime))

	print(result)	 

