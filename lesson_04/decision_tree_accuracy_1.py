import sys
from class_vis import prettyPicture
from prep_terrain_data import makeTerrainData

import matplotlib.pyplot as plt
import numpy as np
import pylab as pl

features_train, labels_train, features_test, labels_test = makeTerrainData()

from sklearn import tree
from sklearn.metrics import accuracy_score


########################## DECISION TREE #################################


### your code goes here--now create 2 decision tree classifiers,
### one with min_samples_split=2 and one with min_samples_split=50
### compute the accuracies on the testing data and store
### the accuracy numbers to acc_min_samples_split_2 and
### acc_min_samples_split_50, respectively


clf = tree.DecisionTreeClassifier(min_samples_split=50)
clf.fit(features_train, labels_train)
print clf.score(features_test, labels_test)


clf = tree.DecisionTreeClassifier(min_samples_split=2)
clf.fit(features_train, labels_train)
print clf.score(features_test, labels_test)



def submitAccuracies():
  return {"min_samples_split_2":round(min_samples_split_2,3),
          "min_samples_split_50":round(min_samples_split_50,3)}