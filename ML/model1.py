import joblib
import numpy as np

# Load trained model
model = joblib.load("model1_marks_to_percentile.pkl")

def prediction(marks: float):
    if not (0 <= marks <= 300):
        raise ValueError("Marks must be between 0 and 300.")

    result = model.predict(np.array([[marks]]))
    return float(result[0])

