import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib

url = 'https://raw.githubusercontent.com/rusita-ai/data/master/iris.csv'
data = pd.read_csv(url)

X = data.drop(columns = ['species'])
y = data['species']
X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                    test_size = 0.3,
                                                    random_state = 2045)

model = LogisticRegression()
model.fit(X_train, y_train)

joblib.dump(model, 'model/model_iris_lr.pkl')
