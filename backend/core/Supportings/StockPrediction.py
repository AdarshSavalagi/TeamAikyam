import numpy as np
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import load_model

# Load the saved model
loaded_model = load_model('ML/amazon.h5')

# Assuming your loaded model is named 'loaded_model' and you have a new input 'new_input'
new_input = int(input("Enter the value: "))  # Ensure the input is converted to an integer
scaler = MinMaxScaler(feature_range=(0, 1))
# Preprocess the new input similar to how you processed your training data
scaled_new_input = scaler.transform(np.array([[new_input]]).reshape(1, -1, 1))

# Make predictions using your loaded model
predicted_value = loaded_model.predict(scaled_new_input)

# Inverse transform the predicted value to the original scale
predicted_value_original_scale = scaler.inverse_transform(predicted_value.reshape(-1, 1))

# Define a threshold to classify as high or low risk
threshold = 560  # Adjust this based on your specific use case and evaluation

# Make a risk classification based on the threshold
if predicted_value_original_scale > threshold:
    print("High Risk")
else:
    print("Low Risk")