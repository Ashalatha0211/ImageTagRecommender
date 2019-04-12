# USAGE
# python search.py --index index.csv --query queries/103100.png --result-path dataset

# import the necessary packages
from pyimagesearch.colordescriptor import ColorDescriptor
from pyimagesearch.searcher import Searcher
import argparse
import cv2

## construct the argument parser and parse the arguments
#ap = argparse.ArgumentParser()
#ap.add_argument("-i", "--index", required = True,
#	help = "Path to where the computed index will be stored")
#ap.add_argument("-q", "--query", required = True,
#	help = "Path to the query image")
#ap.add_argument("-r", "--result-path", required = True,
#	help = "Path to the result path")
#args = vars(ap.parse_args())
#%%
# initialize the image descriptor
cd = ColorDescriptor((8, 12, 3))

# load the query image and describe it
query = cv2.imread('monkey.jpg')
#%%
features = cd.describe(query)
#%%
# perform the search
searcher = Searcher('index.csv')
results = searcher.search(features)

# display the query
cv2.imwrite("Query.jpg", query)
#%%
# loop over the results
import os
path = 'C:/Users/User/Documents/fyp/image-extraction/module1/results'
length = len(results)
with open("C:/Users/User/Documents/fyp/image-extraction/module1/results/candidate.txt","w") as f1:
    
    for i, (score,resultID) in zip(range(length),results):
        x = resultID.split(".")
        y = str(x[0]) + '.txt'
        with open(y) as f:
            for line in f:
                f1.write(line)
        result = cv2.imread(resultID)
        cv2.imwrite(os.path.join(path, str(i+1) + '.jpg'), result)
    