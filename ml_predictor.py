import joblib
import numpy as np

model = joblib.load("model.joblib")
encoder = joblib.load("encoder.joblib")
role_names = model.classes_

def predict_top_roles(skills, top_n=3):
    try:
        skills_encoded = encoder.transform([skills])
        probs = model.predict_proba(skills_encoded)[0]
        top_indices = np.argsort(probs)[::-1][:top_n]
        top_roles = [(role_names[i].title(), round(probs[i]*100, 2)) for i in top_indices]
        return top_roles
    except:
        return [("Unknown", 0.0)]
