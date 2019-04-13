# ImageTagRecommender
Module 1:
1) First run the colordescriptor.py file which creates a 3D HSV color histogram for 5 different regions(The top-left corner, the top-right corner, the bottom-right corner, the bottom-left corner, and the center) of the image.
2) Next the index.py file is run which extracts features from each image of our dataset and stores it in a file called index.csv. It takes two arguments: the dataset and the index.csv file.
3) Now we run the searcher.py file which computes similarity between input image and the dataset images using chi-sqaured similarity metric.
4) Next we run the search.py file. Which moves the most similar images to our input image into a folder called results and stores their candidate tags into a text file(candidate.txt).
5) freq.py files calcutes the frequency of occurance of each of the tags in the candidate.txt file.

Module 2: 
An ontology has been created for the animal kingdom domain which relates various attributes to each other in the form of a tree structure. This is stored in a .owl file which is basically like an xml file storing the ontology.

Module 3:
In this module we are required to take the top k most frequent tags from candidate.txt and trace the ontology to find out additional information about these tags and recommend these to the user.
