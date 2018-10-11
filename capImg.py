import json
import base64
import cv2
import sys
import datetime
import time
import csv

QUALITY=3

def readInput(input):

	#message = cv2.imread(input)
	message = open(input,'rb').read()

	return message

def capImg(cam):

	ret, frame = cam.read()

	encode_param = [int(cv2.IMWRITE_PNG_COMPRESSION), QUALITY]
	result, encImg = cv2.imencode('.png', frame, encode_param)

	return encImg

def getTime():

	time = datetime.datetime.now()
	charTime = time.strftime('%Y%m%d-%H_%M_%S')

	return charTime

def jsonData(nowTime, cam):

	img = capImg(cam)

	#fname = nowTime + ".png"
	#writeData(fname, img)

	size = sys.getsizeof(img)
	binImg = base64.b64encode(img).decode('utf-8')
	
	dictdata = {
		"type": "png",
		"ts": nowTime,
		"size": size,
		"img": binImg,
	}
	
	return dictdata

def writeData(fname, data):

	open(fname, 'wb').write(data)

def setLOG(fname):

	f = open(fname, 'a')
	writer = csv.writer(f, lineterminator='\n')

	return writer


if __name__ == '__main__':

	args = sys.argv

	if len(args) != 2:
		print("Usage:python program.py [Output file name (without file extension)]")
		exit(1)

	cam = cv2.VideoCapture(0)

	img = capImg(cam)

	fname = args[1] + ".png"
	writeData(fname, img)

	cam.release()
