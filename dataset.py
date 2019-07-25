import glob
import os
import pickle
from PIL import Image
from extractor import FeatureExtractor

fe = FeatureExtractor()

for img_path in sorted(glob.glob('static/animal/*.png')):
    print(img_path)
    img = Image.open(img_path)  # PIL image
    feature = fe.extract(img)
    feature_path = 'static/feature/' + os.path.splitext(os.path.basename(img_path))[0] + '.pkl' 
    pickle.dump(feature, open(feature_path, 'wb')) #array di save ke folder feature dg format .pkl
