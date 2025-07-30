import numpy as np
from tensorflow.keras.models import load_model
from metrics import dice_coef, accuracy, sensitivity, specificity, iou

def evaluate_model(model_path, X_test, y_test):
    model = load_model(model_path, custom_objects={
        'dice_coef': dice_coef,
        'accuracy': accuracy,
        'sensitivity': sensitivity,
        'specificity': specificity,
        'iou': iou
    })
    results = model.evaluate(X_test, y_test, verbose=0)
    print("Test Metrics:")
    for name, val in zip(model.metrics_names, results):
        print(f"{name}: {val:.4f}")