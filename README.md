# Practical Deep Learning

This repository documents my personal journey into **practical deep learning**.  
It contains hands-on notebooks, experiments, and notes as I learn and apply deep learning concepts through practice.

## What you’ll find

- **Jupyter Notebooks**: Experiments, exercises, and model training logs.
- **Implementations**: Practical code inspired by real-world use cases.
- **Learning Notes**: Observations and "gotchas" encountered while building intuition around DL frameworks.

## Purpose

The goal of this repository is **learning by doing**:
- Understanding concepts through experimentation.
- Making mistakes and improving over time.
- Building intuition around deep learning workflows and data pipelines.

---

## Datasets

This repository utilizes two primary datasets for computer vision tasks:

### 1. Microsoft Cats vs Dogs Dataset
* **Source:** [Kaggle - Microsoft Cats vs Dogs Dataset](https://www.kaggle.com/datasets/shaunthesheep/microsoft-catsvsdogs-dataset)
* **Categories:** Cat and Dog.
* **Important Note:** This dataset contains **corrupted images** (notably `666.jpg` and `11702.jpg`) and non-image system files like `Thumbs.db`. A validation step is mandatory during data loading to prevent training crashes.

### 2. UTKFace Dataset
* **Source:** [Kaggle - UTKFace (New)](https://www.kaggle.com/datasets/jangedoo/utkface-new)
* **Categories:** Human faces with diverse demographics (over 20,000 images).
* **Labels:** Age, Gender, and Ethnicity. 
* **Filename Format:** `[age]_[gender]_[race]_[date&time].jpg`

| Label | Description | Mapping |
| :--- | :--- | :--- |
| **Age** | Integer | 0 to 116 |
| **Gender** | Binary | 0 (Male), 1 (Female) |
| **Race** | Categorical | 0 (White), 1 (Black), 2 (Asian), 3 (Indian), 4 (Others) |



---

> **Tip for Implementation:** Since the **UTKFace** dataset encodes labels in the filename, you will need a custom parser (e.g., using Python's `os.listdir` and `string.split('_')`) to extract the target variables. 

---

This repo reflects my progress step by step as I grow my skills in deep learning.
