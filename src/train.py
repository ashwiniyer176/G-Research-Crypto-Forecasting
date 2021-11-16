import joblib
import numpy as np
import pandas as pd
from sklearn import metrics
from sklearn import tree
import os
import config


def returnXandY(data, label):
    '''
    Takes a dataset and its target column name and returns X and y
    '''
    X = data.drop(label, axis=1)
    y = data[label]
    return X, y


def run(ratio, model, metric):
    """
    Takes in ratio as an argument and runs the Decision Tree Model and prints Accuracy for the model per ratio.
    """
    df = pd.read_csv("data/final_train.csv")
    trainSize = int((1-ratio)*len(df))
    valSize = int(ratio*len(df))
    # Setting train data where ratio value != ratio and validation where ratio value==ratio
    df_train = df.iloc[:trainSize, :]
    df_valid = df.iloc[trainSize:, :]
    X_train, y_train = returnXandY(df_train, "Target")
    X_val, y_val = returnXandY(df_valid, "Target")

    net = model
    net.fit(X_train, y_train)
    preds = net.predict(X_val)
    accuracy = metric(y_val, preds)
    print(f"Ratio={ratio}  Metric={accuracy}")
    file = open(f"models/model_ratio_{ratio}.bin", "wb")
    joblib.dump(net, file)


if __name__ == "__main__":
    df = pd.read_csv("data/train_folds.csv")
    for k in df['ratio'].unique():
        run(ratio=k, model=config.model, metric=config.metric)
