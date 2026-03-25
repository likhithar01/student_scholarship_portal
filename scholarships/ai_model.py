import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# Sample training data
data = {
    'marks': [90, 75, 60, 85, 50],
    'income': [200000, 500000, 800000, 300000, 900000],
    'eligible': [1, 1, 0, 1, 0]
}

df = pd.DataFrame(data)

X = df[['marks', 'income']]
y = df['eligible']

model = DecisionTreeClassifier()
model.fit(X, y)


def check_eligibility(marks, income):
    result = model.predict([[marks, income]])
    return "Eligible" if result[0] == 1 else "Not Eligible"