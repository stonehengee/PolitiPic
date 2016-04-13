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
def compare():
		# f=open('results2.txt', 'w')
		# for i in range(34):
		# 	for x in range(34):
	path_to_json = 'picture_jsons'
	json_files = [pos_json for pos_json in os.listdir(path_to_json)]
	score_data = pd.read_csv('phase_3_data.csv')
	echo_list = score_data['economic'].tolist()
	soc_list = score_data['social'].tolist()
	eco_array = np.asarray(echo_list)
	soc_array = np.asarray(soc_list)
	list_of_dst=[]
	jsons_data = pd.DataFrame(columns=['type','position x','position y','position z','type_2', 'position a','position b','position c'])
	for index, jf in enumerate(json_files):
		with open(os.path.join(path_to_json, jf)) as json_file:
			data = json.load(json_file)

			type_ = data['landmarks'][9]['type']
			positionx = data['landmarks'][9]['position']['x']
			l = 100/positionx
			positionx = 100
			positiony = (data['landmarks'][9]['position']['y'])
			positiony = positiony*l
			positionz = data['landmarks'][9]['position']['z']
			positionz = positionz*l

			type_2 = data['landmarks'][12]['type']
			positiona = data['landmarks'][12]['position']['x']
			positiona = positiona*l
			positionb = data['landmarks'][12]['position']['y']
			positionb = positionb*l
			positionc = data['landmarks'][12]['position']['z']
			positionc = positionc*l
			jsons_data.loc[index] = [type_, positionx, positiony, positionz,type_2,positiona,positionb,positionc]
			a = (positiona,positionb,positionc)
			b = (positionx,positiony,positionz)
			dst = distance.euclidean(a,b)
			list_of_dst.append(dst)
		print(type_,type_2)
		
	# list_of_dst.append(type_)
	# list_of_dst.append(type_2)
	# strlist = str(list_of_dst)
	# f.write(strlist)

	list_of_dst2=[]
	jsons_data = pd.DataFrame(columns=['type','position x','position y','position z','type_2', 'position a','position b','position c'])
	for index, jf in enumerate(json_files):
		with open(os.path.join(path_to_json, jf)) as json_file:
			data = json.load(json_file)

			type_ = data['landmarks'][0]['type']
			positionx = data['landmarks'][0]['position']['x']
			l = 100/positionx
			positionx = 100
			positiony = (data['landmarks'][0]['position']['y'])
			positiony = positiony*l
			positionz = data['landmarks'][0]['position']['z']
			positionz = positionz*l

			type_2 = data['landmarks'][20]['type']
			positiona = data['landmarks'][20]['position']['x']
			positiona = positiona*l
			positionb = data['landmarks'][20]['position']['y']
			positionb = positionb*l
			positionc = data['landmarks'][20]['position']['z']
			positionc = positionc*l
			jsons_data.loc[index] = [type_, positionx, positiony, positionz,type_2,positiona,positionb,positionc]
			a = (positiona,positionb,positionc)
			b = (positionx,positiony,positionz)
			dst = distance.euclidean(a,b)
			list_of_dst2.append(dst)
		print(type_)
		print(type_2)
	new_list =[x + y for x, y in zip(list_of_dst, list_of_dst2)]
	result = open('refaces2.csv', 'a', newline='')
	writer = csv.writer(result, delimiter=',')
	row1 = zip(new_list, echo_list)
	for row in row1:
		writer.writerow(row)



	print(new_list)


compare()