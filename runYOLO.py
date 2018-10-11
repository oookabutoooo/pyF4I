import json
import base64
import cv2
import sys
import datetime
import time
import subprocess
import collections as cl
import csv

def res_cmd_lfeed(cmd):

	return subprocess.Popen(
		cmd, stdout=subprocess.PIPE,
		shell=True).stdout.readlines()


def res_cmd_no_lfeed(cmd):

	return [str(x).rstrip("\n") for x in res_cmd_lfeed(cmd)]


def read_input(input):

	#message = cv2.imread(input)
	message = open(input,'rb').read()

	return message

def getTime():

	time = datetime.datetime.now()
	charTime = time.strftime('%Y%m%d-%H_%M_%S')

	return charTime

def dictYOLO(name, score, log):
	
	dictdata = cl.OrderedDict()
	classdata = cl.OrderedDict()

	for i in range(len(log)):
		result = cl.OrderedDict()
		result["score"] = score[i]
		result["box"] =  log[i]

		classdata[name[i]] = result

	dictdata["yolo"] = classdata
	
	return dictdata

def jsonData(subdata, yolodata):

	binImg = base64.b64encode(subdata['img']).decode('utf-8')

	dictdata = {
		"type" : subdata['type'],
		"ts" : subdata['ts'],
		"size": subdata['size'],
	}

	imgData = {"img": binImg}

	dictdata.update(yolodata)
	#print(dictdata)

	dictdata.update(imgData)

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
		print("Usage:python prgoram.py [Input file name (without file extension)]")
		exit(1)

	fname = args[1] + ".png"

	#YOLOv3 full spec
	#cmd = ("./darknet detect cfg/yolov3.cfg yolov3.weights " + fname)

	#YOLOv3 tiny version
	cmd = ("./darknet detect cfg/yolov3-tiny.cfg yolov3-tiny.weights " + fname)

	start = time.time()
	result = res_cmd_no_lfeed(cmd)
	end = time.time()

	log = []
	name = []
	score = []
	output = []

	flag = 0

	for i in range(len(result)):
		log.append(result[i].split())
		name.append(log[i][0])
		score.append(log[i][1])
		log[i].pop(0)
		log[i].pop(1)
		
		if name[i] == "person":
			flag = 1

	#dictyolo = dictYOLO(name, score, log)
	detectTime = end - start

	if flag == 1:

		print("person detected")

	else:

		print("No person")

	print("Detection time: {0} (sec)".format(detectTime))

	#cmd = ('rm -rf ' + fname)
	#res = res_cmd_no_lfeed(cmd)

