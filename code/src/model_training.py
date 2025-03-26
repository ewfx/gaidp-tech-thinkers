import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def preprocess_data(data, target_column):
    # Exclude Customer_ID from features
    X = data.drop(columns=[target_column, 'Customer_ID'])
    y = data[target_column]
    
    # Convert categorical variables to dummy variables
    X = pd.get_dummies(X, drop_first=True)
    
    return X, y

def train_model(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    clf = RandomForestClassifier()
    clf.fit(X_train, y_train)
    accuracy = accuracy_score(y_test, clf.predict(X_test))
    return clf, accuracy

def evaluate_model(clf, X_test, y_test):
    y_pred = clf.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    return accuracy

def main(data, target_column):
    X, y = preprocess_data(data, target_column)
    model, accuracy = train_model(X, y)
    return model, accuracy