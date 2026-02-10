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
@article{RAJA2026113956,
title = {Spatially enhanced U-Net with non-local attention gates for automated retinal vasculature and foveal avascular zone segmentation in optical coherence tomography angiography images},
journal = {Engineering Applications of Artificial Intelligence},
volume = {167},
pages = {113956},
year = {2026},
issn = {0952-1976},
doi = {https://doi.org/10.1016/j.engappai.2026.113956},
url = {https://www.sciencedirect.com/science/article/pii/S095219762600237X},
author = {Nisan Pranavah Raja and Srivatsan Sarvesan and Varun P. Gopi},
keywords = {Deep learning, Segmentation, Capillary, Artery, Vein, Foveal Avascular Zone, Diabetic retinopathy, Optical Coherence Tomography Angiography, U-Net, Non-local attention gate, Spatial attention gate},
abstract = {Diabetic Retinopathy (DR) is a chronic diabetes complication caused by prolonged high blood glucose levels, damaging the retina and potentially leading to irreversible vision loss. In clinical settings, Optical Coherence Tomography Angiography (OCTA) plays a key role in managing vision-related diseases by providing clear, cross-sectional images of retinal structures. We propose an ingenious automated deep learning-based segmentation technique by enhancing the conventional U-Net by integrating attention-gating mechanisms into the skip connections to combine refined features from the encoder and the previous level of the decoder. This creates a Non-Local Attention Gate in the first decoder and Spatial Attention Gates in the rest. Each encoder and decoder level uses three convolutional layers with batch normalization and Rectified Linear Unit activation. Deep learning methods to segment retinal structures, including capillaries, arteries, veins, and the Foveal Avascular Zone (FAZ), are vital in research and medical use. Extensive experiments and analysis are conducted on the open-access OCTA-500 dataset, encompassing 500 subjects. In the segmentation task, we evaluated our proposed method using seven quantitative metrics: Dice coefficient, Intersection over Union, accuracy, sensitivity, specificity, 95th Percentile Hausdorff Distance, and Average Symmetric Surface Distance. Our proposed method achieved Dice scores of 87.59% and 89.90% for capillary segmentation, 87.19% and 88.73% for artery segmentation, and 86.66% and 88.84% for vein segmentation. In the FAZ region, the method attained 92.57% and 98.45% for the OCTA 6 mm and 3 mm subsets, respectively. Our design framework is simple, resource-efficient, and accurate, achieving precise segmentation of the microvasculature and Foveal Avascular Zone}
}
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
