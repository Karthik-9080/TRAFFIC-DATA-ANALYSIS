from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

def train_model(data):
    x = data[['Hour', 'Month', 'Visibility_km', 'Temperature_C', 'Traffic_Signal', 'Is_Weekend']]
    y = data['Severity']

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

    model = DecisionTreeClassifier(random_state=42, max_depth=5, min_samples_split=10)
    model.fit(x_train, y_train)

    preds = model.predict(x_test)
    acc = accuracy_score(y_test, preds)

    return acc