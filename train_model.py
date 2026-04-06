from simulation.data_simulator import stream_data
from edge.feature_extraction import extract_features
from sklearn.ensemble import RandomForestClassifier
import numpy as np
import pickle

X = []
y = []

for _ in range(500):
    data, state = stream_data()
    features = extract_features(data)

    X.append(features)
    y.append(int(state))  # 1 = drowsy

model = RandomForestClassifier()
model.fit(X, y)

pickle.dump(model, open("model.pkl", "wb"))

print("✅ Model trained")