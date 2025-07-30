# 🌐 Spatially Enhanced U-Net with Non-Local Attention Gates (SpatialUNet)

**SpatialUNet** is a deep learning model for the segmentation of retinal vasculature and the Foveal Avascular Zone (FAZ) from Optical Coherence Tomography Angiography (OCTA) images. It integrates Spatial Attention, Channel Attention, and Non-Local Attention Gates (NLAG) into a U-Net backbone for enhanced segmentation accuracy.

This repository contains a clean, modular implementation of the full model pipeline—ready for training, testing, evaluation, and deployment.

---

## 📁 File Overview

All components are organized as flat files for easy upload and navigation:

| File | Description |
|------|-------------|
| `model.py` | Full architecture: U-Net + Spatial/Channel/NL Attention |
| `train.py` | Trains the model on OCTA datasets |
| `evaluate.py` | Evaluates the model performance on test set |
| `test.py` | Loads model and runs prediction on a sample image |
| `data_loader.py` | Image generators with augmentation |
| `losses.py` | Dice, Focal, BCE, and Tversky losses |
| `metrics.py` | Dice, IoU, Accuracy, Sensitivity, Specificity, Tversky |
| `config.yaml` | Configuration for image size, paths, batch size, etc. |
| `requirements.txt` | Python dependencies |
| `LICENSE` | MIT License |
| `README.md` | Documentation and usage instructions |

---

## 🚀 Getting Started

### 🔧 Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 🧠 Step 2: Train the Model

```bash
python train.py
```

Ensure your dataset is organized properly and update `config.yaml` accordingly.

---

### 📊 Step 3: Evaluate on Test Set

```bash
python evaluate.py
```

This script loads the saved model and prints performance metrics on the test set.

---

### 🧪 Step 4: Run Inference on a Single Image

```bash
python test.py
```

Replace the path in `test.py` with your own test image and model file.

---

## 📌 Citation

If you use this repository, please cite the following publication:

```
N. P. Raja, S. Sarvesan, A. Thomas and V. P. Gopi,
"Spatially Enhanced U-Net with Non-Local Attention Gates for Automated Retinal Vasculature and FAZ Segmentation in OCTA Images,"
IEEE Journal (To Appear), 2025.
```

---

## 👤 Maintainer

**Nisan Pranavah Raja**  
Ph.D. Scholar – AI for Medical Imaging 
This repository is maintained by Nisan Pranavah Raja, the first author and lead contributor of the original IEEE publication. While the research and model development were carried out collaboratively with co-authors, this GitHub implementation has been independently refined, documented, and curated by Nisan to enable broader accessibility, reproducibility, and real-world application.
🔗 [LinkedIn](https://www.linkedin.com/in/nisan-pranavah-raja)  
🔗 [Google Scholar](https://scholar.google.com/citations?user=_PW0aeYAAAAJ&hl=en)

---

## 📄 License

This project is licensed under the MIT License.
