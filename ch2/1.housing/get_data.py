"""
"""
import urllib.request
import os, os.path, tarfile, pickle
import numpy as np
import pandas as pd

URL = "https://raw.githubusercontent.com/ageron/handson-ml/master/"
CURRENT_ROOT = os.path.dirname(os.path.abspath(__file__))
HOUSING_PATH = os.path.join(CURRENT_ROOT, "datasets", "housing")
HOUSING_DIR_ROOT = ("datasets" + "/housing" + "/housing.tgz")
HOUSING_URL = URL+HOUSING_DIR_ROOT

def download_data():
	if not os.path.exists(HOUSING_PATH):
		os.makedirs(HOUSING_PATH)
	tgz_file = os.path.join(HOUSING_PATH, "housing.tgz")
	try:
		urllib.request.urlretrieve(HOUSING_URL, tgz_file)
	except:
		print("not found")
		return
	with tarfile.open(tgz_file) as tgz:
		tgz.extractall(path=HOUSING_PATH)

def read_csv():
	csv_path = os.path.join(HOUSING_PATH, "housing.csv")
	return pd.read_csv(csv_path, engine="python")

def save_to_pickle():
	csv = read_csv()
	save_pickle = os.path.join(HOUSING_PATH, "housing.pkl")
	with open(save_pickle, 'wb'):
		pickle.dump(csv, f, -1)

def load_to_pickle():
	with open(os.path.join(HOUSING_PATH, "housing.pkl")) as pkl:
		dataset = pickle.load(pkl)

def shuffle_dataset(dataset):
	"""
		dataset : csv file of pandas.read()
	"""
	replaced_index = np.random.permutation(len(dataset))
	return dataset.iloc[replaced_index]

def split_train_test(dataset, test_ratio):
	"""
		dataset : csv file of pandas.read()
		return : training part, test part
	"""
	if test_ratio > 1 and test_ratio < 0:
		print(" test ratio is must (0 < ratio < 1)")
		return

	length_data = len(dataset)
	test_part = int(length_data * test_ratio)
	train_part = int(length_data - test_part)
	return dataset[:train_part], dataset[train_part:]




