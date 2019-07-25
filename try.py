import csv
from bs4 import BeautifulSoup
import numpy as np
from PIL import Image
from extractor import FeatureExtractor
import glob
import pickle
from datetime import datetime
import cv2
from flask import Flask, request, render_template

# Read image features
fe = FeatureExtractor()
features = [] 
img_paths = []
for feature_path in glob.glob("static/feature/*"): 
    features.append(pickle.load(open(feature_path, 'rb'))) #pkl" disatukan di jadikan 1 array feature
    img_paths.append('static/animal/' + os.path.splitext(os.path.basename(feature_path))[0] + '.png') #path dijadikan 1 array


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['query_img'] #file_test yang di open akan di tampung di file->bentuk path

        img = Image.open(file.stream)  # PIL image, dari path ditampilkan bentuk gambar
        uploaded_img_path = "static/uploaded/" + file.filename #nyimpen file_test ke bentuk gambar biar bisa tampil
        img.save(uploaded_img_path)  #path u/ nampilkan file_test      
	    #ekstraksi fitur
        query = fe.extract(img) #ekstraksi di query bentuk histogram
        dists = np.linalg.norm(features - query, axis=1)  # Do search, 
        ids = np.argsort(dists)[:10] # Top 10 results, paling kecil paling mirip
        scores = [(dists[id], img_paths[id]) for id in ids]

        ##
        new_data = ["dists", "scores"]
        new_data_dist = np.array(ids, scores)
        print(new_data_dist)

#         return render_template('index.html',
#                                query_path=uploaded_img_path,
#                                scores=scores)
#     else:
#         return render_template('index.html')

# #html
# html = open("index.html").read()
# soup = BeautifulSoup(html, features='lxml')

# output_rows = []
# for table_row in table.findAll('tr'):
#     columns = table_row.findAll('td')
#     output_row = []
#     for column in columns:
#         output_row.append(column.text)
#     output_rows.append(output_row)

#  df = pd.DataFrame(output_rows)
#  print(df)

# app = Flask(__name__)

