import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import MultiLabelBinarizer
import joblib

# Simulated Dataset (skill set -> role)
data = [
    (["python", "machine learning", "numpy", "pandas"], "Data Scientist"),
    (["html", "css", "javascript"], "Frontend Developer"),
    (["python", "flask", "api"], "Backend Developer"),
    (["java", "c++", "oop"], "Software Developer"),
    (["sql", "database", "mysql"], "Database Administrator"),
    (["html", "python", "sql"], "Full Stack Developer"),
]

# Convert to DataFrame
df = pd.DataFrame(data, columns=["skills", "role"])

# Binarize skills
mlb = MultiLabelBinarizer()
X = mlb.fit_transform(df["skills"])
y = df["role"]

# Train model
clf = RandomForestClassifier()
clf.fit(X, y)

# Save the model and encoder
joblib.dump(clf, "model.joblib")
joblib.dump(mlb, "encoder.joblib")
