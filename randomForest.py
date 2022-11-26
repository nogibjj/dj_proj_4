# random forest classifier

from sklearn.ensemble import RandomForestClassifier

def randomforest_clf():
    clf = RandomForestClassifier(n_estimators=100, random_state=0)
    clf.fit(X, y)

    test_df = pd.read_csv("test.csv")

    test_X = test_df.drop(['EmployeeID', 'EmployeeCount', 'Over18', 'StandardHours'], axis=1)

    test_X = pd.get_dummies(test_X)

    train_accuracy = clf.score(X,y)
    pred_y = clf.predict(test_X)
    pred_df = test_df
    pred_df['pred_y'] = pred_y

    payload = pred_df.to_dict()
    return train_accuracy, payload

