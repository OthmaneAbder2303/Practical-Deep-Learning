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


### Articles, Blogs & Theoretical Deep Dives

#### Long Short-Term Memory (LSTMs)
* **[Understanding LSTMs](https://colah.github.io/posts/2015-08-Understanding-LSTMs/)**: A visual and intuitive explanation of Long Short-Term Memory networks and how they solve the vanishing gradient problem.

#### Recurrent Neural Networks (RNNs)
* **[Backpropagation in RNNs](https://medium.com/@amritsinghbist/understanding-backpropagation-in-recurrent-neural-networks-rnns-5977013be8a9)**: A deep dive into how gradients flow through time.
* **[RNN Architectures & Use Cases](https://medium.com/@shrutishalom/understanding-different-types-of-rnns-architectures-use-cases-and-how-to-choose-15d425143cfd)**: A guide to choosing the right structure for sequential data.

#### Convolutional Neural Networks (CNNs)
* **[Convolutions and Backpropagation](https://medium.com/@pavisj/convolutions-and-backpropagations-46026a8f5d2c)**: Visualizing the math behind the spatial feature extraction.
* **[Padding and Strides in CNN](https://medium.com/@minhazc.engg/padding-and-strides-in-cnn-58dc56493887)**: Understanding how these parameters affect the output feature map size.
* **[Practical Guide to Data Augmentation](https://medium.com/@tubelwj/practical-guide-to-data-augmentation-for-cnn-model-training-5b7cc9baeed1)**: Techniques to improve model generalization (crucial for datasets like UTKFace).

#### Optimization & Initialization
* **[Types of Optimizers](https://medium.com/@sushmita2310/types-of-optimizers-in-deep-learning-a-comprehensive-guide-af258d6acf66)**: Comparison between SGD, Adam, RMSprop, and more.
* **[Weight Initialization Techniques](https://www.geeksforgeeks.org/machine-learning/weight-initialization-techniques-for-deep-neural-networks/)**: Why Xavier and He initialization are vital for training deep architectures.

#### Hardware & Productivity
* **[How to use Kaggle GPU](https://medium.com/featurepreneur/how-to-use-kaggle-gpu-74b1e184242c)**: Maximizing free compute resources for training your models.

---

This repo reflects my progress step by step as I grow my skills in deep learning.
