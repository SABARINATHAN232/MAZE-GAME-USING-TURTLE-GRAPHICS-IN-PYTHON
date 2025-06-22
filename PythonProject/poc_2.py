import tensorflow as tf
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image
import numpy as np

# Load pre-trained model (MobileNetV2 is light and accurate)
model = MobileNetV2(weights='imagenet')

def predict_image_class(img_path):
    try:
        # Load the image and resize to 224x224
        img = image.load_img(img_path, target_size=(224, 224))
        x = image.img_to_array(img) # Convert image to numpy array
        x = np.expand_dims(x, axis=0) # Add batch dimension
        x = preprocess_input(x) # Normalize for model input

        # Get predictions
        preds = model.predict(x)
        decoded = decode_predictions(preds, top=3)[0]

        # Print top 3 predictions
        print("Top predictions:")
        for i, (_, label, prob) in enumerate(decoded):
            print(f"{i+1}. {label} ({prob*100:.2f}%)")

        # Check for bike or car in labels
        for _, label, _ in decoded:
            if 'bike' in label.lower() or 'bicycle' in label.lower():
                return 'Bike'
            elif 'car' in label.lower() or 'vehicle' in label.lower() or 'cab' in label.lower():
                return 'Car'
        return 'Unknown'

    except Exception as e:
        return f"Error: {e}"

# --- Main Program ---

# Ask user for image file name
img_file = input("Enter the image file name (e.g., car.jpg): ")

# Call prediction function
result = predict_image_class(img_file)
print("Detected:", result)