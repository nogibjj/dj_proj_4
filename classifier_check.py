from adaBoost import adaboost_clf
from gradientBoosting import gradientboosting_clf
from randomForest import randomforest_clf
from preprocess import get_data

def predict_attrition():
    df = get_data()
    clf_list = [adaboost_clf, gradientboosting_clf, randomforest_clf]
    max_acc = 0
    payload = None
    for clf in clf_list:
        train_accuracy, pred = clf(df)
        if train_accuracy > max_acc:
            max_acc = train_accuracy
            payload = pred
    return payload


if __name__ == "__main__": 
    train_models()

