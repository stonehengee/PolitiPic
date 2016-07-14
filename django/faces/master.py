import pandas as pd
import numpy as np
from scipy.spatial import distance
import csv
from scipy import stats
import math
import json
import os
import argparse
import base64
from PIL import Image
from django.http import HttpResponse
from django.shortcuts import render_to_response
from googleapiclient import discovery
import httplib2
from oauth2client.client import GoogleCredentials
from django.conf import settings

class RunTests():
	path_to_json = settings.BASE_DIR + '/faces/picture_jsons'
	json_files = [pos_json for pos_json in os.listdir(path_to_json)]
	score_data = pd.read_csv(settings.BASE_DIR + '/faces/phase_3_data.csv')
	echo_list = score_data['economic'].tolist()
	soc_list = score_data['social'].tolist()
	eco_array = np.asarray(echo_list)
	soc_array = np.asarray(soc_list)

	# must specify eco_array or soc_array
	political_attr = None

	def compare(self):
		f=open('results2.txt', 'w')
		for i in range(34):
			for x in range(34):
				list_of_dst=[]
				jsons_data = pd.DataFrame(columns=['type','position x','position y','position z','type_2', 'position a','position b','position c'])
				for index, jf in enumerate(self.json_files):
					with open(settings.BASE_DIR + os.path.join(self.path_to_json, jf)) as json_file:
						data = json.load(json_file)

						type_ = data['landmarks'][i]['type']
						positionx = data['landmarks'][i]['position']['x']
						l = 100/positionx
						positionx = 100
						positiony = (data['landmarks'][i]['position']['y'])
						positiony = positiony*l
						positionz = data['landmarks'][i]['position']['z']
						positionz = positionz*l

						type_2 = data['landmarks'][x]['type']
						if type_ != type_2:
							positiona = data['landmarks'][x]['position']['x']
							positiona = positiona*l
							positionb = data['landmarks'][x]['position']['y']
							positionb = positionb*l
							positionc = data['landmarks'][x]['position']['z']
							positionc = positionc*l
						else:
							# print('twinnies')
							positiona = positionx
							positionb = positiony
							positionc = positionz
						jsons_data.loc[index] = [type_, positionx, positiony, positionz,type_2,positiona,positionb,positionc]
						a = (positiona,positionb,positionc)
						b = (positionx,positiony,positionz)
						dst = distance.euclidean(a,b)
						list_of_dst.append(dst)
				list_of_dst.append(type_)
				list_of_dst.append(type_2)


				strlist = str(list_of_dst)
				f.write(strlist)

				print(str((x/34)/34 + i/34)[2:4]+'%' + 'compare')
		f.close()
		print ('100%')

	
	def sum_dist(self):
		result = open('faces/results.csv', 'w', newline='')
		writer = csv.writer(result, delimiter=',')
		writer.writerow(["types1_2", "type2_3", "slope", "yintercept", "rvalue", "pvalue", "stderr"])
		with open('faces/results2.txt', 'r') as f:
			for each in f:
				each = each.replace('[', '')
				each = each.split(']')
				for i in range (1156):	
					for x in range (1156):
						item = each[i].split(',')
						item2 = each[x].split(',')
						bar_list = []
						y = len(item)-1
						for foo in range(y):
							if foo <= y-2:
								bar = float(item[foo].strip()) + float(item2[foo].strip())
								bar_list.append(bar)
							if foo == y-1:
								bar = (item[foo].strip() + item[foo+1].strip()).replace("''", ',').replace("'", '')
								bar1 = (item2[foo].strip() + item2[foo+1].strip()).replace("''", ',').replace("'", '')
								bar_list.append(bar)
								bar_list.append(bar1)
						distance_array = np.asarray(bar_list[:39])
						bar = stats.linregress(distance_array, self.political_attr)
						writer.writerow([bar_list[39], bar_list[40], bar.slope, bar.intercept, bar.rvalue, bar.pvalue, bar.stderr])
						print(str((x/1156)/1156 + i/1156)[2:4]+'%' + 'sum')
		print ('100%')

	def pandafy(self):
		df = pd.read_csv('faces/results.csv')
		df = df.sort_values('pvalue',ascending=True, kind='mergesort')
		df = df.drop_duplicates()

		df.to_csv('results_sorted.csv')	

class ApiCall():
	DISCOVERY_URL='https://{api}.googleapis.com/$discovery/rest?version={apiVersion}'
	picture = None
	sum_s = 0
	sum_e = 0

	def compare(self, your_face):

		# for social
		# jsons_data = pd.DataFrame(columns=['type','position x','position y','position z','type_2', 'position a','position b','position c'])
		data = your_face
		# print(data)
		#lower lip
		type_ = data['landmarks'][9]['type']
		positionx = data['landmarks'][9]['position']['x']
		l = 100/positionx
		positionx = 100
		positiony = (data['landmarks'][9]['position']['y'])
		positiony = positiony*l
		positionz = data['landmarks'][9]['position']['z']
		positionz = positionz*l
		# mouth center
		type_2 = data['landmarks'][12]['type']
		positiona = data['landmarks'][12]['position']['x']
		positiona = positiona*l
		positionb = data['landmarks'][12]['position']['y']
		positionb = positionb*l
		positionc = data['landmarks'][12]['position']['z']
		positionc = positionc*l
		# jsons_data.loc = [type_, positionx, positiony, positionz,type_2,positiona,positionb,positionc]
		a = (positiona,positionb,positionc)
		b = (positionx,positiony,positionz)
		dst = distance.euclidean(a,b)
		# print(type_,type_2)
		

	#	FOR social
		data = your_face
#  left eye
		type_ = data['landmarks'][0]['type']
		positionx = data['landmarks'][0]['position']['x']
		l = 100/positionx
		positionx = 100
		positiony = (data['landmarks'][0]['position']['y'])
		positiony = positiony*l
		positionz = data['landmarks'][0]['position']['z']
		positionz = positionz*l
#  left eye pupil
		type_2 = data['landmarks'][20]['type']
		positiona = data['landmarks'][20]['position']['x']
		positiona = positiona*l
		positionb = data['landmarks'][20]['position']['y']
		positionb = positionb*l
		positionc = data['landmarks'][20]['position']['z']
		positionc = positionc*l
		# jsons_data.loc = [type_, positionx, positiony, positionz,type_2,positiona,positionb,positionc]
		a = (positiona,positionb,positionc)
		b = (positionx,positiony,positionz)
		dst2 = distance.euclidean(a,b)
		# print(type_,type_2)
		self.sum_s = (dst + dst2)

	# ---------------------------------------------------------------------------
	# for economic

		# jsons_data = pd.DataFrame(columns=['type','position x','position y','position z','type_2', 'position a','position b','position c'])
		data = your_face
		#left eye
		type_ = data['landmarks'][0]['type']
		positionx = data['landmarks'][0]['position']['x']
		l = 100/positionx
		positionx = 100
		positiony = (data['landmarks'][0]['position']['y'])
		positiony = positiony*l
		positionz = data['landmarks'][0]['position']['z']
		positionz = positionz*l
		# left eye pupil
		type_2 = data['landmarks'][20]['type']
		positiona = data['landmarks'][20]['position']['x']
		positiona = positiona*l
		positionb = data['landmarks'][20]['position']['y']
		positionb = positionb*l
		positionc = data['landmarks'][20]['position']['z']
		positionc = positionc*l
		# jsons_data.loc = [type_, positionx, positiony, positionz,type_2,positiona,positionb,positionc]
		a = (positiona,positionb,positionc)
		b = (positionx,positiony,positionz)
		dst = distance.euclidean(a,b)
		# print(type_,type_2)
		

	# for economic
		data = your_face
#  right eye
		type_ = data['landmarks'][1]['type']
		positionx = data['landmarks'][1]['position']['x']
		l = 100/positionx
		positionx = 100
		positiony = (data['landmarks'][1]['position']['y'])
		positiony = positiony*l
		positionz = data['landmarks'][1]['position']['z']
		positionz = positionz*l
#  right eye left coner
		type_2 = data['landmarks'][24]['type']
		positiona = data['landmarks'][24]['position']['x']
		positiona = positiona*l
		positionb = data['landmarks'][24]['position']['y']
		positionb = positionb*l
		positionc = data['landmarks'][24]['position']['z']
		positionc = positionc*l
		# jsons_data.loc = [type_, positionx, positiony, positionz,type_2,positiona,positionb,positionc]
		a = (positiona,positionb,positionc)
		b = (positionx,positiony,positionz)
		dst2 = distance.euclidean(a,b)
		# print(type_,type_2)
		self.sum_e = (dst + dst2)
		# print ("hit compare")
		return self.graph()

	def graph(self):
		# economic graph
		# y=mx+b
		# print("How many times are we hitting this?")
		predicted_econ = -0.1736911*self.sum_e + -0.9262656
		predicted_soc = -0.0635138*self.sum_s + -2.0714823
		values = [predicted_econ,predicted_soc]
		# print("hit graph", values)
		return values 

		# return HttpResponse(values)


	def get_vision_service(self):
		os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = settings.BASE_DIR + "/faces/auth.json"
		credentials = GoogleCredentials.get_application_default()
		return discovery.build('vision', 'v1', credentials=credentials,
							   discoveryServiceUrl=self.DISCOVERY_URL)

	def run(self):
		# with open('pictures/{}'.format(self.picture),'rb') as image:
		image_content = self.picture.read()

		batch_request = [{
			'image': {
				'content': base64.b64encode(image_content).decode('ascii')
				},
			'features': [{
				'type': 'FACE_DETECTION',
				'maxResults': 4,
				}]
			}]
		service = self.get_vision_service()
		request = service.images().annotate(body={
			'requests': batch_request,
			})
		response = request.execute()
		# print (response)
		# exit()
		# try :
		try:
			your_face = response['responses'][0]['faceAnnotations'][0]
		except KeyError:
			return ["There was an issue with your photo.", "Please try again later."]
		# print ("run hit")
		return self.compare(your_face)
