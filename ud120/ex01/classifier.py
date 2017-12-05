# import the sklearn module for GaussianNB
from sklearn.naive_bayes import GaussianNB


def classifyNB(features_train, labels_train):
    # create classifier
    gnb = GaussianNB()
    # fit the classifier on the training features and labels
    gnb.fit(features_train, labels_train)
    # return the fit classifier
    return gnb


def accuracyNB(trainedClf, features_test, labels_test):
    # use the trained classifier to predict labels for the test features
    pred = trainedClf.predict(features_test)
    # calculate and return the accuracy on the test data
    accuracy = float(sum([pred[i]==labels_test[i] for i in range(len(labels_test))]))/len(labels_test)
    # accuracy = trainedClf.score(features_test, labels_test)
    return accuracy