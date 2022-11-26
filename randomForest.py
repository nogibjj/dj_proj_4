# random forest classifier

from sklearn.ensemble import RandomForestClassifier
import pandas as pd


def randomforest_clf(df):
    df_new = df.drop(['EmployeeID', 'EmployeeCount', 'Over18', 'StandardHours'], axis=1)

    X = df_new.drop(['Attrition'], axis=1)
    X = pd.get_dummies(X)

    y = df_new[['Attrition']]
    y = pd.get_dummies(y).drop(['Attrition_No'], axis=1).rename(columns={'Attrition_Yes':'Attrition'})

    clf = RandomForestClassifier(n_estimators=100, random_state=0)
    clf.fit(X, y.values.ravel())

    test_df = pd.read_csv("test.csv")

    test_X = test_df.drop(['EmployeeID', 'EmployeeCount', 'Over18', 'StandardHours'], axis=1)

    test_X = pd.get_dummies(test_X)

    train_accuracy = clf.score(X,y)
    pred_y = clf.predict(test_X)
    pred_df = test_df
    pred_df['pred_y'] = pred_y

    payload = pred_df.to_dict()
    return train_accuracy, payload

