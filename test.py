import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from metrics import dice_coef, accuracy, sensitivity, specificity, iou
from losses import dice_loss

# Load model
model_path = "best_model.h5"  # Change this to your model file
model = load_model(model_path, custom_objects={
    'dice_coef': dice_coef,
    'accuracy': accuracy,
    'sensitivity': sensitivity,
    'specificity': specificity,
    'iou': iou,
    'dice_loss': dice_loss
})

# Load sample image
image_path = "test_image.png"  # Replace with your test image path
image = load_img(image_path, target_size=(256, 256), color_mode='grayscale')
image_arr = img_to_array(image) / 255.0
image_arr = np.expand_dims(image_arr, axis=0)

# Predict
prediction = model.predict(image_arr)
prediction = np.squeeze(prediction)

# Plot result
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title("Input Image")
plt.imshow(np.squeeze(image_arr), cmap='gray')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title("Predicted Mask")
plt.imshow(prediction, cmap='gray')
plt.axis('off')
plt.tight_layout()
plt.show()