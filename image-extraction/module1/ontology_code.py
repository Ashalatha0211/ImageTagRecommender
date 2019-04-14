# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 08:20:45 2019

@author: User
"""
from owlready2 import *
from rdflib import Graph
from rdflib import URIRef 
#onto_path.append("/home/kurinchi/Downloads/.owl")
onto = get_ontology("file://C:\\Users\\User\\Documents\\fyp\\image-extraction\\module1\\trail3.owl").load()
str1 = onto.search( type = onto.dog)
#str2 = ''.join(str(e) for e in str1)

length = len(str1) 
   
# Iterating the index 
# same as 'for i in range(len(list))' 
for i in range(length): 
     str2=str1[i]
     
     print(str2)	



#list1 = list(onto[vertebrates])
#for item in list1:
#	print(item)
#'''
#print(onto["vertebrates"]["warm_blooded"])
#onto.vertebrates.get_properties(#warm_blooded)
#'''