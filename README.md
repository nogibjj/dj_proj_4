# Automated Prediction System

## Supporting Environment

To help automate the process we include the following:
requirements.txt
dockerfile
makefile
main.yml

## Datastorage and Extraction

We are storing all tables in a database.db file which can be accessed using sqlite queries
- At the moment we only have an attrition data set and we are predicting whether an individual will quit a job

## Algorithms

At the moment we are only use 3 algorithms but the plan is to scale up the number of algorithms
Currently we have
Adaboost
GradientBoosting
RandomForest


<img width="1019" alt="proj1_diagram" src="proj4_flowchart.png">


## Process

Preprocess.py queries the database.db and preprocess the data. check_classifiers.py then reads in the preprocessed data and passes it to all the models to determine which model will perform the best for this data. Then the best performing model will then take in the new unlabeled data and predict the outcome variable and this payload will be outputted through our web framework.

## FastAPI

to run use command: python pred_fastapi-app.py

